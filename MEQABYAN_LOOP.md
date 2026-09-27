# The 1 Meqabyan loop

Andrew (2026-09-27): render 1 Meqabyan, chapter 1 to 36, run after run, until
done or until the week's allowance runs out. **Do your best work on every single
run.** Each run follows this file exactly. `CLAUDE.md` outranks it.

## Every run

1. **Sync and read.** `cd /home/user/bible_bot && git fetch origin main && git
   reset --hard origin/main`. Read `CLAUDE.md` in full, the spec's sections on
   the readability pass, "No And", notes, and "1 Meqabyan", and the model notes
   at Genesis 25:21–23.
2. **Find the next chapter:** the first number from 1 to 36 with no file in
   `books/23-1-meqabyan/`. If there is none, the book is done: say so and stop
   the loop.
3. **Match the voice.** Read the two most recent 1 Meqabyan chapters (for the
   first run, Jubilees 49–50).
4. **Print every chapter's source first:** `python3 source_text.py 1-meqabyan <n>`.
   - The **EOTC Ge'ez** (`ethiopic-eotc`) is the only text. It sets the verse
     count and numbering. Every verse gets a verse.
   - **The Amharic (chapters 1–8 only)** is in the private repo
     `/home/user/ethiopic/1-meqabyan/amharic/NN.txt` (clone
     `andwils21-ballr/Ethiopic` if it is missing). Read it to check meaning and
     numerals. **Never copy, quote or credit it**, and never name it in a
     chapter's notes; it is not cleared for publishing. Where it seems to differ
     in substance from the Ge'ez, keep the Ge'ez and log it in the report.
   - **Numerals.** The file writes some numbers as digits inside the text
     (*ወለደ3አንስተ*, "bore three daughters"). Some are cut short (1:21 has *4*
     for forty; 4:5 has *4* for fourteen) and some are lost to a stray `%` or
     `)` (1:16, 1:22, 10:3). Where the Amharic has the number, the verse uses
     it and a note says the Ge'ez numeral is damaged. Where there is no Amharic
     (chapters 9–36), render the number only if the text itself fixes it;
     otherwise write *[number lost]* in the verse and note it. Never guess.
   - **Meaning.** There is no Greek, Latin, Hebrew or public-domain English to
     check against. Render from the Ge'ez; state a word's meaning as a
     rendering, quote the Ge'ez, and build no argument on its supposed root. A
     word you are not sure of: say so in a note, and list it in the report.
   - **1 Meqabyan draws on the Old Testament** (the Law, the kings, the judgments
     on idolatry). Where it quotes or echoes a verse, print that verse
     (`python3 source_text.py deuteronomy 28`) and read this project's
     rendering if it exists; where the Ge'ez says the same thing, use the same
     English wording. It is **not** the Greek 1 Maccabees: never import that
     book's events or names.
   - Every Old or New Testament link in a note must be printed and checked
     first. Never quote a verse from memory.
5. **Render four to six chapters.** Short chapters allow more; hard ones fewer.
   Stop one chapter early rather than rush the last.
6. **Final pass, before committing,** on this run's chapters only:
   - verse count equals the EOTC's for each chapter;
   - the readability pass (CLAUDE.md section 2, the spec's eight patterns);
   - no sentence starting with "And" except the spec's kept list; no banned
     words; no verse starting lowercase after a finished sentence; no "[ "
     bracket spacing;
   - every numeral checked against the rule above;
   - every note claim re-read against the printed source.
7. **Every chapter's last note** is **Source text**:
   `- **Source text** — Ge'ez: Beta Masaheft, Universität Hamburg (text of the
   EOTC printed Bible), CC BY-SA 4.0. English translation by this project.`
8. **Build and push:** `python3 build_site.py && python3 progress.py`; commit
   `Render 1 Meqabyan <first>–<last>` with the trailers; push to main.
9. **Report** at the top of `PASTE/renders/23-1-meqabyan.md` (tables, Left
   standing on purpose, Choices for you: only this run's new ones, and the
   Amharic differences). A change to a chapter already rendered goes in
   `PASTE/changes/23-1-meqabyan.md`. Chat reply short: chapters landed,
   progress count, Left standing, Choices (every verse listed), times in
   Central. A decision that could affect many chapters or books goes at the top.

Do not touch other books, `PASTE/edits.md`, the spec, `CLAUDE.md` or `sources/`
during a run; log findings in `NOTES_FOR_ANDREW.md`.

## Chapter 1 only

The first note says: the text is the Ge'ez of the Ethiopian Orthodox Tewahedo
printed Bible, the verse numbers follow it, and there is no other ancient
witness; this book is not the Greek 1 Maccabees.

## Fixed terms for 1 Meqabyan

One Ge'ez expression, one English rendering, across the whole book. Add to this
list when a recurring term is settled; bring real choices to Andrew.

| Ge'ez | English | Note the first time |
|---|---|---|
| *ʾƎgziʾabəḥer* | the Lord | as in Jubilees |
| *ʾAmlāk* | God | |
| *ṭaʿot* | idol | |
| names | the name this project's Old Testament uses; a name found only here gets a plain spelling of the EOTC's form | |
