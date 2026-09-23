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
| 2 Meqabyan | `5001-6000/LIT5840SecondEthioMaccabees.xml` | full text, 21 chapters |
| 3 Meqabyan | `5001-6000/LIT5839ThirdEthioMaccabees.xml` | full text, 10 chapters, every chapter filled |

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
| **1 Enoch** | Greek (48 chapters), Ge'ez (71), Qumran Aramaic (8), Latin (3) |
| **Jubilees** | Latin (34 chapters), Greek (26) |

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

CC BY 4.0 asks one thing: that this credit stays with the text. It places no
condition on the renderings or the notes in this repository, which are original
work, and none on what is done with them.
