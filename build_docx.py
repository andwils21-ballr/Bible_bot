#!/usr/bin/env python3
"""Build one printable .docx per book from the chapter Markdown.

    pip install python-docx
    python3 build_docx.py            # every book that has chapters
    python3 build_docx.py matthew    # one book by slug
"""
import json
import os
import re
import sys

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt, Inches

from build_site import parse_chapter, split_notes, VERSE_RE

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "docx")

BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
ITAL_RE = re.compile(r"(?<!\*)\*([^*]+?)\*(?!\*)")


def add_rich(par, text):
    """Add text to a paragraph, honouring **bold** and *italic*."""
    for chunk in re.split(r"(\*\*.+?\*\*|(?<!\*)\*[^*]+?\*(?!\*))", text):
        if not chunk:
            continue
        b, i = BOLD_RE.fullmatch(chunk), ITAL_RE.fullmatch(chunk)
        run = par.add_run(b.group(1) if b else i.group(1) if i else chunk)
        run.bold, run.italic = bool(b), bool(i)


def setup(doc, title):
    normal = doc.styles["Normal"]
    normal.font.name = "Georgia"
    normal.font.size = Pt(11)
    normal.paragraph_format.space_after = Pt(8)
    for section in doc.sections:
        section.left_margin = section.right_margin = Inches(1.15)
    head = doc.add_paragraph()
    head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = head.add_run(title)
    run.bold, run.font.size = True, Pt(26)
    sub = doc.add_paragraph()
    sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    srun = sub.add_run("A Close Rendering")
    srun.italic, srun.font.size = True, Pt(12)
    doc.add_page_break()


def build(book):
    folder = os.path.join(ROOT, "books", f"{book['order']}-{book['slug']}")
    if not os.path.isdir(folder):
        return None
    files = sorted(f for f in os.listdir(folder) if f.endswith(".md"))
    if not files:
        return None

    doc = Document()
    setup(doc, book["title"])
    for idx, name in enumerate(files):
        meta, body = parse_chapter(os.path.join(folder, name))
        if idx:
            doc.add_page_break()
        prose, notes = split_notes(body)
        for block in re.split(r"\n\s*\n", prose):
            block = block.strip()
            if not block or block == "---":
                continue
            if block.startswith("# "):
                doc.add_heading(block[2:].strip(), level=1)
            elif block.startswith("## "):
                doc.add_heading(block[3:].strip(), level=2)
            else:
                par = doc.add_paragraph()
                m = VERSE_RE.match(block)
                if m:
                    num = par.add_run(m.group(1) + " ")
                    num.bold, num.font.size = True, Pt(8)
                    add_rich(par, m.group(2).replace("  \n", "\n"))
                else:
                    add_rich(par, block)
        if notes:
            doc.add_heading("Notes", level=2)
            for item in notes:
                for i, para in enumerate(item):
                    # first paragraph is the bullet; the rest indent under it
                    par = doc.add_paragraph(
                        style="List Bullet" if i == 0 else None)
                    if i:
                        par.paragraph_format.left_indent = Inches(0.5)
                    add_rich(par, para)
                    for run in par.runs:
                        run.font.size = Pt(9.5)

    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, f"{book['order']:02d}-{book['slug']}.docx")
    doc.save(path)
    return path


def main():
    books = json.load(open(os.path.join(ROOT, "manifest.json"),
                           encoding="utf-8"))["books"]
    wanted = sys.argv[1:]
    if wanted:
        books = [b for b in books if b["slug"] in wanted]
    for book in books:
        path = build(book)
        if path:
            print("wrote", os.path.relpath(path, ROOT))


if __name__ == "__main__":
    main()
