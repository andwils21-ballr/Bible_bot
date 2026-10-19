#!/usr/bin/env python3
"""Check rendered chapters against the rules a program can check, so they hold
on the thousandth chapter as well as the first. A run of Claude can drift; this
cannot. Every flag is a lead to look at, not a verdict: a flagged line may be
right, and the report or the note should then say why.

Usage:
  python3 check_chapters.py                 chapters changed since origin/main
  python3 check_chapters.py --all           every rendered chapter
  python3 check_chapters.py genesis 2-kings every chapter of these books
  python3 check_chapters.py books/13-1-chronicles/14.md ...
  python3 check_chapters.py --docs          the instruction files (CLAUDE.md §8)

With no arguments it also checks the instruction files if one of them has
changed, and the lines added to PASTE/ against the choice layout (CLAUDE.md §5).
Exit status is 1 if any ERROR was found, so a render cycle can stop on it.
What it cannot check (pronouns for God, doubled verbs, idioms, whether a note
is true) still needs reading; see RENDERING_SPEC.md.
"""
import json
import os
import re
import subprocess
import sys

import yaml

ROOT = os.path.dirname(os.path.abspath(__file__))
BOOKS = {b["slug"]: b for b in
         json.load(open(os.path.join(ROOT, "manifest.json"), encoding="utf-8"))["books"]}
HEBREW = {f[:-4] for f in os.listdir(os.path.join(ROOT, "sources", "hebrew"))
          if f.endswith(".txt")}
NEW_TESTAMENT = range(55, 82)

# Words the spec bans from the rendered text.
BANNED = ["lest", "behold", "unto", "thee", "thou", "thy", "thine", "ye",
          "verily", "wherefore", "whence", "thence", "hither", "thither",
          "peradventure", "nay", "yea", "ere", "betwixt", "amongst", "whilst",
          "hearken", "hearkened", "bade", "wrought", "albeit"]
BANNED_PHRASES = [r"\bin the midst of\b", r"\bart thou\b", r"\bthou art\b"]

# Openings with "And" that the spec keeps.
AND_KEPT = re.compile(r"And (it came to pass|it shall come to pass|it will come to pass"
                      r"|it would come to pass|now\b|here —)")
# Chapters where every "And" is kept (the creation week, book titles).
AND_FREE = {("genesis", 1), ("genesis", 2), ("exodus", 1), ("leviticus", 1)}

# The "here —" / "look —" ruling (Andrew, 2026-09-28), and its disguises.
HINNEH = re.compile(r"(?:^|[.!?\"“‘'—:;] )(Here —|Look —|Lo\b|Behold\b)")
# These may be a real verb (*re'eh*, see), so they are a lead, not an error.
HINNEH_SOFT = re.compile(r"(?:^|[.!?\"“‘'—:;] )(Look now\b|See now\b)")
HINNEH_KEPT = {("genesis", 29, 25), ("jubilees", 28, 4), ("1-enoch", 1, 9)}

# Fixed terms: the wrong word on the left, the ruling on the right.
FIXED_HEBREW = [  # only in books rendered from the Hebrew
    (r"\bangel of (the LORD|God)\b", "mal'akh of God or of the LORD is *messenger*"),
    (r"\bleprosy\b|\bleprous\b|\blepers?\b", "tsara'at is *blight*"),
    (r"\babominations?\b", "to'evah is *detestable*"),
]
FIXED_ALL = [
    (r"\bunblemished\b", "tamim is *without defect*"),
    (r"\bharlots?\b", "zonah is *prostitute*, never *harlot*"),
    (r"\bAbib\b", "the month is *Aviv*"),
    (r"\bsojourn", "gur is *live as a guest*; ger is *guest*"),
    (r"\bafter (its|their) kind\b", "le-mino is *of every kind*"),
    (r"\b(pleasing|sweet) (aroma|savou?r)\b", "re'ach nichoach is *soothing aroma*"),
    (r"\bspirit of (the LORD|God)\b", "the ruach of God is *the Spirit* (capital S)"),
    (r"\bthe thing that\b", "use *what*"),
]

# Notes are written for a reader who never sees the curtain. The first list is
# always talk about the work; the second usually is, so it is a lead to read.
PROCESS = re.compile(r"\b(fixed as|fixed rendering|Andrew|readability|for clarity"
                     r"|we (chose|decided)|I (chose|decided))\b", re.I)
