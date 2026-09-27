# Source texts

Where the text in `sources/` came from, and what may be done with it.

## Hebrew — the Old Testament

`sources/hebrew/` holds the **Westminster Leningrad Codex**, the standard
digital edition of the Masoretic Hebrew text, from the
[Open Scriptures Hebrew Bible](https://github.com/openscriptures/morphhb).
Public domain.

## Greek — the New Testament

`sources/greek/` holds the **SBL Greek New Testament**, from
[morphgnt](https://github.com/morphgnt/sblgnt).

## Swete's Septuagint (the deuterocanon)

**H. B. Swete, THE OLD TESTAMENT IN GREEK ACCORDING TO THE SEPTUAGINT**
(Cambridge University Press): Vol. I 4th ed. 1909, Vol. II 3rd ed. 1907,
Vol. III 4th ed. 1912. **Public domain by age.** Swete died in 1917 and all
three volumes were published before 1929.

The digital transcription came from `github.com/eliranwong/LXX-Swete-1930`,
which links the scanned volumes it was keyed from. That repository carries a
GPL-3 file, which is a software licence; what this project takes from it is the
Greek words and their verse numbers -- that is Swete's public-domain text, not
the morphology, transliteration or gloss layers the digitisers added, none of
which are used here.

`fetch_swete.py` does the conversion, from the two CSVs kept in
`sources/swete-src/`:

    python3 fetch_swete.py sources/swete-src

## Sources examined and rejected

- **LXX-Rahlfs-1935** (`eliranwong/LXX-Rahlfs-1935`) -- CC BY-NC-SA 4.0:
  non-commercial *and* share-alike, and derived from CCAT data that requires a
  signed user declaration. Not used.
- **`sleeptillseven/LXX`**, **`nathans/lxx-swete`** -- CC BY-SA (share-alike). Not used.
  (`LPettay/ethiopian-bible` was on this list too; see the exception below.)
- **A Ge'ez Tewahedo text set** found in a public-domain-licensed repository was
  examined for the Meqabyan books, Ge'ez Jubilees and Ge'ez 1 Enoch, and
  **rejected**. Its own headers record it as `ocr-tier3` quality with
  *"Parser chapter labels discarded; verses assigned sequentially to canonical
  chapters"* -- the verse numbers are synthesised, not read from the page.
  Sampling also showed the text to be Amharic rather than Ge'ez, carrying
  column artifacts from a scanned parallel Bible. A source whose references are
  manufactured is worse than no source, because it reads as authoritative.
- **Wikisource "Translation:1 Meqabyan", "2 Meqabyan", "3 Meqabyan"** -- English
  added anonymously in January 2026 and proposed for deletion in June 2026 as not
  meeting Wikisource's translation policy. Where they came from cannot be traced.
  Not used.
- **"The Three Books of Meqabyan: A CC0 1.0 English Translation from Amharic"**
  (archive.org, `three-books-of-meqabyan-cc0-translation`, May 2026). CC0, so free
  to use, but it is an AI-assisted translation of the modern Amharic, not of the
  Ge'ez. Not used as a source; held for Andrew to decide (see the report of
  2026-09-27).

## Exception: CC BY-SA allowed for Ethiopian-only books (Andrew, 2026-09-23)

The no-share-alike rule stands for everything else. For books that survive only
in the Ethiopian canon and have no other usable source, Andrew approved CC BY-SA.

**Ge'ez from Beta Masaheft** (Universität Hamburg, <https://betamasaheft.eu/>),
CC BY-SA 4.0, as packaged in `github.com/LPettay/ethiopian-bible`
(`public/data/chapters/<Book>/<n>.json`). Checked 2026-09-23 for 1 Meqabyan:
36 chapters, 753 verses, none empty, real verse numbers; verse counts match
Andrew's Amharic (Ethiopian Bible App) in chapters 1-4 and 7-8, and chapters
5-6 differ only by one verse boundary (77 verses across the pair in both).

What the licence requires, and all it requires:
- credit on every chapter built from it: *Ge'ez text: Beta Masaheft,
  Universität Hamburg, CC BY-SA 4.0. English translation by this project.*
- those chapters are themselves published under CC BY-SA 4.0 (no "all rights
  reserved", no restrictions on copying them). Selling a printed book is fine.
- nothing applies to any book not built from this source.

Checked 2026-09-23 against Beta Masaheft's own repo, `github.com/BetaMasaheft/Works`
(commit a0b38ff, TEI XML, CC BY-SA 4.0, reachable from here). Use these files, not
the LPettay copy:

| Book | Beta Masaheft file | State |
|---|---|---|
| 1 Meqabyan | `1001-2000/LIT1819Maccab.xml` | full text, 36 chapters |
| 2 Meqabyan | `5001-6000/LIT5840SecondEthioMaccabees.xml` | full text, 21 chapters; in `sources/ethiopic-eotc/` |
| 3 Meqabyan | `5001-6000/LIT5839ThirdEthioMaccabees.xml` | full text, 10 chapters, every chapter filled; in `sources/ethiopic-eotc/` |
| 1 Enoch | `1001-2000/LIT1340EnochE.xml`, edition `EOTCed` ("Text of the EOTC printed Bible") | full text, 108 chapters, 1,058 numbered verses; in `sources/ethiopic-eotc/` |
| Jubilees | `1001-2000/LIT1697Jubilees.xml`, editions `EOTCed` and `Ran` | EOTC: 50 chapters and a 2-verse prologue, 1,292 numbered verses, none empty; in `sources/ethiopic-eotc/`. `Ran`: a second Ge'ez text, 1,139 verses; in `sources/ethiopic/` |

**1 Enoch (Andrew, 2026-09-26):** 1 Enoch is rendered from the EOTC Ge'ez
(`sources/ethiopic-eotc/1-enoch.txt`), which is the base text and sets the verse
numbering. Knibb's Ge'ez from the OCP (`sources/ethiopic/`, chapters 1-71)
stays as a second witness to check against. Andrew chose this knowing the
share-alike terms above then apply to the 1 Enoch renderings. Converted from
Beta Masaheft commit `90ab9cf` (2026-09-26); the XML is kept in
`sources/betamasaheft-xml/`. Only the markup was removed; no word was altered.
The EOTC numbering matches Knibb's in 69 of 71 chapters (not 21 and 28).

**Jubilees (Andrew, 2026-09-26):** Jubilees is rendered from the EOTC Ge'ez
(`sources/ethiopic-eotc/jubilees.txt`), which is the base text and sets the verse
numbering, on the same terms as 1 Enoch: the share-alike terms above apply to the
Jubilees renderings. Converted from Beta Masaheft commit `90ab9cf`; the XML is
kept in `sources/betamasaheft-xml/`. Only the markup was removed; no word was
altered. The prologue before chapter 1 is stored as chapter 0 (`0:1`, `0:2`).

- **The second Ge'ez text** (`sources/ethiopic/jubilees.txt`) is the file's `Ran`
  edition: Ran HaCohen's transcription, from his *Biblia Veteris Testamenti
  Aethiopica* site, released under the same licence. It has misspellings that
  look like typing or OCR slips (4:5 *ጽሳተ* where the EOTC's word elsewhere is
  *ጽላተ*), and repeats the numbers 26:26, 27:27 and 28:28. Use it to check the
  EOTC and to fill its gaps, never silently over it.
- **Gaps in the EOTC text as held here.** Chapter 4 jumps from verse 2 to verse
  15: its verse 2 runs from Cain killing Abel straight into the end of 4:14
  (Mahalalel's birth), and 4:3-14 are absent. The `Ran` text has 4:3-11 and
  4:13-14. Verse 26:33 (Isaac's answer to Esau) is in neither Beta Masaheft text; the Asmara printing has it.
  Chapter 1 skips the numbers 18 and 19, and chapter 11 has 24 verses to
  Charles's 23. Whether a gap is in the printed Bible or in the transcription
  cannot be checked from here.
- **Cut verses.** Beyond those gaps, about 150 verses (roughly one in eight)
  are cut to under half of what Charles translates, in both Ge'ez texts and in
  nearly every chapter: 3:5-6 has Adam sleep and wake with no rib and no woman
  made, 3:20-21 never has the fruit eaten, 22:4 stops at *before Ishmael his
  brother*. The rendering now gives them from the Asmara printing (see below and the spec's Jubilees rule); brackets remain only where no Ge'ez text here has the words (all repaired 2026-09-27; record in `PASTE/changes/15-jubilees.md`).
- **Correction (2026-09-27): the "cut verses" are losses in the digitization,
  not in the Ge'ez.** A third, complete Ge'ez text (below) has the words in
  every cut verse checked (3:5-6, the rib; 47:4, Miriam and the birds; 47:10,
  the Egyptian; 50:12-13, the Sabbath list). The two Beta Masaheft texts share
  spellings and gaps (both write *ወአንቅሆ* at 3:6, where the printed text below
  has *ወአንቅሖ*), so they are not independent of each other.
- **The Asmara printing** (`sources/ethiopic-gff/jubilees.txt`): the Ge'ez
  Octateuch and Jubilees printed at Asmara in 1955 E.C. (1962/63), in the 32nd
  year of Haile Selassie, typed by the Ge'ez Frontier Foundation,
  `github.com/geezorg/ebooks` (commit 8ec402c),
  `geez/religious/BiluyKidan/src/`, licensed **CC BY-SA 4.0**, the same licence
  as Beta Masaheft. The source file is kept in `sources/gff-src/`. The printing
  divides Jubilees into 39 chapters; its text has been aligned word by word to
  the EOTC's verse numbers, so the verse boundaries are approximate (a few words
  can sit in the neighbouring verse). The typed file lacks 14:16-16:13 (its
  chapter 15), and has no text for 7:15. The alignment matched 15,728 of the
  EOTC's 19,627 words; the printing has about 5,000 more words than the EOTC
  text as held here.
- **Dates checked against it (2026-09-27).** Most of the dates that break the
  book's arithmetic read the same in the Asmara printing (5:22, 21:1, 22:1,
  24:21, 31:27), so they are in the printed text, not the digitization. It
  differs at 16:16 (*seven* sons, where the EOTC has *six*), 46:8 (Joseph dies
  in the *third week of the forty-seventh* jubilee, where the EOTC has the
  *sixth week of the forty-sixth*) and 48:1 (*six* weeks and one year, where the
  EOTC has *five*). It carries dates the EOTC text had lost: 11:15 (Abram's
  naming), 28:24 (Joseph's birth), 36:18 (Isaac's age at death).
- The Latin and Greek witnesses (OCP, below) are numbered as in Charles, as far
  as spot checks show (20:5, 30:1, 45:10). The EOTC's verse count matches
  Charles's in 46 of the 50 chapters (not 1, 4, 11, 26).

**1 Meqabyan (Andrew, 2026-09-27):** 1 Meqabyan is rendered from the EOTC Ge'ez
(`sources/ethiopic-eotc/1-meqabyan.txt`, from `1001-2000/LIT1819Maccab.xml`,
edition "Text of the EOTC printed Bible"), which is the base text and sets the
verse numbering, on the same terms as 1 Enoch and Jubilees: the share-alike terms
above apply to the 1 Meqabyan renderings. Downloaded 2026-09-27 from the `master`
branch of `BetaMasaheft/Works` (the commit hash could not be read from here); the
XML is kept in `sources/betamasaheft-xml/`. Only the markup was removed; no word
was altered. 36 chapters, 753 verses.

- **Numerals split off as verses.** Nine `<l n>` lines in the XML carry a verse
  number out of sequence. They are Arabic numerals written inside the text (the
  file writes numbers as digits elsewhere too, *ለ5አኃው*), which the markup read
  as verse numbers. They are rejoined to the verse they belong to, as digits:
  1:21, 4:5, 5:4, 8:3, 8:6, 10:3, 14:2, 28:6 (twice). Some are cut short: 1:21
  has *4* where Andrew's Amharic has *forty*, and 4:5 has *4* where it has
  *fourteen*. Other numerals are lost to stray characters (`%` or `)`, as in
  1:16, 1:22, 10:3).
- **Checked against Andrew's Amharic** (Ethiopian Bible App, chapters 1-8, held
  privately in `andwils21-ballr/Ethiopic`, not cleared for redistribution): verse
  counts match in chapters 1-4 and 7-8; chapters 5-6 differ by one verse
  boundary (40/37 here, 39/38 there).
- **No other witness.** There is no Greek, Latin or Hebrew text of this book, and
  no public-domain English translation has been found. The Amharic may be read
  to check meaning, never copied or quoted.

**2 and 3 Meqabyan (2026-09-27):** rendered from the EOTC Ge'ez on the same terms
as 1 Meqabyan (`sources/ethiopic-eotc/2-meqabyan.txt`, `3-meqabyan.txt`), from
`5001-6000/LIT5840SecondEthioMaccabees.xml` and `LIT5839ThirdEthioMaccabees.xml`
(Beta Masaheft commit `90ab9cf`, edition "Text of the EOTC printed Bible"; the XML
is kept in `sources/betamasaheft-xml/`). Only the markup was removed; no word was
altered. 2 Meqabyan: 21 chapters, 424 verses. 3 Meqabyan: 10 chapters, 208
verses. Both match the EOTC Amharic chapter by chapter (EOTCOpenSource, read
privately; CC BY-NC-ND, never copied).

- **Numerals rejoined** as in 1 Meqabyan: 2 Meqabyan 5:3, 8:23 (twice), 9:8,
  10:26, 11:10, 13:1, 13:9, 16:15; 3 Meqabyan 2:13. Every one is a single digit
  (1, 2 or 5), and each agrees with the Amharic.
- **Why numbers are damaged, in all three books.** The printed Bible's Ethiopic
  numerals did not survive the conversion to Unicode. The units (፩ to ፱) came
  through as digits; larger numbers were cut short to a digit (1 Meqabyan 1:21
  *4* for forty, 4:5 *4* for fourteen), turned into `%` or `)` (1 Meqabyan 1:16,
  1:22, 10:3; 2 Meqabyan 3:9 *))*, 8:23 *2))*), or lost.
