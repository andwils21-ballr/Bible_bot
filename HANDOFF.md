# Handoff

How a new Claude picks this project up if the driving session is gone. Nothing
lives in a model's memory; everything is in this repo.

**Andrew: give a fresh Claude Code session this repo and say "read CLAUDE.md,
then HANDOFF.md, and take over."** That is the whole recovery procedure.

## Where the state lives

| Question | Answer |
|---|---|
| The goals, your role, the rules | `CLAUDE.md` (read first, every time) |
| How to write a chapter | `RENDERING_SPEC.md` |
| What chapter is next? | `python3 progress.py` |
| The source text | `python3 source_text.py <slug> <chapter>` |
| Andrew's requests (checkmarks only; cleared when all are done) | `PASTE/edits.md` |
| Render reports (new chapters), one file per book | `PASTE/renders/` |
| Before/after of every change to finished chapters, one file per book | `PASTE/changes/` |
| Known problems, findings for Andrew | `NOTES_FOR_ANDREW.md` |

## Taking over

1. Attach the repo: `add_repo` with owner `andwils21-ballr`, repo `Bible_bot`,
   access `push`. Clone where the tool says, then `register_repo_root`.
2. Read `CLAUDE.md`, then `RENDERING_SPEC.md`, in full.
3. Read the last three rendered chapters, and the Genesis 25 notes, for voice.
4. Recreate the Routine (below), and do one render cycle by hand first.

## The Routine

- **Timing:** four runs a day, at 7:45 AM, 12:45 PM, 5:45 PM and 10:45 PM
  Central, from one trigger: `CRON_TZ=America/Chicago 45 7,12,17,22 * * *`.
  The cron is written in Central time, so the runs do not move when daylight
  time ends. The prompt is in `ROUTINE_PROMPT.md`.
- **Binding:** it is self-bound, meaning it fires into the session that created
  it, which gives it that session's repo access and model.
- **To recreate it:** `create_trigger` with neither `create_new_session_on_fire`
  nor `persistent_session_id`, from an Opus session, with the prompt in
  `ROUTINE_PROMPT.md`.
- **Do not test with `fire_trigger`.** It spawns a separate session and gives a
  misleading failure. Wait for a real scheduled firing.

## Drift, and what stops it

A long-running session slides away from the rules without noticing, because it
copies its own recent output. The shadow run of 2026-10-03 showed it: notes
saying a word was "fixed as" something, in every run since 1 Kings 13, and
wording copied from Samuel into Chronicles where the Hebrew differs. Rereading
CLAUDE.md does not stop this; the examples are fresher than the rules. Four
things do (Andrew, 2026-10-03):

1. **`check_chapters.py`** runs before every commit and checks what a program
   can check. A program does not drift.
2. **Fixed models** (spec, "Two kinds of example"): Genesis 25, Exodus 33 and
   Leviticus 17 hold the rules; the book's recent chapters only set its
   writer's style.
3. **The session-start hook** (`.claude/hooks/session-start.sh`) installs the
   Python packages and puts the three rules above in front of every new cloud
   session on this repo.
4. **The weekly spot check** (`SPOT_CHECK.md`): a fresh session re-renders the
   latest cycle blind and reports the differences.

A fresh session taking over should keep all four running, and should keep chat
with Andrew apart from render work where it can.

## Hard-won technical facts

- **Hebrew and English chapter divisions differ.** We follow the English;
  `source_text.py` prints the Hebrew numbering. Known offsets:
  - Genesis 31:55 = Hebrew 32:1.
  - Exodus 8:1–4 = Hebrew 7:26–29.
  - Leviticus 6:1–7 = Hebrew 5:20–26, and Leviticus 6:8–30 = Hebrew 6:1–23.
  - Numbers 16:36–50 = Hebrew 17:1–15, and Numbers 17:1–13 = Hebrew 17:16–28.
    Swete's Greek follows the English here.
  - Numbers 25 has 18 verses: Hebrew 25:19 is English 26:1.
  - Numbers 29:40 = Hebrew 30:1, and Numbers 30:1–16 = Hebrew 30:2–17. Swete's
    Greek follows the Hebrew here.
  - 1 Chronicles 6:1–15 = Hebrew 5:27–41, and 1 Chronicles 6:16–81 = Hebrew
    6:1–66. `source_text.py 1-chronicles 6` prints only Hebrew 6, so Hebrew
    5:27–41 must be printed too.

  Count the verses per chapter in the Hebrew file before rendering.
- **Swete's Greek does not line up with the Hebrew.**
  - It is out of step at Genesis 35:21–22, Exodus 7/8, Exodus 21/22,
    Leviticus 7 (Hebrew 7:21 is Swete 7:11) and Numbers 13 (Greek 13:1 is
    Hebrew 12:16, so Hebrew 13:33 is Greek 13:34).
  - In Exodus 25–40 it is a shorter, reordered edition, so check what is
    actually at a Greek verse number before citing it.
- **Hebrew searches must allow final letter forms** (ך ם ן ף ץ) or they quietly
  return nothing. Check the vowel points, not just the consonants.
- **Letters written large or small in the Hebrew were once dropped** by
  `fetch_sources.py`. Fixed and re-fetched 2026-09-23; 11 verses changed.
- **The OCP XML splits one verse across several `<unit>` elements.** A verse is
  every unit's `option="0"` reading joined in order. `fetch_ocp.py` does this
  correctly; do not rewrite it casually. Reading only the first unit once
  produced a set of false notes.
- **The Ge'ez English in `sources/english/` is the OCP's translation, not ours.**
  Quote it; never claim to translate Ge'ez.
- **Independent checks are only independent if they don't share an input.**
  Three outside models once "confirmed" a reading taken from the same truncated
  file. Test the source before trusting agreement.
- **The network is open** (tested 2026-10-03): Sefaria, Perseus, Project
  Gutenberg, archive.org, Blue Letter Bible and web search all work. STEPBible
  and academic-bible.com refuse automated access; Beta maṣāḥǝft did not answer.
  Network access is a setting of the cloud environment, not a limit of Claude.
  Outside sources still follow the licence rule below, and a note's claims must
  still be checkable in what `source_text.py` prints.
- **`python-docx` and `playwright` are not preinstalled.** Run
  `pip install python-docx playwright` before `build_docx.py` (do not run
  `playwright install`; the browser is already there), or add the pip line to
  the environment's setup script. Tested 2026-10-03: all 24 Word files built.
- **Licences:** no share-alike or non-commercial sources, except CC BY-SA for the
  Ethiopian-only books (Andrew, 2026-09-23). Details are in `SOURCES.md`.
- **Word files:** `build_docx.py` draws the charts in headless Chromium. In the
  cloud container, run
  `CHROMIUM_PATH=/opt/pw-browsers/chromium python3 build_docx.py`. The `docx/`
  folder is gitignored. Send Word files only when Andrew asks.
- **The website caches by a content fingerprint**, so a normal refresh shows
  new chapters once GitHub Pages has deployed.
