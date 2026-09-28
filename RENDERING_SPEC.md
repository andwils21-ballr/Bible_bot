# Rendering Spec

How to write a chapter. The mission, your role, the notes policy and the
non-negotiables are in `CLAUDE.md`; read that first. Consistency across 1,989
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
- **No "here —" or "look —" for *hinneh* / *idou*** (Andrew, 2026-09-28,
  replacing the ruling of 2026-09-25). In every book, rendered and still to
  come, in narrative and in speech: end the sentence before it and start the
  next with what is seen, or let the clause run on (*He looked: the bush was
  burning*; *A man with blight came and knelt before Him*; *I am old*, not
  *Look now — I am old*). God's *hinneh* + participle is *I am about to…* or
  *I will…* (*I am about to strike the water*, Exodus 7:17). *I — hinneh — I*
  is *I Myself* (Exodus 14:17). A presentation may be *Here is* (*Here is the
  blood of the covenant*, Exodus 24:8; *Here is My servant*, Matthew 12:18;
  *Here is the bridegroom!*, Matthew 25:6). **Keep it only where cutting loses
  something the word carries** — so far: *and here, it was Leah* (Genesis
  29:25; Jubilees 28:4), the morning's discovery; and *And here — He came*
  (1 Enoch 1:9), the words Jude quotes.

### Pronouns for God and for Jesus (Andrew, 2026-09-28)

Capitalize every pronoun that points to God or to Jesus: *He, Him, His,
Himself*, and in their own speech or when they are spoken to, *Me, My, Mine,
Myself, You, Your, Yourself*. This holds whoever is speaking: the disciples
(*Lord, save us*), His enemies (*Let Him be crucified!*) and the narrator. It
holds in an Old Testament quotation where the Gospel applies the words to Jesus
(*I will put My Spirit upon Him*, Matthew 12:18; *they will lift You up*, 4:6).
A note that quotes the Old Testament as the Old Testament keeps its pronouns as
that book has them (*he carried our sicknesses*, Isaiah 53:4). Figures inside a
parable (*the master of the house*) stay lowercase.

### No "And" at the start of a sentence (Andrew, 2026-09-25)

Hebrew joins almost every clause with *ve-*, "and". Do not start a sentence or a
verse with *And*. Keep it only where it does real work, and say why in the
report. The kept cases so far:
- *And it came to pass* (above), and *And here —* where it is kept (above);
- **Exodus 1:1**, *And these are the names*, where the note is built on the book
  continuing Genesis;
- **Leviticus 1:1**, *And He called*, the book's Hebrew title;
- **Genesis 1:1–2:3**, the creation week: *And God said… And it was so… And
  God saw that it was good… And it was evening, and it was morning.* The *And*
  carries the rhythm of the seven days (Andrew, 2026-09-25).
