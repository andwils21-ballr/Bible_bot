"""Build the map after Genesis 50 (books/1-genesis/S2.md) from data.py and ../template.html.

    python3 maps/fathers/make.py <natural-earth-dir>

Needs shapely, and three Natural Earth 10m layers as GeoJSON in one folder
(public domain; https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/):
ne_10m_land, ne_10m_lakes, ne_10m_rivers_lake_centerlines.
The drawing helpers are copied from maps/journey/make.py (the map after Joshua 24)."""
import html, json, math, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from shapely.geometry import shape, box, Polygon, MultiPolygon, LineString, MultiLineString, GeometryCollection
from shapely.ops import unary_union
import data as D

NE = sys.argv[1]
OUT = os.path.join(HERE, "..", "..", D.OUT)

# Plain equirectangular projection, true at 33°N; 100 map units per degree of latitude.
LON0, LAT1, K = D.LON0, D.LAT1, 100.0
C = math.cos(math.radians(D.COSLAT))

def xy(lon, lat):
    return ((lon - LON0) * C * K, (LAT1 - lat) * K)

def fmt(v):
    s = f"{v:.1f}"
    return s[:-2] if s.endswith(".0") else s

BB = box(*D.BBOX)
KEYS = [s["key"] for s in D.STAGES]
IDX = {k: i for i, k in enumerate(KEYS)}

def si(k, default=None):
    return default if k is None else IDX[k]

# ------------------------------------------------------------------ geometry helpers
def feats(name):
    return json.load(open(f"{NE}/{name}.geojson"))["features"]

def polys(g):
    if g is None or g.is_empty: return []
    if isinstance(g, Polygon): return [g]
    if isinstance(g, (MultiPolygon, GeometryCollection)):
        return [p for p in g.geoms if isinstance(p, Polygon)]
    return []

def lines(g):
    if g is None or g.is_empty: return []
    if isinstance(g, LineString): return [g]
    if isinstance(g, (MultiLineString, GeometryCollection)):
        out = []
        for p in g.geoms: out += lines(p)
        return out
    return []

def ring_d(coords, closed=True):
    """Path data in tenths of a map unit: an absolute move, then relative steps
    taken between rounded points, so the rounding never accumulates."""
    pts, last = [], None
    for lon, lat in coords:
        x, y = xy(lon, lat)
        p = (round(x * 10), round(y * 10))
        if p != last: pts.append(p)
        last = p
    if closed and len(pts) > 1 and pts[0] == pts[-1]: pts = pts[:-1]
    if len(pts) < 2: return ""
    t = lambda v: fmt(v / 10)
    d = "M" + t(pts[0][0]) + "," + t(pts[0][1]) + "l"
    steps = []
    for (a, b), (c, e) in zip(pts, pts[1:]):
        dx, dy = t(c - a), t(e - b)
        steps.append(dx + ("," if not dy.startswith("-") else "") + dy)
    out = d + " ".join(steps)
    return out.replace(" -", "-") + ("z" if closed else "")

def poly_d(g, tol=0.0012, min_area=0.00002):
    d = []
    for p in polys(g):
        p = p.simplify(tol, preserve_topology=True)
        if p.area < min_area: continue
        d.append(ring_d(p.exterior.coords))
        for r in p.interiors:
            if Polygon(r).area >= min_area: d.append(ring_d(r.coords))
    return "".join(d)

def line_d(g, tol=0.0012):
    return "".join(ring_d(l.simplify(tol).coords, False) for l in lines(g))

def P(coords):
    return Polygon(coords).buffer(0)

def smooth_d(pts):
    """Catmull-Rom through map points, as cubic Beziers."""
    pts = [xy(*p) for p in pts]
    if len(pts) == 2:
        return f"M{fmt(pts[0][0])},{fmt(pts[0][1])}L{fmt(pts[1][0])},{fmt(pts[1][1])}"
    Q = [pts[0]] + pts + [pts[-1]]
    d = f"M{fmt(pts[0][0])},{fmt(pts[0][1])}"
    for i in range(1, len(Q) - 2):
        p0, p1, p2, p3 = Q[i - 1], Q[i], Q[i + 1], Q[i + 2]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f"C{fmt(c1[0])},{fmt(c1[1])} {fmt(c2[0])},{fmt(c2[1])} {fmt(p2[0])},{fmt(p2[1])}"
    return d