- **Verses cut off at a number.** Twenty verses stop mid-sentence, and in fifteen
  of them the Amharic has a number at the point where the Ge'ez stops (1 Meqabyan
  2:2, *and he had* [three sons]; 2 Meqabyan 4:26, [five hundred] horses; 3
  Meqabyan 2:23, [ten] thoughts). The words after the number are lost with it.
  - 1 Meqabyan: 2:2, 2:27, 3:28, 3:31, 4:5, 4:8, 4:26, 5:25, 8:24, 8:35, 25:18,
    28:34, 30:11.
  - 2 Meqabyan: 4:26, 15:15.
  - 3 Meqabyan: 2:23, 3:1, 3:2, 3:5, 4:26.
- No second complete Ge'ez text of these books has been found online.

- LPettay's `3Meq` folder is **2 Meqabyan** mislabelled: its opening and closing
  words are identical to Beta Masaheft's Second Book. LPettay has no 3 Meqabyan.
- The nine tier-`none` books: **no usable Ge'ez anywhere in either collection.**
  - Josippon (`LIT2598Yosipp.xml`): section headings and scraps only (about
    8,000 letters across 153 sections; most sections empty).
  - Didascalia (`LIT1309Didesq.xml`) and Testamentum Domini, the source of the
    two Books of the Covenant (`LIT2461Testam.xml`): chapter structure with no text.
  - Gitzew, Sirate Tsion, Te'ezaz, Abtilis: catalogue entries only.
  - `LIT2680ClemPeter.xml` (= LPettay `Clem`) is the short *Canons of Clement*
    from Peter, about 7,500 letters. It is not the seven-part Book of Qalementos
    in the canon. Do not use it as Qalementos.
  - LPettay's `Sinod`, `TestLd`, `Lef`, `MysHE`, `Teach` hold English headings
    or scraps, not text. `KN` is the Kebra Nagast, which is not one of the 89.

