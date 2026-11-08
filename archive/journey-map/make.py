"""Build the map after Joshua 24 (books/6-joshua/S1.md) from data.py and template.html.

    python3 maps/journey/make.py <natural-earth-dir>

Needs shapely, and three Natural Earth 10m layers as GeoJSON in one folder
(public domain; https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/):
ne_10m_land, ne_10m_lakes, ne_10m_rivers_lake_centerlines.
Stage numbers are in the notes' links (#/joshua/s1/N): adding or removing a
stage moves them."""
import html, json, math, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from shapely.geometry import shape, box, Polygon, MultiPolygon, LineString, MultiLineString, GeometryCollection
from shapely.ops import unary_union, linemerge
import data as D

NE = sys.argv[1]
OUT = os.path.join(HERE, "..", "..", "books", "6-joshua", "S1.md")

# Plain equirectangular projection, true at 31°N; 100 map units per degree of latitude.
LON0, LAT1, K = 29.8, 34.8, 100.0
C = math.cos(math.radians(31.0))

def xy(lon, lat):
    return ((lon - LON0) * C * K, (LAT1 - lat) * K)

def fmt(v):
    s = f"{v:.1f}"
    return s[:-2] if s.endswith(".0") else s

BB = box(29.8, 26.8, 38.8, 35.6)
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
lakes = {
    "dead": P(D.DEAD_SEA),
    "galilee": nelakes["Sea of Galilee"],
    "bitter": nelakes["Great Bitter Lake"],
    "huleh": P(D.HULEH),
    "timsah": P(D.TIMSAH),
}
alllakes = unary_union(list(lakes.values()))
rv = {}
for f in feats("ne_10m_rivers_lake_centerlines"):
    g = shape(f["geometry"])
    if g.intersects(BB):
        rv[(f["properties"].get("name"), f["properties"].get("featurecla"))] = g.intersection(BB)
jordan_main = [l for l in lines(linemerge(rv[("Jordan", "River")]))]
# keep the river from its sources to the Salt Sea; the Salt Sea itself is drawn by hand
jordan = unary_union([l for l in jordan_main if l.bounds[1] > 31.7]).difference(alllakes.buffer(0.002))
nile = unary_union([rv[("Nile", "River")], rv[("Rosetta Branch", "River")], rv[("Damietta Branch", "River")]])

# Divider between the lands west and east of the Jordan.
div = [(36.7, 35.2), (36.3, 34.3), (35.95, 33.70)]
for l in jordan_main:
    c = list(l.coords)
    if c[0][1] > 33.5:  # the upper Jordan, from its sources to the Sea of Chinnereth
        div += c
div += [(35.597, 32.80), (35.577, 32.72)]
for l in jordan_main:
    c = list(l.coords)
    if abs(c[0][1] - 32.72) < 0.01:
        div += c
div += [(35.52, 31.60), (35.49, 31.30), (35.47, 31.04), (35.40, 30.95), (35.28, 30.55),
        (35.13, 30.00), (35.0, 29.55), (34.7, 26.9)]
WESTR = Polygon(div + [(28.0, 26.9), (28.0, 35.2)]).buffer(0)
EASTR = box(28.0, 26.9, 38.0, 35.2).difference(WESTR)

def west(c): return P(c).intersection(WESTR).intersection(land).difference(alllakes)
def east(c): return P(c).intersection(EASTR).intersection(land).difference(alllakes)

T = {}
for k, c in D.WEST.items():
    T[k] = P(c).intersection(land) if k == "dannorth" else west(c)
T["naphtali"] = T["naphtali"].difference(T["dannorth"])
for k, c in D.EAST.items():
    T[k] = east(c)
geshur, maacah = east(D.GESHUR), east(D.MAACAH).difference(T["dannorth"])
T["manassehE"] = T["manassehE"].difference(geshur).difference(maacah)
moab, ammon = east(D.MOAB), east(D.AMMON)
philistia = P(D.PHILISTIA).intersection(land)
sidon = P(D.SIDON).intersection(land)
anakim = P(D.ANAKIM).intersection(land)
rephaim = T["manassehE"].intersection(box(35.0, 32.62, 37.5, 34.0))
wander = P(D.WANDER).intersection(land)

