# The 1 Enoch loop

Andrew (2026-09-26): render 1 Enoch from chapter 37 to 108, run after run,
until done or until the week's allowance runs out. **Enoch's books are of high
importance to him. Do your best work on every single run.** Each run follows
this file exactly. `CLAUDE.md` outranks it.

## Every run

1. **Sync and read.** `cd /home/user/bible_bot && git fetch origin main && git
   reset --hard origin/main`. Read `CLAUDE.md` in full, the spec's sections on
   the readability pass, "No And", notes, and Tier `witnesses` (the 1 Enoch
   rule), and the model notes at Genesis 25:21–23.
2. **Find the next chapter:** the first number from 37 to 108 with no file in
   `books/16-1-enoch/`. If there is none, the book is done: say so and stop the
   loop.
3. **Match the voice.** Read the two most recent 1 Enoch chapters.
4. **Print every chapter's source first:** `python3 source_text.py 1-enoch <n>`.
   - The **EOTC Ge'ez** (`ethiopic-eotc`) is the base text and sets the verse
     count and numbering. Every EOTC verse gets a verse.
   - Compare **Knibb's Ge'ez** (`ethiopic`, 37–71) and the **Greek** where it
     exists (77–78, 85–87, 89, 97–107) and the **Latin** (99, 106). A real
     difference in meaning gets a note naming the witness.
   - For meaning, use the **OCP English** (37–71) and **Charles** (all). Never
     follow Charles's reordering (91–93, 106) or his emendations. A claim about
     what a Ge'ez word means must rest on those English renderings; quote the
     Ge'ez, build no argument on its supposed root meaning.
   - Every New Testament or Old Testament link in a note must be printed and
     checked first (`python3 source_text.py matthew 25`, etc.). Never quote a
     verse from memory.
5. **Render four to six chapters.** Short chapters allow more; hard ones fewer.
   Stop one chapter early rather than rush the last.
6. **Final pass, before committing,** on this run's chapters only:
   - verse count equals the EOTC's for each chapter;
   - the readability pass (CLAUDE.md section 2, the spec's eight patterns);
   - no sentence starting with "And" except the spec's kept list; no banned
     words; no verse starting lowercase after a finished sentence;
   - every note claim re-read against the printed source.
7. **Every chapter's last note** is **Source text**:
   `- **Source text** — Ge'ez: Beta Masaheft, Universität Hamburg (text of the
   EOTC printed Bible), CC BY-SA 4.0. English translation by this project.`
   (Add the other witnesses used, e.g. *Greek and Knibb's Ge'ez: Online
   Critical Pseudepigrapha, CC BY 4.0.*)
8. **Build and push:** `python3 build_site.py && python3 progress.py`; commit
   `Render 1 Enoch <first>–<last>` with the trailers; push to main.
9. **Report** at the top of `PASTE/renders/16-1-enoch.md` (tables, Left
   standing on purpose, Choices for you: only this run's new ones). A change to
   a chapter already rendered goes in `PASTE/changes/16-1-enoch.md`. Chat reply
   short: chapters landed, progress count, Left standing, Choices (every verse
   listed), times in Central. A decision that could affect many chapters or
   books goes at the top.

Do not touch other books, `PASTE/edits.md`, the spec, `CLAUDE.md` or `sources/`
during a run; log findings in `NOTES_FOR_ANDREW.md`.

## Fixed terms for 1 Enoch

One Ge'ez expression, one English rendering, across the whole book. Add to this
list when a recurring term is settled; bring real choices to Andrew.

| Ge'ez | English | Note the first time |
|---|---|---|
| *ʾƎgziʾa Manāfəst* | the Lord of Spirits | 37:2 |
| *Rəʾsa Mawāʿəl* | the Head of Days | first use (46:1) |
| *Ḫəruy* (of the one figure) | the Chosen One | first use; older English *the Elect One* |
| *ḫəruyān* | the chosen | as in chapters 1–36 |
| *Ṣādəq* (of the one figure) | the Righteous One | first use (38:2) |
| the "Son of Man" expressions: *walda sabʾ* (from 46:2), *walda ʿəgwāla ʾəmmaḥəyāw* (from 62:7) | the Son of Man | say which form, the first time each appears. At 62:5 the EOTC reads *walda bəʾəsit*, **son of a woman**, where other manuscripts have *son of a man*: note it there |
| *Masiḥ* | the Anointed One | 48:10, 52:4; note *Messiah* |
