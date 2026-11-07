# Notes sweep (Andrew, 2026-11-07)

A one-off loop: bring the notes of every chapter rendered before 2026-11-07 to
the rule in `CLAUDE.md` §3, *less is more*. Acts 27–28 are the worked example
(`PASTE/changes/59-acts.md`). When the sweep is finished, this file moves to
`archive/`.

## Cursor

- **Next book:** Leviticus (book 3).
- **Done:** none yet.

## Scope

- Every rendered chapter, in book order, from Leviticus to Acts 26.
- **Left out:** Genesis and Exodus (closed; Andrew went through them himself),
  and the fixed models Leviticus 17 and John 1. Acts 27–28 are already done.

## What to do in each chapter

1. Read each note against the test in `CLAUDE.md` §3. Cut every note that
   fails it: trivia, a mundane choice, a note written to fill a count, a note
   that explains the decision-making.
2. **Always keep** the notes the spec requires: a different chapter or verse
   numbering; a departure from the Hebrew or Greek naming the witness
   followed; a book's first note on its tier or its sources; *El Shaddai*
   the first time in a book; what a name means; a written and read form that
   differ in meaning; a note a ***KEPT AS IS*** literal phrase is built on;
   any note a Part 2 rule asks for (Ecclesiastes 1:2).
3. In a note that stays, cut only sentences about the work (*the context
   fits*, *this rendering supplies*). Do not rewrite what is left, add notes,
   or touch the verses.
4. Never cut a note an Open entry in `COUNCIL.md` is about; leave that chapter's
   note for the council.

## After each book

1. `python3 check_chapters.py` (fix every ERROR), then
   `python3 build_site.py && python3 progress.py`.
2. One entry at the top of that book's `PASTE/changes/` file: the request in
   one line, and a `Where | Before | After` table with one row per chapter,
   giving the number of notes before and after and the anchors cut.
3. Move the cursor above to the next book.
4. `git pull --rebase origin main`, commit `Notes sweep: <Book>`, push to main.

## If the turn ends before the sweep does

Schedule the next step with `send_later`, 30 minutes out:
*Continue the notes sweep from the cursor in NOTES_SWEEP.md.* If it ended
because usage ran out, schedule it for 7:05 AM Central or the next hour after
the reset instead.
