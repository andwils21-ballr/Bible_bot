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
| Render reports (new chapters) | `PASTE/renders.md` |
| Before/after of every change to finished chapters | `PASTE/changes.md` |
| Known problems, findings for Andrew | `NOTES_FOR_ANDREW.md` |

## Taking over

1. Attach the repo: `add_repo` with owner `andwils21-ballr`, repo `Bible_bot`,
   access `push`. Clone where the tool says, then `register_repo_root`.
2. Read `CLAUDE.md`, then `RENDERING_SPEC.md`, in full.
3. Read the last three rendered chapters, and the Genesis 25 notes, for voice.
4. Recreate the Routine (below), and do one render cycle by hand first.

## The Routine

- **Timing:** currently fires at 8:01 AM, 1:01 PM and 6:01 PM Central, which is
  cron `1 13,18,23 * * *` in UTC during daylight time.
- **Binding:** it is self-bound, meaning it fires into the session that created
  it, which gives it that session's repo access and model.
- **To recreate it:** `create_trigger` with neither `create_new_session_on_fire`
  nor `persistent_session_id`, from an Opus session, with the prompt in
  `ROUTINE_PROMPT.md`.
- **Do not test with `fire_trigger`.** It spawns a separate session and gives a
  misleading failure. Wait for a real scheduled firing.

## Hard-won technical facts

- **Hebrew and English chapter divisions differ.** We follow the English;
  `source_text.py` prints the Hebrew numbering. Known offsets:
  - Genesis 31:55 = Hebrew 32:1.
  - Exodus 8:1–4 = Hebrew 7:26–29.
  - Leviticus 6:1–7 = Hebrew 5:20–26, and Leviticus 6:8–30 = Hebrew 6:1–23.

  Count the verses per chapter in the Hebrew file before rendering.
- **Swete's Greek does not line up with the Hebrew.**
  - It is out of step at Genesis 35:21–22, Exodus 7/8, Exodus 21/22 and
    Leviticus 7 (Hebrew 7:21 is Swete 7:11).
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
- **The network reaches GitHub and nothing else.** Clone public repos over https.
- **Licences:** no share-alike or non-commercial sources, except CC BY-SA for the
  Ethiopian-only books (Andrew, 2026-09-23). Details are in `SOURCES.md`.
- **Word files:** `build_docx.py` draws the charts in headless Chromium. In the
  cloud container, run
  `CHROMIUM_PATH=/opt/pw-browsers/chromium python3 build_docx.py`. The `docx/`
  folder is gitignored. Send Word files only when Andrew asks.
- **The website caches by a content fingerprint**, so a normal refresh shows
  new chapters once GitHub Pages has deployed.
