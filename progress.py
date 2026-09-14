#!/usr/bin/env python3
"""Regenerate PROGRESS.md from what is actually on disk. No separate state file
to drift out of sync — the files are the ledger."""
import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
books = json.load(open(os.path.join(ROOT, "manifest.json"),
                      encoding="utf-8"))["books"]

rows, done_total, all_total = [], 0, 0
next_up = None
for b in books:
    folder = os.path.join(ROOT, "books", f"{b['order']}-{b['slug']}")
    done = 0
    if os.path.isdir(folder):
        done = len([f for f in os.listdir(folder)
                    if f.endswith(".md") and f != "00.md"])
    done_total += done
    all_total += b["chapters"]
    if b["tier"] == "none":
        mark = "stub" if os.path.isdir(folder) else "—"
    elif done >= b["chapters"] and b["chapters"]:
        mark = "done"
    else:
        mark = f"{done}/{b['chapters']}"
        if next_up is None:
            next_up = f"{b['title']} {done + 1}"
    rows.append(f"| {b['order']} | {b['title']} | {b['tier']} | {mark} |")

pct = done_total / all_total * 100 if all_total else 0
with open(os.path.join(ROOT, "PROGRESS.md"), "w", encoding="utf-8") as f:
    f.write("# Progress\n\n")
    f.write(f"**{done_total} of {all_total} chapters rendered ({pct:.1f}%).**\n\n")
    f.write(f"Next up: **{next_up or 'complete'}**\n\n")
    f.write("| # | Book | Tier | Status |\n|---|---|---|---|\n")
    f.write("\n".join(rows) + "\n")
print(f"{done_total}/{all_total} ({pct:.1f}%) — next up: {next_up}")
