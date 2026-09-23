#!/usr/bin/env python3
"""One-time fetch of the source texts into sources/.

Hebrew: Westminster Leningrad Codex (openscriptures/morphhb).
Greek NT: SBLGNT with MorphGNT parsing (morphgnt/sblgnt).

Both are converted to one plain file per book, one verse per line, formatted
`<chapter>:<verse>\t<text>` — small, greppable, and readable by a render session
without any parsing. Run once; the output is committed.

    python3 fetch_sources.py
"""
import os
import urllib.request
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.abspath(__file__))
WLC = "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/{}.xml"
GNT = "https://raw.githubusercontent.com/morphgnt/sblgnt/master/{}-morphgnt.txt"

HEBREW = {
    "genesis": "Gen", "exodus": "Exod", "leviticus": "Lev", "numbers": "Num",
    "deuteronomy": "Deut", "joshua": "Josh", "judges": "Judg", "ruth": "Ruth",
    "1-samuel": "1Sam", "2-samuel": "2Sam", "1-kings": "1Kgs", "2-kings": "2Kgs",
    "1-chronicles": "1Chr", "2-chronicles": "2Chr", "ezra": "Ezra",
    "nehemiah": "Neh", "esther": "Esth", "job": "Job", "psalms": "Ps",
    "proverbs": "Prov", "reproof-tegsat": "Prov", "ecclesiastes": "Eccl",
    "song-of-songs": "Song", "isaiah": "Isa", "jeremiah": "Jer",
    "lamentations": "Lam", "ezekiel": "Ezek", "daniel": "Dan", "hosea": "Hos",
    "joel": "Joel", "amos": "Amos", "obadiah": "Obad", "jonah": "Jonah",
    "micah": "Mic", "nahum": "Nah", "habakkuk": "Hab", "zephaniah": "Zeph",
    "haggai": "Hag", "zechariah": "Zech", "malachi": "Mal",
}

GREEK = {
    "matthew": "61-Mt", "mark": "62-Mk", "luke": "63-Lk", "john": "64-Jn",
    "acts": "65-Ac", "romans": "66-Ro", "1-corinthians": "67-1Co",
    "2-corinthians": "68-2Co", "galatians": "69-Ga", "ephesians": "70-Eph",
    "philippians": "71-Php", "colossians": "72-Col", "1-thessalonians": "73-1Th",
    "2-thessalonians": "74-2Th", "1-timothy": "75-1Ti", "2-timothy": "76-2Ti",
    "titus": "77-Tit", "philemon": "78-Phm", "hebrews": "79-Heb",
    "james": "80-Jas", "1-peter": "81-1Pe", "2-peter": "82-2Pe",
    "1-john": "83-1Jn", "2-john": "84-2Jn", "3-john": "85-3Jn",
    "jude": "86-Jud", "revelation": "87-Re",
}

OSIS = "{http://www.bibletechnologies.net/2003/OSIS/namespace}"


def get(url):
    with urllib.request.urlopen(url, timeout=120) as r:
        return r.read()


def hebrew_book(code):
    """WLC OSIS XML -> [(chapter, verse, text)]. Slashes mark morpheme splits
    in the source; they are stripped so the line reads as running Hebrew.
    A letter the Masoretes wrote large, small or raised sits in its own <seg>
    inside the word, so the word is all of its text, not just w.text (which
    stops at the first such letter and once dropped the ayin of Shema)."""
    root = ET.fromstring(get(WLC.format(code)))
    out = []
    for v in root.iter(OSIS + "verse"):
        osis_id = v.get("osisID")
        if not osis_id:
            continue
        _, ch, vs = osis_id.split(".")
        words = ["".join(w.itertext()).replace("/", "") for w in v.iter(OSIS + "w")]
        words = [w for w in words if w]
        out.append((int(ch), int(vs), " ".join(words)))
    return out


def greek_book(code):
    """MorphGNT: `BBCCVV pos parse text word normalized lemma` per line."""
    verses = {}
    for line in get(GNT.format(code)).decode("utf-8").splitlines():
        parts = line.split()
        if len(parts) < 5:
            continue
        ref = parts[0]
        key = (int(ref[2:4]), int(ref[4:6]))
        verses.setdefault(key, []).append(parts[3])
    return [(c, v, " ".join(w)) for (c, v), w in sorted(verses.items())]


def write(folder, slug, rows):
    os.makedirs(os.path.join(ROOT, "sources", folder), exist_ok=True)
    path = os.path.join(ROOT, "sources", folder, slug + ".txt")
    with open(path, "w", encoding="utf-8") as f:
        for ch, vs, text in rows:
            f.write(f"{ch}:{vs}\t{text}\n")
    return os.path.getsize(path)


def main():
    total = 0
    for folder, table, loader in (("hebrew", HEBREW, hebrew_book),
                                  ("greek", GREEK, greek_book)):
        for slug, code in table.items():
            size = write(folder, slug, loader(code))
            total += size
            print(f"  {folder}/{slug}.txt  {size // 1024} KB")
    print(f"total {total // 1024} KB")


if __name__ == "__main__":
    main()
