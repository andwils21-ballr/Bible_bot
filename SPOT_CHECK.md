# The spot check

A blind re-render of the latest render cycle by a fresh session, compared with
what the cycle committed. It tests for drift: the slow slide away from the rules
that a long-running session cannot see in itself. The first one was done by
hand on 2026-10-03 (1 Chronicles 14–17); it found notes saying a word was
"fixed as" something, wording copied from a parallel passage, and a broken
sentence filled in, and it found mistakes of its own.

A spot check never changes a chapter. It reports; Andrew decides.

The Routine "Bible_bot — weekly spot check" sends the prompt below every Sunday
at 3:10 PM Central, each time into a fresh session.

---

Bible_bot spot check.

STEP 0: Clone or sync the repo
(`git clone https://github.com/andwils21-ballr/Bible_bot.git /home/user/bible_bot`,
or `cd /home/user/bible_bot && git fetch origin main && git reset --hard origin/main`),
then read CLAUDE.md, RENDERING_SPEC.md and SPOT_CHECK.md in full.

1. Find the latest render cycle: `git log --format='%h %s' --grep='^Render ' -1`.
   Note its chapters. Do not open those chapter files, their diff, or that
   cycle's entry in `PASTE/renders/` until step 4.
2. Make a copy of the repo as it was before that cycle:
   `git worktree add --detach /tmp/spot <commit>~1`. Work only in `/tmp/spot`.
3. Render the same chapters there, exactly as ROUTINE_PROMPT.md steps 1–6 say
   (fixed models, the source printed first, the readability pass,
   `check_chapters.py`), but commit nothing and push nothing.
4. Now compare yours with the committed chapters, verse by verse and note by
   note. Run `python3 check_chapters.py` on both sets. Sort what differs:
   - **Rule breaks**: a rule in CLAUDE.md or the spec, which side broke it, and
     the rule's words.
   - **Translation differences**: where the two readings differ in meaning, with
     the Hebrew or Greek, and which one the source supports.
   - **Notes**: connections one side found and the other missed; notes that
     break the notes rules.
   - **Your own mistakes**: say them as plainly as the others.
   Leave out differences of wording that change nothing.
5. Write the report to `PASTE/spot-checks/<YYYY-MM-DD>.md`, under the header
   line `# Spot Checks`, and add one line to `NOTES_FOR_ANDREW.md` pointing to
   it. Times in Central. Commit only those two files
   (`Spot check <Book> <first>–<last>`), then
   `git pull --rebase origin main && git push origin main`.
6. Reply in chat with three or four lines: the chapters checked, the number of
   rule breaks on each side, and the one finding that matters most.

Never change a chapter, the spec, CLAUDE.md or any script in a spot check.