## R. H. Charles's English of 1 Enoch (public domain)

`sources/english/1-enoch.charles.txt` is **R. H. Charles, *The Book of Enoch*
(London: SPCK, 1917)**, the revised version of his 1912 translation. Charles died
in 1931, so the text is public domain. It is used only as the scholarly English
for checking *meaning*, chiefly in chapters 72-108, where the OCP has no English.
It is not a witness.

Taken from `github.com/scrollmapper/bible_databases_deuterocanonical`
(commit `271173e`, `sources/en/1-enoch/1-enoch.md`, kept in
`sources/charles-src/`). Converted to `chapter:verse<TAB>text`, with three things
to know:
- Charles prints a second recension beside the first in 22, 27:3 and 32:1-3;
  the second is kept as a lettered verse (`22:2b`).
- Charles moves verses (91-93, 106) and emends the text. The file keeps his
  numbering; the rendering follows the EOTC order and numbering, not his.
- One repair: a stray `[106:1]` marker had split 106:8; the fragment is joined
  back to 106:8 with the missing word shown as `[I]`.

His chapter 44 is missing from that copy. Charles's numbering differs from the
EOTC's by one verse in chapters 8, 10, 15, 20, 21, 28, 40, 51, 68, 85, 89, 98
and 100.

## R. H. Charles's English of Jubilees (public domain)

