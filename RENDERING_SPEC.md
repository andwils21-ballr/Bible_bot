# Rendering Spec

This is the contract every scheduled session follows. It is the only place the
style is defined — do not improvise a different one, and do not "improve" it
mid-project. Consistency across 1,554 chapters matters more than any single
chapter being clever.

## What this project is

A close rendering of the Ethiopian Orthodox Tewahedo canon into English that
carries the **intent, tone, and force** of the source, not the house style of
the English Bible tradition. Word-for-word where the source is word-for-word;
idiom-for-idiom where a literal rendering would mislead. Never a paraphrase,
never a summary.

## What this project is NOT

- Not a summary. Every verse in the source gets a verse in the rendering.
- Not a modernization. If the source is formal, repetitive, or blunt, so are we.
- Not KJV/NIV/ESV with the words shuffled. If a line comes out reading exactly
  like a standard English Bible, that is usually correct — those translators
  were not fools. But it should come out that way because it's right, not
  because it was copied.
- Not a place to guess. See "Honesty rules" below.

## Style rules

1. **Preserve the register.** Legal text sounds legal. Poetry breaks in lines.
   A genealogy is supposed to be monotonous — let it be monotonous. Prophetic
   oracle keeps its abruptness. Letters sound like letters, including the
   places where Paul's sentences run away from him.
2. **Keep the source's word order and emphasis** where English can carry it.
   Hebrew and Greek front the word they want stressed; English can usually
   do the same with a small rearrangement rather than a footnote.
3. **Do not smooth out difficulty.** Where the source is ambiguous, obscure, or
   textually damaged, the English should be too — flag it in the notes rather
   than picking a reading silently.
4. **Divine names.** YHWH → "the LORD" in small caps convention (`the LORD`);
   *Adonai* → "the Lord"; *Elohim* → "God"; *El Shaddai* → "God Almighty" with
   a note the first time it appears in a book. Greek *Kyrios* → "Lord."
5. **Untranslatable weight goes in the notes, not in brackets in the text.**
   Keep the rendering clean and readable.
6. **Repeated formulas stay identical.** "And it was evening and it was
   morning" reads the same every time. Concordance beats variety.

## Required file format

One file per chapter: `books/<order>-<slug>/<NN>.md` — e.g. `books/55-matthew/01.md`.
Chapter numbers are zero-padded to two digits (three for Psalms: `119.md` is fine,
use `%03d` for any book over 99 chapters).

```
---
book: Matthew
book_order: 55
slug: matthew
chapter: 1
title: The Origin of Jesus the Messiah
status: rendered
tier: primary
rendered: 2026-09-14
---

# Matthew 1

## The Origin of Jesus the Messiah

**1** A record of the origin of Jesus the Messiah, son of David, son of Abraham:

**2** Abraham fathered Isaac, and Isaac fathered Jacob, ...

---

## Notes

- **v1 "record of the origin"** — Gk. *biblos geneseōs*, literally "book of
  genesis." Matthew opens his gospel with the title of the first book of the
  Torah. The English reader should hear a new beginning being claimed.
- **v18 "promised in marriage"** — Gk. *mnēsteutheisēs*. Not "engaged" in the
  modern sense: a binding legal state that required a divorce to dissolve.
  This is why v19 is about divorce, not a broken promise.
```

### Format rules

- **Frontmatter is mandatory** and must be valid YAML. `status` is `rendered`
  or `need_source`. Nothing else.
- **`# <Book> <Chapter>`** is the one H1. Section headings inside a chapter are
  H2 and are yours to choose where the text has natural movements — but only
  where the text actually has them.
- **Every verse starts with `**N** `** at the start of its own paragraph.
  Poetry: keep the verse marker, then break lines with a trailing double-space.
  This single convention is what the website turns into clickable verse anchors
  and what the .docx build turns into bold verse numbers. Do not deviate.
- **`## Notes` is mandatory** and is the part that makes this worth doing.
  Three to ten entries per chapter. Each one anchored to a verse, naming the
  source word where it matters, explaining what English loses. No filler —
  if a chapter honestly has three things worth saying, write three.
- No preamble, no "this rendering seeks to..." paragraph, no sign-off. The
  notes carry the commentary.

## Work from the source text, never from memory

Before rendering any chapter, print its source and keep it in front of you:

```
python3 source_text.py <slug> <chapter>
```

