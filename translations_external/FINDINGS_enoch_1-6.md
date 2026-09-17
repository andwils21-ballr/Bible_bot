# What the three outside readings showed — 1 Enoch 1–6

Three independent word-by-word Ge'ez renderings (ChatGPT, Gemini, Grok), read
against the Greek and Qumran Aramaic in `sources/`. Checked 2026-09-17.

The useful result is not that they agreed. It is **where each one silently
replaced the Ge'ez with a reading it already knew from the Greek** — and the
word-by-word format caught it every time, because the literal line and the
smooth line of the same model contradict each other.

## Gemini imports the Greek into its English three times

| Verse | Gemini's own literal line | Gemini's smooth English |
|---|---|---|
| 1:5 | "And they shall fear **[all men / the watchers]**" — the bracket is its own guess | "And all shall be smitten with fear, **and the Watchers shall quake**" |
| 1:7 | "And it [the earth] shall be **submerged**" | "And the earth shall be wholly **rent asunder**, and all that is upon the earth shall perish" |
| 6:6 | "ʾArdīs — **Ardis**" | "who descended **in the days of Jared**" |

In all three the Ge'ez has no such words. The Watchers, the rending, and Jared
are in the Greek and the Aramaic — not in the Ethiopic text being translated.
Gemini's smooth line is the standard English Enoch, not a translation of what
is in front of it.

## GPT does the same twice, more quietly

- **1:7** — glosses ወትሰጠም as "broken/rent" in the literal line itself, against
  Gemini's and Grok's "submerged." This is the one place GPT reaches the Greek
  reading at the lexical level rather than in the paraphrase.
- **1:6** — literal line reads ግራ as "perhaps honeycomb/honey," then the smooth
  line prints **"like wax"** — the King James phrase, not what it just glossed.
- **1:4** — alone of the three, glosses በትዕይንቱ as "in his strength/power," which
  is what the **Aramaic** says. Gemini and Grok both read it as "in his camp/host."

To its credit GPT flagged one of these in a note of its own: it recorded that
the supplied text reads አርዲስ where common editions have Mount Hermon and the
days of Jared, and said it did not substitute.

## Grok is the most conservative

Grok's literal and smooth lines agree with each other everywhere checked. It
never imports a reading it cannot see in the Ge'ez. It is also the shortest and
least explained of the three.

## Where this leaves the rendering in `books/16-1-enoch/`

| Point | Verdict |
|---|---|
| 1:4 "in his camp" is what the Ge'ez says | **Confirmed** — Gemini and Grok both; GPT's outlier reading is the Aramaic's |
| 1:6 "honeycomb," not "wax" | **Confirmed** — all three literal lines |
| 1:7 the Ge'ez sinks where the Greek splits | **Confirmed** — Gemini's and Grok's literal lines; this is the finding the format was for |
| 6:6 Ardis, not Jared | **Confirmed** — all three literal lines |
| 1:5 the Ge'ez has no Watchers | **Confirmed** — all three; Gemini added them anyway |
| 1:6 the Ge'ez verb means terror rather than shaking | **Overstated — note corrected.** All three gloss it as shake/tremble |
| 1:9 the Ge'ez tense matches Jude's | **Overstated — note corrected.** All three declined to commit; the form is perfect but prophetic perfects read as future |

Two of my notes were stronger than the evidence and have been rewritten. Five
held.
