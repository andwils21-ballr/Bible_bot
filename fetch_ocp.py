#!/usr/bin/env python3
"""Convert Online Critical Pseudepigrapha TEI-ish XML into this project's
`<chapter>:<verse>\t<text>` files, one per witness language.

The OCP format splits a single verse into several <unit> elements so it can
carry an apparatus, and each unit offers one or more <reading option="N">.
Option 0 is the base reading. A verse is every unit's option-0 reading joined
in document order -- reading only the first unit truncates two thirds of them.

    python3 fetch_ocp.py <dir-of-xml>
"""
import os
import sys
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.abspath(__file__))

# xml file -> book slug in manifest.json
BOOKS = {
    "1En.xml": "1-enoch",
    "Jub.xml": "jubilees",
    "4Ezra.xml": "ezra-sutuel",
    "4Bar.xml": "4-baruch",
}

LANG_DIR = {
    "Ethiopic": "ethiopic", "Greek": "greek", "Aramaic": "aramaic",
    "Latin": "latin", "Syriac": "syriac", "Hebrew": "hebrew",
}


def verses(version):
    """-> [(chapter, verse, text)], joining every unit of each verse."""
    out = []
    text = version.find("text")
    if text is None:
        return out
    for chap in text.findall("div"):
        cn = chap.get("number")
        for vs in chap.findall("div"):
            parts = []
            for unit in vs.findall("unit"):
                readings = unit.findall("reading")
                if not readings:
                    continue
                base = next((r for r in readings if r.get("option") == "0"),
                            readings[0])
                if base.text:
                    parts.append(base.text.strip())
            line = " ".join(p for p in parts if p)
            line = " ".join(line.split())
            if line:
                out.append((cn, vs.get("number"), line))
    return out


def write(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for c, v, t in rows:
            f.write(f"{c}:{v}\t{t}\n")
    chapters = len({c for c, _, _ in rows})
    return len(rows), chapters


def main(src):
    for fname, slug in BOOKS.items():
        path = os.path.join(src, fname)
        if not os.path.exists(path):
            print(f"# {fname}: not found, skipped")
            continue
        root = ET.parse(path).getroot()
        for version in root.findall("version"):
            lang = version.get("language")
            title = (version.get("title") or "").strip()
            rows = verses(version)
            if not rows:
                continue
            if lang in LANG_DIR:
                out = os.path.join(ROOT, "sources", LANG_DIR[lang], slug + ".txt")
            elif lang == "English":
                witness = title.replace("(English)", "").strip().lower()
                witness = witness.replace(" ", "-") or "english"
                out = os.path.join(ROOT, "sources", "english",
                                   f"{slug}.{witness}.txt")
            else:
                continue
            n, ch = write(out, rows)
            print(f"{slug:14} {lang:10} {title[:26]:26} {n:5} verses  {ch:3} ch"
                  f"  -> {os.path.relpath(out, ROOT)}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "/tmp/ocp/static/docs")
