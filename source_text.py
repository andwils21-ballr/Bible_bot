#!/usr/bin/env python3
"""Print the source text of a chapter, for the session that is rendering it.

    python3 source_text.py genesis 4
    python3 source_text.py john 1

When there is no source file, says what the book's tier requires instead —
a secondary-tier book is worked from established translations, a none-tier
book gets a stub. Neither is ever rendered from memory.
"""
import json
import os
import signal
import sys

# Sessions will pipe this into head; don't spew a traceback when they do.
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

ROOT = os.path.dirname(os.path.abspath(__file__))


def last_chapter(path):
    with open(path, encoding="utf-8") as f:
        return max(int(line.split(":", 1)[0]) for line in f if ":" in line)


def main():
    if len(sys.argv) != 3:
        sys.exit("usage: source_text.py <slug> <chapter>")
    slug, chapter = sys.argv[1], sys.argv[2]

    books = json.load(open(os.path.join(ROOT, "manifest.json"),
                           encoding="utf-8"))["books"]
    book = next((b for b in books if b["slug"] == slug), None)

    # Some books are a slice of another book's source (Reproof = Proverbs 25-31).
    lookup_slug = (book or {}).get("source_book", slug)
    offset = (book or {}).get("source_offset", 0)
    lookup_chapter = str(int(chapter) + offset)

    # A book may survive in several witnesses (1 Enoch is extant in Greek,
    # Ge'ez, Qumran Aramaic and Latin). Print every one that has this chapter,
    # because the places they disagree are the point.
    LANGS = ("hebrew", "greek", "aramaic", "ethiopic", "latin")
    found = covered = False
    for lang in LANGS:
        path = os.path.join(ROOT, "sources", lang, lookup_slug + ".txt")
        if not os.path.exists(path):
            continue
        rows = []
        with open(path, encoding="utf-8") as f:
            for line in f:
                ref, _, text = line.partition("\t")
                ch, _, vs = ref.partition(":")
                if ch == lookup_chapter:
                    rows.append((int(vs), text.rstrip("\n")))
        label = f"{lookup_slug} {lookup_chapter}" if offset else f"{slug} {chapter}"
        if not rows:
            print(f"# {label} — {lang}: this chapter is not extant in this "
                  f"witness (it covers chapter {last_chapter(path)} at most).")
            print()
            found = True
            continue
        print(f"# {label} — {lang} source")
        for vs, text in sorted(rows):
            print(f"{vs}\t{text}")
        print()
        found = True
        covered = True
    if covered:
        return
    if found:
        # Witness files exist for this book, but none of them reaches this
        # chapter. That is the secondary case, and the session needs telling.
        print("NO WITNESS COVERS THIS CHAPTER.")
        print("Per RENDERING_SPEC.md treat it as tier 'secondary': work from an\n"
              "established English translation, never from memory, and say so in\n"
              "the first note of the chapter.")
        return

    books = json.load(open(os.path.join(ROOT, "manifest.json"),
                           encoding="utf-8"))["books"]
    tier = next((b["tier"] for b in books if b["slug"] == slug), None)
    print(f"NO SOURCE-LANGUAGE FILE for '{slug}' (tier: {tier}).")
    if tier == "secondary":
        print("Per RENDERING_SPEC.md this book is worked from established English\n"
              "translations, NOT from the Ge'ez and NOT from memory. Say which\n"
              "tradition you are following in the first note of chapter 1.")
    elif tier == "none":
        print("Per RENDERING_SPEC.md write the (NEED SOURCE TO TRANSLATE) stub\n"
              "and move on to the next renderable book. Do not attempt the text.")
    else:
        print("This book is tier 'primary' but has no source file — that is a\n"
              "gap in fetch_sources.py, not a licence to render from memory.\n"
              "Record it in NOTES_FOR_ANDREW.md and skip to the next book.")


if __name__ == "__main__":
    main()
