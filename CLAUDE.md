# CLAUDE.md — Bible_bot

A close rendering of the Ethiopian Orthodox Tewahedo canon into English: 89 books,
1,554 chapters, built a few chapters at a time by a scheduled Routine.

## About Andrew

Math teacher and coach, Mathematics degree, 15 years trading. Not a coder — explain
in plain terms and never assume programming knowledge. Values honesty and being
told plainly when something is wrong or unverified.

**Always give times in Andrew's local Central time, never UTC.** America/Chicago:
CDT (UTC-5) in summer, CST (UTC-6) in winter — use whichever is actually in effect
on the date in question, and label it. Tool output and logs come back in UTC;
convert before showing him. `TZ=America/Chicago date -d "<utc timestamp>"` handles
DST correctly.

## If you are a fresh session picking this up

Read **`HANDOFF.md`** first. It carries Andrew's editorial rules as settled in
conversation, the technical facts that cost real time to learn, and how to
recreate the scheduled Routine. Nothing about this project lives in a model's
memory; it is all in this repo.

## Before writing anything

Read `RENDERING_SPEC.md` in full. It is the style contract — the voice, the file
format, the depth standard for notes, and the honesty rules. It is not yours to
revise. If you think it is wrong, append the finding to `NOTES_FOR_ANDREW.md` and
leave the spec alone; Andrew decides.

`python3 progress.py` tells you which chapter is next. Read the last two rendered
chapters before starting, to match voice and note density.

## The one rule above all others

**Never invent source text.** Fluent invention reads exactly as authoritative as
real work, and a single fabricated note poisons every true note beside it. Where
there is no real basis, the `(NEED SOURCE TO TRANSLATE)` stub is the finished,
correct output. Tier `none` books get stubs, never attempts. "This word is
uncertain, and here is the range" is a complete note, not a failure.

## A hedge means you stopped researching

A note that ends in a shrug — *which is strange*, a deadpan restatement, a
balance-sounding non-conclusion — is almost never balanced judgment. It is
research that stopped one step early. And it does not read as neutral: it reads
as quiet contempt for the reading being presented, which readers hear correctly.

The tell is that you are about to present a reading and cannot say what follows
from it. The fix is not rewording, it is going and finding out — where else the
word appears, what is built from it elsewhere, who else does the same thing.
Then state the conclusion with conviction, or state the uncertainty as a finding
that names what was checked. See "The hedge is a symptom" in RENDERING_SPEC.md.

## Do not touch

`RENDERING_SPEC.md`, `manifest.json`, `build_site.py`, `build_docx.py`,
`progress.py`. Chapters are what changes; the machinery is not.

## Build

```
python3 build_site.py    # books/ -> docs/   (stdlib only)
python3 progress.py      # regenerates PROGRESS.md from files on disk
python3 build_docx.py    # books/ -> docx/   (pip install python-docx)
```

Run `build_site.py` and `progress.py` before every commit.
