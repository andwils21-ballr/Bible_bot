# Rendering Spec

How to write a chapter. The mission, your role, the notes policy and the
non-negotiables are in `CLAUDE.md`; read that first. Consistency across 1,554
chapters matters more than any one chapter being clever.

## Style

1. **Preserve the register.** Law sounds like law, poetry breaks in lines, a
   genealogy stays monotonous, prophecy keeps its abruptness, letters sound like
   letters.
2. **Keep the source's word order and emphasis** where English can carry it.
3. **Do not smooth out difficulty.** Where the source is ambiguous or damaged,
   the English stays so, and the note says so.
4. **Divine names:** YHWH → *the LORD*; *Adonai* → *the Lord*; *Elohim* → *God*;
   *El Shaddai* → *God Almighty* (note the first time in a book); Greek
   *Kyrios* → *Lord*.
5. **Weight goes in the notes, not in brackets** in the text.
6. **Repeated formulas stay identical** every time they occur.

Not a summary and not a paraphrase: every verse in the source gets a verse. If a
line comes out like a standard English Bible, that is usually right, as long as
it came out that way because it is right, not because it was copied.

## File format

One file per chapter: `books/<order>-<slug>/<NN>.md` (two digits; three for
books over 99 chapters).

```
---
book: Matthew
book_order: 55
slug: matthew
chapter: 1
title: The Origin of Jesus the Messiah
status: rendered
tier: source
rendered: 2026-09-14
---

# Matthew 1

## The Origin of Jesus the Messiah

**1** A record of the origin of Jesus the Messiah, son of David, son of Abraham:

---

## Notes

- **v1 "record of the origin"** — Gk. *biblos geneseōs*, literally "book of
  genesis"…
```

- Frontmatter is mandatory valid YAML. `status` is `rendered` or `need_source`.
- One H1, `# <Book> <Chapter>`. H2 section headings only where the text has
  real movements.
- Every verse starts its own paragraph with `**N** `. For poetry, keep the
  marker and break lines with a trailing double space. The site and the Word
  build depend on this exact convention.
- `## Notes` is mandatory: three to ten entries, each anchored to a verse.
- No preamble and no sign-off.

## Word rules

### Banned in the rendered text

*lest, behold, unto, thee, thou, thy, thine, ye, art* (as a verb), *verily,
wherefore, whence, thence, hither, thither, peradventure, nay, yea, ere,
betwixt, amongst, whilst, hearken, bade, wrought, albeit, abide* (meaning
remain), *in the midst of* (use *among*, *in the middle of*, *inside*).

For *pen*, the Hebrew behind most *lest*: *or you will…*, *otherwise…*, *in
case…*, or a dash and a plain clause.

### Kept on purpose (settled rulings)

- **"And it came to pass"** for *va-yehi*, the scene-opening formula.
- **"And here —"** for *hinneh*, the word that puts the reader inside someone's
  eyes at the moment of seeing. **Not in laws that describe an inspection**
  (Andrew, 2026-09-25): there *hinneh* only introduces what the priest finds, so
  the sentence ends and the finding starts a new one: *The priest shall look at
  him on the seventh day. If the mark has stayed as it was…* (Leviticus 13:5).

### No "And" at the start of a sentence (Andrew, 2026-09-25)

Hebrew joins almost every clause with *ve-*, "and". Do not start a sentence or a
verse with *And*. Keep it only where it does real work, and say why in the
report. The kept cases so far:
- *And it came to pass* and *And here —* (above);
- **Exodus 1:1**, *And these are the names*, where the note is built on the book
  continuing Genesis;
- **Leviticus 1:1**, *And He called*, the book's Hebrew title.

Where the joining word means *but*, *so* or *then*, use that word.

### Already ruled

| Instead of | Use |
|---|---|
| *sojourn* (*gur*) | *live as a guest*; the noun *ger* is *a guest* |
| *after its kind* (*le-mino*) | *of every kind* |
| *the bone of that same day* (*be-etsem ha-yom*) | *on that very day* |
| *bring* for motion away from the speaker | *take* (*take me out of this house*); the formula *the LORD who brought you out of Egypt* stays |
| *the thing that* | *what* (*this is what the LORD has commanded*) |
| a doubled verb (*boiled a boiling*) | the plain verb; the doubling may go in a note |
| an idiom a reader must decode (*with a high hand*) | say what it does (*in open defiance*); the literal form in the note |