PROCESS_SOFT = re.compile(r"\b(fixed term|this project|the project's|the spec|chosen for|we (render|use|keep|follow|read)"
                          r"|I (render|kept))\b", re.I)
# Leads in the text that a reader has to judge (spec, "No And" and "Already ruled").
LEADS = [
    (re.compile(r"\bNow then\b"), "never for *ve-attah*: *So*, *So now*, *But now*, *Now*, "
     "or cut it (spec, \"No And\")"),
    (re.compile(r"\b(come|comes|came|coming) into\b(?! being)(?! (?i:his|her|their|your|my|our) "
                r"(heart|mind)s?\b)"),
     "a place is *enter*, *go into* or *arrive in*; *come* stays only where the speaker "
     "is there, or for an idiom (spec, \"Already ruled\")"),
]
# A note that ends in a shrug is unfinished work.
SHRUG = re.compile(r"\b(which is (strange|odd|curious|interesting)|strangely|curiously"
                   r"|it is not clear why|for some reason)\b", re.I)


def chapter_files(args):
    if not args:
        out = subprocess.run(["git", "diff", "--name-only", "origin/main", "--", "books"],
                             cwd=ROOT, capture_output=True, text=True).stdout.split()
        out += subprocess.run(["git", "ls-files", "--others", "--exclude-standard", "books"],
                              cwd=ROOT, capture_output=True, text=True).stdout.split()
        return sorted({os.path.join(ROOT, f) for f in out if re.search(r"/\d+\.md$", f)
                       and os.path.exists(os.path.join(ROOT, f))})
    files = []
    for a in args:
        if a == "--all":
            a = None
        if a and a.endswith(".md"):
            files.append(os.path.abspath(a))
            continue
        for d in sorted(os.listdir(os.path.join(ROOT, "books"))):
            if a and d.split("-", 1)[1] != a:
                continue
            folder = os.path.join(ROOT, "books", d)
            files += [os.path.join(folder, f) for f in sorted(os.listdir(folder))
                      if re.fullmatch(r"\d+\.md", f) and f != "00.md"]
    return files


def source_verse_count(slug, chapter):
    if slug not in HEBREW:
        return None
    n = 0
    with open(os.path.join(ROOT, "sources", "hebrew", f"{slug}.txt"), encoding="utf-8") as f:
        for line in f:
            if line.startswith(f"{chapter}:"):
                n += 1
    return n or None


