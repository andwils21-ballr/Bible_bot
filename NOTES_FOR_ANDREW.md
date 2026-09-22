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

## Swete's Greek reorders and shortens the tabernacle chapters

Added 2026-09-18, while rendering Exodus 28.

Hebrew Exodus 28 has 43 verses; Swete's Greek has 39, and the contents are not
in the same order — Greek 28:30, for instance, is the gold bells and
pomegranates, which is Hebrew 28:34. This is not the one-verse offset seen at
Exodus 7/8 and 21/22. The Greek of the tabernacle section (roughly chapters
25-40) is a genuinely different edition: shorter, differently arranged, and in
places missing material the Hebrew has.

**What this means for a render session.** Do not cite a Greek verse number in
these chapters without checking what is actually at that number. `source_text.py`
prints both texts as they stand and does not align them, so the two columns will
not line up. Exodus 28 was rendered from the Hebrew with no Greek claims made,
which is the safe default here. Where a Greek reading is worth a note in
chapters 25-40, quote the Greek words and say where they sit, rather than
giving a verse reference that will not check out.

---

## Leviticus 5/6: the Hebrew and English chapters do not divide at the same place

Found 2026-09-22, before rendering Leviticus 6, by counting verses per chapter
in `sources/hebrew/leviticus.txt`.

Hebrew Leviticus 5 runs to **26 verses**; English Leviticus 5 stops at **19**.
Hebrew chapter 6 runs to **23 verses**; English chapter 6 has **30**. The seven
verses in between are the same text under two different addresses:

| English | Hebrew |
|---|---|
| 6:1-7 | 5:20-26 |
| 6:8-30 | 6:1-23 |

`RENDERING_SPEC.md` says to follow the English/KJV division, so English 6:1 must
be rendered from Hebrew 5:20, and the Hebrew chapter-6 material starts at
English 6:8. Getting this wrong would shift the whole chapter by seven verses
and would not be visible from the English side.

Chapters 3, 4 and 5 are unaffected — Hebrew and English agree verse for verse
through Leviticus 5:19.

**This is the same class of problem as the Exodus 7/8 and 21/22 offsets.** Check
the per-chapter verse counts against an English Bible before rendering any
chapter in a book where an offset is suspected, not after.

## Twelve British spellings survive in Genesis and Exodus

Found 2026-09-22 while rendering Leviticus 6-9, by checking the new chapters
against the rest of the corpus.

The project is overwhelmingly American-spelled: 49 `color`, 35 `favor`, 27
`neighbor`, 10 `honor`. Against that, twelve stragglers remain across ten
files, all of them inside notes rather than rendered verses:

| File | Word |
|---|---|
| `1-genesis/01.md` | neighbour |
| `1-genesis/24.md` | defence |
| `1-genesis/31.md` | honour, defence |
| `1-genesis/34.md` | honour |
| `1-genesis/35.md` | favour |
| `1-genesis/36.md` | honour |
| `1-genesis/37.md` | colour, favour |
| `1-genesis/40.md` | favour |
| `1-genesis/43.md` | favour |
| `2-exodus/28.md` | honour |

Eleven of the twelve are in Genesis, which Andrew signed off on 2026-09-21, so
they have been left alone rather than swept up on a scheduled cycle. They are a
one-command fix whenever he wants it. New chapters use American spelling.

## The Hebrew source drops Masoretically marked letters — including in the Shema

Found 2026-09-22 while rendering Leviticus 11. **This one matters.**

Leviticus 11:42 should read *holekh al gachon*, "goes on its belly" — the word
that ties the crawling things back to the serpent of Genesis 3:14. The file has
`גָּח`, missing the vav and the final nun. Checking further turned up a pattern:
`sources/hebrew/` silently drops letters that the Masoretic apparatus marks as
visually special (enlarged, suspended), and when the dropped letter is what
distinguishes the word, the word is truncated or disappears.

Tested against the standard list of enlarged, reduced and suspended letters:

| Reference | Word should be | File has | Marked letter |
|---|---|---|---|
| **Deuteronomy 6:4** | **שמע** | **שמ** | **large ayin** |
| **Deuteronomy 6:4** | **אחד** | **אח** | **large dalet** |
| Leviticus 11:42 | גחון | גח | large vav |
| Numbers 27:5 | משפטן | משפט | large nun |
| Deuteronomy 32:6 | הליהוה | ליהוה | large he |
| Judges 18:30 | מנשה | *word absent* | suspended nun |
| Psalm 80:14 | מיער | *word absent* | suspended ayin |
| Job 38:13 | רשעים | *word absent* | suspended ayin |