def pt(p):
    if isinstance(p, str):
        q = D.P[p]; return (q["lon"], q["lat"])
    return p

# ------------------------------------------------------------------ base layers
land = unary_union([shape(f["geometry"]).intersection(BB) for f in feats("ne_10m_land")
                    if shape(f["geometry"]).intersects(BB)])
nelakes = {f["properties"]["name"]: shape(f["geometry"]) for f in feats("ne_10m_lakes")
           if shape(f["geometry"]).intersects(BB)}
# the Salt Sea is drawn by hand at its old extent; modern reservoirs are left out
lakes = [P(D.DEAD_SEA), nelakes["Sea of Galilee"], nelakes["Lake Hammar"], nelakes["Lake Urmia"]]
alllakes = unary_union(lakes)
rv = {}
for f in feats("ne_10m_rivers_lake_centerlines"):
    g = shape(f["geometry"])
    if g.intersects(BB):
        rv.setdefault(f["properties"].get("name"), []).append(g.intersection(BB))
def river(*names):
    return unary_union([g for n in names for g in rv[n]])
rivers = [
    river("Firat", "Al Furat", "Euphrates", "Shatt al Arab"),
    river("Dicle", "Tigris"),
    river("Nile", "Rosetta Branch", "Damietta Branch"),
    river("Jordan").intersection(box(35.3, 31.75, 36, 33.7)).difference(alllakes.buffer(0.002)),
]

sea = BB.difference(land)
waterlines = []
for dd in (0.02, 0.045):
    ring = land.buffer(dd, quad_segs=3).boundary.intersection(sea.buffer(-0.002))
    waterlines.append(line_d(ring, tol=0.006))

# ------------------------------------------------------------------ SVG pieces
def attrs_ft(f, t):
    s = f' data-f="{f}"'
    if t is not None: s += f' data-t="{t}"'
    return s

def esc(s): return html.escape(s, quote=True)

svg = []
W, H = xy(D.BBOX[2], D.BBOX[1])   # the whole drawing, in map units; the views are windows on it
svg.append(f'<path class="sea" d="{poly_d(sea, 0.002, 0.0005)}"/>')
svg.append('<g class="g-wl">' + "".join(f'<path d="{d}"/>' for d in waterlines) + '</g>')

# water
svg.append('<g class="g-lake">' + "".join(f'<path d="{poly_d(g, 0.0008, 0)}"/>' for g in lakes) + '</g>')
for r in rivers:
    svg.append(f'<path class="g-river" d="{line_d(r, 0.002)}"/>')
for r in D.RIVERS_EXTRA:
    svg.append(f'<path class="g-river" d="{smooth_d(r)}"/>')
svg.append('<g class="g-wadi">' + "".join(f'<path d="{smooth_d(p)}"/>' for _, p, _ in D.WADIS) + '</g>')

# mountains: a little hill with hachures, two sizes for the two views
def hill(lon, lat, s):
    x, y = xy(lon, lat)
    return (f'M{fmt(x-s)},{fmt(y+s*.45)}Q{fmt(x-s*.35)},{fmt(y-s*.9)} {fmt(x)},{fmt(y-s*.75)}'
            f'Q{fmt(x+s*.35)},{fmt(y-s*.9)} {fmt(x+s)},{fmt(y+s*.45)}'
            f'M{fmt(x+s*.15)},{fmt(y-s*.35)}l{fmt(s*.3)},{fmt(s*.55)}'
            f'M{fmt(x+s*.45)},{fmt(y-s*.25)}l{fmt(s*.25)},{fmt(s*.5)}')
svg.append('<g class="g-mt mt-j">' + "".join(f'<path d="{hill(a, b, s)}"/>' for a, b, s in D.MOUNTAINS_J) + '</g>')
svg.append('<g class="g-mt mt-l">' + "".join(f'<path d="{hill(a, b, s)}"/>' for a, b, s in D.MOUNTAINS_L) + '</g>')

# the land promised (Genesis 15:18), from the covenant on
svg.append(f'<path class="g-promise" d="{smooth_d(D.PROMISE)}"{attrs_ft(IDX[D.PROMISE_STAGE], None)}/>')

# Abram's view from between Bethel and Ai (Genesis 13:14)
nx, ny = xy(*D.SIGHT_FROM)
sight = "".join(f'M{fmt(nx)},{fmt(ny)}L{fmt(xy(*p)[0])},{fmt(xy(*p)[1])}' for p in D.SIGHT)
svg.append(f'<path class="g-sight" d="{sight}"{attrs_ft(IDX[D.SIGHT_STAGE], IDX[D.SIGHT_STAGE])}/>')

