# Notes sweep (Andrew, 2026-11-07)

A one-off loop: bring the notes of every chapter rendered before 2026-11-07 to
the rule in `CLAUDE.md` §3, *less is more*. Acts 27–28 are the worked example.
It runs **every Thursday at 6:00 AM Central until finished**, split three ways
(Andrew, 2026-11-07). When all three parts are done, this file moves to
`archive/`.

## The three parts and their cursors

Each session works only its own part, in book order, and moves only its own
cursor line.

- **Bible Main** (`trig_01EGtPCNGG8RR8LGXjZFkBEK`): Leviticus to Jubilees.
  Next: **Joshua**.
- **Bible 2** (`trig_011UWcyhrwAiuuBgZnvFx3xf`): 1 Enoch to Wisdom of Solomon.
  Done.
- **Bible 3** (`trig_01SUixp7UxNVNqmtdXa98RnN`): Sirach to Acts 26, then the opening
  chapters of books 82–89. Next: **Isaiah**.

**Left out:** Genesis and Exodus (closed), the fixed model Leviticus 17, the
model John 1, and Acts 27–28 (done).

## What to do in each chapter

1. Read each note against `CLAUDE.md` §3 and cut every note that fails it.
   Use your judgement; Andrew trusts it.
2. **Always keep** the notes the spec requires: a different chapter or verse
   numbering; a departure from the Hebrew or Greek naming the witness
   followed; a book's first note on its tier or sources; *El Shaddai* the
   first time in a book; what a name means; a written and read form that
   differ in meaning; a note a ***KEPT AS IS*** literal phrase is built on;
   a note a Part 2 rule asks for (Ecclesiastes 1:2).
3. In a note that stays, cut only sentences about the work. Do not rewrite
   what is left, add notes, or touch the verses.
4. Leave alone any note an Open entry in `COUNCIL.md` is about.

## What to record

**No before/after tables** (Andrew, 2026-11-07). Record only a note you are
genuinely unsure about: leave it in place and add it as a choice for Andrew,
in the layout of `CLAUDE.md` §5, at the top of that book's `PASTE/changes/`
file under `## Notes sweep: <Book> (<date>)` (options: (a) keep (now),
(b) cut; and your recommendation).

## After each book

1. `python3 check_chapters.py` and fix every ERROR.
2. Move your cursor line to the next book.
3. Commit only `books/`, `NOTES_SWEEP.md` and any `PASTE/changes/` file:
   `git add books NOTES_SWEEP.md PASTE/changes`, commit
   `Notes sweep: <Book>`, `git pull --rebase origin main`, push to main.
   Skip `build_site.py` and `progress.py`: three sessions pushing at once
   would collide in `docs/`, and the next render cycle rebuilds the site.

## When the run ends

Stop when the turn or the usage runs out; the next Thursday picks up from
your cursor. Do not schedule anything in between. Tell Andrew in one line
which books you finished and how many notes were cut. When your whole part
is done, say so, and turn your trigger off (`update_trigger`, its id above,
`enabled: false`).
