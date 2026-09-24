# The Routine prompt

The exact text the scheduled Routine sends on each firing. Keep this file and
the live Routine identical.

---

Bible_bot render cycle.

STEP 0: DO THIS BEFORE ANY INTERPRETING, PLANNING, RENDERING OR REPLYING.
Sync the repo, then read /home/user/bible_bot/CLAUDE.md in full, every word.
It holds the mission, your role, the notes policy, the reporting format and the
non-negotiables, and it outranks this prompt.
- Sync: `cd /home/user/bible_bot && git fetch origin main && git reset --hard origin/main`
- If the folder is missing: `git clone https://github.com/andwils21-ballr/Bible_bot.git /home/user/bible_bot`

Then:
1. Read RENDERING_SPEC.md in full. Re-read the model notes: Genesis 25, vv21–23.
2. Run `python3 progress.py` for the next chapter. Read the two most recent
   chapters to match voice and note density.
3. For each chapter, print the source first:
   `python3 source_text.py <slug> <chapter>`. Every claim in a note must be
   checkable against that printed text. If there is no source, do exactly what
   the book's tier says.
4. Render the next four to six chapters. Four excellent chapters beat six thin
   ones.
5. Readability pass on every chapter (CLAUDE.md section 2). Stay close to the
   text and clean it up in its own style: remove friction, never force. Never
   flatten a real difficulty; keep it and mark it ***KEPT AS IS*** in the report.
6. Run `python3 build_site.py && python3 progress.py`. Commit
   `Render <Book> <first>–<last>` and push to main.
7. Report exactly as CLAUDE.md section 5 says:
   - Full judgment-call tables at the top of PASTE/renders.md.
   - A short chat reply with the progress count, "Left standing on purpose",
     and "Choices for you", listing every verse for each choice.
   - Times in Central.

Do not act on PASTE/edits.md in a render cycle; only mention requests that have
no Delivered section. Do not modify CLAUDE.md, RENDERING_SPEC.md, HANDOFF.md,
manifest.json, the build scripts, progress.py, source_text.py or sources/; log
findings in NOTES_FOR_ANDREW.md. Never invent source text; the stub is the
honest output when there is no source.
