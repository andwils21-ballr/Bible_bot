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
