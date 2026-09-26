# The Jubilees loop

Andrew (2026-09-26): render Jubilees, chapter 1 to 50, run after run, until done
or until the week's allowance runs out. **Do your best work on every single
run.** Each run follows this file exactly. `CLAUDE.md` outranks it.

## Every run

1. **Sync and read.** `cd /home/user/bible_bot && git fetch origin main && git
   reset --hard origin/main`. Read `CLAUDE.md` in full, the spec's sections on
   the readability pass, "No And", notes, and Tier `witnesses` (the Jubilees
   rule), and the model notes at Genesis 25:21–23.
2. **Find the next chapter:** the first number from 1 to 50 with no file in
   `books/15-jubilees/`. If there is none, the book is done: say so, tell Andrew
   that 1 Meqabyan needs its own setup first (its Ge'ez is not yet in
   `sources/`, and no public-domain English of it has been found to check
   meaning against), and stop the loop.
3. **Match the voice.** Read the two most recent Jubilees chapters (for the
   first run, the last two 1 Enoch chapters).
4. **Print every chapter's source first:** `python3 source_text.py jubilees <n>`
   (chapter 1 also needs `python3 source_text.py jubilees 0`, the prologue).
   - The **EOTC Ge'ez** (`ethiopic-eotc`) is the base text and sets the verse
     count and numbering. Every EOTC verse gets a verse.
   - The **second Ge'ez text** (`ethiopic`, Ran HaCohen's) checks the EOTC.
     Where the EOTC lacks a verse (4:3–14, 26:33), fill it from the second
     Ge'ez; failing that from the Latin; failing that from Charles; and say in
     a note which source the verse comes from. A real difference in meaning
     between the two Ge'ez texts gets a note.
   - Compare the **Latin** (chapters 13–49 in part) and the **Greek** where they
     exist. The Greek lines are mostly short excerpts and summaries made by
     later writers, not continuous text; a difference there is worth a note
     only when it tells the event differently.
   - For meaning, use the **OCP English** (Latin, Greek) and **Charles** (all).
     Charles's bracketed dates (`[2073 A.M.]`) are his own sums, not the text:
     never carry them in. A claim about what a Ge'ez word means must rest on
     those English renderings; quote the Ge'ez, build no argument on its
     supposed root meaning.
   - **Jubilees retells Genesis 1 through the exodus.** Print the Genesis or Exodus
     verse it retells (`python3 source_text.py genesis 12`) and read this
     project's rendering of it (`books/1-genesis/`, `books/2-exodus/`). Where
     the Ge'ez says the same thing, use the same English wording, so the reader
     sees the same words. Where Jubilees adds, drops or changes something, that
     is the best material for a note.
   - Every New Testament or Old Testament link in a note must be printed and
     checked first. Never quote a verse from memory.
5. **Render four to six chapters.** Short chapters allow more; hard ones fewer.
   Stop one chapter early rather than rush the last.
6. **Final pass, before committing,** on this run's chapters only:
   - verse count equals the EOTC's for each chapter (plus any verse filled from
     another source, each with its note);
   - the readability pass (CLAUDE.md section 2, the spec's eight patterns);
   - no sentence starting with "And" except the spec's kept list; no banned
     words; no verse starting lowercase after a finished sentence;
   - the dates: every jubilee, week and year checked against the chapter's own
     arithmetic and the chapters before it; a number that breaks it is handled
     as 1 Enoch's are (follow the arithmetic, note what the EOTC reads, and
     list it in the report) until Andrew rules on choice #1 of the 1 Enoch 72
     report;
   - every note claim re-read against the printed source.
7. **Every chapter's last note** is **Source text**:
   `- **Source text** — Ge'ez: Beta Masaheft, Universität Hamburg (text of the
   EOTC printed Bible), CC BY-SA 4.0. English translation by this project.`
   Add the other sources used: *Second Ge'ez text: Ran HaCohen, via Beta
   Masaheft, CC BY-SA 4.0.* / *Latin and Greek: Online Critical
   Pseudepigrapha, CC BY 4.0.*
8. **Build and push:** `python3 build_site.py && python3 progress.py`; commit
   `Render Jubilees <first>–<last>` with the trailers; push to main.
9. **Report** at the top of `PASTE/renders/15-jubilees.md` (tables, Left
   standing on purpose, Choices for you: only this run's new ones). A change to
   a chapter already rendered goes in `PASTE/changes/15-jubilees.md`. Chat reply
   short: chapters landed, progress count, Left standing, Choices (every verse
   listed), times in Central. A decision that could affect many chapters or
   books goes at the top.

Do not touch other books, `PASTE/edits.md`, the spec, `CLAUDE.md` or `sources/`
during a run; log findings in `NOTES_FOR_ANDREW.md`.

## Chapter 1 only

- The **prologue** (`jubilees 0`, two verses: *This is the account of the
  division of the days…*) goes above verse 1 without a number, as a Psalm title
  does.
- The first note says the verse numbers follow the EOTC printed Bible, and
  where they differ from other English editions.

## Fixed terms for Jubilees

One Ge'ez expression, one English rendering, across the whole book. Add to this
list when a recurring term is settled; bring real choices to Andrew.

| Ge'ez | English | Note the first time |
|---|---|---|
| *ʾƎgziʾabəḥer* | the Lord | as in 1 Enoch |
| *ʾAmlāk* | God | |
| *ʾiyobelwu* | jubilee | a period of 49 years (seven weeks of years) |
| *subāʿe* (of years) | week | a week of years, seven years |
| *ṣəlāta samāy* | the tablets of heaven | as in 1 Enoch 81:1–2 and 93:2, which have *ṣafṣafa samāy* |
| *malʾaka gaṣṣ* | the angel of the presence | *the angel of the face*; Isaiah 63:9 |
| *təguhān* | the Watchers | as in 1 Enoch |
| *kufāle* | division | the book's Ge'ez title, *Maṣḥafa Kufāle*, **the Book of Division** |
| names | the name this project's Genesis and Exodus use; a name found only in Jubilees gets a plain spelling of the EOTC's form | |
