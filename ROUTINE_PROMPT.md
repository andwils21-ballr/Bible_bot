# The Routine prompt

The exact text the scheduled Routine sends on each firing. Keep this file and
the live Routine identical (`CLAUDE.md` §8): steps only, never rules.

---

Bible_bot render cycle.

STEP 0: DO THIS BEFORE ANY INTERPRETING, PLANNING, RENDERING OR REPLYING.
Sync the repo, then read /home/user/bible_bot/CLAUDE.md in full, every word.
It outranks this prompt. This prompt lists the steps; the rules are in
CLAUDE.md and RENDERING_SPEC.md.
- Sync: `cd /home/user/bible_bot && git fetch origin main && git reset --hard origin/main`
- If the folder is missing: `git clone https://github.com/andwils21-ballr/Bible_bot.git /home/user/bible_bot`

Then:
1. Read RENDERING_SPEC.md in full down to Part 2, and the part of Part 2 for
   this book if it has one. Read the three fixed models in full (spec, "Two
   kinds of example").
2. Run `python3 progress.py` for the next chapter. Read the two most recent
   chapters of the same book for its writer's style.
3. For each chapter, print the source first:
   `python3 source_text.py <slug> <chapter>`.
4. Render the next four to six chapters, with the readability pass on each.
5. Run `python3 check_chapters.py`: fix every ERROR, and fix each CHECK or say
   in the report why it stands. Then run
   `python3 build_site.py && python3 progress.py`. Commit
   `Render <Book> <first>–<last>` and push to main.
6. Report as CLAUDE.md §5 says: the renders file first, then the short chat
   reply.