c_east = unary_union([T["reuben"], T["gad"], T["manassehE"]])
c_south = unary_union([T["judah"], T["simeon"], T["benjamin"], T["dansouth"]]).difference(philistia)
c_north = unary_union([T[k] for k in ("ephraim", "manasseh", "issachar", "zebulun", "asher", "naphtali")]).difference(sidon)
sihon = unary_union([T["reuben"], T["gad"]])

def borders(keys):
    b = unary_union([T[k].boundary for k in keys])
    shore = land.boundary.buffer(0.006).union(alllakes.boundary.buffer(0.006))
    return b.difference(shore)
west_keys = ["judah", "simeon", "benjamin", "dansouth", "ephraim", "manasseh", "issachar", "zebulun", "asher", "naphtali", "dannorth"]
east_keys = ["reuben", "gad", "manassehE"]
wb = borders(west_keys).difference(WESTR.boundary.buffer(0.004))
eb = borders(east_keys).difference(EASTR.boundary.buffer(0.004))

# Engraver's water-lines, offset into the sea.
sea = BB.difference(land)
waterlines = []
for dd in (0.013, 0.03):
    ring = land.buffer(dd, quad_segs=3).boundary.intersection(sea.buffer(-0.002))
    waterlines.append(line_d(ring, tol=0.004))

# ------------------------------------------------------------------ SVG pieces
def attrs_ft(f, t):
    s = f' data-f="{f}"'
    if t is not None: s += f' data-t="{t}"'
    return s

def esc(s): return html.escape(s, quote=True)

svg = []
W, H = xy(38.8, 26.8)   # the whole drawing, in map units; the views are windows on it
svg.append(f'<path class="sea" d="{poly_d(sea, 0.0015, 0.0003)}"/>')
svg.append('<g class="g-wl">' + "".join(f'<path d="{d}"/>' for d in waterlines) + '</g>')

# territories under the water features
def area(cls, g, f, t=None):
    d = poly_d(g, 0.001)
    return f'<path class="{cls}" d="{d}"{attrs_ft(f, t)}/>' if d else ""
svg.append('<g class="g-areas">')
svg.append(area("a-wander", wander, IDX["years"], IDX["years"]))
svg.append(area("a-isr", c_east, IDX["sihon"]))
svg.append(area("a-isr", c_south, IDX["south"]))
svg.append(area("a-isr", c_north, IDX["north"]))
svg.append(area("a-isr", T["dannorth"], IDX["divide"]))
svg.append(area("a-king", sihon, IDX["edom"], IDX["edom"]))
svg.append(area("a-king", T["manassehE"], IDX["edom"], IDX["edom"]))
svg.append(area("a-giant on", anakim, 0, IDX["south"]))
svg.append(area("a-giant gone", anakim, IDX["north"]))
svg.append(area("a-giant on", rephaim, 0, IDX["edom"]))
svg.append(area("a-giant gone", rephaim, IDX["sihon"]))
svg.append(area("a-giant former", moab, 0))
svg.append(area("a-giant former", ammon, 0))
svg.append(area("a-rem", philistia, IDX["divide"]))
svg.append(area("a-rem", sidon, IDX["divide"]))
svg.append('</g>')
svg.append(f'<path class="g-tribe" d="{line_d(wb, 0.0008)}"{attrs_ft(IDX["divide"], None)}/>')
svg.append(f'<path class="g-tribe" d="{line_d(eb, 0.0008)}"{attrs_ft(IDX["moab"], None)}/>')

# water
svg.append('<g class="g-lake">' + "".join(f'<path d="{poly_d(g, 0.0006, 0)}"/>' for g in lakes.values()) + '</g>')
svg.append(f'<path class="g-river" d="{line_d(nile, 0.002)}"/>')
svg.append(f'<path class="g-river" d="{line_d(jordan, 0.0008)}"/>')
svg.append('<g class="g-wadi">' + "".join(f'<path d="{smooth_d(p)}"/>' for _, p, _ in D.WADIS) + '</g>')