`sources/english/jubilees.charles.txt` is **R. H. Charles's English translation
of Jubilees**. The copy does not say which of his editions it is; every one was
published before 1929 and Charles died in 1931, so all are public domain. Used
only for checking *meaning*, like his Enoch; it is not a witness.

Taken from `github.com/scrollmapper/bible_databases_deuterocanonical`
(commit `271173e`, `sources/en/book-of-jubilees/book-of-jubilees.md`, kept in
`sources/charles-src/jubilees.md`). Converted to `chapter:verse<TAB>text`, 1,305
verses. Two things to know:
- The copy has 24:1 twice, once with Charles's date `[2073 A.M.]` and once
  without; the first is kept.
- Square brackets are Charles's own. Seventeen verses carry a year from creation
  (`[2073 A.M.]`) that he worked out; it is not in any witness.

## How the OCP witnesses are built

The Online Critical Pseudepigrapha publishes each book as XML in which a single
verse is split across several `<unit>` elements, so the edition can carry its
apparatus, and each unit offers one or more `<reading option="N">`. Option 0 is
the base reading. **A verse is every unit's option-0 reading joined in document
order.** Reading only the first unit of each verse silently truncates about two
thirds of them, mid-sentence, with no error -- which is exactly what this
repository did until 2026-09-17.

`fetch_ocp.py` does the conversion. The XML it reads is kept in
`sources/ocp-xml/` so the text files can be rebuilt without network access:

    python3 fetch_ocp.py sources/ocp-xml

## 1 Enoch and Jubilees — four witnesses

These two books do not survive whole in any one language. What survives is
several partial witnesses that often disagree, and the disagreements are the
reason this rendering prints all of them together.

| Book | Witnesses held here |
|---|---|
| **1 Enoch** | Greek (48 chapters), Ge'ez (71), Qumran Aramaic (8), Latin (3); plus the EOTC Ge'ez, all 108 chapters, from Beta Masaheft (see the exception above) |
| **Jubilees** | Latin (34 chapters), Greek (26); plus the EOTC Ge'ez and a second Ge'ez text, all 50 chapters, from Beta Masaheft (see the exception above) |