- **"And it shall come to pass"** / **"And it will come to pass"** for
  *ve-hayah* as a formula (*ve-hayah ki…*, *ve-hayah ka'asher…*: "and it shall
  be, when…"), the future twin of *And it came to pass*; the past habitual is
  *And it would come to pass* (Exodus 33:8). Not *It will be, when* (Andrew,
  2026-09-26). Where *ve-hayah* is only "it shall be" + a noun (*It shall be a
  sign*), it stays plain.
- **"And now"** for *ve-attah* inside speech: it keeps the speaker's own turn
  toward what they want, heard through their mouth (Andrew, 2026-09-26). Where
  the sense is contrast or consequence, *But now* or *So now* stays.

Not kept: *The LORD spoke to Moses, saying*; *These are the generations of*;
*He lifted up his eyes and saw* (the *And here —* that follows is the marker);
*the word of the LORD came to*; the Judges refrain, *The sons of Israel did
evil in the eyes of the LORD*, and its companions (*cried out to the LORD*,
*the land had rest*) (Andrew, 2026-09-26).

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
| *tamim*, of an animal for offering | without defect (never *unblemished*; *blemish* is *mum*) | 2026-09-28 |
| Greek *lepra* / *lepros* (New Testament) | leprosy / leper, with a note on *tsara'at* | 2026-09-28 |
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
  first note says so. Currently: Esther 11–16 and books 82–89 except
  Sirate Tsion (below).
- **`none`** gets the stub only (see Honesty rules). Currently: Josippon and
  Sirate Tsion.

Never accept an OCR'd text with made-up verse numbers as a source.

### Books 82–89, the broader canon (Andrew, 2026-09-27)

Tier `english-only` (Sirate Tsion excepted: no text of it has been found, so it
is tier `none`): no Ge'ez text of these books can be quoted, so each is
worked from a public-domain scholar's translation (`SOURCES.md`, "The broader
canon"). Chapter and verse follow that edition, as `source_text.py` prints them.

| Book | Worked from | Chapters |
|---|---|---|
| 1st Book of the Covenant | Cooper and Maclean 1902, **from the Syriac** | 73 |
| 2nd Book of the Covenant | Guerrier and Grébaut 1913 (French); James 1924 for sections 12–62 | 62 |
| Te'ezaz | Horner 1904 | 72 |
| Gitzew | Schodde 1885 | 57 |
| Abtilis | Tattam 1848, **from the Coptic** | 85 |
| Didascalia | Harden 1920 | 43 |
| Qalementos | Grébaut 1911-1928 (French) | 43 |

- **Chapter 1's first note** names the translation the book is worked from.
  Where it is a sister version (in bold above), the note says so plainly: the
  text is the Syriac or Coptic form of the work, and the Ethiopic differs from
  it in wording and in places in order. Abtilis follows Tattam's numbering of
  the 85 Apostolic Canons; the Ethiopic has 81, and the note says so.
  Qalementos stops where Grébaut stopped, in its third of seven books.
- **2nd Book of the Covenant:** Guerrier's French is the Ethiopic and governs.
  James's English follows the Coptic where it survives; use it for the sense of
  a sentence the French OCR has spoiled, and where the two differ in substance,
  follow the French and note the Coptic reading.
- **The opening.** Where the edition prints an opening before chapter 1,
  `source_text.py` prints it with chapter 1; render it above verse 1,
  unnumbered.
- **A chapter with no text** (a heading the scan lost, canons the edition prints
  as one, a page missing from the scan): the helper says so. Write the stub
  (Honesty rule 5) with a note saying where the text is or why it is missing.
- **The Ge'ez OCR** (`ethiopic-ocr`), where there is one, checks names, numbers
  and the shape of a passage. Never quote it.
- Every chapter ends with the **Source text** note naming the edition and
  translator (all public domain), and *English translation by this project*.

### Written and read forms (Andrew, 2026-09-26)

Where the Hebrew is written one way and the scribes' reading tradition says it
another way (*ketiv* and *qere*), follow the **read** form. Add a note only where
the two differ in meaning (Numbers 21:32, *took possession* or *drove out*); a
spelling difference gets no note.

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

- **1 Enoch (Andrew, 2026-09-26):** the base text is the EOTC Ge'ez
  (`ethiopic-eotc`), and verse numbers follow it. Knibb's Ge'ez (`ethiopic`,
  chapters 1-71), the Greek, the Aramaic and the Latin are the other witnesses.
  For meaning, use the OCP English (1-71) and Charles (all chapters); never
  follow Charles's reordering or his emendations without a note. Every 1 Enoch
  chapter from 37 on ends with a last note, **Source text**, carrying the credit
  line in `SOURCES.md` (Beta Masaheft, CC BY-SA 4.0).
- **Jubilees (Andrew, 2026-09-26):** the base text is the EOTC Ge'ez
  (`ethiopic-eotc`), and verse numbers follow it. The second Ge'ez text
  (`ethiopic`, Ran HaCohen's), the Latin and the Greek are the other witnesses;
  the Greek lines are mostly short excerpts and summaries, not continuous text.
  For meaning, use the OCP English (Latin, Greek) and Charles (all chapters);
  never carry Charles's bracketed dates or his emendations into the text. Where
  the EOTC lacks a verse (4:3-14, 26:33), fill it from the other Ge'ez text.
  **Cut verses (Andrew, 2026-09-27, replacing the rule of 2026-09-26):** the
  EOTC text as held here is cut short in several hundred verses; these are
  losses in its digitization, not in the Ge'ez. Where it is cut, render the
  missing words from the **Asmara printing** (`ethiopic-gff`), without
  brackets, and name that text in the chapter's notes. Where the Asmara file
  lacks them too (7:11, 7:15 and 14:16-16:13), render them from **Charles's
  edition of the Ge'ez** (1895, `ethiopic-ocr`, read through his English),
  also without brackets (Andrew, 2026-09-27). Words Charles supplied by his own
  correction (his footnote says *emended* or *restored*) are in no manuscript:
  they go in [square brackets] with a note saying so (7:18, 7:24, 15:32). Every
  chapter ends with the **Source text** note.

### 1–3 Meqabyan (Andrew, 2026-09-27)

Tier `source`, worked from the one text there is: the EOTC Ge'ez
(`ethiopic-eotc`), which sets the verse count and numbering. There is no Greek,
Latin or Hebrew witness and no public-domain English. Andrew's Amharic (chapters
1-8, private) may be read to check meaning, never copied, quoted or credited as a
source. Where a numeral in the Ge'ez is cut short or lost (see `SOURCES.md`), the
verse follows the Amharic's number and a note quotes what the Ge'ez has. A claim
about what a Ge'ez word means is stated as a rendering, with the Ge'ez quoted;
build no argument on its supposed root. Every chapter ends with the **Source
text** note.

2 and 3 Meqabyan follow the same rule (Ge'ez added 2026-09-27); their private
Amharic check is the EOTCOpenSource Amharic, on the same never-copied terms. In
all three books some verses stop where a number was due (`SOURCES.md` lists
them). In 1 Meqabyan 2:27, 3:31, 4:5 and 4:8 Horovitz's Ge'ez excerpts
(`ethiopic-ocr`, 1905) have the rest: render it without brackets and name
Horovitz in the chapter's notes. Everywhere else render what the Ge'ez has,
write *[words lost]* where it breaks off, and note it; a better source is still
being sought (Andrew, 2026-09-27).

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
