# The spot check

A blind re-render of the latest render cycle by a fresh session, compared with
what the cycle committed. It tests for drift: the slow slide away from the rules
that a long-running session cannot see in itself. The first one was done by
hand on 2026-10-03 (1 Chronicles 14–17); it found notes saying a word was
"fixed as" something, wording copied from a parallel passage, and a broken
sentence filled in, and it found mistakes of its own.

A spot check never changes a chapter. It reports; Andrew decides.

The Routine "Bible_bot — weekly spot check (in Bible 2)" pings the Bible 2
session every Sunday at 3:10 PM Central (Andrew did not want a new session on
his dashboard every week). Bible 2 has seen the work, so it is not blind; the
rendering goes to a **fresh helper agent** (the Agent tool), which starts with
no memory and sees only the brief below. Bible 2 then does the comparison,
which needs no blindness. Any session that takes this over works the same way.


## The steps

1. Sync the repo (`git fetch origin main && git reset --hard origin/main`).
   Find the latest render cycle: `git log --format='%h %s' --grep='^Render ' -1`,
   and note its chapters.
2. Make a copy of the repo as it was before that cycle:
   `git worktree add --detach <scratch>/spot <commit>~1`. That copy does not
   contain the cycle's chapters.
3. Give the rendering to a fresh helper agent, **on Opus** (pass the model
   explicitly, so a changed default can never put it on a smaller model),
   with **only** this brief, filled in, and nothing about the cycle being
   checked:

   > You are rendering chapters for the Bible_bot project in `<scratch>/spot`.
   > Work only in that folder. Read CLAUDE.md, RENDERING_SPEC.md and the fixed
   > models in full, then render <Book> <first>–<last> exactly as
   > ROUTINE_PROMPT.md steps 1–6 say (print the source first, readability pass,
   > `python3 check_chapters.py <files>`), writing each chapter file and a
   > judgment-call table per chapter. Do not commit, push, or look at git
   > history. Reply with the list of files written and your choices for Andrew.

4. Compare the helper's chapters with the committed ones, verse by verse and
   note by note. Run `python3 check_chapters.py` on both sets. Sort what
   differs:
   - **Rule breaks**: the rule's words, and which side broke it.
   - **Translation differences**: where the meaning differs, with the Hebrew or
     Greek, and which one the source supports.
   - **Notes**: connections one side found and the other missed; notes that
     break the notes rules.
   - **The helper's own mistakes**, as plainly as the others.
   Leave out differences of wording that change nothing.
5. Write the report to `PASTE/spot-checks/<YYYY-MM-DD>.md`, under the header
   line `# Spot Checks`, and add one line to `NOTES_FOR_ANDREW.md` pointing to
   it. Times in Central. Commit only those two files
   (`Spot check <Book> <first>–<last>`), then
   `git pull --rebase origin main && git push origin main`. Remove the scratch
   copy (`git worktree remove`).
6. Tell Andrew in three or four lines: the chapters checked, the rule breaks on
   each side, and the one finding that matters most.

Never change a chapter, the spec, CLAUDE.md or any script in a spot check.
