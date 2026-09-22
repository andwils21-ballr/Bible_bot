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

## Genesis is closed

Andrew signed off on **Genesis 1-50** on 2026-09-21, after reading it
through and working two rounds of fixes with it open in front of him. Treat
the book as finished.

Rule 0's readability pass is part of rendering a chapter and never sweeps
back over finished books, so nothing in the normal cycle touches Genesis
anyway. This section is about your own initiative: do not reopen it to
"improve" its wording, re-pass it, or rewrite its notes. Fix it only when he
asks, or when something in it is provably wrong - a mistranslation, a false
claim in a note, a broken cross-reference.

A whole-book pass over already-finished chapters happens only when he asks
for one, the way he asked for Genesis 26-50 on 2026-09-18.

He may reopen it himself once the whole canon is drafted. That is his call.

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

## Andrew's editorial rules

These were settled in conversation, not all of them are in the spec, and
breaking one wastes his time. They are listed in the order they cost the most.

0. **The readability pass is now part of rendering, not a later round.**
   Added 2026-09-18, because catching these by hand was eating his evenings.
   After the chapter is written and before it is committed, read it once more
   as an ordinary English reader and hunt for exactly two things:
   - **Cognate-accusative literalism** — *boiled a boiling*, *a going-up*,
     *come from coming to*, *the lives of Sarah were*. Hebrew doubles a verb
     with its own noun constantly; English does not, and it reads as broken.
     Render it as the plain verb and put the doubling in the note.
   - **A preposition or idiom carried over word for word** — *opposite his
     wife*, *from before the face of*, *press for me with*, *the silver of the
     field*, *possess the gate of*, *by the neck*. Ask what the phrase is
     actually doing, then say that.
   Also: words no one says (*reprove*, *concubine*, *tamarisk* with no noun
   after it); a noun that sounds childish (*stuff*); an elliptical Hebrew
   sentence left elliptical in English with no note; a term rendered one way
   in one chapter and another way elsewhere.
   **What the pass must never do:** flatten a real difficulty, adopt the Greek
   over the Hebrew silently, or smooth a verse the source leaves rough. The
   test is *trivially awkward by today's standards* versus *genuinely hard in
   the source*. Fix the first, keep the second and note it.
   **And never trade a word that carries weight for a flatter one.** Andrew's
   ruling, 2026-09-18, on *la-tohar* at Exodus 24:10: "purity carries a FEELING
   with it. Clearness is just something you see. I don't want to take the
   feeling out of words. That's what strips the authenticity." Both were
   defensible renderings of the same noun; the flatter one was wrong anyway.
   The pass removes **friction**, never **force**. If the plainer candidate is
   colder, drier, or more clinical than the source word, it is the wrong
   candidate — go find a third one.
   **Then give Andrew a before/after table** — one row per change, for every
   chapter, in the reply. No table, no confidence that anything was checked.
1. **Never explain our own decisions in a note.** No "English cannot carry
   this", no "this rendering chose", no "we changed it because". Write for a
   reader who will never see the curtain. Record the reasoning in the commit
   message or in `NOTES_FOR_ANDREW.md` instead.
2. **A change that only clarifies the story does not earn a note.** Notes are
   for things that change what a reader *understands*. Rewording a confusing
   verse is just rewording; it needs no footnote.
3. **Length is not the test — value is.** Andrew is fine with a long note if it
   serves a purpose or is genuinely interesting. He is not fine with a short one
   that carries nothing. No single note should be exceptionally long unless it
   matters to the overarching story of the Bible.
4. **Capital Lord means God. Lowercase lord means a human of rank.** There is no
   ambiguity to preserve; pick one and be consistent.
5. **No Bible English** — the banned list is in `RENDERING_SPEC.md`. Two
   deliberate exceptions, already argued and settled: keep **"and it came to
   pass"** and **"and here"**. Do not strip them.
6. **Versification follows the English/KJV division** so a reader can set this
   beside a King James Bible.
7. **When he asks a question, the deliverable is the answer.** He is often
   diagnosing or thinking out loud. Report the finding and stop. Do not apply a
   fix until he asks for one.
8. **Default is: you edit and push, he reviews the diff.** But always include a
   before/after table in the reply too, one row per change — settled
   2026-09-22, updating the earlier note that he didn't want these. Keep the
   commentary short: no explanation needed for a change that's just his own
   suggestion applied as given. Save the explaining for cases where you
   corrected, pushed back on, or added something beyond what he asked for.
9. **Times in Central, never UTC.**
10. **Label what is a note in the project and what is just chat.** He asked for
    this explicitly. Keep the two visibly separate in every report.

## Hard-won technical facts

- **The Ge'ez English in `sources/english/` is the OCP's own scholarly
  translation, not ours.** We do not translate Ge'ez and must never claim to.
  Quote it, report where it differs from the Greek or Aramaic, and do not build
  an argument on what a Ge'ez word supposedly means.
- **The OCP XML splits one verse across several `<unit>` elements.** A verse is
  every unit's `option="0"` reading joined in order. Reading only the first unit
  silently truncates about two thirds of them mid-sentence, with no error. That
  bug produced a whole set of false "the Ethiopic drops this" notes before it
  was caught. `fetch_ocp.py` does it correctly now — do not rewrite it casually.
- **`sources/swete-src/` holds the entire Septuagint, not just the
  deuterocanon.** Any Greek Old Testament verse can be looked up from those two
  CSVs. That is how the Genesis 11 Kainan and Genesis 46 seventy-five findings
  were confirmed rather than asserted.
- **Swete follows the Greek verse division.** In Exodus it runs four verses out
  of step with the Hebrew around chapter 7/8. See `NOTES_FOR_ANDREW.md`.
- **The network in this container reaches GitHub and nothing else.**
  archive.org, crosswire, ebible, wikisource and pseudepigrapha.org all fail.
  Clone public repos over https; that works.
- **Check a licence before you build on a source.** Andrew does not want
  share-alike or non-commercial obligations. `SOURCES.md` records four sources
  examined and rejected, and why.

## The most expensive lesson

Three other AI models were asked, independently, to translate the same Ge'ez
passage. All three agreed with each other and with us. All four of us were
wrong, because the file every one of us was reading had been truncated by the
parser bug above.

**Independent opinions are only independent if they do not share an input.**
Before commissioning an outside check on a source, test the source itself. The
thing that actually caught it was one command counting Ge'ez full stops.

## What is not automated

Building the `.docx` files (`python3 build_docx.py`) and sending them to Andrew.
He reads the chapters that way. Do it after a render cycle worth looking at.
