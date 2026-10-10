# The review loop

Andrew (2026-10-10, 5:13 PM CDT): check the renders and changes files and the
chapters, systematically from the earliest chapters forward, for things that
can be cleaned up without his attention. Bible 2 and Bible 3 both review;
Bible 2 applies what is settled and mediates the council (`COUNCIL.md`, "Who
is in it"). The goal is less work for Andrew, not more. `CLAUDE.md` outranks
this file.

## One run

A run is one unit, small enough to finish well: **one render-report entry**
(usually four chapters) or, where a book has no render report, **four
chapters**. Books go in canon order (`manifest.json`), chapters in order. For
each unit:

1. `git pull --rebase origin main`. Read `COUNCIL.md`: answer any **Open**
   entry not yet answered (sealed: write before reading the other answers),
   and, as mediator (Bible 2 only), note any entry that breaks the council's
   rules. Apply every entry that has become **Settled** and is not yet done.
2. Read the unit's entry in `PASTE/renders/<book>.md` (oldest first) and any
   `PASTE/changes/<book>.md` entries touching those chapters. Then read the
   chapters, with `python3 source_text.py <slug> <chapter>` beside them.
3. Run `python3 check_chapters.py <files>`.
4. Look for what can be cleaned up without Andrew:
   - a checker ERROR, or a CHECK that is a real problem;
   - a report that says the text reads one way when the chapter reads another;
   - a choice marked `✅ Decided` that was never applied, or applied in one
     verse and missed in another;
   - a later ruling (the spec, `PASTE/changes/`) that this chapter predates
     and plainly falls under: *And it came to pass* keep/cut, *hinneh*,
     capital pronouns, *And now*, the fixed terms;
   - notes: talk about the translating, a bare cross-reference, a hedge, a
     claim the printed source does not support, a hidden meaning;
   - typos, missing words, broken formatting.
   Leave alone what is a real choice of meaning (CLAUDE.md §2: Andrew decides)
   and differences of taste.
5. Post each finding in `COUNCIL.md` under **Open**, one entry each, with the
   answer you propose. Group several of the same kind in one chapter into one
   entry.
6. Move your line under **Review cursors** to the next unit. Commit
   (`Council: review <Book> <first>–<last>`) and push.
7. Schedule the next run five minutes later (`send_later`, `own_followup`).

Bible 2 applies settled cleanups with a before/after line in the book's
`PASTE/changes/` file, runs `check_chapters.py`, `build_site.py` and
`progress.py`, and commits `Council cleanup: <reference>`.

## Stop

When Andrew says stop, or the cursor reaches the last rendered chapter. Then
cancel the pending run and say so in one line.