**The Shema is damaged in our source.** "Hear, O Israel… the LORD is one" is in
the file as *shem… echa*. Eight failures found; ten other special letters tested
came through intact (Genesis 1:1, Leviticus 1:1, Leviticus 13:33 and others), so
this is not total corruption, and ordinary words are unaffected.

**What this changes about how notes get written:**

1. Never build a note on the exact spelling of a word that carries one of these
   marks. The Leviticus 11:42 / Genesis 3:14 serpent link is real in the
   Masoretic text and was **left out of the rendering** because it cannot be
   checked here.
2. A rarity count from a consonantal search can undercount by one if the missing
   instance was a specially-marked word. The counts already published rest on
   ordinary words, but the caveat is real.
3. The rendered English is not affected — verse text and word order are intact.
   This is about what the notes are allowed to claim.

The list of these letters is finite and traditional, about twenty across the
whole Bible, so the exposure is bounded. A second Hebrew witness would close it.
`source_text.py` and `sources/` were left alone per the standing rule.

## Terminology decision: tsara'at rendered "blight", and Exodus 4:6 does not match

Made 2026-09-22 while rendering Leviticus 13. **Andrew should rule on this**, because
it recurs through chapter 14 and into Numbers, 2 Kings and 2 Chronicles.

*Tsara'at* is not leprosy. The chapter legislates for something that turns hair
white, that can cover a body completely and leave the person **clean** (13:13),
and that breaks out in wool, linen and leather (13:47-59) and in the plaster of
a house (14:37). No single illness does all of that, and at Exodus 4:6 it comes
and goes from Moses' hand inside two verses.

Leviticus 13 renders it **"blight"** — the one ordinary English word that covers
skin, cloth and masonry without naming a disease, and without flattening the
dread the Hebrew carries. *Nega* is **"mark"**, from *naga*, to touch.

**The inconsistency:** `books/2-exodus/04.md` already renders *metsora'at* as
**"diseased"**, and its v6 note explains that it is not modern leprosy. That was
a good call for a one-word narrative moment, but it does not match "blight", and
rule 0 lists cross-chapter term drift as something the pass exists to catch.

Exodus 4:6 was **left alone** rather than harmonized, because Andrew's ruling of
2026-09-21 is that the readability pass applies to newly created chapters only
and does not sweep back over finished ones. The choice is his:

1. Leave both. "Diseased" in a narrative, "blight" in the law.
2. Change Exodus 4:6 to "blighted" and trim its note to point at Leviticus 13.
3. Use something else in both, and Leviticus 13-14 gets rewritten to match.

## Still waiting on the tsara'at ruling

Leviticus 14 was rendered 2026-09-22 using **"blight"**, consistent with chapter 13,
because the scheduled cycle cannot wait on a decision and the whole chapter turns on
the word. If Andrew picks a different rendering it is a mechanical find-and-replace
across `books/3-leviticus/13.md` and `14.md` plus the two notes that name it, not a
rewrite. `books/2-exodus/04.md` still reads "diseased" and is still untouched.

## Term drift: to'evah is "abomination" in Genesis and "detestable" in Exodus

Found 2026-09-22 while rendering Leviticus 18, which uses the word four times.

Three different Hebrew words are currently colliding onto two English ones:

| Hebrew | Where | Rendered |
|---|---|---|
| *to'evah* | Genesis 43:32, 46:34 | abomination |
| *to'evah* | Exodus 8:26 | detestable |
| *sheqets* | Leviticus 11:10-13, 41-43 | detestable |

So *to'evah* has two English words, and one of them is shared with a different
Hebrew word. Worse: **the note on Exodus 8:26 misquotes our own Genesis.** It
prints *"for that is detestable to Egypt (43:32)"*, but `books/1-genesis/43.md`
actually reads **abomination**. That is a factual error in a note, not a style
preference.

Leviticus 18 uses **"abomination"** for *to'evah*, matching Genesis and keeping it
distinct from *sheqets*. Exodus 8:26 was **left untouched** — fixing it means
choosing which word wins, and that is the same kind of decision as the pending
*tsara'at* ruling, so it should not be made unilaterally on a scheduled cycle.

Andrew's options:
1. Harmonize Exodus 8:26 to "abomination" (two words in the verse, two in the note).
2. Leave the verse and fix only the misquote in the note.
3. Pick a third word for *to'evah* everywhere.

Genesis is signed off, so option 3 would need his explicit go-ahead to touch it.
