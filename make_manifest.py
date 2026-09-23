"""One-time generator for manifest.json — the canon ledger the render Routine reads."""
import json

# (order, title, slug, chapters, tier)
#   tier "source"       - I can work from the Hebrew/Aramaic/Greek text itself
#   tier "english-only" - no source language access; work from established English translations
#   tier "none"         - no usable source text available; emit a NEED SOURCE stub
BOOKS = [
    (1,  "Genesis",              "genesis",          50,  "source"),
    (2,  "Exodus",               "exodus",           40,  "source"),
    (3,  "Leviticus",            "leviticus",        27,  "source"),
    (4,  "Numbers",              "numbers",          36,  "source"),
    (5,  "Deuteronomy",          "deuteronomy",      34,  "source"),
    (6,  "Joshua",               "joshua",           24,  "source"),
    (7,  "Judges",               "judges",           21,  "source"),
    (8,  "Ruth",                 "ruth",              4,  "source"),
    (9,  "1 Samuel",             "1-samuel",         31,  "source"),
    (10, "2 Samuel",             "2-samuel",         24,  "source"),
    (11, "1 Kings",              "1-kings",          22,  "source"),
    (12, "2 Kings",              "2-kings",          25,  "source"),
    (13, "1 Chronicles",         "1-chronicles",     29,  "source"),
    (14, "2 Chronicles",         "2-chronicles",     36,  "source"),
    (15, "Jubilees",             "jubilees",         50,  "english-only"),
    (16, "1 Enoch",              "1-enoch",         108,  "english-only"),
    (17, "Ezra",                 "ezra",             10,  "source"),
    (18, "Nehemiah",             "nehemiah",         13,  "source"),
    (19, "Ezra Sutuel",          "ezra-sutuel",      16,  "english-only"),
    (20, "Tobit",                "tobit",            14,  "source"),
    (21, "Judith",               "judith",           16,  "source"),
    (22, "Esther",               "esther",           16,  "source"),
    (23, "1 Meqabyan",           "1-meqabyan",       36,  "english-only"),
    (24, "2 Meqabyan",           "2-meqabyan",       21,  "english-only"),
    (25, "3 Meqabyan",           "3-meqabyan",       10,  "english-only"),
    (26, "Job",                  "job",              42,  "source"),
    (27, "Psalms",               "psalms",          151,  "source"),
    (28, "Proverbs",             "proverbs",         24,  "source"),
    (29, "Reproof (Tegsat)",     "reproof-tegsat",    7,  "source"),
    (30, "Ecclesiastes",         "ecclesiastes",     12,  "source"),
    (31, "Song of Songs",        "song-of-songs",     8,  "source"),
    (32, "Wisdom of Solomon",    "wisdom-of-solomon", 19, "source"),
    (33, "Sirach",               "sirach",           51,  "source"),
    (34, "Isaiah",               "isaiah",           66,  "source"),
    (35, "Jeremiah",             "jeremiah",         52,  "source"),
    (36, "Lamentations",         "lamentations",      5,  "source"),
    (37, "Baruch",               "baruch",            5,  "source"),
    (38, "Letter of Jeremiah",   "letter-of-jeremiah",1,  "source"),
    (39, "4 Baruch",             "4-baruch",          9,  "english-only"),
    (40, "Ezekiel",              "ezekiel",          48,  "source"),
    (41, "Daniel",               "daniel",           14,  "source"),
    (42, "Hosea",                "hosea",            14,  "source"),
    (43, "Amos",                 "amos",              9,  "source"),
    (44, "Micah",                "micah",             7,  "source"),
    (45, "Joel",                 "joel",              3,  "source"),
    (46, "Obadiah",              "obadiah",           1,  "source"),
    (47, "Jonah",                "jonah",             4,  "source"),
    (48, "Nahum",                "nahum",             3,  "source"),
    (49, "Habakkuk",             "habakkuk",          3,  "source"),
    (50, "Zephaniah",            "zephaniah",         3,  "source"),
    (51, "Haggai",               "haggai",            2,  "source"),
    (52, "Zechariah",            "zechariah",        14,  "source"),
    (53, "Malachi",              "malachi",           4,  "source"),
    (54, "Josippon",             "josippon",          0,  "none"),
    (55, "Matthew",              "matthew",          28,  "source"),
    (56, "Mark",                 "mark",             16,  "source"),
    (57, "Luke",                 "luke",             24,  "source"),
    (58, "John",                 "john",             21,  "source"),
    (59, "Acts",                 "acts",             28,  "source"),
    (60, "Romans",               "romans",           16,  "source"),
    (61, "1 Corinthians",        "1-corinthians",    16,  "source"),
    (62, "2 Corinthians",        "2-corinthians",    13,  "source"),
    (63, "Galatians",            "galatians",         6,  "source"),
    (64, "Ephesians",            "ephesians",         6,  "source"),
    (65, "Philippians",          "philippians",       4,  "source"),
    (66, "Colossians",           "colossians",        4,  "source"),
    (67, "1 Thessalonians",      "1-thessalonians",   5,  "source"),
    (68, "2 Thessalonians",      "2-thessalonians",   3,  "source"),
    (69, "1 Timothy",            "1-timothy",         6,  "source"),
    (70, "2 Timothy",            "2-timothy",         4,  "source"),
    (71, "Titus",                "titus",             3,  "source"),
    (72, "Philemon",             "philemon",          1,  "source"),
    (73, "Hebrews",              "hebrews",          13,  "source"),
    (74, "James",                "james",             5,  "source"),
    (75, "1 Peter",              "1-peter",           5,  "source"),
    (76, "2 Peter",              "2-peter",           3,  "source"),
    (77, "1 John",               "1-john",            5,  "source"),
    (78, "2 John",               "2-john",            1,  "source"),
    (79, "3 John",               "3-john",            1,  "source"),
    (80, "Jude",                 "jude",              1,  "source"),
    (81, "Revelation",           "revelation",       22,  "source"),
    (82, "1st Book of the Covenant", "1-covenant",    0,  "none"),
    (83, "2nd Book of the Covenant", "2-covenant",    0,  "none"),
    (84, "Sirate Tsion",         "sirate-tsion",      0,  "none"),
    (85, "Te'ezaz",              "teezaz",            0,  "none"),
    (86, "Gitzew",               "gitzew",            0,  "none"),
    (87, "Abtilis",              "abtilis",           0,  "none"),
    (88, "Didascalia",           "didascalia",        0,  "none"),
    (89, "Qalementos",           "qalementos",        0,  "none"),
]

books = [
    {"order": o, "title": t, "slug": s, "chapters": c, "tier": tier}
    for o, t, s, c, tier in BOOKS
]
with open("manifest.json", "w") as f:
    json.dump({"books": books}, f, indent=2)

total = sum(b["chapters"] for b in books)
by_tier = {}
for b in books:
    by_tier.setdefault(b["tier"], [0, 0])
    by_tier[b["tier"]][0] += 1
    by_tier[b["tier"]][1] += b["chapters"]
print(f"{len(books)} books, {total} renderable chapters")
for tier, (nb, nc) in sorted(by_tier.items()):
    print(f"  {tier:<10} {nb:>2} books  {nc:>5} chapters")
