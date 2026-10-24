# Decision Making with Before/After: Deuteronomy

Changes to chapters already rendered, filed under the book the request started in (a word decision can reach into other books; its table lists every verse). Newest at the top. Each entry: the request, the options, and a `Where | Before | After` table.

## The map after Joshua 24: closer stages, the giants' lands, a wider view (2026-10-23, 10:53 PM Central)

**Request:** Andrew, in chat: zoom in more on each move; the three cities of the giants sit in an area too small to see; the giants' land solid crimson, not striped, with small crimson dots for the cities, since the big dots take over the territory; shade everything Israel took, over the whole territory of the peoples they took it from; and a wider whole map, so the action is not crowded into the upper right corner.

**What was done:** every stage now has its own frame, drawn around that stage's routes and the places it names. There are + and − buttons on the map, and you can drag the map to move it; the next stage puts the frame back. The southern campaign (stage 17) now shows Hebron, Debir and Anab large. The Genesis map shares the new town dots and the zoom buttons. The shading of the taken land waits on the choice below.

| Where | Before | After |
|---|---|---|
| The map, each stage | one of two fixed views (the whole journey; the land) | a frame around that stage's routes and places |
| The map, zooming | none | + and − buttons; drag to move |
| Giants' lands | crimson stripes | solid crimson (paler once the giants are gone) |
| Giants' towns | a large crimson ring | a small crimson dot |
| Whole journey view | Bashan and Lebo-hamath at the top right edge | about 80 miles more on the right and 55 at the top |

**Choices for you:**
- **Shading the land Israel took**
  - (a) **as it is** (now): Israel's land turns green as it is taken (Sihon and Og at Numbers 21, the south at Joshua 10, the north at Joshua 11); Sihon's and Og's kingdoms are outlined for one stage.
  - (b) **by kingdom**: each kingdom Israel took, shaded over its whole extent from the stage Israel meets it and named with its people, using the borders the text gives: Sihon king of the Amorites, from the Arnon to the Jabbok (Joshua 12:2); Og of Bashan, to Mount Hermon (12:4–5); the five Amorite kings of the south, from Kadesh-barnea to Gaza and to Gibeon (10:41); Jabin's kings of the north, as far as Baal-gad under Mount Hermon (11:17). Once taken, each stays shaded, with Israel's green over it.
  - (c) **by people**: the land of each people named in Joshua 12:8 (Hittite, Amorite, Canaanite, Perizzite, Hivite, Jebusite), placed from Numbers 13:29 and Joshua 11:3. The Bible gives these as regions, not borders, and several share the hill country, so their edges would be guesses.
  - Recommend (b): the text draws these borders itself, and Joshua 12 counts what was taken the same way, king by king.

## The map after Joshua 24, and links to it from the notes (2026-10-23, 5:35 PM Central)

**Request:** Andrew: a map, at the end of Joshua, of the path the sons of Israel took out of Egypt and the land they took on the way, shown as a time-lapse; Israel's land coloured and the tribes named where they settled; the giant peoples' lands in another colour, with their names and towns; places not known are fine, but follow the directions the text gives; an old parchment look; and links from a few notes, from leaving Egypt to the end of the journey.

**What was done:**
- **The map**, *From Egypt to the Land*, after Joshua 24 on the site: 21 stages from Rameses (Numbers 33:3) to the burial of Joseph's bones at Shechem (Joshua 24:32), with Play, step buttons, a slider, and two views (the whole journey; the land). Each stage gives its date from the text and quotes this rendering; every reference opens the verse.
- **Directions followed:** not by the way of the Philistines (Exodus 13:17); out to the edge of the wilderness and back to the sea (13:20, 14:2); south along the gulf after Elim (Numbers 33:10); eleven days from Horeb by the way of Mount Seir (Deuteronomy 1:2); Mount Hor *on the border of the land of Edom* (Numbers 20:23), so not the traditional site inside Edom; around Edom by the Sea of Reeds, past Elath, then north by the wilderness of Moab (Numbers 21:4; Deuteronomy 2:8); east of Moab and across the Arnon in the wilderness (Judges 11:18). A site not located is an open ring.
- **The giants:** Anakim (Hebron, Debir, Anab; after Joshua 11, the remnant in Gaza, Gath and Ashdod), Rephaim in Bashan (Og at Ashtaroth and Edrei), Emim in Moab and Zamzummim in Ammon (both gone before the Exodus, Deuteronomy 2:10–11, 20–21), the Valley of Rephaim and the forest of Joshua 17:15.
- **The land:** Sihon's and Og's land filled at Numbers 21, the south at Joshua 10, the north at Joshua 11; the tribal borders of Joshua 13–19, approximate; the land that remained (Joshua 13:2–6) hatched; the six cities of refuge.
- **Word edition:** the map prints as two pages (the whole journey; the land at the end of Joshua), then the key and the 21 stages in words.
- **Machinery:** `build_site.py` now runs a supplement's scripts and turns `[words](#/…)` in a note into a link; `build_docx.py` prints such a link as its words; the link form is in `RENDERING_SPEC.md` (file format). The map is built by `maps/journey/make.py`; `maps/journey/quotecheck.py` found all 34 quotations word for word in the verses they cite.