Plain old words still in use stay: *flesh, seed, loins, womb, dread, kindred*.
The goal is simplicity, not blandness. It is the translationese that goes, not
the force.

### The readability pass (Andrew's rulings on Exodus 16–19, 2026-09-25)

Run this on every chapter before it is committed. Each item is a pattern Andrew
had to flag by hand; the reader should never meet one.

1. **Doubled words.** A verb with its own noun becomes the plain verb: *the sin
   he sinned* → *the sin he has committed*; *grumblings you grumble* → *your
   grumblings*; *stone him with stones* → *stone him*; *swarming things that
   swarm* → *things that swarm*. The same noun twice in one clause becomes a
   pronoun when the pronoun is clear: *bring the blood and dash the blood* →
   *dash it*.
2. **Word order.** The object goes after the verb: *And all its fat he shall
   turn into smoke* → *He shall turn all its fat into smoke*. Keep the Hebrew
   order only where a note is built on the emphasis.
3. **Hebrew verb-nouns become clauses.** *in His hearing your grumblings* →
   *because He has heard your grumblings*; *of the going out of the sons of
   Israel* → *after the sons of Israel went out*.
4. **Strings of small words.** *on the wood that is on the fire that is on the
   altar* → *on the wood burning on the altar*; *for he had said* → *because he
   said*; *this thing* → *this*.
5. **Who is doing it.** When two people are in the scene (priest and worshipper,
   owner and buyer) and *he* could be either, name the one who acts. A people
   called by its ancestor's name is the people: *Amalek came* → *the Amalekites
   came*.
6. **Hand and face idioms.** *his hand cannot reach* → *he cannot afford*;
   *favor the face of the poor* → *show favor to the poor*; *by the mouth of the
   sword* → *with the sword*. The literal form goes in a note when the note has
   something to say about it.
7. **Read the English for what it says.** *The land will not vomit you out when
   you make it unclean* said the opposite of the Hebrew; it is now *Otherwise,
   when you make the land unclean, it will vomit you out* (Leviticus 18:28).
8. **Old words with a plain equal.** *talebearer* → *slanderer*; *earthen
   vessel* → *clay pot*; *go in to a dead body* → *go near*.

Keep a literal phrase only when a note is built on it, and say so in the render
report (`***KEPT AS IS***`).

### Fixed terms: one Hebrew word, one English word

Use these everywhere. Never give two of these Hebrew words the same English word.

| Hebrew | English | Decided |
|---|---|---|
| *tsara'at* (and *metsora*) | blight | 2026-09-23 |
| *to'evah* | detestable (plural: detestable things) | 2026-09-23 |
| *sheqets* / *shiqquts* (verb *shiqqets*) | loathsome (verb: loathe) | 2026-09-23 |
| *toshav* | resident | 2026-09-24 |
| *re'ach nichoach* | soothing aroma | 2026-09-24 |
| *eved* when God is the master | servant | 2026-09-24 |
| *ben nekhar* (a person of another nation) | foreigner | 2026-09-24 |
| *ger* (and the verb *gur*) | guest (verb: live as a guest) | 2026-09-24 |

When a recurring word needs a fixed rendering, bring the choice to Andrew with
every verse it occurs in, then add it here.

## Names

Use the English name the reader already knows: **Abel, not Vapor; Eve, not
Living.** The names are the same Hebrew words worn smooth by three thousand
years of use, and a reader must be able to find Cain and Abel in Genesis 4.
What a name means goes in a note, together with what the verse does with it.

No inline glosses on names English already knows (*Beersheba*, not *Beersheba —
Well of the Oath*). The one allowance is a place with no English identity at
all, and even there prefer the note.

One standing exception: the town where Terah dies is spelled **Harran**, to
keep it apart from his son **Haran**. The two are different Hebrew words.
Any further exception must be argued in a note and added here.

## Versification

Follow the English (KJV) chapter and verse numbering, even where the source file
divides differently. `source_text.py` prints the source's own numbering; see
`HANDOFF.md` for the known offsets. Psalm titles go above verse 1 without a
number. Where no English tradition exists (Enoch, Jubilees, Meqabyan, the
Ethiopian books), follow the source and say so in the first note of chapter 1.
One short note where the numbering differs is enough.

