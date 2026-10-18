# The Jubilees repair loop

Andrew (2026-09-27): the Jubilees "cut verses" were losses in the Beta Masaheft
digitization, not in the Ge'ez. The Asmara printing (`ethiopic-gff`, see
`SOURCES.md`) has the missing words. Re-render every repaired verse from the
Ge'ez, chapter 1 to 50, run after run, until done. **Do your best work on every
run.** `CLAUDE.md` outranks this file.

## Every run

1. **Sync and read.** `cd /home/user/bible_bot && git fetch origin main && git
   reset --hard origin/main`. Read `CLAUDE.md` in full, the spec's Jubilees rule
   (Tier `witnesses`), and the readability pass.
2. **Find the next chapter:** the first chapter listed as not done in the
   progress line at the top of `PASTE/changes/15-jubilees.md`. If all 50 are
   done, say so and stop the loop.
3. **For each chapter,** print `python3 source_text.py jubilees <n>` and read
   the chapter file. Then:
   - **Every verse with [brackets]:** compare the bracketed words with the
     Asmara printing (`ethiopic-gff`). If it has them, render its words, drop
     the brackets, and keep the English of the rest of the verse. If it words
     them differently from the old fill, follow the Ge'ez; a difference in
     meaning gets a note. If it lacks them (14:16–16:13, 7:15), keep the
     bracket and its note.
   - **Verses the Asmara printing makes much longer** with no bracket now
     (3:23, 8:13, 26:32, 33:9, 42:12, and any the divergence list flags):
     render what the EOTC lacks.
   - The Asmara text's verse boundaries are approximate: read the verses on
     either side before deciding a word is missing or extra.
   - A real difference in meaning between the EOTC and the Asmara printing gets
     a note, as the second Ge'ez text did.
   - **Notes:** replace the "Words in [brackets]… not in either Ge'ez text"
     note with one that names the verses rendered from the Asmara printing,
     because the EOTC text as held here is cut short in them. Correct every
     other note that rests on the Ge'ez lacking something (for example 47:
     *Without v10's bracket the Ge'ez never tells of the Egyptian*). Add the
     date variants where they fall: 16:16, 46:8, 48:1.
   - **Source text** note: add *Asmara printing (1962/63): Ge'ez Frontier
     Foundation, CC BY-SA 4.0.*
4. **Four to eight chapters a run.** Stop early rather than rush.
5. **Final pass** on this run's chapters: verse count unchanged; readability
   pass; no "And"-starts except the kept list; banned words; no "[ " spacing;
   caps.py; every quotation printed.
6. **Record every change** in `PASTE/changes/15-jubilees.md`, newest at the
   top: a `Where | Before | After` table per chapter, one row per verse or note
   changed, and update the progress line.
7. **Build and push:** `python3 build_site.py && python3 progress.py`; commit
   `Jubilees repair: <first>–<last> from the Asmara printing` with the
   trailers; push to main.
8. **Chat reply short:** chapters done, anything left bracketed, any meaning
   difference worth Andrew's eye, times in Central.

Do not touch other books, `PASTE/edits.md`, the spec, `CLAUDE.md` or `sources/`
during a run.