The texts come from the **Online Critical Pseudepigrapha**
(<https://pseudepigrapha.org>, [source repository](https://github.com/OnlineCriticalPseudepigrapha/Online-Critical-Pseudepigrapha)),
used under a [Creative Commons Attribution 4.0 International licence](https://creativecommons.org/licenses/by/4.0/).
Their TEI XML has been converted to this project's plain `chapter:verse<TAB>text`
format; nothing has been altered, added to, or corrected. Their scholarly
English rendering of each witness is kept alongside, in `sources/english/`,
because a claim about what the Ge'ez or Latin *means* has to rest on published
scholarship rather than on a reading this project cannot check.

The editions the OCP built those witnesses from, as cited in their own
manuscript metadata:

- **1 Enoch, Ge'ez** — M. Knibb, *The Ethiopic Book of Enoch: A New Edition in
  the Light of the Aramaic Dead Sea Fragments* (Oxford: Clarendon, 1978)
- **1 Enoch, Greek** — M. Baillet, in Baillet, Milik and de Vaux, *Les "petites
  grottes" de Qumrân* (DJD III; Oxford: Clarendon, 1965); É. Puech, *Revue
  Biblique* 103 (1996)
- **Jubilees, Greek** — R. H. Charles, *The Ethiopic Book of Jubilees* (Oxford:
  Clarendon, 1895); A.-M. Denis, *Fragmenta pseudepigraphorum quae supersunt
  graeca* (PVTG 3; Leiden: Brill, 1970)

The OCP also supplies the witnesses held for **Ezra Sutuel** (4 Ezra, chapters
3-14): the Latin, edited by David M. Miller, and the Syriac, edited by Andy Chi
Kit Wong, each with the OCP's English; and the Greek of **4 Baruch** with its
English. The same licence and credit apply.

CC BY 4.0 asks one thing: that this credit stays with the text. It places no
condition on the renderings or the notes in this repository, which are original
work, and none on what is done with them.

## The broader canon: public-domain editions found 2026-09-27

Cowley (*Ostkirchliche Studien* 23, 1974, pp. 318-323) names the printed edition
of each book of the broader canon. The ones that are public domain by age are on
archive.org and are being added here. Scans are not kept in this repository;
the archive.org identifier and page range are given so the text can be checked.

**OCR Ge'ez** (`sources/ethiopic-ocr/`). Ge'ez read by machine (Tesseract, its
Amharic model) from a scanned public-domain edition and **not proofread**. Letter
accuracy is roughly 95%; the word dividers are normalized to ፡. Every line starts
`[p. N]`, the printed page, so any word can be checked against the scan. Use it
only to check names, numbers and the shape of a passage against the editor's
translation. Never quote a Ge'ez word from it without looking at the page.

**Editors' translations** sit in `sources/english/` (and `sources/french/`,
`sources/german/` where there is no English), named `<slug>.<editor>.txt`. They
are OCR'd, then compared word by word with archive.org's own OCR of the same
pages; the two agree except where noted, and the disagreements were settled from
the page image. Where the edition has no verse numbers, the verse number is the
edition's paragraph, counted in order, and the chapter is the edition's own
numbered unit.

### Te'ezaz — Horner 1904 (public domain)

**G. W. Horner, *The Statutes of the Apostles, or Canones Ecclesiastici*
(London: Williams & Norgate, 1904)**, archive.org `statutesapostle00unkngoog`.
Horner died in 1930. Cowley: Te'ezaz, the 71 or 72 canons of the Sinodos, "has
been printed in G. Horner, *The Statutes of the Apostles*."

- `sources/english/teezaz.horner.txt`: Horner's *Translation of the Ethiopic
  Text*, pp. 127-232 (PDF pages 173-278). Chapter = Horner's statute number, 1 to
  72; chapter 0 is the opening blessing. Horner prints two statutes numbered 40
  (pp. 162 and 178); both are chapter 40. Verse = Horner's paragraph. Footnotes
  are left out. His transliterated names keep their macrons (Pētros, Amēn).
- `sources/ethiopic-ocr/teezaz.txt`: his Ethiopic text, pp. 1-87 (PDF 45-131).
  The Google scan repeats some pages and **lacks printed pages 5, 9, 17, 21, 25,
  35, 41, 49, 53, 60, 70 and 71**; the file marks each gap. The headings of
  statutes 12-13, 17-21, 27-28, 35-37, 48-49, 51-52 and 67-68 fall on missing
  pages or could not be read, so their Ge'ez, where the scan has it, sits under
  the statute before. Chapter = statute; verse = the statute's share of one
  printed page.
- The other copy on archive.org (`bwb_T4-BAF-989`) is the 1915 reprint, which
  leaves out the Ethiopic.
- Naming: Cowley's four sections are Ser`atä Seyon (30 canons), Te'ezaz (71),
  Gessew (56) and Abtelis (81), and this project follows him. An Ethiopian
  scholar cited by Wanger (2013) gives the names to the canon collections
  differently; the difference is noted for Andrew, not settled here.

### Gitzew — Fell 1871 and Schodde 1885 (public domain)

**Winand Fell, *Canones Apostolorum aethiopice* (Leipzig: Brockhaus, 1871)**,
archive.org `canonesapostolor00unse` (a second, poorer scan is
`canonesapostolo00canogoog`). Cowley: Gessew, the 56 or 57 canons, "has been
printed in W. Fell." It is the Ethiopic version of the Apostolic Canons (the
Greek has 85), which Fell edited from Berlin and Tübingen manuscripts.