| Where | Before | After |
|---|---|---|
| Exodus 13, note v17 | …the people may change their minds when they see war. | …the people may change their minds when they see war. See the map after Joshua 24, stage 1. |
| Exodus 14, note vv21–22 | …in the vocabulary of the world's making and of its drowning. | …in the vocabulary of the world's making and of its drowning. See the map after Joshua 24, stage 3. |
| Numbers 13, note v33 | …The Greek has only *we saw the giants*, and not that clause. | …The Greek has only *we saw the giants*, and not that clause. See the map after Joshua 24, stage 8. |
| Numbers 21, note vv17–18 | …*I will give them water* (v16). | …*I will give them water* (v16). See the map after Joshua 24, stage 11. |
| Numbers 33, note v2 | …the verb of every line that follows: *they set out*. | …the verb of every line that follows: *they set out*. See the map after Joshua 24, stage 1. |
| Deuteronomy 2, note vv10–12, 20–23 | …Each people took its land from an older people, and the LORD gave it. | …Each people took its land from an older people, and the LORD gave it. See the map after Joshua 24, stage 11. |
| Deuteronomy 3, note v11 | …the verse is an aside from the speech, set in parentheses. | …the verse is an aside from the speech, set in parentheses. See the map after Joshua 24, stage 12. |
| Deuteronomy 34, note vv1–3 | …before any of it is taken. | …before any of it is taken. See the map after Joshua 24, stage 14. |
| Joshua 3, note v16 | …the pile-up reached from Adam down. | …the pile-up reached from Adam down. See the map after Joshua 24, stage 15. |
| Joshua 11, note vv21–22 | …Goliath of Gath will come from them (1 Samuel 17:4). | …Goliath of Gath will come from them (1 Samuel 17:4). See the map after Joshua 24, stage 18. |
| Joshua 21, note vv43–45 | …what remains is Israel's part. | …what remains is Israel's part. See the map after Joshua 24, stage 20. |
| Joshua 24, note vv29–33 | …the story Judges 3 tells. | …the story Judges 3 tells. See the map after Joshua 24, stage 21. |

**Choices for you:**
- **The borders promised in Numbers 34**
  - ✅ Decided 2026-10-23: (b), add the promised line. Done the same day: a gold dashed line from stage 13 (the plains of Moab, where Numbers 34 is given) to the end, with Zedad and Hazar-enan marked, the stage 13 caption quoting *the land of Canaan with its borders* (Numbers 34:2), and a line in the key.
  - (a) **leave the map as it is** (now): it shows the land taken and the land that remained.
  - (b) **add the promised line**: Numbers 34:1–12 draws the land from the Brook of Egypt to Lebo-hamath, from the Great Sea to the Jordan; a gold line on the last stages would show the promise beside what was held. Several of its points (Zedad, Ziphron, Hazar-enan) are disputed.
  - Recommend (b): it answers the question the map raises, how much of the promise Joshua's generation held.
- **A companion map for Genesis**
  - ✅ Decided 2026-10-23: (b), make it. Done 2026-10-24: *The Journeys of the Fathers*, after the House of Terah chart at the end of Genesis. It has 19 stages, from Terah leaving Ur (Genesis 11) to Jacob carried up to Machpelah and Joseph's oath about his bones (Genesis 50), where the Joshua map takes over. It includes the four kings of Genesis 14 with the Rephaim, Zuzim and Emim, Abram's view from Bethel in four directions (13:14), and a gold line for the covenant's *from the river of Egypt to the great river* (15:18). Genesis says *nehar*, a river, so the line starts at the Nile, not at the Brook of Egypt of Numbers 34:5. The map is wide, so its text sits below it. On a phone it is small; turning the phone sideways helps.
  - (a) **none** (now).
  - (b) **Abraham, Isaac and Jacob**: Ur and Haran to Shechem, Bethel, Hebron and Egypt, ending where this map begins. Genesis is closed, so it waits on your word.
  - Recommend (a) for now: finish reading Joshua with this one first.

## Deuteronomy 1–3: *there*, the speaker, *Rephaim*, *from before them*, 2:25, Og's bed (2026-10-23, 10:00 AM Central)

**Request:** Andrew, `PASTE/edits.md`: 1:37, *Where is "there"?*; 1:46, *should there be an ending quotation mark?*; chapter 2, *is this still Moses talking?*; 2:11, *What is Rephaim?*; 2:12, *clunky sentence with 3 "thems"*; 2:25, *worded strangely*; 3:11, *confused by the question about where the iron bed is; why parentheses?*

