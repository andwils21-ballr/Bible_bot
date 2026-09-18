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

## Genesis 31/32 numbering — RESOLVED, we follow the KJV division (2026-09-16)

The Hebrew source starts chapter 32 with Laban going home in the morning;
English Bibles put that sentence at the end of chapter 31 as 31:55. I had
followed the Hebrew. You said KJV-close numbering is more convenient for
comparisons, so I moved it: **Genesis 31 now ends at verse 55 and Genesis 32 has
32 verses**, the same as a KJV/NIV/ESV. Cross-references in the notes of
chapters 30, 33 and 35 were updated to match.

This is now a standing rule in `RENDERING_SPEC.md` under "Versification": where
an English tradition exists, match it; where it does not (Enoch, Jubilees,
Meqabyan), follow the source. The next place it will bite is Psalms, where the
Hebrew counts *A psalm of David* as verse 1 and English does not — we'll follow
English there too.

## Exodus 7/8 — the Hebrew and English chapter divisions differ

Found while rendering, 2026-09-17. The Hebrew of Exodus 7 runs to **29 verses**,
not 25: the announcement of the frogs sits at Hebrew 7:26-29, where English
Bibles print it as 8:1-4. Hebrew chapter 8 then has 28 verses where English has
32. The totals match exactly (4 + 28 = 32), so nothing is missing on either
side -- only the seam between the chapters moves.

Per the spec's versification rule this rendering follows the English division,
so `books/2-exodus/08.md` has 32 verses while `source_text.py exodus 8` prints
28. That mismatch is expected and is stated in the first note of chapter 8.
`manifest.json` is correct at 40 chapters and needs no change.

Worth knowing this will recur: the same offset affects Hebrew/English numbering
in several places later (Psalms superscriptions, Malachi, Joel).

## The Septuagint is now a second witness for Genesis and Exodus

Added 2026-09-17, after checking the rendered work against it.

`sources/greek/genesis.txt` (1,530 verses) and `sources/greek/exodus.txt`
(1,172 verses) now sit beside the Hebrew, so `source_text.py genesis 11`
prints both and the divergence detector runs on the pair. Swete's Greek was
already in the repo for the deuterocanon; these two books cost nothing but
a line in `fetch_swete.py`.

**One caveat that will bite a render session.** Swete follows the *Greek*
verse division, which parts from the Hebrew in places. Exodus is the known
one: Hebrew 7:26-29 is Greek and English 8:1-4, so for that chapter the two
printed sources are four verses out of step with each other. The helper
prints both as they stand and does not try to align them.

What the check turned up is in the commit; the short version is that four
notes were strengthened, one was wrong and is fixed, and three new notes
were added at Genesis 1:14, 11:13 and 46:27.

## Genesis 35:21/22 — another Swete versification offset, and a near-miss

Added 2026-09-18.

While replacing "concubine" I read Swete's Genesis 35:22 as *And the sons of
Jacob were twelve* and nothing else, and reported to Andrew that the Greek had
dropped the Reuben and Bilhah incident. **That was wrong.** Checking the raw
Swete word index (words 22100-22127) shows the incident is there in full — it
is versified as the tail of **35:21**, not 35:22. Nothing was lost in
`fetch_swete.py`; the offset is Swete's own.

The Greek in fact has **more** than the Hebrew here. Hebrew 35:22 stops at
*And Israel heard.* Swete adds *kai ponēron ephanē enantion autou* — **and it
appeared evil before him**. The Hebrew records the hearing and refuses to
record the reaction; the Greek supplies it.

**The lesson, and it is the OCP truncation lesson again:** when a verse looks
short or a passage looks missing, check the verse on either side before
concluding anything. Two of the three false alarms in this project so far have
been a unit or verse boundary, not a missing text. A single verse printed alone
is not evidence that anything is absent.

## Exodus 21:22-23 renders the Greek, not the Hebrew — the first such departure

Added 2026-09-18, at Andrew's instruction.

Everywhere else in Genesis and Exodus the body text renders the **Hebrew** and
the Greek appears only in the notes. This verse is the exception, and it is
deliberate, so it should not be "corrected" by a later session.

- **Hebrew**: the test is *ason*, harm. No *ason* → a fine; *ason* → life for
  life. The Hebrew never says whose harm, the woman's or the child's.
- **Greek**: the test is whether the child came out *mē exeikonismenon*, **not
  yet formed**. Unformed → a fine; formed → life for life.

The two are not versions of each other: one asks what damage was done, the
other how far along the pregnancy was. Andrew chose the Greek.

**The precedent this sets, and its limit.** It does not make the rendering
"whichever witness reads better." The rule stays: render the Hebrew, note the
Greek. A departure like this one happens only when Andrew asks for it by verse,
and every instance gets a paragraph here. If a future session finds a second
one undocumented, that is drift, not policy.