# routes
masks, segs = [], []
order = {}
for n, (k, kind, pts) in enumerate(D.SEGS):
    i = IDX[k]
    o = order.get(i, 0); order[i] = o + 1
    d = smooth_d([pt(p) for p in pts])
    masks.append(f'<mask id="jm-m{n}" maskUnits="userSpaceOnUse" x="0" y="0" width="{fmt(W)}" height="{fmt(H)}">'
                 f'<path class="mk" d="{d}" pathLength="1"/></mask>')
    segs.append(f'<g class="seg k-{kind}" data-f="{i}" data-o="{o}" mask="url(#jm-m{n})">'
                f'<path d="{d}" marker-end="url(#jm-ar)"/></g>')
svg.append('<g class="g-route">' + "".join(segs) + '</g>')

# places
def pos_attrs(pos):
    return {"e": ('start', '.62em', '.34em'), "w": ('end', '-.62em', '.34em'),
            "n": ('middle', '0', '-.72em'), "s": ('middle', '0', '1.22em'),
            "ne": ('start', '.45em', '-.42em'), "nw": ('end', '-.45em', '-.42em'),
            "se": ('start', '.45em', '1.05em'), "sw": ('end', '-.45em', '1.05em')}[pos]

first, acts = {}, {}
for i, st in enumerate(D.STAGES):
    for a in st["act"]:
        acts.setdefault(a, []).append(i)
        first.setdefault(a, i)
for k, kind, pts in D.SEGS:            # a place a route passes through is drawn from that stage
    for p in pts:
        if isinstance(p, str): first[p] = min(first.get(p, 99), IDX[k])
gt = {}
for pid, state, f, t in D.GIANT_TOWNS:
    gt.setdefault(pid, []).append((state, IDX[f], si(t)))
    first[pid] = min(first.get(pid, 99), IDX[f])
dots, labels = [], []
for pid, p in D.P.items():
    if pid not in first: continue
    x, y = xy(p["lon"], p["lat"])
    a, dx, dy = pos_attrs(p["pos"])
    act = ",".join(map(str, acts.get(pid, [])))
    rings = "".join(f'<path class="gr {s}" d="M{fmt(x)},{fmt(y)}h0"{attrs_ft(f, t)}/>' for s, f, t in gt.get(pid, []))
    kind = "k" if p["sure"] else "u"
    dots.append(f'<g class="pl {kind} t{p["tier"]}" data-id="{pid}" data-f="{first[pid]}" data-a="{act}">{rings}'
                f'<path class="d" d="M{fmt(x)},{fmt(y)}h0"/><path class="di" d="M{fmt(x)},{fmt(y)}h0"/>'
                f'<path class="hit" d="M{fmt(x)},{fmt(y)}h0"/></g>')
    labels.append(f'<text class="pt t{p["tier"]}" data-id="{pid}" data-f="{first[pid]}" data-a="{act}" x="{fmt(x)}" y="{fmt(y)}" '
                  f'text-anchor="{a}" dx="{dx}" dy="{dy}">{esc(p["name"])}</text>')
svg.append('<g class="g-pl">' + "".join(dots) + '</g>')

# area labels
def label(text, lon, lat, cls, f, t, rot=0):
    x, y = xy(lon, lat)
    r = f' transform="rotate({rot} {fmt(x)} {fmt(y)})"' if rot else ""
    return f'<text class="{cls}" x="{fmt(x)}" y="{fmt(y)}"{r}{attrs_ft(f, t)}>{esc(text)}</text>'
alab = []
for text, lon, lat, cls, f, t, rot, *view in D.LABELS:
    alab.append(label(text, lon, lat, "al " + cls + (" v" + view[0] if view else ""), si(f, 0), si(t), rot))
for text, lon, lat, f, t, kind, view, act in D.GIANT_LABELS:
    cls = "al giant " + kind + (" v" + view if view else "")
    a = ",".join(str(IDX[k]) for k in act)
    alab.append(label(text, lon, lat, cls, IDX[f], si(t)).replace("<text ", f'<text data-a="{a}" ', 1))