**What was done, checked against the Hebrew:**
- **1:37–39** *lo tavo sham*, "you shall not come there," three times: *there* is the good land of v35, two verses back. Now *enter the land* (v37), then *enter it* (vv38–39).
- **1:46 and chapter 2:** no closing mark belongs at 1:46. Moses' speech runs from 1:6 to 4:40 without a break, so the quotation opens at 1:6 and closes at 4:40; each new section reopens with a quotation mark. The v5 note now says so.
- **2:11:** *Rephaim* is the name for the old giant peoples, and the same Hebrew word names the dead, *the shades* (Psalm 88:10; Isaiah 26:14, 19). The vv10–12 note now says so.
- **2:12, 21, 22:** *hishmid… mi-peneihem*, "destroyed… from before them," the idiom CLAUDE.md names (*from before the face of*). Said plainly in all three verses of the chapter.
- **2:25:** the relative clause split off into its own sentence; *lay the dread of you and the fear of you* kept, as in 11:25, where the same Hebrew stands.
- **3:11:** *halo hi be-Rabbat*, "is it not in Rabbah?", a question that means "you can go and see it": given as the statement it makes. The parentheses mark the verse as an aside from the speech, like 2:10–12 and 20–23; the v11 note now says so.

| Where | Before | After |
|---|---|---|
| Deuteronomy 1:37 | 'You also shall not go in there. | 'You also shall not enter the land. |
| Deuteronomy 1:38 | he shall go in there. | he shall enter it. |
| Deuteronomy 1:39 | they shall go in there. | they shall enter it. |
| Deuteronomy 1, note v5 | …not yet a name for five books. | …not yet a name for five books. That teaching is one long speech, from v6 to 4:40: its quotation marks open at v6 and close only at 4:40. |
| Deuteronomy 2:12 | but the sons of Esau dispossessed them and destroyed them from before them and settled in their place, as Israel did to the land of its possession that the LORD gave them.) | but the sons of Esau dispossessed and destroyed them and settled in their place, as Israel did in the land the LORD gave it to possess.) |
| Deuteronomy 2:21 | But the LORD destroyed them from before them, and they dispossessed them | But the LORD destroyed them for the Ammonites, who dispossessed them |
| Deuteronomy 2:22 | when He destroyed the Horites from before them | when He destroyed the Horites for them |
| Deuteronomy 2:25 | This day I will begin to put the dread and fear of you on the peoples under the whole heaven, who will hear the report of you and tremble and be in anguish because of you.' | This day I will begin to lay the dread of you and the fear of you on the peoples under the whole heaven. When they hear the report of you, they will tremble and be in anguish because of you.' |
| Deuteronomy 2, note vv10–12, 20–23 | both counted among the *Rephaim*. | both counted among the *Rephaim*, the name the Hebrew gives the old giant peoples, and the same word it uses for the dead, the shades: *Do the shades rise up to praise You?* (Psalm 88:10). |
| Deuteronomy 3:11 | His bed was a bed of iron; is it not in Rabbah of the sons of Ammon? Nine cubits was its length and four cubits its width, by the cubit of a man.) | His bed, a bed of iron, is still in Rabbah of the Ammonites: nine cubits long and four cubits wide, by the cubit of a man.) |
| Deuteronomy 3, note v11 | *Is it not in Rabbah?* speaks to readers who could go and see it. | The Hebrew asks *Is it not in Rabbah of the sons of Ammon?*, a question that tells readers they could go and see it; the English gives it as the statement it makes, *is still in Rabbah*. Like 2:10–12 and 20–23, the verse is an aside from the speech, set in parentheses. |

**Choices for you:**
- **The same idiom elsewhere, *drive out… from before you* (*mi-penei*)**
  - ✅ Decided 2026-10-23: (a), leave *drive them out from before you* as it is.
  - (a) **leave it** (now): *drive them out from before you* is still found in Exodus 23:28–31, 34:11; Numbers 32:21, 33:52, 55; Deuteronomy 6:19, 7:1, 7:22, 9:4–5, 11:23, 18:12, and with other verbs in a few other books. With *drive out* it reads as English, unlike *destroyed them from before them*.
  - (b) **say it plainly everywhere**: *drive them out ahead of you*, or *drive them out for you*, in every one of those verses.
  - Recommend (a): only the *destroy… from before them* form tripped the reader, and it is fixed; a sweep over finished books waits on your word.

## *And now* reviewed, every verse (2026-10-03, 2:30 PM Central)

**Request:** Andrew: go through every *And now* under the *ve-attah* rule written today (RENDERING_SPEC.md, the *And now* entry). *And now* stays where the turn carries weight; otherwise *So*, *Now*, *But now*, or cut. Only the verses that changed are listed.