## Sources and tiers

Before rendering any chapter, print its source and keep it in front of you:
`python3 source_text.py <slug> <chapter>`. `sources/hebrew/` is the
Westminster Leningrad Codex. `sources/greek/` holds the SBLGNT (New
Testament) and Swete's Septuagint where it has been extracted (Genesis, Exodus,
the deuterocanon). `sources/swete-src/` holds the whole Septuagint.

If the helper reports no source, obey what it says for the book's tier:

- **`english-only`** is worked from established translations, and chapter 1's
  first note says so. Currently: 1–3 Meqabyan (Ge'ez found, not yet in
  `sources/`) and Esther 11–16.
- **`none`** gets the stub only (see Honesty rules). Currently: Josippon and
  books 82–89.

Never accept an OCR'd text with made-up verse numbers as a source.

### When the witnesses differ (Andrew's rule, 2026-09-23)

The aim is the most accurate account of the event the text describes.

1. **Start from the text closest to the original language**: Hebrew for the Old
   Testament, Greek for the New. Most verses never leave it.
2. **Use another witness where it tells the event better and the context backs
   it**, whether because it has a clearer word or preserves a reading the rest
   of the book supports.
3. **Keep detail one witness has and another lacks, if the context supports it.**
4. **"The context supports it" must be checkable:** another passage that says
   the same (Numbers 26:59 backs the Greek of Exodus 6:20 naming Miriam), the
   logic of the passage, or agreement among witnesses. Never "smoother" or
   "more familiar".
5. **Every departure gets a note** naming the witness followed and quoting what
   the default text says. The witness must be in `sources/`.

### Tier `witnesses`: 1 Enoch, Jubilees, Ezra Sutuel, 4 Baruch

These survive as partial witnesses that disagree. `source_text.py` prints each
witness, its scholarly English, and a mechanical divergence list.

- Render from the witnesses, and say which witness each statement comes from.
- The divergences are the best material, but a flagged verse is a lead, not a
  finding.
- A chapter with no witness is `english-only`.
- A claim about a Ge'ez word cannot be checked the way Hebrew or Greek can:
  quote it and report differences, but build no argument on what it supposedly
  means.

## The notes standard

**Dig as far as the word goes.** The worked example is John 1:1, *logos*. English
hears "word", but Greek had a plain word for an utterance (*rhēma*) and John did
not use it. *Logos* comes from *legō*, to gather or lay in order. It came to
mean an account, a ratio, the governing principle of a thing (the *-ology*
words). And *en archē* is letter for letter the opening of Genesis in Greek. That
depth, with no invented manuscript, no scholar cited, and no secret claimed, is
the target.

**The test:** would someone who reads the source language agree this is
actually in the word? If a note needs a wink to work (a hidden layer asserted
because a plain verse felt plain, or a modern idea read backwards) cut it. One
reaching note makes every true note untrustworthy.

**A hedge is unfinished work.** A note that ends in a shrug (*which is
strange*, a deadpan restatement) reads as quiet contempt for the reading it
presents. The fix is never rewording. Go and find out where else the word
appears and what follows, then state the conclusion, or state the uncertainty
as a finding that names what was checked.

**Written for a reader who never sees the curtain.** No first person about the
work, no process history. Where a substantive choice needs explaining, explain
it from the language: the options, what each means, which one the text uses.
Genesis 25:22 is the model.

## Honesty rules

1. **Tier `none` books get a stub.** One file, `books/<order>-<slug>/00.md`, with
   the book title and `(NEED SOURCE TO TRANSLATE)`, `status: need_source`. Then
   move on.
2. **Tier `english-only` books say so** in the first note of chapter 1: which
   tradition is followed, and that no source language was involved.
3. **If you do not know a word, say so.**
4. **Never fabricate a manuscript reading, a variant, or a scholar.**
5. **If a chapter does not exist** in this canon's numbering, write the stub
   and note it.

## Pace

Quality over throughput: four excellent chapters beat twelve thin ones. Never
pad notes, and stop one chapter early rather than rush the last.