# mountains: a little hill with hachures, two sizes for the two views
def hill(lon, lat, s):
    x, y = xy(lon, lat)
    return (f'M{fmt(x-s)},{fmt(y+s*.45)}Q{fmt(x-s*.35)},{fmt(y-s*.9)} {fmt(x)},{fmt(y-s*.75)}'
            f'Q{fmt(x+s*.35)},{fmt(y-s*.9)} {fmt(x+s)},{fmt(y+s*.45)}'
            f'M{fmt(x+s*.15)},{fmt(y-s*.35)}l{fmt(s*.3)},{fmt(s*.55)}'
            f'M{fmt(x+s*.45)},{fmt(y-s*.25)}l{fmt(s*.25)},{fmt(s*.5)}')
MJ = [(33.975, 28.54, 6), (33.80, 28.70, 4.5), (34.15, 28.72, 4.5), (33.72, 28.40, 4), (34.10, 28.32, 4),
      (33.90, 28.90, 4), (35.50, 30.08, 5), (35.55, 30.32, 5), (35.60, 30.58, 5), (35.62, 30.82, 4.5),
      (35.86, 33.42, 6), (35.95, 33.85, 5), (36.15, 34.12, 5), (36.25, 33.70, 4.5),
      (35.16, 31.62, 4), (35.24, 32.00, 4), (35.30, 32.35, 3.5), (35.40, 33.05, 4), (35.75, 32.25, 4),
      (35.72, 31.70, 3.5), (34.85, 30.62, 3.5), (34.95, 30.45, 3.5)]
ML = [(35.86, 33.42, 3.4), (35.80, 33.52, 2.4), (35.95, 33.36, 2.4), (35.52, 30.10, 2.4), (35.55, 30.30, 2.4),
      (35.58, 30.50, 2.4), (35.60, 30.70, 2.4), (35.63, 30.88, 2.2),
      (35.12, 31.48, 2), (35.18, 31.66, 2), (35.20, 31.84, 1.8), (35.22, 31.99, 1.8), (35.30, 32.10, 1.8),
      (35.33, 32.30, 1.8), (35.274, 32.236, 1.6), (35.273, 32.20, 1.6), (35.39, 32.687, 1.8),
      (35.42, 32.46, 1.8), (35.02, 32.71, 1.8), (35.09, 32.65, 1.6), (35.40, 33.00, 2), (35.45, 33.10, 2),
      (35.35, 32.92, 1.8), (35.70, 32.05, 2), (35.76, 32.30, 2), (35.80, 32.45, 1.8), (35.725, 31.765, 1.9),
      (35.70, 31.62, 1.8), (35.66, 31.30, 1.8), (35.03, 30.88, 2), (34.93, 30.92, 1.8),
      (33.975, 28.54, 2.8), (33.88, 28.64, 2.2), (34.07, 28.63, 2.2), (33.80, 28.45, 2), (34.10, 28.40, 2),
      (33.92, 28.85, 2), (34.15, 28.75, 2), (33.70, 28.62, 1.8), (35.50, 29.90, 2.2), (35.45, 29.70, 2)]
svg.append('<g class="g-mt mt-j">' + "".join(f'<path d="{hill(a, b, s)}"/>' for a, b, s in MJ) + '</g>')
svg.append('<g class="g-mt mt-l">' + "".join(f'<path d="{hill(a, b, s)}"/>' for a, b, s in ML) + '</g>')

# roads
for name, f, t, pts in D.ROADS:
    svg.append(f'<path class="g-road" d="{smooth_d(pts)}"{attrs_ft(IDX[f], si(t))}/>')

# the borders promised (Numbers 34), from the plains of Moab on
svg.append(f'<path class="g-promise" d="{smooth_d(D.PROMISED)}"{attrs_ft(IDX["moab"], None)}/>')

# Nebo sight lines
nx, ny = xy(D.P["nebo"]["lon"], D.P["nebo"]["lat"])
sight = "".join(f'M{fmt(nx)},{fmt(ny)}L{fmt(xy(*p)[0])},{fmt(xy(*p)[1])}' for p in D.SIGHT)
svg.append(f'<path class="g-sight" d="{sight}"{attrs_ft(IDX["nebo"], IDX["nebo"])}/>')

