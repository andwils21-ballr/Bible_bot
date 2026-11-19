# Decision Making with Before/After: 1 Kings

Changes to chapters already rendered, newest at the top. Format: CLAUDE.md, section 5.

## Fidelity audit against the Hebrew, 1 Kings 1–22 (Bible 3, 2026-11-18, 12:15 to 1:30 AM CST)

**Request:** Andrew, 2026-11-18: audit the finished books against the source from Leviticus on. 1 Kings 1–22 read verse by verse beside the Hebrew (English 4:21–34 is Hebrew 5:1–14, English 5:1–18 is Hebrew 5:15–32, and English 22:44–53 is Hebrew 22:45–54), and every quotation and count in the notes checked against this repo's own text. No verse was changed; six note quotations were put into the wording of the verses they cite.

| Where | Before | After |
|---|---|---|
| 1 Kings 4, note v25 (Micah 4:4) | *They shall sit each man under his vine and under his fig tree, and none shall make them afraid* | *But they shall sit, each man under his vine and under his fig tree, and no one shall make them afraid* |
| 1 Kings 8, note vv65–66 (2 Chronicles 7:9) | *the dedication of the altar they kept seven days, and the feast seven days* | *they had kept the dedication of the altar seven days and the feast seven days* |
| 1 Kings 15, note vv2, 10 (2 Chronicles 13:2) | *Micaiah daughter of Uriel of Gibeah* | *Micaiah the daughter of Uriel of Gibeah* |
| 1 Kings 15, note vv2, 10 (2 Chronicles 11:20) | *Maacah daughter of Absalom* | *Maacah the daughter of Absalom* |
| 1 Kings 17, note v9 (Luke 4:26) | *was sent to none of them except to Zarephath in the land of Sidon, to a widow* | *was sent to none of them, but only to Zarephath in Sidon, to a woman who was a widow* |
| 1 Kings 19, note v18 (Romans 11:4) | *I have kept for Myself seven thousand men, who have not bowed the knee to Baal* | *I have kept for Myself seven thousand men who have not bowed the knee to Baal* |

**Choices for you:** none new.

## *And now* reviewed, every verse (2026-10-03, 2:30 PM Central)

**Request:** Andrew: go through every *And now* under the *ve-attah* rule written today (RENDERING_SPEC.md, the *And now* entry). *And now* stays where the turn carries weight; otherwise *So*, *Now*, *But now*, or cut. Only the verses that changed are listed.

| Where | Before | After |
|---|---|---|
| 1 Kings 12:11 | And now, whereas my father… | Now, whereas my father… |

## *And* start removed (2026-10-03, 2:26 PM Central)

**Why:** the new checker (check_chapters.py) flagged a sentence starting with *And* that is not on the kept list.

| Where | Before | After |
|---|---|---|
| 1 Kings 20:12 | And they took their positions against the city. | So they took their positions against the city. |

## *And it came to pass* rule (2026-10-03, 2:06 PM Central)

**Request:** Andrew, after the drift audit: keep *And it came to pass* where it carries meaning and feeling, and write the rule for when to keep and when to cut. The rule is now in RENDERING_SPEC.md under *Kept on purpose*. It keeps the formula when *va-yehi* is followed by a time or circumstance and then the event, and cuts it for *was / became / had*, the word of the LORD, a reason, a habit, or a clause inside a running sentence. These verses had drifted from it.

| Where | Before | After |
|---|---|---|
| 1 Kings 5:7 | When Hiram heard the words of Solomon, he rejoiced greatly | And it came to pass, when Hiram heard the words of Solomon, that he rejoiced greatly |
| 1 Kings 11:15 | For when David was in Edom… he struck down every male in Edom. | For it came to pass, when David was in Edom… that he struck down every male in Edom. |
| 1 Kings 14:6 | When Ahijah heard the sound of her feet… he said, | And it came to pass, when Ahijah heard the sound of her feet… that he said, |
| 1 Kings 18:7 | As Obadiah was on the way, Elijah met him. | And it came to pass, as Obadiah was on the way, that Elijah met him. |
| 1 Kings 20:39 | As the king passed by, he cried out to the king | And it came to pass, as the king passed by, that he cried out to the king |

## notes without *fixed as* (2026-10-03, 2:06 PM Central)

**Request:** Andrew approved removing the project-decision wording (*fixed as*, *the fixed term*) from the notes. Each note keeps the Hebrew word and any real connection.

| Where | Before | After |
|---|---|---|
| 13, note on v18 | *mal'akh*, fixed as **messenger**. | *mal'akh*, **messenger**. |
| 17, note on vv20–21 | from *gur*, fixed as **live as a guest**: | from *gur*, **to live as a guest**: |
| 19, note on vv5–7 | *mal'akh*, fixed as **messenger**. | *mal'akh*, **messenger**. |
| 21, note on v26 | from *to'evah*, fixed as **detestable**; | from *to'evah*, **a detestable thing**; |
| 22, note on v38 | *Zonot*, fixed as **prostitutes**. | *Zonot*, **prostitutes**. |