**George H. Schodde, "The Apostolic Canons, Translated from the Ethiopic,"
*Journal of the Society of Biblical Literature and Exegesis* 5 (1885), pp.
61-72**, archive.org `jstor-3268629` (JSTOR's free Early Journal Content).
Schodde translated Fell's text.

- `sources/english/gitzew.schodde.txt`: Schodde's translation. Chapter = canon,
  1 to 57; chapter 0 is the opening. Checked word by word against archive.org's
  OCR; four misreadings corrected from it.
- `sources/ethiopic-ocr/gitzew.txt`: Fell's Ethiopic text, printed pp. 13-25,
  uncorrected OCR. All 57 canon headings were found, in order, so the chapters
  line up with Schodde's. Fell's variant readings (pp. 26-32) and his Latin
  translation are not transcribed.
- Fell's introduction lists the whole Ethiopic Sinodos. Two of its sections
  matter for the canon: *81 further decrees of the apostles, called "tituli"*
  (Ethiopic *Abtelisat*), "nothing other than a longer edition of the Apostolic
  Canons", not printed (this is Abtilis, see below); and *30 decrees of the
  apostles given through Clement*, extant in Arabic and in a Syriac version in
  27 decrees printed by Lagarde (1856) (this is Sirate Tsion, see below).

### Didascalia — Harden 1920 and Platt 1834 (public domain)

**J. M. Harden, *The Ethiopic Didascalia* (London: SPCK, 1920)**, archive.org
`cu31924096083336` (Cornell's scan: two book pages per image, every other image
blank; all 188 printed pages of the translation are present). Harden died in
1931. Cowley: "Complete English translation in J. M. Harden, *The Ethiopic
Didascalia*, London 1920."

- `sources/english/didascalia.harden.txt`: Harden's translation. Chapter =
  Harden's chapter, 1 to 43; verse = his paragraph (verse 1 is the chapter's
  title). His references to the Greek *Apostolic Constitutions* (`[ii., 57.]`)
  are kept at the head of paragraphs; his footnotes (variant readings) are left
  out. OCR'd with each two-page image split in two; the letter confusions of
  this print (*c* for *e*, *y* for *g*) were corrected only where one English
  word fits, and the rest checked against archive.org's own OCR. A few OCR slips
  remain (roughly one word in 500); read with the page when a word matters.