`sources/hebrew/` holds the Westminster Leningrad Codex; `sources/greek/` holds
the SBLGNT. Every claim a note makes about a word must be checkable against the
line the helper just printed. Recalling what a verse says is not the same as
reading it, and the difference shows up exactly where the notes are most
confident.

When the helper reports no source, it tells you what that book's tier requires.
Obey it. A missing source is never a licence to render from memory — it is the
instruction to work from established translations (tier `secondary`, and say so
in the notes) or to write the stub (tier `none`).

Known gaps, as of this writing: there is no Septuagint in `sources/`, so Tobit,
Judith, Wisdom of Solomon, Sirach, Baruch, and the Letter of Jeremiah are tier
`secondary`, and so are Psalm 151, Daniel 13-14, and Esther 11-16, which lie
past the end of the Hebrew. If an LXX is ever added, those tiers should be
raised and this paragraph corrected.

## The depth standard for notes

The notes are the reason this project exists. A rendering without them is just
another English Bible. Aim at the thing English readers are never told.

Worked example — John 1:1, *en archē ēn ho logos*. "In the beginning was the
Word" makes an English reader picture speech, vocabulary, a message. What the
Greek actually carries:

- Greek has a plain word for an individual utterance, *rhēma*. John did not
  use it.
- *Logos* comes from *legō*, which meant **to gather, collect, lay side by side
  in order, count up** long before it meant "to speak." Speaking is the late
  sense — you say things because you first arranged them. Latin *legere* is the
  same root, which is why "collect," "select," and "legible" are cousins.
- By the classical period *logos* also means an account or reckoning; a
  **ratio** (it is the term for ratio in Euclid's *Elements* Book V, which the
  Romans rendered *ratio*, giving us "rational"); the governing principle of a
  thing (the sense surviving in every "-ology" — biology is the ordering
  account of life, not words about it); and a structured argument.
- Heraclitus had already used it for the underlying law by which all things
  come to pass. The Stoics made it the rational principle pervading the cosmos.
  Philo made it the blueprint God worked from. Educated readers had all of that
  loaded when they saw the word.
- And the first two words are, letter for letter, the opening of Genesis 1:1 in
  the Greek Old Testament. John is not starting a story; he is restarting *that*
  one.

So the honest note says: the sense is closer to **the ordering principle by
which everything holds together, the reckoning the universe adds up to** — and
then notes the guardrail, that John immediately personalizes it, so it is not
impersonal mechanism.

That is the target depth. Note also what the example does *not* do: it invents
no manuscript, cites no scholar, and claims no secret. Every load-bearing claim
is a fact about the word.

### The test every note must pass

**Would someone who reads the source language agree this is actually in the
word?**

- If yes, dig as far as it goes. Etymology, semantic range, what the
  neighbouring culture heard, what the author chose *not* to say, sound and
  rhythm, a deliberate echo of another passage.
- If it needs a wink to work — a hidden layer asserted because a plain verse
  felt too plain, a modern idea read backwards into an ancient word — cut it.

The moment one note reaches, every other note becomes untrustworthy, including
the true ones. Three honest notes beat ten impressive ones. "This word is
uncertain and here is the range" is a finished note, not a failure.

## Honesty rules

These are not negotiable. The failure mode of this project is fluent invention
that reads exactly as authoritative as real work.

1. **Tier `none` books get a stub, not a rendering.** Write one file,
   `books/<order>-<slug>/00.md`, whose body is the book title and the line
   `(NEED SOURCE TO TRANSLATE)`, with `status: need_source`. Then move on to
   the next book that can actually be rendered. Do not attempt the text.
2. **Tier `secondary` books say so.** These are worked from established English
   translations, not from the Ge'ez. The first note on chapter 1 of every
   secondary book states which tradition it is following and that no source
   language access was involved.
3. **If you do not know a word, say so in the notes.** "Uncertain" is a real
   answer and is always better than a confident wrong one.
4. **Never fabricate a manuscript reading, a variant, or a scholar's name.**
   Notes cite the source language and the sense, not a bibliography.
5. **If a chapter turns out not to exist** in this canon's versification, do not
   invent it. Write the stub, note the discrepancy, move on.

## Pace

Quality over throughput. A session that renders four excellent chapters with
real notes has done better work than one that renders twelve thin ones.
Never pad the notes to hit a count. Never rush the last chapter of a session —
stop one chapter early instead.
