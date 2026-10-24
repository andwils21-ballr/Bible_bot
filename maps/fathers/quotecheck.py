"""Every quoted phrase in a caption or note, “in quotation marks” or *in italics*,
must appear word for word in a verse it cites, as this project renders it:
first the verses its own sentence cites, then any the caption or note cites.
An italic phrase with nothing cited is listed to check by hand (most are names)."""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import data as D
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
books = {b["slug"]: b for b in json.load(open(os.path.join(ROOT, "manifest.json")))["books"]}
SLUG = {"Genesis": "genesis", "Joshua": "joshua", "2 Chronicles": "2-chronicles", "Psalm": "psalms"}
REF = r"\{((?:\d )?\w+) (\d+):(\d+)\}"
def verse(book, c, v):
    b = books[SLUG[book]]
    t = open(os.path.join(ROOT, "books", f"{b['order']}-{b['slug']}", f"{int(c):02d}.md"), encoding="utf-8").read()
    m = re.search(r"\*\*%s\*\* (.*?)(?:\n\s*\n|\n---)" % v, t.split("\n## Notes")[0] + "\n\n", re.S)
    return " ".join(m.group(1).split()) if m else ""
def found(q, refs):
    """Each piece of a quote cut with "…" must be in one cited verse, or in the
    cited verses read together (a quote that runs on into the next verse)."""
    text = [verse(b, c, v).lower() for b, c, v in refs]
    return bool(refs) and all(any(part in t for t in text + [" ".join(text)])
                              for part in [x.strip(" ,") for x in q.lower().split("…")])
bad = 0
texts = [("stage " + s["key"], s["text"]) for s in D.STAGES] + [("place " + k, p["note"]) for k, p in D.P.items() if p["note"]]
for where, text in texts:
    allrefs = re.findall(REF, text)
    for sent in re.split(r"(?<=[.!?])\s+(?=[A-Z“*])", text):
        refs = re.findall(REF, sent)
        for kind, q in [("quote", q) for q in re.findall(r"“([^”]+)”", sent)] + \
                       [("italic", q) for q in re.findall(r"\*([^*]+)\*", sent)]:
            if found(q, refs) or found(q, allrefs):
                continue
            if kind == "italic" and not allrefs:
                print("BY HAND  ", where, "|", q)
                continue
            bad += 1
            print("NOT FOUND", where, "|", q, "|", refs or allrefs)
print("quotes checked; problems:", bad)
