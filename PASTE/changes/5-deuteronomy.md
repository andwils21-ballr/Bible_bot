# Decision Making with Before/After: Deuteronomy

Changes to chapters already rendered, filed under the book the request started in (a word decision can reach into other books; its table lists every verse). Newest at the top. Each entry: the request, the options, and a `Where | Before | After` table.

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