**T. P. Platt, *The Ethiopic Didascalia* (London: Oriental Translation Fund,
1834)**, archive.org `ethiopicdidascal00platrich`. Platt died in 1852. Ge'ez text
with his English below it on each page, in 22 sections that cover Harden's
chapters 1 to 23 (Platt's section numbering differs from Harden's: his section
X is Harden's chapter XII). Cowley: "Incomplete text and translation in T. P.
Platt."

- `sources/ethiopic-ocr/didascalia.txt`: Platt's Ethiopic text, printed pp.
  1-131 (PDF pages 26-156), uncorrected OCR, filed under Harden's chapters 1-23
  by Platt's own table of sections (the page where each section begins). Verse =
  one printed page, marked `[p. N]`; a page where one section ends and the next
  begins is filed under both chapters, so the Ge'ez of a chapter's first and last
  verse may run into its neighbour. Harden's chapters 4 and 5 fall in one section
  of Platt's (filed under 4), and two of Platt's sections make Harden's chapter
  17. Chapters 24-43 have no Ge'ez here.

### 2nd Book of the Covenant — Guerrier and Grébaut 1913 (public domain)

**L. Guerrier with S. Grébaut, *Le Testament en Galilée de Notre-Seigneur
Jésus-Christ*, Patrologia Orientalis 9, fasc. 3 (Paris: Firmin-Didot, 1913)**,
archive.org `patrologia-orientalis_202105`, file `9.pdf`, PDF pages 186-241
(fascicle pp. [37]-[92]). Guerrier died in 1933 (BnF) and Grébaut in 1955, so
the edition is public domain in the United States and in Europe. Cowley: the
second part of the Book of the Covenant, "a discourse of our Lord to his
disciples in Galilee after his resurrection," "has been printed as L. Guerrier
and S. Grébaut, *Le Testament en Galilée*."

- `sources/french/2-covenant.guerrier.txt`: Guerrier's French translation.
  Chapter = his section, 0 (prologue) to 62, located by the titles in his table
  of contents; verse = paragraph. His variant apparatus and footnotes are left
  out. OCR'd and corrected only where one French word fits; misreadings remain,
  especially in the small-capital section titles.
- `sources/ethiopic-ocr/2-covenant.txt`: his Ethiopic text (manuscript C with
  variants from A, B, D), uncorrected OCR. The Ge'ez carries no section numbers,
  so each printed page is filed under every section whose French is on that page
  (`[p. N]` is the fascicle page); a section's first and last verse may run into
  its neighbour.
- His part 1 (sections 1-11) is the apocalypse spoken in Galilee; parts 2-4 are
  the text known elsewhere as the *Epistle of the Apostles*. Both are the second
  Book of the Covenant as the manuscripts give it.

## Ezra Sutuel: the Ge'ez, from Dillmann 1894 (public domain)

**A. Dillmann, *Veteris Testamenti Aethiopici Tomus Quintus, quo continentur
Libri Apocryphi* (Berlin: Asher, 1894)**, pp. 153-192, the book headed ዕዝራ፡ ነቢይ
("Ezra the prophet"); archive.org `veteristestamen00dillgoog`, PDF pages
162-201. Dillmann died in July 1894. He edited it from ten manuscripts (his
list, p. 192) and printed it with verse numbers.

- `sources/ethiopic-ocr/ezra-sutuel.txt`: his Ge'ez, uncorrected OCR (see *OCR
  Ge'ez* above), in the Latin chapter and verse numbers the other witnesses use.
  Dillmann's chapters I-IV are Latin 3-6; he divides Latin 7 into V (7:1-35),
  VI (7:36-105) and VII (7:106-139); VIII-XIV are Latin 8-14. His verses match
  the Latin one for one, checked by content, with one exception: he splits
  Latin 7:104 in two (his VI:69-70, joined here as 7:104), so his VI:71 is
  7:105.
- Each page's two columns were read separately. The verse numbers were found as
  small raised numerals on the page, read, and checked in sequence; every
  doubtful one was checked on the page image.
- Where the Ethiopic has a gap, Dillmann prints dots, and so does this file
  (`...`): 3:16 and 5:48 are dots only; 3:17, 3:36, 4:29, 6:5, 6:9, 7:51-52,
  9:35, 9:38 and 10:55 have dots in them. He has no verses 9:36-37, and prints
  no number 40 in Latin chapter 9: 9:40 here begins at ወእቤላ, where the Latin
  verse begins.
- 5:56 is his, numbered as the Syriac numbers it (the Latin has it as the end
  of 5:55). 14:48 is the Ethiopic ending, which the Latin lacks.
- No English translation of the Ethiopic is held here. Laurence's (1820, from
  one manuscript, Dillmann's L) could not be downloaded: Google Books refused
  and HathiTrust blocks downloads. For meaning, use the Latin and Syriac English.

## 4 Baruch: the Ge'ez, from Dillmann 1866 (public domain)

**A. Dillmann, *Chrestomathia Aethiopica* (Leipzig: Weigel, 1866)**, pp. 1-15,
"Liber Baruch" (ተረፈ፡ ነገር፡ ዘባሮክ); archive.org `chrestomathiaaet00dilluoft`,
PDF pages 20-34. Dillmann died in 1894.

- `sources/ethiopic-ocr/4-baruch.txt`: his Ge'ez, uncorrected OCR (see *OCR
  Ge'ez* above), keyed to the OCP Greek's chapters and verses. **Dillmann prints
  no chapter or verse numbers**: where each Greek verse begins in the Ge'ez was
  set by reading the Ge'ez against the OCP English, verse by verse. Where the
  Ethiopic has words the Greek lacks, they stay with the verse before (9:22 ends
  with Baruch and Abimelech's cry, "do not kill him by this death").
- **The letter, 6:19-25.** In the main text the Ethiopic breaks off at "and he
  wrote, saying: ....". Dillmann prints the letter in his note 8 (p. 9), "since
  the words of the letter are corrupt and defective". It is taken from that note
  (tagged `[p. 9, note 8]`); his variant readings inside it are left out.
- Two differences worth knowing, read from the Ge'ez: in 9:1 the sacrifice
  lasts seven days (ሰቡዐ፡ ዕለተ), not nine; in 9:15 the time to the coming is
  given as three hundred and three weeks of days, not 477 years.
- No English translation of the Ethiopic is held here; for meaning use the OCP
  English of the Greek.

## Jubilees: Charles's Ethiopic, 1895 (public domain), chapters 7 and 14-16

**R. H. Charles, *The Ethiopic Version of the Hebrew Book of Jubilees*
(Oxford: Clarendon, 1895)**, pp. 25-30 and 48-60; archive.org
`CharlesEthiopicJubilees` (the scan holds the book twice; PDF pages 60-65 and
119-131 are used).

- `sources/ethiopic-ocr/jubilees.txt`: his Ge'ez for chapters 7 and 14-16,
  uncorrected OCR (see *OCR Ge'ez* above). These are the chapters where the
  rendered text had words in [brackets] as "in no Ge'ez text here"; they are
  now rendered from this text (2026-09-27), except three words or phrases
  that Charles supplied by his own correction (his notes say *emended*: 7:18
  *and Lud*, 7:24 *they sinned against*, 15:32 *all His powers*), which stay
  in brackets. Both Beta
  Masaheft texts (EOTC and HaCohen) are cut short in the same verses, and the
  Asmara file lacks 14:16-16:13. Charles's Ge'ez has the missing words in all
  24 bracketed verses (7:11, 7:18, 7:24; 14:18-24; 15:2-34; 16:2, 16:5).
- Charles prints verse numbers only in the margin. Each verse here starts
  where the EOTC's opening words are found in his text. Five starts were set
  by reading (7:14, 7:15, 14:19, 15:12, 15:25). 14:15 and 15:3 could not be
  placed and are joined to the verse before. The OCR confuses vowel forms of
  the same letter (ለ/ሰ, ን/ነ).
- HaCohen's file runs some verses together with the number inline (15:9 holds
  15:10, "10 [ወእሁብ ..."); it is not missing them.

## 1 Meqabyan: Horovitz's excerpts, 1905 (public domain)

**J. Horovitz, "Das äthiopische Maccabäerbuch," *Zeitschrift für Assyriologie*
19 (1905-06), pp. 194-233**; archive.org `dedupmrg1016100231_IE146043324-5-47`.
Horovitz died in 1931. He prints Ge'ez excerpts from the Frankfurt manuscript
(Rüppell II 7) with a German translation.

- `sources/ethiopic-ocr/1-meqabyan.txt`: his Ge'ez, uncorrected OCR (see *OCR
  Ge'ez* above), keyed to the EOTC verses where the EOTC's opening words are
  found in it: 1:12-4:18 (pp. 196-204) and 17:4-19:6 (pp. 218-219). A verse
  whose opening could not be placed is joined to the verse before.
- **Cut verses.** It completes four of the twenty (see above): 2:27 "two men"
  (ክልኤቱ፡ አደው), 3:31 the brothers "together" (ኅቡረ), 4:5 "for the bodies
  of the five martyrs" (ለኃምስቲሆሙ፡ ሰማዕት), 4:8 "the five martyrs". 2:2 and
  3:28 are not in the excerpts: their EOTC text (ወቦቱ, ወመጽኡ) is one word and
  matched other passages, which were checked and rejected. Its orthography is
  the Frankfurt manuscript's, not the EOTC's.

### Qalementos — Grébaut 1911-1928 (French)

**S. Grébaut, "Littérature éthiopienne pseudo-clémentine. III. Traduction du
Qalêmentos," *Revue de l'Orient chrétien* 16 (1911) to 26 (1927-28)**,
archive.org `revuedelorientch161911pari` and the following volumes. Grébaut
died in 1955; the volumes are public domain in the United States (published
before 1931) and in Europe from 2026. He translated the d'Abbadie manuscript
78 and stopped partway through Book III ("à suivre", never continued): the
work has seven books.

- `sources/french/qalementos.grebaut.txt`: his translation, from archive.org's
  OCR of each volume, corrected only where one French word fits. Chapter =
  Grébaut's chapter numbered straight through the books: Book I chapters I-XXIV
  = 1-24, Book II I-IX = 25-33, Book III I-X = 34-43. Verse = his numbered
  section (verse 1 of a section begins with his section title).
- Gaps: chapter 25 (Book II ch. I) is missing: its first page (ROC 17, p. 244)
  is absent from the scan. Chapter 40 (Book III ch. VII, ROC 21, 1918-19) is
  left out: that volume's scan is too poor to read reliably. In the last
  installment (1927-28) Grébaut prints no section numbers; 43:5 onward are his
  paragraphs, counted in order.
- No Ge'ez text has been found in print; Gibson's *Apocrypha Arabica* (1901)
  has the Arabic Book I with English, not used here.

### 1st Book of the Covenant — Cooper and Maclean 1902 (a sister version)

The first Book of the Covenant is the Ethiopic *Testamentum Domini*. Its only
edition of the Ge'ez (Beylot, 1984) is under copyright. The work survives
more fully in Syriac, and the Ethiopic descends from the same text.

**J. Cooper and A. J. Maclean, *The Testament of Our Lord, translated into
English from the Syriac* (Edinburgh: T. & T. Clark, 1902)**, archive.org
`cu31924029296170`. Cooper died in 1922, Maclean in 1943.

- `sources/english/1-covenant.cooper.txt`: their translation, from archive.org's
  OCR. Chapter = their chapter, Book II numbered on from Book I (Book I 1-46,
  Book II 1-27 = 47-73); chapter 0 is the opening narrative. Verse = paragraph.
  Their footnotes are left out. The headings of chapters 7 and 19 are
  unreadable in the scan, so those chapters sit under 6 and 18.
- **It is the Syriac, not the Ethiopic.** The Ethiopic differs from it in
  wording and in places in order; use it for the substance of a chapter and say
  that it is the Syriac.

### Sirate Tsion and Abtilis — Tattam 1848 (sister versions)

No Ge'ez text of either has been printed (Fell 1871 names both and prints
neither; see Gitzew above). Both survive in Coptic, and the Ethiopic Sinodos
was translated from the same Coptic-Arabic collection.

**Henry Tattam, *The Apostolical Constitutions, or Canons of the Apostles, in
Coptic, with an English translation* (London: Oriental Translation Fund,
1848)**, archive.org `apostolicalconst00tattrich`. Tattam died in 1868. The
book alternates Coptic and English pages; only the English is taken.

- `sources/english/sirate-tsion.tattam.txt`: Tattam's first book, the 30 canons
  "of our Fathers the Apostles … by the hands of Clemens" (the Apostolic Church
  Order: John, Matthew, Peter and the other apostles speak in turn). This is
  Fell's "30 decrees of the apostles given through Clement", which Cowley calls
  Ser`atä Seyon. Chapter = canon, 1 to 30; canon 1 carries no number in the
  print and begins with the opening address. Verse = paragraph.
- `sources/english/abtilis.tattam.txt`: Tattam's Seventh Book, the 85 Apostolic
  Canons (pp. 174-214). Fell calls the Ethiopic Abtilis "a longer edition of the
  Apostolic Canons"; Cowley counts 81 in it, so **its numbering will not match
  Tattam's 85**. Chapter = Tattam's canon number; verse = paragraph. Tattam
  prints 12-13, 18-19 and 21-22 as one canon each, so their text sits under 12,
  18 and 21 and chapters 13, 19 and 22 are empty. Canons 47-50 are not in the
  Coptic (his note, p. 190). He prints 66 between 63 and 64; it is kept as 66.
  The closing blessing is part of 85; the scribe's colophon is left out.
- Both from archive.org's OCR. Footnotes, margin marks and page heads are left
  out. About thirty OCR misreadings were corrected where context settles them (`Matfhew`,
  `Jill` for "till", `Joss` for "loss", `fleet` for "fled", and the like).
- **It is the Coptic, not the Ethiopic.** Use it for the substance of a canon
  and say that it is the Coptic.
