# 1 Enoch 1–6 — what the checks found

Two rounds of checking, 2026-09-17.

## Round 1 — three outside Ge'ez readings

ChatGPT, Gemini and Grok each rendered the same Ge'ez word by word,
independently. The useful result was **where each silently replaced the Ge'ez
with the standard English Enoch it already knew**, which the word-by-word
format exposed because each model's literal line and smooth line contradict
each other.

- **Gemini**, three times: at 1:5 its literal reads "And they shall fear
  [all men / the watchers]" — the bracket is its own guess — and its smooth
  English asserts "and the Watchers shall quake." At 1:7 its literal says
  "submerged" and its smooth says "rent asunder." At 6:6 its literal says
  "Ardis" and its smooth says "in the days of Jared."
- **GPT**, twice: at 1:6 it glosses "perhaps honeycomb" and prints "like wax";
  at 1:4 it alone reads "in his strength/power," which is the Aramaic's word,
  not the Ethiopic's. To its credit it flagged the Ardis/Hermon difference in a
  note of its own and refused to substitute.
- **Grok** never diverged between its own two lines. The most conservative of
  the three, and the shortest.

## Round 2 — the file itself was broken

Every one of those three models was translating a **truncated text**, because
the Ge'ez file in this repository was truncated. The OCP XML splits each verse
across several `<unit>` elements to carry its apparatus; `fetch_ocp.py`'s
predecessor read only the first unit. **361 of 543 Ge'ez verses in 1 Enoch
ended mid-sentence.**

So three independent checks agreed with each other and with me, and all four of
us were wrong together — because the disagreement was never in the text, it was
in the input all of us shared. What caught it was a structural test on the file
(counting Ge'ez full stops `።`), not a second opinion.

With the parser fixed, 1:5 reads to its end and contains **ትጉሃን** *təguhān*,
**the Watchers** — present in the Ge'ez all along.

## What survived, and what it cost

| Claim | Verdict |
|---|---|
| 1:7 the Ge'ez has the earth **submerged** where the Greek **splits** it | **Stands, and is now solid.** Full text on both sides; a real disagreement about how the world ends |
| 1:6 the Ge'ez says **honeycomb**, printed English says **wax** | **Stands.** Three outside readings gave honeycomb; the OCP's own English gives wax |
| 1:4 the Ge'ez says **camp/host** | **Half right.** The full verse has *both* — appear with His host, **and** appear in the strength of His power |
| 6:6 the Ge'ez names **Ardis** instead of dating the descent | **Wrong as stated.** Ardis is the *summit of Hermon*; the verse continues, and explains the name from the oath |
| 6:6 no witness connects Hermon to the oath | **Backwards.** The Ge'ez states it outright: *they called it Mount Hermon, because they had sworn upon it* |
| 1:5 / 5:4 / 5:8 / 2:2 / 6:8 "the Ethiopic drops this" | **All artifacts of the bug.** Deleted |
| 1:6 the verb means terror rather than shaking | **Overstated.** Corrected in round 1 |
| 1:9 the Ge'ez tense matches Jude's | **Overstated.** Corrected in round 1 |

## The lesson worth keeping

Independent opinions are only independent if they do not share an input. Three
models fed the same corrupted file produce three confident confirmations of the
corruption. Before commissioning an outside check on a source, test the source:
does every verse end where a sentence ends?