def check(path):
    found = []  # (level, where, message)
    add = lambda level, where, msg: found.append((level, where, msg))
    text = open(path, encoding="utf-8").read()

    parts = text.split("---\n")
    try:
        fm = yaml.safe_load(parts[1])
        assert isinstance(fm, dict)
    except Exception:
        add("ERROR", "frontmatter", "missing or not valid YAML (a title with ': ' "
            "needs quotation marks)")
        return found
    for key in ("book", "book_order", "slug", "chapter", "title", "status", "tier", "rendered"):
        if key not in fm:
            add("ERROR", "frontmatter", f"no `{key}`")
    slug, ch = fm.get("slug"), fm.get("chapter")
    if fm.get("status") == "need_source":
        return found

    body, _, notes = text.partition("\n## Notes")
    if not _:
        add("ERROR", "notes", "no `## Notes` section")
    if len(re.findall(r"^# ", body, re.M)) != 1:
        add("ERROR", "format", "there must be exactly one `# ` title line")

    # Verses: every one present, in order, once.
    nums = [int(n) for n in re.findall(r"^\*\*(\d+)\*\* ", body, re.M)]
    if nums != sorted(set(nums)) or (nums and nums[0] != 1):
        add("ERROR", "verses", "verse numbers repeat, go backward or do not start at 1")
    elif nums != list(range(1, len(nums) + 1)):
        missing = sorted(set(range(1, nums[-1] + 1)) - set(nums))
        add("CHECK", "verses", f"no verse {missing[:8]} (fine if the source lacks it; "
            "the notes should say so)")
    src = source_verse_count(slug, ch)
    if src and nums and src != len(nums):
        add("CHECK", "verses", f"{len(nums)} verses; the Hebrew file has {src} "
            "(fine if a known chapter-break offset, see HANDOFF.md)")

    # Each verse paragraph, with its number, so a flag can say where it is.
    verses = re.findall(r"^\*\*(\d+)\*\* (.*?)(?=^\*\*\d+\*\* |^## |^---|\Z)", body, re.M | re.S)
    order = BOOKS.get(slug, {}).get("order", 0)
    from_hebrew = slug in HEBREW and order not in NEW_TESTAMENT
    for v, t in verses:
        v = int(v)
        where = f"v{v}"
        flat = " ".join(t.split())
        for w in BANNED:
            if re.search(rf"\b{w}\b", flat, re.I):
                add("ERROR", where, f"banned word *{w}*")
        for p in BANNED_PHRASES:
            if re.search(p, flat, re.I):
                add("ERROR", where, f"banned phrase *{re.search(p, flat, re.I).group(0)}*")
        if (slug, ch) not in AND_FREE:
            for m in re.finditer(r"(?:^|[.!?:;]\s+[\"“‘']?|[\"“‘]\s*)(And\b.{0,40})", flat):
                if not AND_KEPT.match(m.group(1)):
                    add("ERROR", where, f"sentence starts with *And*: “{m.group(1)}…”")
        if (slug, ch, v) not in HINNEH_KEPT:
            for m in HINNEH.finditer(flat):
                add("ERROR", where, f"*{m.group(1)}* (the hinneh ruling, 2026-09-28)")
            for m in HINNEH_SOFT.finditer(flat):
                add("CHECK", where, f"*{m.group(1)}*: fine for a real verb *see*; "
                    "not for *hinneh* (2026-09-28)")
        for pat, rule in LEADS:
            m = pat.search(flat)
            if m:
                add("CHECK", where, f"*{m.group(0)}*: {rule}")
        rules = FIXED_ALL + (FIXED_HEBREW if from_hebrew else [])
        for pat, rule in rules:
            m = re.search(pat, flat)
            if m:
                add("ERROR", where, f"*{m.group(0)}*: {rule}")

    # Notes: three to ten, each anchored, none about the work itself.
    entries = re.findall(r"^- \*\*(.*?)$((?:\n(?!- \*\*).*)*)", notes, re.M)
    if _ and not 3 <= len(entries) <= 10:
        add("CHECK", "notes", f"{len(entries)} notes (the spec says three to ten)")
    for head, rest in entries:
        anchor = head.split("**")[0]
        full = head + rest
        if not re.match(r"(vv?\d|Source text|The |vv?\.)", anchor) and "v" not in anchor[:6]:
            add("CHECK", f"note “{anchor[:30]}”", "not anchored to a verse")
        if anchor.startswith("Source text"):
            continue
        m = PROCESS.search(full)
        if m:
            add("ERROR", f"note “{anchor[:30]}”",
                f"*{m.group(0)}*: notes never talk about the translating (CLAUDE.md §3)")
        m = PROCESS_SOFT.search(full)
        if m:
            add("CHECK", f"note “{anchor[:30]}”",
                f"*{m.group(0)}*: is this about the text, or about the translating?")
        m = SHRUG.search(full)
        if m:
            add("CHECK", f"note “{anchor[:30]}”", f"*{m.group(0)}*: a hedge is unfinished work")
    return found


# The instruction files (CLAUDE.md §8) and their word budgets. Over budget means
# tighten the wording or move history to RULINGS_HISTORY.md; never drop a ruling
# to fit. A budget is raised only when Andrew adds rules that cannot be shortened.
SPEC_PART2 = "\n## Part 2"
DOCS = [  # (file, part, budget in words)
    ("CLAUDE.md", None, 2400),
    ("RENDERING_SPEC.md", "part 1", 4400),
    ("RENDERING_SPEC.md", "part 2", 1200),
    ("problem_solving.md", None, 1400),
    ("REVIEW_LOOP.md", None, 500),
    ("ROUTINE_PROMPT.md", None, 300),
    ("COUNCIL.md", "Open", 2000),
]
RULE_FILES = ["CLAUDE.md", "RENDERING_SPEC.md", "problem_solving.md", "REVIEW_LOOP.md",
              "ROUTINE_PROMPT.md"]
