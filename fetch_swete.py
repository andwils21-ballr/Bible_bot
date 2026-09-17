#!/usr/bin/env python3
"""Extract the deuterocanonical books from Swete's Septuagint into this
project's `<chapter>:<verse>\t<text>` format.

Swete, THE OLD TESTAMENT IN GREEK ACCORDING TO THE SEPTUAGINT (Cambridge,
1909-1930), is public domain by age. Two files carry the text: a
versification index (word-number -> Book.Chapter:Verse) and the word list.
A verse is the words from its own index up to the next verse's index.

Only the Greek words and their verse numbers are taken -- not the
morphology, transliteration or gloss layers added by the digitisers.

    python3 fetch_swete.py sources/swete-src
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))

# Swete abbreviation -> (book slug, chapter offset)
# Susanna and Bel are printed as separate books; in this canon they are
# Daniel 13 and 14, so they are written into daniel.txt at that offset.
BOOKS = {
    "Tob": ("tobit", 0),
    "Jdt": ("judith", 0),
    "Wis": ("wisdom-of-solomon", 0),
    "Sir": ("sirach", 0),
    "Bar": ("baruch", 0),
    "Epj": ("letter-of-jeremiah", 0),
    "Est": ("esther", 0),
    "Sus": ("daniel", 12),
    "Bel": ("daniel", 13),
}


def load(src):
    words = {}
    with open(os.path.join(src, "01-Swete_word_with_punctuations.csv"),
              encoding="utf-8") as f:
        for line in f:
            if "\t" in line:
                i, w = line.rstrip("\n").split("\t", 1)
                words[int(i)] = w
    refs = []
    with open(os.path.join(src, "00-Swete_versification.csv"),
              encoding="utf-8") as f:
        for line in f:
            if "\t" in line:
                i, r = line.rstrip("\n").split("\t")
                refs.append((int(i), r))
    refs.sort()
    return words, refs


def main(src):
    words, refs = load(src)
    out = {}
    for k, (start, ref) in enumerate(refs):
        book, cv = ref.split(".", 1)
        if book not in BOOKS:
            continue
        slug, offset = BOOKS[book]
        end = refs[k + 1][0] if k + 1 < len(refs) else max(words) + 1
        text = " ".join(words[j] for j in range(start, end) if j in words)
        text = " ".join(text.split())
        if not text:
            continue
        chap, verse = cv.split(":", 1)
        out.setdefault(slug, []).append((int(chap) + offset, verse, text))

    for slug, rows in sorted(out.items()):
        rows.sort(key=lambda r: (r[0], r[1].zfill(4)))
        path = os.path.join(ROOT, "sources", "greek", slug + ".txt")
        with open(path, "w", encoding="utf-8") as f:
            for c, v, t in rows:
                f.write(f"{c}:{v}\t{t}\n")
        chapters = len({c for c, _, _ in rows})
        print(f"{slug:22} {len(rows):5} verses  {chapters:3} chapters"
              f"  -> sources/greek/{slug}.txt")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "sources/swete-src")
