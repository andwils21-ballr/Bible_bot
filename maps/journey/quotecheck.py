"""Every “quoted” phrase in a caption or note must appear word for word in a
verse the same sentence cites, as this project renders it."""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import data as D
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
books = {b["slug"]: b for b in json.load(open(os.path.join(ROOT, "manifest.json")))["books"]}
SLUG = {"Genesis": "genesis", "Exodus": "exodus", "Numbers": "numbers", "Deuteronomy": "deuteronomy",
        "Joshua": "joshua", "Judges": "judges"}
def verse(book, c, v):
    b = books[SLUG[book]]
    t = open(os.path.join(ROOT, "books", f"{b['order']}-{b['slug']}", f"{int(c):02d}.md"), encoding="utf-8").read()
    m = re.search(r"\*\*%s\*\* (.*?)(?:\n\s*\n|\n---)" % v, t.split("\n## Notes")[0] + "\n\n", re.S)
    return " ".join(m.group(1).split()) if m else ""
bad = 0
texts = [("stage " + s["key"], s["text"]) for s in D.STAGES] + [("place " + k, p["note"]) for k, p in D.P.items() if p["note"]]
for where, text in texts:
    for sent in re.split(r"(?<=[.!?])\s+(?=[A-Z“])", text):
        refs = re.findall(r"\{(\w+) (\d+):(\d+)\}", sent)
        for q in re.findall(r"“([^”]+)”", sent):
            q2 = q.rstrip(",")
            hit = any(q2 in verse(b, c, v) for b, c, v in refs)
            if not hit:
                bad += 1
                print("NOT FOUND", where, "|", q2, "|", refs)
print("quotes checked; problems:", bad)
