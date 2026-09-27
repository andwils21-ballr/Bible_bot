# The broader-canon and Matthew loop

Andrew (2026-09-27): render chapter 1 of each of books 82–89 (Sirate Tsion excepted, tier `none`), to make sure they
render, run after run until those are done; then Matthew, chapter 1 to 28, run
after run until it is finished. **Do your best work on every run.** Each run
follows this file exactly. `CLAUDE.md` outranks it.

## Every run

1. **Sync and read.** `cd /home/user/bible_bot && git fetch origin main && git
   reset --hard origin/main`. Read `CLAUDE.md` in full and the spec in full
   (for phase 1, its section "Books 82–89" above all), and the model notes at
   Genesis 25:21–23.
2. **Find the next chapters.**
   - **Phase 1:** the books among 82–89 with no `01.md` yet, in order:
     `82-1-covenant`, `83-2-covenant`, `85-teezaz`,
     `86-gitzew`, `87-abtilis`, `88-didascalia`, `89-qalementos`. Render up to
     four of them in a run.
   - **Phase 2**, once all seven have `01.md`: the first Matthew chapter with no
     file in `books/55-matthew/`. Render four to six chapters.
   - If Matthew 28 exists, the loop is done: say so and stop the loop.
3. **Match the voice.** Read the two most recent chapters of the same book (for
   a first chapter: phase 1, the latest Jubilees chapter; phase 2, Genesis 25
   and the latest Numbers chapter).
4. **Print every chapter's source first:** `python3 source_text.py <slug> <n>`.
   Every claim in a note must be checkable against what it prints.
5. **Render.** Stop one chapter early rather than rush the last.
6. **Final pass, before committing,** on this run's chapters only:
   - every verse the source prints has a verse (verse 0, a heading, goes above
     verse 1 unnumbered);
   - the readability pass (the spec's eight patterns);
   - no sentence starting with "And" except the spec's kept list; no banned
     words; no "[ " bracket spacing;
   - every quotation of Scripture printed with `source_text.py` and checked;
     where this project has rendered the verse, use its wording;
   - every note claim re-read against the printed source.
7. **Build and push:** `python3 build_site.py && python3 progress.py`; commit
   `Render <Book> <first>–<last>` (phase 1: `Render first chapters: <books>`)
   with the trailers; push to main.
8. **Report** at the top of `PASTE/renders/<order>-<slug>.md`, one file per
   book (start a new book's file with its header, `# New Chapters: <Book>`):
   the judgment-call table, Left standing on purpose, Choices for you (only
   this run's new ones, every verse listed). Chat reply short: what landed,
   progress count, Left standing, Choices, times in Central. A decision that
   could affect many chapters or books goes at the top.
9. **Schedule the next run** (the `/loop` wakeup) unless the loop is done.

Do not touch other books, `PASTE/edits.md`, the spec, `CLAUDE.md`,
`manifest.json`, the build scripts, `progress.py`, `source_text.py` or
`sources/` during a run; log findings in `NOTES_FOR_ANDREW.md`.

## Phase 1: books 82–89, chapter 1

Tier `english-only`: worked from the editor's translation that
`source_text.py` prints, never from memory. The Ge'ez OCR, where printed,
checks names, numbers and the shape of a passage only; never quote it.

- **Verse numbers** are the edition's paragraphs as the helper numbers them.
  Verse 0 of a chapter is a heading: set it as the chapter's `## ` heading,
  unnumbered. The book's opening (printed as chapter 0 with chapter 1) goes
  above verse 1, unnumbered, before the heading if any.
- **Editors' labels are not text.** *Statute 1.* (Horner), *Canon I.*
  (Schodde), Guerrier's and Grébaut's section titles (*16. — Vie publique de
  Jésus-Christ. —*; Grébaut says he added his subtitles), `[ii., 15.]`
  references to the Greek *Apostolic Constitutions* (Harden), folio marks
  *(F. 1 r° a)* (Grébaut): leave them out of the verse. A title that belongs to
  the work (Schodde's canon titles, Harden's chapter titles, which translate
  the Ethiopic) becomes the `## ` heading. Editors' words in parentheses that
  fill out the sense (*(de Jésus-Christ)*) are rendered plainly where the
  sentence needs them.
- **French sources** (Guerrier, Grébaut): translate the French for meaning,
  staying as close to it as English allows. For 2nd Covenant sections 12–62,
  read James's English beside it; where the two differ in substance, follow the
  French and note James's (Coptic) reading. Where the French OCR is spoiled
  past reading and James does not cover it, render what can be read and mark
  the rest *[unreadable in the edition as held]* with a note; never guess.
- **English sources** in Bible English (*thou, ye, unto, verily*): the banned
  words apply as everywhere; the English must read as this project's, not as
  the editor's.
- **Chapter 1's first note** names the translation the book is worked from and
  says no Ge'ez or other source language was used. For 1st Covenant and
  Abtilis it says plainly that the text is a sister version (the
  Syriac or Coptic form of the work) and that the Ethiopic differs from it in
  wording and in places in order. For Abtilis: Tattam's numbering of the 85
  Apostolic Canons is followed; the Ethiopic has 81. For Qalementos: the text
  stops where Grébaut's translation stopped, in the third of seven books.
- **Every chapter's last note** is **Source text**, e.g.
  `- **Source text** — J. M. Harden, *The Ethiopic Didascalia* (1920), public
  domain. English translation by this project.` Name each edition used
  (2nd Covenant: Guerrier and Grébaut 1913, and James 1924 where used).
- **Frontmatter `tier: english-only`.**

## Phase 2: Matthew

Tier `source`: the Greek is the SBLGNT (`sources/greek/matthew.txt`), and the
verse numbers are the English ones it carries. The signs ⸀ ⸂ ⸃ in it are the
edition's markers for places where manuscripts differ; they are not words.

- **The Old Testament in Matthew.** Every quotation and every genealogy name:
  print the Old Testament verse (`python3 source_text.py isaiah 7`) and, where
  this project has rendered it, use its wording and spelling of names (Perez,
  Zerah, Tamar, Hezron, and so on). Where Matthew's Greek differs from the
  Hebrew, follow the Greek and note the difference only where it changes the
  sense.
- **Terms to hold for the whole book** (choices flagged to Andrew in the first
  Matthew report; until he rules, use these):
  - *Christos*: **the Messiah** as a title, as in the spec's example of
    Matthew 1:1; note it the first time.
  - *idou*: the Greek of *hinneh*, so the same ruling: **And here —** for
    *kai idou*, **Here —** alone; not *behold*.
  - *Kyrios*: **Lord** (the spec's divine-names rule).
  - *basileia tōn ouranōn*: **the kingdom of heaven** (Greek plural *heavens*;
    note it once).
- **Frontmatter `tier: source`.** No Source-text note is required for the
  Greek; follow the Numbers chapters.
