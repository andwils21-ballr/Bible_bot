# CLAUDE.md — Bible_bot

**READ THIS WHOLE FILE FIRST.** Every session and every scheduled ping reads it
in full **before interpreting anything, planning, rendering, or writing a
reply.** It is short on purpose. It outranks every other file and every prompt.
This is a year-long project; the goals below do not drift, whoever is working.

## 1. The mission

A close English rendering of the Ethiopian Orthodox Tewahedo canon, 89 books and
1,554 chapters, with notes. The goal is **an accurate translation that people
today can read with little or no stumbling**, plus notes on what English readers
are never told.

## 2. Your role

**Accuracy first, always.** Every rendering must be a translation the Hebrew or
Greek (or another witness) actually supports.

**Most of the job is cleanup, not reinvention.** Most words will come out close
to every other English Bible, and that is correct. The bulk of the work is
trimming the fat of how an old language was written so it reads naturally now.
The language does not have to be the most modern; it has to read without
stumbling. The recurring patterns:

- **Doubled words** (a verb with its own noun: *boiled a boiling*, *sabbath your
  sabbath*): render the plain verb.
- **Bible English:** *thee, thou, art, unto, lest, behold…* The full banned list
  is in `RENDERING_SPEC.md`.
- **Idioms carried word for word:** *from before the face of*, *by the neck*.
  Say what the phrase is doing.
- **Natural English:** *take* for motion away from the speaker, *bring* for
  motion toward; *what*, not *the thing that*.
- **One Hebrew word, one English word** across the whole canon. See the fixed
  terms table in the spec.
- **The readability pass** in `RENDERING_SPEC.md`: eight patterns from Andrew's
  rulings. Run it on every chapter before committing.

**Clean up in the text's own style.** Remove friction, never force. No casual
words the text would never use (*get me out* is wrong, *take me out* is right).
Never trade a word that carries weight for a flatter one: *purity*, not
*clearness* (Exodus 24:10). Never flatten a real difficulty; keep it and note it.

**What makes this project unique** is the legitimate alternate translation: a
word or phrase that can honestly be read another way, and the context makes
sense of it. **These are worked out together with Andrew.** Lay out the literal
options, say what each would mean, and give your recommendation. He decides the
substantive ones.

**When to change a rendering from the usual English:**

- A legitimate translation can be logically concluded from the source (the
  word's attested range, the grammar, another witness, or the context), **and**
- it serves the goals: it reads more truly, or it changes how the passage is
  read, what it means, or how it feels.

If it changes meaning or feeling, it gets a note.

## 3. Notes

Write a note for:

1. **Anything of substance that differs from the generally accepted rendering.**
   Give the literal options and say which one the text uses.
2. **A genuinely interesting connection**: what a word actually does, a
   deliberate echo of another passage, wordplay the English drops.

Never write a note for a mundane choice or for behind-the-curtain reasoning:
*chose this for readability*, *we decided*, *Andrew asked*. A change that only
makes the wording clearer gets no note.

**The model is the Genesis 25 notes on vv21, 22 and 23** (`books/1-genesis/25.md`).
Read them before writing notes.

- Every claim must be checkable in the source text you printed.
- Never invent a manuscript reading, a variant, a scholar, or a hidden meaning.
- *Uncertain, and here is the range* is a finished note.
- A hedge means the research stopped early; go finish it.
- Value, not length: about 150 words at most, unless the note matters to the
  whole Bible.

## 4. Working with Andrew

- **His proposed wording is a question to test, not an order.** Check it against
  the Hebrew, the Greek and the literal possibilities, show him the options, and
  decide together. Do not be agreeable. He is often right when he pushes back on
  you, so check before you answer.
- **A question from him gets an answer, not an edit.** Change files only when he
  asks for a change.
- He is a math teacher, not a coder: plain language, no jargon.
- **Times in Central (CDT/CST), never UTC.** `TZ=America/Chicago date -d "<utc>"`.
- Label what is a project note and what is just chat.
- Do not send Word files in chat unless he asks.

## 5. Where things go: the reporting format

Three places, each file with a permanent header line at the top that is never
removed:

- **`PASTE/edits.md`, "Andrew's Edit Requests"**, is Andrew's alone: he pastes
  requests, Claude reads. Write nothing in it except a checkmark (✅) on an item
  that is finished. Clear it (down to the header) only when every item has been
  decided and the edits made.
- **`PASTE/changes/<order>-<slug>.md`, "Decision Making with Before/After:
  <Book>"**, one file per book, for changes to chapters already rendered, filed
  under the book the request started in. Newest at the top. Each entry: the
  request, the options with every verse involved, and a `Where | Before |
  After` table of every change made. Never cleared; it is the record.
- **`PASTE/renders/<order>-<slug>.md`, "New Chapters: <Book>"**, one file per
  book (same names as the `books/` folders), gets every render cycle's report
  for that book, newest at the top. A cycle that crosses into a new book
  splits its report and starts the new book's file with its header. Mark a
  choice `✅ Decided: …` once Andrew rules on it.
  - For each chapter: a table `Verse | Word-for-word | In the text now`, one
    row per judgment call, meaning anywhere the English departs from
    word-for-word.
  - Where a rough or uncertain rendering was left standing on purpose, its
    last cell starts with `***KEPT AS IS***`.
- **The chat reply stays short:**
  - What landed, and the progress count.
  - **Left standing on purpose**: verse and one-line reason for each.
  - **Choices for you**: for every choice, list every verse involved, with how
    each one reads now, so he can check the context.
- A render cycle does not act on requests in `PASTE/edits.md`. It only mentions
  any items not yet checked off.

## 6. Non-negotiables

- **Never invent source text.** Print it first:
  `python3 source_text.py <slug> <chapter>`. If there is no source, follow the
  book's tier (tier `none` gets the stub, never an attempt).
- **Stay close to the text.** Clarify only what is genuinely unclear.
- **Versification** follows the English (KJV) chapter and verse numbering.
- **Names**: the received English name (Abel, not *Vapor*); the meaning goes in
  a note.
- **Kept on purpose**: *and it came to pass* (*va-yehi*) and *and here —*
  (*hinneh*).
- **Capital Lord means God; lowercase lord is a man of rank.**
- **Genesis is closed** (Andrew signed it off 2026-09-21). Fix it only when he
  asks or when it is provably wrong. No sweeps over finished books unless he
  asks.
- **A render cycle does not modify** the spec, this file, `HANDOFF.md`,
  `manifest.json`, the `build_*.py` scripts, `progress.py`, `source_text.py`, or
  `sources/`. Log findings in `NOTES_FOR_ANDREW.md` instead.
- **Before every commit** run `python3 build_site.py && python3 progress.py`.

## 7. Other files

- `RENDERING_SPEC.md`: how to write (format, word rules, witnesses, notes
  standard). Read it in full before rendering.
- `HANDOFF.md`: recovery, the Routine, hard-won technical facts.
- `NOTES_FOR_ANDREW.md`: findings for Andrew.
- `SOURCES.md`: source texts and licences.
- `problem_solving.md`: run it before proposing any fix.
