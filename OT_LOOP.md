# The Old Testament loop (Numbers onward)

Andrew (2026-09-28, 5:51 PM CDT): "continue with Numbers and the OT books in
order on loop for the next 10 hours." Run after run until **3:51 AM CDT,
2026-09-29** (08:51 UTC). Each run follows `ROUTINE_PROMPT.md` exactly
(sync, read CLAUDE.md and the spec in full, render the next four to six
chapters `progress.py` names, readability pass, build, push, report).
`CLAUDE.md` outranks this file.

Rulings of 2026-09-28 that every run applies (all in the spec):
- No *here —* or *look —* for *hinneh*; keep it only where cutting loses
  something the word carries, and say so in the report.
- *tamim* of an offering is *without defect*; *blemish* is *mum*.
- *tsara'at* is *blight*.
- Capital pronouns for God.

Each run:
1. `ReadNotifications`, then sync.
2. If it is past 3:51 AM CDT on 2026-09-29, the loop is done: say so and do not
   schedule another run.
3. Otherwise render, push and report, then schedule the next run with
   `send_later`, 2 minutes, `initiation: human_schedule`, name
   "OT render loop: next run", message: "/loop OT render run: follow
   /home/user/bible_bot/OT_LOOP.md exactly."
