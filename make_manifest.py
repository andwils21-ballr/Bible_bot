"""One-time generator for manifest.json — the canon ledger the render Routine reads."""
import json

# (order, title, slug, chapters, tier)
#   tier "primary"   - I can work from the Hebrew/Aramaic/Greek text itself
#   tier "secondary" - no source language access; work from established English translations
#   tier "none"      - no usable source text available; emit a NEED SOURCE stub
BOOKS = [
    (1,  "Genesis",              "genesis",          50,  "primary"),
    (2,  "Exodus",               "exodus",           40,  "primary"),
    (3,  "Leviticus",            "leviticus",        27,  "primary"),
    (4,  "Numbers",              "numbers",          36,  "primary"),
    (5,  "Deuteronomy",          "deuteronomy",      34,  "primary"),
    (6,  "Joshua",               "joshua",           24,  "primary"),
    (7,  "Judges",               "judges",           21,  "primary"),
    (8,  "Ruth",                 "ruth",              4,  "primary"),
    (9,  "1 Samuel",             "1-samuel",         31,  "primary"),
    (10, "2 Samuel",             "2-samuel",         24,  "primary"),
    (11, "1 Kings",              "1-kings",          22,  "primary"),
    (12, "2 Kings",              "2-kings",          25,  "primary"),
    (13, "1 Chronicles",         "1-chronicles",     29,  "primary"),
    (14, "2 Chronicles",         "2-chronicles",     36,  "primary"),
    (15, "Jubilees",             "jubilees",         50,  "secondary"),
    (16, "1 Enoch",              "1-enoch",         108,  "secondary"),
    (17, "Ezra",                 "ezra",             10,  "primary"),
    (18, "Nehemiah",             "nehemiah",         13,  "primary"),
    (19, "Ezra Sutuel",          "ezra-sutuel",      16,  "secondary"),
    (20, "Tobit",                "tobit",            14,  "primary"),
    (21, "Judith",               "judith",           16,  "primary"),
    (22, "Esther",               "esther",           16,  "primary"),
    (23, "1 Meqabyan",           "1-meqabyan",       36,  "secondary"),
    (24, "2 Meqabyan",           "2-meqabyan",       21,  "secondary"),
    (25, "3 Meqabyan",           "3-meqabyan",       10,  "secondary"),
    (26, "Job",                  "job",              42,  "primary"),
    (27, "Psalms",               "psalms",          151,  "primary"),
    (28, "Proverbs",             "proverbs",         24,  "primary"),
    (29, "Reproof (Tegsat)",     "reproof-tegsat",    7,  "primary"),
    (30, "Ecclesiastes",         "ecclesiastes",     12,  "primary"),
    (31, "Song of Songs",        "song-of-songs",     8,  "primary"),
    (32, "Wisdom of Solomon",    "wisdom-of-solomon", 19, "primary"),
    (33, "Sirach",               "sirach",           51,  "primary"),
    (34, "Isaiah",               "isaiah",           66,  "primary"),
    (35, "Jeremiah",             "jeremiah",         52,  "primary"),
    (36, "Lamentations",         "lamentations",      5,  "primary"),
    (37, "Baruch",               "baruch",            5,  "primary"),
    (38, "Letter of Jeremiah",   "letter-of-jeremiah",1,  "primary"),
    (39, "4 Baruch",             "4-baruch",          9,  "secondary"),
    (40, "Ezekiel",              "ezekiel",          48,  "primary"),
    (41, "Daniel",               "daniel",           14,  "primary"),
    (42, "Hosea",                "hosea",            14,  "primary"),
    (43, "Amos",                 "amos",              9,  "primary"),
    (44, "Micah",                "micah",             7,  "primary"),
    (45, "Joel",                 "joel",              3,  "primary"),
    (46, "Obadiah",              "obadiah",           1,  "primary"),
    (47, "Jonah",                "jonah",             4,  "primary"),
    (48, "Nahum",                "nahum",             3,  "primary"),
    (49, "Habakkuk",             "habakkuk",          3,  "primary"),
    (50, "Zephaniah",            "zephaniah",         3,  "primary"),
    (51, "Haggai",               "haggai",            2,  "primary"),
    (52, "Zechariah",            "zechariah",        14,  "primary"),
    (53, "Malachi",              "malachi",           4,  "primary"),
    (54, "Josippon",             "josippon",          0,  "none"),
    (55, "Matthew",              "matthew",          28,  "primary"),
    (56, "Mark",                 "mark",             16,  "primary"),
    (57, "Luke",                 "luke",             24,  "primary"),
    (58, "John",                 "john",             21,  "primary"),
    (59, "Acts",                 "acts",             28,  "primary"),
    (60, "Romans",               "romans",           16,  "primary"),
    (61, "1 Corinthians",        "1-corinthians",    16,  "primary"),
    (62, "2 Corinthians",        "2-corinthians",    13,  "primary"),
    (63, "Galatians",            "galatians",         6,  "primary"),
    (64, "Ephesians",            "ephesians",         6,  "primary"),
    (65, "Philippians",          "philippians",       4,  "primary"),
    (66, "Colossians",           "colossians",        4,  "primary"),
    (67, "1 Thessalonians",      "1-thessalonians",   5,  "primary"),
    (68, "2 Thessalonians",      "2-thessalonians",   3,  "primary"),
    (69, "1 Timothy",            "1-timothy",         6,  "primary"),
    (70, "2 Timothy",            "2-timothy",         4,  "primary"),
    (71, "Titus",                "titus",             3,  "primary"),
    (72, "Philemon",             "philemon",          1,  "primary"),
    (73, "Hebrews",              "hebrews",          13,  "primary"),
    (74, "James",                "james",             5,  "primary"),
    (75, "1 Peter",              "1-peter",           5,  "primary"),
    (76, "2 Peter",              "2-peter",           3,  "primary"),
    (77, "1 John",               "1-john",            5,  "primary"),
    (78, "2 John",               "2-john",            1,  "primary"),
    (79, "3 John",               "3-john",            1,  "primary"),
    (80, "Jude",                 "jude",              1,  "primary"),
    (81, "Revelation",           "revelation",       22,  "primary"),
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