# History belongs in RULINGS_HISTORY.md, not in a rule.
HISTORY = re.compile(r"\breplacing (the|an?) (rule|ruling)s?\b|\b(was|were) swept\b"
                     r"|\bswept to (this|the) rule\b|\brendered before (this|the) rule\b", re.I)
# The choice layout (CLAUDE.md §5).
NOW_LINE = re.compile(r"^\s*- (\*\*)?Now(\*\*)?:")
OFFERED = re.compile(r"\b(open to you|please confirm|for your attention)\b", re.I)


def changed(paths):
    out = subprocess.run(["git", "diff", "--name-only", "origin/main", "--"] + paths,
                         cwd=ROOT, capture_output=True, text=True).stdout.split()
    out += subprocess.run(["git", "ls-files", "--others", "--exclude-standard"] + paths,
                          cwd=ROOT, capture_output=True, text=True).stdout.split()
    return set(out)


def doc_part(name, part):
    text = open(os.path.join(ROOT, name), encoding="utf-8").read()
    if part == "part 1":
        return text.split(SPEC_PART2)[0]
    if part == "part 2":
        return text.partition(SPEC_PART2)[2]
    if part == "Open":
        return text.partition("\n## Open\n")[2].split("\n## ")[0]
    return text


def sentences(text):
    flat = re.sub(r"[*`_|>#]", "", " ".join(text.split())).lower()
    return {s.strip() for s in re.split(r"(?<=[.;:!?])\s+", flat) if len(s.split()) >= 14}


def check_docs():
    found = []
    for name, part, budget in DOCS:
        n = len(doc_part(name, part).split())
        if n > budget:
            label = f"{name} ({part})" if part else name
            found.append((label, f"{n} words; the budget is {budget} (CLAUDE.md §8)"))
    seen = {}
    for name in RULE_FILES:
        text = open(os.path.join(ROOT, name), encoding="utf-8").read()
        for m in HISTORY.finditer(text):
            found.append((name, f"*{m.group(0)}*: history goes in RULINGS_HISTORY.md"))
        for s in sentences(text):
            if s in seen and seen[s] != name:
                found.append((name, f"also in {seen[s]}: “{s[:70]}…” (one home per rule)"))
            seen.setdefault(s, name)
    return found


def check_paste():
    found = []
    diff = subprocess.run(["git", "diff", "-U0", "origin/main", "--", "PASTE"], cwd=ROOT,
                          capture_output=True, text=True).stdout
    added = added_lines(diff)
    for f in subprocess.run(["git", "ls-files", "--others", "--exclude-standard", "PASTE"],
                            cwd=ROOT, capture_output=True, text=True).stdout.split():
        added += [(f, l) for l in open(os.path.join(ROOT, f), encoding="utf-8").read().split("\n")]
    for f, line in added:
        if NOW_LINE.match(line):
            found.append((f, f"a separate *Now:* line: mark the option *(now)* instead "
                          f"(CLAUDE.md §5): “{line.strip()[:60]}”"))
        m = OFFERED.search(line)
        if m:
            found.append((f, f"*{m.group(0)}*: only **Choices for you** is offered to Andrew "
                          "(CLAUDE.md §5)"))
    return found


def added_lines(diff):
    out, name = [], None
    for line in diff.split("\n"):
        if line.startswith("+++ "):
            name = line[6:]
        elif line.startswith("+") and name:
            out.append((name, line[1:]))
    return out


def main():
    args = sys.argv[1:]
    docs = "--docs" in args
    args = [a for a in args if a != "--docs"]
    errors = checks = 0
    extra = []
    if docs or (not args and changed(sorted({d[0] for d in DOCS}))):
        extra += check_docs()
    if not args and not docs:
        extra += check_paste()
    for where, msg in extra:
        print(f"  CHECK  {where}: {msg}")
        checks += 1
    if docs and not args:
        print(f"\nInstruction files checked: {checks} to look at.")
        return 0
    files = chapter_files(args)
    if not files:
        print("No chapters to check (nothing changed since origin/main).")
        return 0
    for path in files:
        found = check(path)
        if not found:
            continue
        print(os.path.relpath(path, ROOT))
        for level, where, msg in found:
            print(f"  {level:5}  {where}: {msg}")
            errors += level == "ERROR"
            checks += level == "CHECK"
    print(f"\n{len(files)} chapters checked: {errors} errors, {checks} to look at.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