# routes
masks, segs = [], []
order = {}
for n, (k, kind, pts) in enumerate(D.SEGS):
    i = IDX[k]
    o = order.get(i, 0); order[i] = o + 1
    d = smooth_d([pt(p) for p in pts])
    masks.append(f'<mask id="jm-m{n}" maskUnits="userSpaceOnUse" x="0" y="0" width="{fmt(W)}" height="{fmt(H)}">'
                 f'<path class="mk" d="{d}" pathLength="1"/></mask>')
    arrow = ' marker-end="url(#jm-ar)"' if kind in ("camp", "march", "spies", "return") else ""
    segs.append(f'<g class="seg k-{kind}" data-f="{i}" data-o="{o}" mask="url(#jm-m{n})">'
                f'<path d="{d}"{arrow}/></g>')
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
    dots.append(f'<g class="pl {kind} t{p["tier"]}" data-id="{pid}" data-f="{first[pid]}" data-a="{act}">'
                f'<path class="d" d="M{fmt(x)},{fmt(y)}h0"/><path class="di" d="M{fmt(x)},{fmt(y)}h0"/>{rings}'
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
for k, (text, lon, lat) in D.TRIBE_LABELS.items():
    f = IDX["moab"] if k in D.EAST else IDX["divide"]
    alab.append(label(text, lon, lat, "al tribe", f, None))
for text, lon, lat, f, t, kind, view, act in D.GIANT_LABELS:
    cls = "al giant " + kind + (" v" + view if view else "")
    a = ",".join(str(IDX[k]) for k in act)
    alab.append(label(text, lon, lat, cls, IDX[f], si(t)).replace("<text ", f'<text data-a="{a}" ', 1))
for name, pts, li in D.WADIS:
    if name and li is not None:
        (a1, b1), (a2, b2) = pts[li - 1], pts[li]
        x1, y1 = xy(a1, b1); x2, y2 = xy(a2, b2)
        ang = math.degrees(math.atan2(y2 - y1, x2 - x1))
        if ang > 90: ang -= 180
        if ang < -90: ang += 180
        lon, lat = (a1 + a2) / 2, (b1 + b2) / 2
        alab.append(label(name, lon, lat, "al river w", 0, None, round(ang)))
for name, f, t, pts in D.ROADS:
    (a1, b1), (a2, b2) = pts[3], pts[4]
    x1, y1 = xy(a1, b1); x2, y2 = xy(a2, b2)
    ang = math.degrees(math.atan2(y2 - y1, x2 - x1))
    if ang > 90: ang -= 180
    if ang < -90: ang += 180
    alab.append(label(name, (a1 + a2) / 2, (b1 + b2) / 2, "al road", IDX[f], si(t), round(ang)))
(a1, b1), (a2, b2) = D.PROMISED[5], D.PROMISED[6]
x1, y1 = xy(a1, b1); x2, y2 = xy(a2, b2)
alab.append(label("the borders promised", (a1 + a2) / 2, (b1 + b2) / 2 - 0.05, "al promise", IDX["moab"], None,
                  round(math.degrees(math.atan2(y2 - y1, x2 - x1)))))
svg.append('<g class="g-al">' + "".join(alab) + '</g>')
svg.append('<g class="g-pt">' + "".join(labels) + '</g>')

defs = f'''<defs>
<pattern id="jm-hg" patternUnits="userSpaceOnUse" width="6" height="6" patternTransform="rotate(45)"><path d="M0,0V6" class="hg"/></pattern>
<pattern id="jm-hr" patternUnits="userSpaceOnUse" width="7" height="7" patternTransform="rotate(-45)"><path d="M0,0V7M3.5,0V7" class="hr"/></pattern>
<pattern id="jm-hw" patternUnits="userSpaceOnUse" width="6" height="6" patternTransform="rotate(30)"><path d="M0,0V6" class="hw"/></pattern>
<marker id="jm-ar" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="4.2" markerHeight="4.2" orient="auto-start-reverse"><path d="M0,1L9,5L0,9Z" class="ar"/></marker>
{"".join(masks)}
</defs>'''

VB_J = [xy(30.45, 35.25)[0], xy(30.45, 35.25)[1]]
VB_J += [xy(38.3, 35.25)[0] - VB_J[0], None]
VB_J[3] = VB_J[2] / 0.82
VB_L = [xy(33.72, 33.76)[0], xy(33.72, 33.76)[1]]
VB_L += [xy(36.92, 33.76)[0] - VB_L[0], None]
VB_L[3] = VB_L[2] / 0.82
VB_J = [round(v, 1) for v in VB_J]
VB_L = [round(v, 1) for v in VB_L]

# Each stage's own frame: its routes and the places it names, with a margin,
# no closer than MIN_H map units tall, kept inside the whole-journey view.
MIN_H = 200
EXTRA = {"nebo": D.SIGHT, "moab": D.PROMISED}
def frame(st):
    pts = [pt(p) for k, kind, ps in D.SEGS if k == st["key"] for p in ps]
    pts += [pt(a) for a in st["act"]] + EXTRA.get(st["key"], [])
    xs, ys = zip(*[xy(*p) for p in pts])
    w, h = (max(xs) - min(xs)) * 1.4, (max(ys) - min(ys)) * 1.4
    h = min(VB_J[3], max(h, w / 0.82, MIN_H)); w = h * 0.82
    x = min(max((max(xs) + min(xs) - w) / 2, VB_J[0]), VB_J[0] + VB_J[2] - w)
    y = min(max((max(ys) + min(ys) - h) / 2, VB_J[1]), VB_J[1] + VB_J[3] - h)
    return [round(v, 1) for v in (x, y, w, h)]

svg_html = (f'<svg class="jm-svg" viewBox="{" ".join(map(str, VB_J))}" role="img" '
            f'aria-label="Map of the journey from Egypt to the land of Canaan">{defs}{"".join(svg)}</svg>')

# ------------------------------------------------------------------ captions and data
ABBR = {"Genesis": "genesis", "Exodus": "exodus", "Numbers": "numbers", "Deuteronomy": "deuteronomy",
        "Joshua": "joshua", "Judges": "judges"}
REF = re.compile(r"\{(\w+) (\d+):(\d+)\}")
def caption(text):
    t = esc(text).replace("&quot;", '"').replace("&#x27;", "'")
    def r(m):
        b, c, v = m.group(1), m.group(2), m.group(3)
        return f'<a class="jm-ref" href="#/{ABBR[b]}/{c}" data-r="{ABBR[b]}|{c}|{v}">{b}&nbsp;{c}:{v}</a>'
    t = REF.sub(r, t)
    # adjacent refs read as one parenthesis: (Exodus 12:37; Numbers 33:3)
    A = r'<a class="jm-ref"[^>]*>[^<]*</a>'
    t = re.sub(f"({A}(?:\\s+{A})*)", lambda m: "(" + "; ".join(re.findall(A, m.group(1))) + ")", t)
    return t

stages = [dict(t=s["title"], w=s["when"], c=s["cam"], v=frame(s), x=caption(s["text"])) for s in D.STAGES]
notes = {pid: dict(n=p["name"], s=p["sure"], x=caption(p["note"]) if p["note"] else "")
         for pid, p in D.P.items() if pid in first}
blob = json.dumps(dict(stages=stages, places=notes, vb=dict(j=VB_J, l=VB_L), bones=True), ensure_ascii=False, separators=(",", ":"))
blob = blob.replace("</", "<\\/")

TEMPLATE = open(os.path.join(HERE, "..", "template.html"), encoding="utf-8").read()
out = (TEMPLATE.replace("@@SVG@@", svg_html).replace("@@DATA@@", blob)
       .replace("@@N@@", str(len(stages))).replace("@@KEY@@", D.KEY).replace("@@SRC@@", D.SRC)
       .replace("@@CART@@", D.CART).replace("@@ASPECT@@", D.ASPECT).replace("@@ROOTCLASS@@", "")
       .replace("@@FROM@@", "Egypt").replace("@@CLOSE@@", "Close up"))
fm = ("---\nkind: supplement\norder: 1\ntitle: From Egypt to the Land\n---\n\n"
      "<!-- Made by maps/journey/make.py from maps/journey/data.py: edit those and rebuild. -->\n")
open(OUT, "w", encoding="utf-8").write(fm + out + "\n")
print("wrote books/6-joshua/S1.md,", len(out) // 1024, "KB")
