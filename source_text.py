#!/usr/bin/env python3
"""Print the source text of a chapter, for the session that is rendering it.

    python3 source_text.py genesis 4
    python3 source_text.py john 1

When there is no source file, says what the book's tier requires instead —
an english-only-tier book is worked from established translations, a none-tier
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
    LANGS = ("hebrew", "greek", "aramaic", "ethiopic", "syriac", "latin")
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
        _english(slug, lookup_chapter)
        _divergence(slug, lookup_chapter)
        return
    if found:
        # Witness files exist for this book, but none of them reaches this
        # chapter. That is the english-only case, and the session needs telling.
        print("NO WITNESS COVERS THIS CHAPTER.")
        print("Per RENDERING_SPEC.md treat it as tier 'english-only': work from an\n"
              "established English translation, never from memory, and say so in\n"
              "the first note of the chapter.")
        return

    books = json.load(open(os.path.join(ROOT, "manifest.json"),
                           encoding="utf-8"))["books"]
    tier = next((b["tier"] for b in books if b["slug"] == slug), None)
    print(f"NO SOURCE-LANGUAGE FILE for '{slug}' (tier: {tier}).")
    if tier == "english-only":
        print("Per RENDERING_SPEC.md this book is worked from established English\n"
              "translations, NOT from the Ge'ez and NOT from memory. Say which\n"
              "tradition you are following in the first note of chapter 1.")
    elif tier == "none":
        print("Per RENDERING_SPEC.md write the (NEED SOURCE TO TRANSLATE) stub\n"
              "and move on to the next renderable book. Do not attempt the text.")
    else:
        print("This book is tier 'source' but has no source file — that is a\n"
              "gap in fetch_sources.py, not a licence to render from memory.\n"
              "Record it in NOTES_FOR_ANDREW.md and skip to the next book.")


WITNESS_LANGS = ("hebrew", "greek", "aramaic", "ethiopic", "syriac", "latin")


def _load(path, chapter):
    rows = {}
    if not os.path.exists(path):
        return rows
    with open(path, encoding="utf-8") as f:
        for line in f:
            ref, _, text = line.partition("\t")
            ch, _, vs = ref.partition(":")
            if ch == chapter and vs.isdigit():
                rows[int(vs)] = text.rstrip("\n")
    return rows


def _english(slug, chapter):
    """The OCP's scholarly English for each witness.

    A claim about what a witness *means* rests on these, not on the renderer's
    own reading of a language it cannot check.
    """
    import glob
    files = sorted(glob.glob(os.path.join(ROOT, "sources", "english",
                                          slug + ".*.txt")))
    printed = False
    for path in files:
        rows = _load(path, chapter)
        if not rows:
            continue
        name = os.path.basename(path).split(".")[1]
        if not printed:
            print("# " + "=" * 62)
            print("# scholarly English of each witness — use this for MEANING")
            printed = True
        print(f"\n## {name} (English)")
        for v in sorted(rows):
            print(f"{v}\t{rows[v]}")
    if printed:
        print()


def _divergence(slug, chapter):
    """Flag, mechanically, where the witnesses disagree.

    This makes no claim about meaning — it only says where to look. Two things
    are checkable without reading any of these languages: which witnesses carry
    a verse at all, and where one is markedly fuller than another.
    """
    wit = {}
    for lang in WITNESS_LANGS:
        rows = _load(os.path.join(ROOT, "sources", lang, slug + ".txt"), chapter)
        if rows:
            wit[lang] = rows
    if len(wit) < 2:
        return
    print("# " + "=" * 62)
    print("# WHERE THE WITNESSES DIVERGE (mechanical: coverage and length only)")
    langs = list(wit)
    for v in sorted(set().union(*(set(r) for r in wit.values()))):
        has = [l for l in langs if v in wit[l]]
        missing = [l for l in langs if v not in wit[l]]
        flags = []
        if missing:
            flags.append("only in " + ", ".join(has))
        if len(has) > 1:
            lens = {l: len(wit[l][v]) for l in has}
            lo, hi = min(lens, key=lens.get), max(lens, key=lens.get)
            if lens[lo] and lens[hi] / lens[lo] >= 2.0:
                flags.append(f"{hi} is {lens[hi]/lens[lo]:.1f}x the length of {lo}")
        if flags:
            print(f"  v{v}: " + "; ".join(flags))
    print("\n# These are places to look, not findings. What a difference means")
    print("# has to come from the English above or from the Greek/Aramaic.")
    print()


if __name__ == "__main__":
    main()