| Where | Before | After |
|---|---|---|
| Deuteronomy 5:25 | And now, why should we die?… | But now, why should we die?… |
| Deuteronomy 31:19 | And now write this song… | So now write this song… |

## Spec checks missed in the OT loop, fixed (render cycle, 2026-09-29)

**Why:** reading RENDERING_SPEC.md in full at the start of this cycle turned up three rules the loop chapters of 2026-09-28 broke. Filed here because most of the fixes are in Deuteronomy; the Joshua rows are listed too.

1. **Doubled words** (readability pass, item 1: *stone him with stones* → *stone him*).
2. **Written and read forms** (follow the read form; note only where the meaning differs).
3. **Notes: three to ten per chapter.**

| Where | Before | After |
|---|---|---|
| Deuteronomy 13:10 | You shall stone him with stones | You shall stone him |
| Deuteronomy 17:5 | stone them with stones | stone them |
| Deuteronomy 21:21 | shall stone him with stones | shall stone him |
| Deuteronomy 22:21 | shall stone her with stones | shall stone her |
| Deuteronomy 22:24 | stone them with stones | stone them |
| Deuteronomy 9:18 | all your sin that you had sinned | all the sin you had committed |
| Joshua 6:5 | shall shout a great shout | shall give a great shout |
| Joshua 6:20 | the people shouted a great shout | the people gave a great shout |
| Joshua 7:25 | stoned him with stones… stoned them with stones | stoned him… stoned them |
| Joshua 10:10 | He struck them with a great blow | He dealt them a great defeat |
| Joshua 10:20 | striking them with a very great blow | dealing them a very great defeat |
| Joshua 3:16 | very far away, at Adam (the written form) | very far away, from Adam (the read form; the note keeps both, since the sense differs) |
| Joshua 15:53 | Janim (written) | Janum (read) |
| Joshua 18:24 | Chephar-ammoni (written) | Chephar-haammonah (read) |
| Joshua 19:22 | Shahazumah (written) | Shahazimah (read) |
| Deuteronomy 22 notes | a note on *na'ar* written for *na'arah* | cut (spelling only; the text already follows the read form) |
| Deuteronomy 28:27, 28:30 notes | sentences on written vs read forms | cut (same meaning) |
| Deuteronomy 28 notes | 12 | 10 (cut: v23, v27) |
| Deuteronomy 32 notes | 16 | 10 (cut: v1, v11, v17, v39, v44, vv49–52) |
| Deuteronomy 33 notes | 17 | 10 (cut: v4, v6, v7, v10, v17, v22, v29) |
| Joshua 7 notes | 11 | 10 (cut: v21 Shinar) |
| Joshua 10 notes | 12 | 10 (cut: v13, vv26–27) |

## Verse numbers put back on the English (KJV) numbering (render cycle, 2026-09-29, 7:50 AM Central)

**Why:** CLAUDE.md section 6 and RENDERING_SPEC.md ("Versification") say to follow the English chapter and verse numbering. Three chapter breaks in Deuteronomy were rendered on the Hebrew numbering during the OT loop of 2026-09-28. No wording changed; only verse numbers, the verse moved across each break, and the notes and cross-references that cite those numbers. The render reports for those runs in `PASTE/renders/5-deuteronomy.md` still show the old (Hebrew) numbers.

| Where | Before | After |
|---|---|---|
| Deuteronomy 12–13 | 12 ended at v31; *Every word that I command you…* was 13:1; 13:2–19 | that verse is now 12:32 (note added); 13:1–18 |
| Deuteronomy 22–23 | 22 ended at v29; *A man shall not take his father's wife…* was 23:1; 23:2–26 | that verse is now 22:30 (note moved with it); 23:1–25 |
| Deuteronomy 28–29 | 28 ended at v69 (*These are the words of the covenant…*); 29:1–28 | that verse is now 29:1 (note moved with it); 29:2–29 |
| Notes in 13, 23, 29 | verse labels on the Hebrew numbers | shifted to the English numbers |
| Deuteronomy 8:4 note | *made again in 29:4* | *made again in 29:5* |
| Deuteronomy 15:9 note | *worthless men* in 13:14 | in 13:13 |
| Deuteronomy 17:4 note | the words of 13:15 | the words of 13:14 |
| Deuteronomy 18:20–22 note | 13:2–4 | 13:1–3 |
| Deuteronomy 19:13 note | the formula of 13:6 | the formula of 13:5 |
| Deuteronomy 24:1 note | the phrase of 23:15 | the phrase of 23:14 |
| Deuteronomy 33:10 note | *kalil*, the word of 13:17 | 13:16 |
| Joshua 8:28 note | Deuteronomy 13:17 | Deuteronomy 13:16 |
| Joshua 9:21 note | Deuteronomy 29:10 | Deuteronomy 29:11 |
