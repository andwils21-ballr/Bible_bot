# Notes for Andrew

Things found while working that are yours to decide, not mine to change.

## Open: no Septuagint in `sources/` (2026-09-14)

Hebrew (Westminster Leningrad Codex) and the Greek New Testament (SBLGNT) are
both in `sources/`. No freely-fetchable Septuagint was found, so these are
worked from established English translations instead of a source language, and
are marked tier `secondary`:

- Tobit, Judith, Wisdom of Solomon, Sirach, Baruch, Letter of Jeremiah (106 ch)
- Psalm 151, Daniel 13-14, Esther 11-16 — past the end of the Hebrew text

If an LXX with a usable licence turns up, add it to `fetch_sources.py`, raise
those tiers, and fix the "Known gaps" paragraph in `RENDERING_SPEC.md`.

## Fixed: four manifest errors the source texts exposed (2026-09-14)

The chapter counts in `manifest.json` were written from memory and did not
survive contact with the actual texts:

- **Reproof (Tegsat)** is Proverbs 25-31, so its chapter 1 is Proverbs 25.
  Without an offset, every session would have rendered Proverbs 1 twice under
  two different book names. Fixed with `source_book` / `source_offset`.
- **Psalms** — the Hebrew has 150; Psalm 151 is Greek/Syriac only.
- **Daniel** — the Hebrew/Aramaic has 12; chapters 13-14 are Greek.
- **Esther** — the Hebrew has 10; the additions are Greek.

The lesson worth keeping: the manifest is still partly from memory, and the
remaining books' chapter counts have not been checked against anything.
Expect more of these as the project reaches books with no source file.

## Genesis 31/32: a one-verse numbering difference from English Bibles (2026-09-16)

The Hebrew text in `sources/` starts chapter 32 with Laban going home in the
morning. Every English Bible I know of puts that sentence at the **end of
chapter 31** instead, as 31:55, and then numbers chapter 32 as verses 1–32.

I followed the Hebrew, because that is the text I am rendering from and the spec
says to work from the source. The result:

- our Genesis 31 ends at verse 54; an English Bible's ends at 55
- our Genesis 32 has 33 verses; an English Bible's has 32
- so for this one chapter, our verse numbers run **one higher** than an NIV/ESV.
  The wrestling match is 32:25–33 here, 32:24–32 there.
- Genesis 33 lines up again, and so does everything after it.

I put a note at the top of the Genesis 32 notes so a reader comparing to a
printed Bible isn't lost. If you'd rather match the English numbering
everywhere — which would mean moving that verse back into chapter 31 — say so
and I'll change it before we get much further into the canon. It's a one-time
decision that will recur in a few other books (the Psalm headings in particular
are numbered as verse 1 in Hebrew and not counted in English, which shifts whole
psalms by one).