for name, pts, li in D.WADIS:
    (a1, b1), (a2, b2) = pts[li - 1], pts[li]
    x1, y1 = xy(a1, b1); x2, y2 = xy(a2, b2)
    ang = math.degrees(math.atan2(y2 - y1, x2 - x1))
    if ang > 90: ang -= 180
    if ang < -90: ang += 180
    alab.append(label(name, (a1 + a2) / 2, (b1 + b2) / 2, "al river w vl", 0, None, round(ang)))
svg.append('<g class="g-al">' + "".join(alab) + '</g>')
svg.append('<g class="g-pt">' + "".join(labels) + '</g>')

defs = f'''<defs>
<pattern id="jm-hg" patternUnits="userSpaceOnUse" width="6" height="6" patternTransform="rotate(45)"><path d="M0,0V6" class="hg"/></pattern>
<pattern id="jm-hr" patternUnits="userSpaceOnUse" width="7" height="7" patternTransform="rotate(-45)"><path d="M0,0V7M3.5,0V7" class="hr"/></pattern>
<pattern id="jm-hw" patternUnits="userSpaceOnUse" width="6" height="6" patternTransform="rotate(30)"><path d="M0,0V6" class="hw"/></pattern>
<marker id="jm-ar" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="4.2" markerHeight="4.2" orient="auto-start-reverse"><path d="M0,1L9,5L0,9Z" class="ar"/></marker>
{"".join(masks)}
</defs>'''

def view(west, east, top):
    x, y = xy(west, top)
    w = xy(east, top)[0] - x
    return [round(v, 1) for v in (x, y, w, w / D.ASPECT)]
VB_J, VB_L = view(*D.VIEW_J), view(*D.VIEW_L)

svg_html = (f'<svg class="jm-svg" viewBox="{" ".join(map(str, VB_J))}" role="img" '
            f'aria-label="{esc(D.LINK_NOTE)}">{defs}{"".join(svg)}</svg>')

# ------------------------------------------------------------------ captions and data
ABBR = {"Genesis": "genesis", "Joshua": "joshua", "2 Chronicles": "2-chronicles", "Psalm": "psalms"}
REF = re.compile(r"\{((?:\d )?\w+) (\d+):(\d+)\}")
def caption(text):
    t = esc(text).replace("&quot;", '"').replace("&#x27;", "'")
    t = re.sub(r"\*([^*]+)\*", r"<i>\1</i>", t)
    def r(m):
        b, c, v = m.group(1), m.group(2), m.group(3)
        return f'<a class="jm-ref" href="#/{ABBR[b]}/{c}" data-r="{ABBR[b]}|{c}|{v}">{b.replace(" ", "&nbsp;")}&nbsp;{c}:{v}</a>'
    t = REF.sub(r, t)
    # adjacent refs read as one parenthesis: (Genesis 14:5; Genesis 14:6)
    A = r'<a class="jm-ref"[^>]*>[^<]*</a>'
    t = re.sub(f"({A}(?:\\s+{A})*)", lambda m: "(" + "; ".join(re.findall(A, m.group(1))) + ")", t)
    return t

stages = [dict(t=s["title"], w=s["when"], c=s["cam"], x=caption(s["text"])) for s in D.STAGES]
notes = {pid: dict(n=p["name"], s=p["sure"], x=caption(p["note"]) if p["note"] else "")
         for pid, p in D.P.items() if pid in first}
blob = json.dumps(dict(stages=stages, places=notes, vb=dict(j=VB_J, l=VB_L)), ensure_ascii=False, separators=(",", ":"))
blob = blob.replace("</", "<\\/")

TEMPLATE = open(os.path.join(HERE, "..", "template.html"), encoding="utf-8").read()
out = (TEMPLATE.replace("@@SVG@@", svg_html).replace("@@DATA@@", blob)
       .replace("@@N@@", str(len(stages))).replace("@@KEY@@", D.KEY).replace("@@SRC@@", D.SRC)
       .replace("@@CART@@", D.CART).replace("@@ASPECT@@", str(D.ASPECT)).replace("@@ROOTCLASS@@", " wide faint")
       .replace("@@FROM@@", D.FROM))
fm = (f"---\nkind: supplement\norder: {D.ORDER}\ntitle: {D.TITLE}\n---\n\n"
      "<!-- Made by maps/fathers/make.py from maps/fathers/data.py: edit those and rebuild. -->\n")
open(OUT, "w", encoding="utf-8").write(fm + out + "\n")
print("wrote", D.OUT + ",", len(out) // 1024, "KB")
