# Handoff

If the session that was driving this project is gone — hit a limit, was
reclaimed, ended — nothing is lost. Everything needed to continue is in this
repo. This file is how a new Claude picks it up.

**Andrew: hand this file to a fresh Claude Code session and say "read HANDOFF.md
and take over."** That is the whole recovery procedure.

## What the project is

A close rendering of the Ethiopian Orthodox Tewahedo canon into English — 89
books, 1,554 chapters — with notes on what English normally loses. Built a few
chapters at a time by a scheduled Routine that fires every five hours.

## Where the state lives

Nowhere but this repo. There is no memory to restore.

| Question | Answer lives in |
|---|---|
| What chapter is next? | `python3 progress.py` — reads the files on disk |
| How am I supposed to write? | `RENDERING_SPEC.md` — read it in full, it is the contract |
| What are the standing rules? | `CLAUDE.md` — loads automatically each session |
| What is the source text? | `sources/hebrew/`, `sources/greek/`; print with `source_text.py` |
| What is known-broken? | `NOTES_FOR_ANDREW.md` |

## Taking over in four steps

1. **Attach the repo.** `add_repo` with owner `andwils21-ballr`, repo
   `Bible_bot`, access `push`. Clone where the tool says, then
   `register_repo_root`.
2. **Read `RENDERING_SPEC.md` in full.** Especially "Work from the source text,
   never from memory", "The depth standard for notes", "The hedge is a symptom",
   and "Honesty rules".
3. **Read the last three rendered chapters** to match voice and note density
   before writing anything.
4. **Recreate the Routine** (below), then do a render cycle by hand to confirm
   the pipeline works before trusting the schedule.

## Recreating the Routine

Use `create_trigger` with `cron_expression: "0 */5 * * *"` (every five hours;
the server anchors it to the creation minute). Bind it to the new session by
passing neither `create_new_session_on_fire` nor `persistent_session_id` — it
then fires into the session that created it, which is what you want, because a
self-bound Routine inherits that session's repo access and model.

**Do not test it with `fire_trigger`.** That spawns a separate session instead
of delivering into yours, which produces a misleading failure. This was learned
the hard way; it cost two hours. Wait for a real scheduled firing.

The prompt to give it is in `ROUTINE_PROMPT.md`.

## Things that were learned the hard way

- **The model matters.** Fresh-session Routines defaulted to a cheaper model and
  produced nothing usable. Andrew asked for Opus. A self-bound Routine inherits
  the model of the session that created it, so create it from an Opus session.
- **Never render from memory.** Print the source text for every chapter first.
  Within minutes of wiring `sources/` in, the actual Hebrew exposed four errors
  in `manifest.json` that had been written from recall — including one that
  would have rendered Proverbs 1 twice under two different book names.
- **Andrew pushes back, and he is usually right.** Several of the best notes in
  this corpus exist because he questioned a claim. Do not be agreeable; he has
  said so directly. When he says a note sounds like it has no conviction, it
  means the research stopped early — go finish it.
- **Times in Central, never UTC.**

## What is not automated

Building the `.docx` files (`python3 build_docx.py`) and sending them to Andrew.
He reads the chapters that way. Do it after a render cycle worth looking at.
