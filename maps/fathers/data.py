"""Content of the map after Genesis 50: the journeys of Abraham, Isaac and Jacob.
Coordinates are (lon, lat). Names and quotations follow the project's rendering
of Genesis. `sure=False` marks a site whose location is not known; it is drawn
as an open ring and placed by what the text says."""

# ---------------------------------------------------------------- projection and views
LON0, LAT1, COSLAT = 29.8, 38.6, 33.0
BBOX = (29.8, 27.3, 48.3, 38.6)
ASPECT = 1.45
VIEW_J = (30.2, 47.8, 38.05)     # west, east, top
VIEW_L = (31.9, 39.34, 33.78)    # tall enough for Genesis 14, from Hobah to El-paran

# ---------------------------------------------------------------- places
P = {}
def place(pid, name, lon, lat, sure=True, pos="e", tier=2, note=""):
    P[pid] = dict(id=pid, name=name, lon=lon, lat=lat, sure=sure, pos=pos, tier=tier, note=note)

place("ur", "Ur of the Chaldeans", 46.103, 30.963, pos="w", tier=1,
      note="Usually placed at Tell el-Muqayyar, on the lower Euphrates.")
place("harran", "Harran", 39.03, 36.865, pos="e", tier=1,
      note="Spelled *Harran* to keep the town apart from Abram's brother Haran.")
place("damascus", "Damascus", 36.29, 33.51, pos="e", tier=1)
place("shechem", "Shechem", 35.285, 32.213, pos="w", tier=1, note="The oak of Moreh stood here {Genesis 12:6}.")
place("bethel", "Bethel", 35.235, 31.93, pos="w", tier=1, note="Earlier Luz {Genesis 28:19}.")
place("ai", "Ai", 35.26, 31.917, False, pos="e", tier=3, note="Usually placed at et-Tell; disputed.")
place("hebron", "Hebron", 35.10, 31.53, pos="w", tier=1,
      note="Kiriath-arba, with the oaks of Mamre {Genesis 13:18} and the cave of Machpelah {Genesis 23:19}.")
place("sodom", "Sodom", 35.42, 31.15, False, pos="w", tier=2,
      note="Not located. Genesis sets the cities of the plain by the Valley of Siddim, *that is the Salt Sea* {Genesis 14:3}.")
place("zoar", "Zoar", 35.47, 31.03, False, pos="e", tier=3, note="Also called Bela {Genesis 14:2}; not located for certain.")
place("salem", "Salem", 35.235, 31.777, False, pos="e", tier=3,
      note="Melchizedek's city. *His tent is in Salem, His dwelling place in Zion* {Psalm 76:2}.")
place("moriah", "Moriah", 35.235, 31.777, False, pos="e", tier=3,
      note="*The land of Moriah* {Genesis 22:2}. Solomon built the house of the LORD *in Jerusalem on Mount Moriah* {2 Chronicles 3:1}.")
place("dan", "Dan", 35.652, 33.249, pos="w", tier=2, note="Called Leshem until the sons of Dan took it and renamed it {Joshua 19:47}; Genesis uses the later name.")
place("hobah", "Hobah", 36.35, 33.66, False, pos="e", tier=3,
      note="*To the left of Damascus* {Genesis 14:15}: facing east, the left hand is north.")
place("ashteroth", "Ashteroth-karnaim", 36.03, 32.82, pos="e", tier=3)
place("ham", "Ham", 35.76, 32.54, False, pos="e", tier=3, note="Not located for certain.")
place("shaveh", "Shaveh-kiriathaim", 35.74, 31.62, False, pos="e", tier=3, note="Kiriathaim, in later Moab; not located.")
place("elparan", "El-paran", 35.00, 29.56, False, pos="e", tier=3, note="*Which is by the wilderness* {Genesis 14:6}; not located.")
place("kadesh", "Kadesh", 34.43, 30.63, pos="w", tier=2, note="Also called En-mishpat {Genesis 14:7}.")
place("hazazon", "Hazazon-tamar", 35.39, 31.46, False, pos="e", tier=3,
      note="Placed at En-gedi: of Hazazon-tamar the Chronicler adds, *that is, En-gedi* {2 Chronicles 20:2}.")
place("shur", "Shur", 33.60, 30.85, False, pos="s", tier=3, note="*Shur, which faces Egypt* {Genesis 25:18}; not located.")
place("lahairoi", "Beer-lahai-roi", 34.62, 30.78, False, pos="e", tier=3,
      note="*Between Kadesh and Bered* {Genesis 16:14}; not located.")
place("gerar", "Gerar", 34.60, 31.38, False, pos="w", tier=2, note="Not located for certain.")
place("beersheba", "Beersheba", 34.84, 31.245, pos="e", tier=1)
place("rehoboth", "Rehoboth", 34.66, 31.07, False, pos="w", tier=3, note="Isaac's third well {Genesis 26:22}; not located for certain.")
place("galeed", "Galeed, Mizpah", 35.80, 32.38, False, pos="e", tier=3, note="The heap of witness {Genesis 31:48}; not located.")
place("mahanaim", "Mahanaim", 35.66, 32.24, False, pos="n", tier=3, note="Not located for certain.")
place("penuel", "Penuel", 35.74, 32.18, False, pos="e", tier=3, note="Also spelled Peniel {Genesis 32:30}; not located for certain.")
place("succoth", "Succoth", 35.62, 32.19, False, pos="s", tier=3, note="Usually placed at Tell Deir Alla.")
place("bethlehem", "Bethlehem", 35.20, 31.705, pos="w", tier=3, note="*Ephrath — that is Bethlehem* {Genesis 35:19}.")
place("dothan", "Dothan", 35.24, 32.41, pos="w", tier=3)
place("atad", "the threshing floor of the Bramble", 35.57, 31.88, False, pos="e", tier=3,
      note="Abel-mizraim, *across the Jordan* {Genesis 50:11}; not located.")
place("rameses", "Rameses", 31.83, 30.80, pos="w", tier=2, note="*The land of Rameses* {Genesis 47:11}, in Goshen.")

# ---------------------------------------------------------------- stages
# cam: "j" Ur to Egypt, "l" the land.  Caption refs in {Book c:v}.
STAGES = [
 dict(key="ur", title="Out of Ur", when="Genesis 11", cam="j", act=["ur", "harran"],
      text="Terah took Abram, Lot and Sarai and went out “from Ur of the Chaldeans to go to the land of Canaan,” but they came only as far as Harran and settled there {Genesis 11:31}. Terah died in Harran {Genesis 11:32}."),
 dict(key="canaan", title="To the land I will show you", when="Abram is 75", cam="j", act=["harran", "shechem", "bethel", "ai"],
      text="“Go, for yourself, from your land, and from your kindred, and from your father's house, to the land that I will show you” {Genesis 12:1}. Abram was seventy-five years old when he went out from Harran {Genesis 12:4}. At Shechem the LORD said, “To your seed I will give this land” {Genesis 12:7}, and Abram built altars there and between Bethel and Ai, then journeyed toward the Negev {Genesis 12:8} {Genesis 12:9}."),
 dict(key="egypt", title="Down to Egypt and back", when="Genesis 12–13", cam="j", act=["bethel"],
      text="A famine drove Abram down to Egypt {Genesis 12:10}, and Pharaoh sent him away with his wife and all that was his {Genesis 12:20}. He went back up through the Negev to Bethel, *to the place where his tent had been at the beginning* {Genesis 13:3}."),
 dict(key="lot", title="Lot chooses the plain", when="Genesis 13", cam="l", act=["bethel", "sodom", "hebron"],
      text="Lot saw that the plain of the Jordan was “well watered… like the garden of the LORD,” chose it, and pitched his tent as far as Sodom {Genesis 13:10} {Genesis 13:12}. The LORD told Abram to look “northward and southward and eastward and seaward”: “all the land that you see, to you I will give it” {Genesis 13:14} {Genesis 13:15}. Abram settled by the oaks of Mamre in Hebron {Genesis 13:18}."),
 dict(key="kings", title="The war of the kings", when="Genesis 14", cam="l",
      act=["ashteroth", "ham", "shaveh", "elparan", "kadesh", "hazazon", "sodom", "dan", "hobah", "damascus", "salem"],
      text="Four kings, among them the kings of Shinar and Elam {Genesis 14:1}, struck “the Rephaim in Ashteroth-karnaim, and the Zuzim in Ham, and the Emim in Shaveh-kiriathaim, and the Horite in their hill country of Seir” {Genesis 14:5} {Genesis 14:6}, turned back to Kadesh and Hazazon-tamar {Genesis 14:7}, and routed the kings of the plain in the Valley of Siddim {Genesis 14:10}. They took Lot. Abram pursued them as far as Dan, and on to Hobah, “to the left of Damascus” {Genesis 14:14} {Genesis 14:15}. Coming back, he was met by Melchizedek king of Salem with bread and wine {Genesis 14:18}."),
 dict(key="covenant", title="The covenant between the pieces", when="Genesis 15", cam="j", act=["ur", "hebron"],
      text="“I am the LORD, who brought you out from Ur of the Chaldeans, to give you this land” {Genesis 15:7}. His seed would be guests in a land not theirs four hundred years {Genesis 15:13}, and return in the fourth generation {Genesis 15:16}. “To your seed I have given this land, from the river of Egypt to the great river, the river Euphrates,” with its peoples, the Rephaim among them {Genesis 15:18} {Genesis 15:20}."),
 dict(key="hagar", title="Hagar at the well", when="Genesis 16", cam="l", act=["shur", "lahairoi"],
      text="Hagar fled from Sarai, and the messenger of the LORD found her “by the spring on the way to Shur” {Genesis 16:7}. The well was called Beer-lahai-roi; “it lies between Kadesh and Bered” {Genesis 16:14}."),
 dict(key="sodom", title="Sodom and Zoar", when="Genesis 18–19", cam="l", act=["hebron", "sodom", "zoar"],
      text="The LORD appeared to Abraham among the oaks of Mamre {Genesis 18:1}. Lot escaped to Zoar {Genesis 19:23}, and the LORD rained sulfur and fire on Sodom and Gomorrah {Genesis 19:24}. Abraham looked down toward Sodom and “saw the smoke of the land going up like the smoke of a kiln” {Genesis 19:28}. Lot's sons were the fathers of Moab and of the sons of Ammon {Genesis 19:37} {Genesis 19:38}."),
 dict(key="gerar", title="Gerar and Beersheba", when="Genesis 20–21", cam="l", act=["gerar", "beersheba"],
      text="Abraham settled between Kadesh and Shur and lived as a guest in Gerar {Genesis 20:1}. Isaac was born {Genesis 21:2}. Hagar and Ishmael wandered in the wilderness of Beersheba {Genesis 21:14}, and Ishmael settled in the wilderness of Paran {Genesis 21:21}. Abraham and Abimelech swore an oath at the well, “therefore that place was called Beersheba” {Genesis 21:31}."),
 dict(key="moriah", title="The land of Moriah", when="Genesis 22", cam="l", act=["moriah", "beersheba"],
      text="“Go, for yourself, to the land of Moriah, and bring him up there as a burnt offering” {Genesis 22:2}. On the third day Abraham saw the place from far off {Genesis 22:4}; afterward he went back and settled in Beersheba {Genesis 22:19}."),
 dict(key="machpelah", title="The cave of Machpelah", when="Genesis 23–25", cam="l", act=["hebron"],
      text="Sarah died in Kiriath-arba, that is Hebron {Genesis 23:2}, and Abraham bought the field and the cave of Machpelah “as a holding for a grave” {Genesis 23:20}, the first ground of the promised land he owned. Isaac and Ishmael buried Abraham there {Genesis 25:9}."),
 dict(key="rebekah", title="A wife from Aram-naharaim", when="Genesis 24", cam="j", act=["harran", "lahairoi"],
      text="Abraham's servant took ten camels and went “to Aram-naharaim, to the city of Nahor” {Genesis 24:10}. Rebekah came back with him to Isaac, who had come from the way to Beer-lahai-roi and was living in the Negev {Genesis 24:62}."),
 dict(key="wells", title="Isaac's wells", when="Genesis 26", cam="l", act=["gerar", "rehoboth", "beersheba"],
      text="In another famine Isaac went to Gerar {Genesis 26:1}. The herdsmen of Gerar quarreled over his wells, Esek and Sitnah, until at Rehoboth he said, “For now the LORD has made room for us” {Genesis 26:20} {Genesis 26:22}. At Beersheba the LORD appeared to him {Genesis 26:23} {Genesis 26:24}."),
 dict(key="jacobgoes", title="Jacob flees to Harran", when="Genesis 28–31", cam="j", act=["beersheba", "bethel", "harran"],
      text="Jacob went out from Beersheba toward Harran {Genesis 28:10}, and on the way slept with a stone at his head at the place he called Bethel {Genesis 28:19}. He served Laban twenty years: “fourteen years for your two daughters and six years for your flock” {Genesis 31:41}."),
 dict(key="jacomes", title="Jacob comes home", when="Genesis 31–33", cam="l", act=["galeed", "mahanaim", "penuel", "succoth", "shechem"],
      text="Jacob crossed the River and set his face toward the hill country of Gilead {Genesis 31:21}, where Laban overtook him and they set up the heap called Galeed and Mizpah {Genesis 31:48} {Genesis 31:49}. He named Mahanaim {Genesis 32:2}, crossed the ford of the Jabbok, wrestled at Peniel, and limped on {Genesis 32:22} {Genesis 32:30} {Genesis 32:31}. He built a house at Succoth, and came to Shechem and bought a field there {Genesis 33:17} {Genesis 33:19}."),
 dict(key="hebron2", title="Bethel, Ephrath and Mamre", when="Genesis 35–36", cam="l", act=["bethel", "bethlehem", "hebron"],
      text="At Bethel Jacob built the altar he had been told to build {Genesis 35:1} {Genesis 35:7}. Rachel died on the road and was buried “on the road to Ephrath — that is Bethlehem” {Genesis 35:19}. Jacob came to Isaac at Mamre, and Esau and Jacob buried their father {Genesis 35:27} {Genesis 35:29}. Esau settled in the hill country of Seir {Genesis 36:8}."),
 dict(key="joseph", title="Joseph sold into Egypt", when="Genesis 37", cam="l", act=["hebron", "shechem", "dothan"],
      text="Jacob sent Joseph from the valley of Hebron to Shechem, and he found his brothers at Dothan {Genesis 37:14} {Genesis 37:17}. They sold him to a caravan of Ishmaelites coming from Gilead, taking gum, balm and ladanum down to Egypt {Genesis 37:25} {Genesis 37:28}."),
 dict(key="down", title="Seventy souls go down to Egypt", when="Genesis 46–47", cam="j", act=["beersheba", "rameses"],
      text="Israel set out with all that was his and offered sacrifices at Beersheba {Genesis 46:1}. “All the souls of the house of Jacob coming to Egypt: seventy” {Genesis 46:27}. Joseph met his father in Goshen {Genesis 46:29}, and settled them “in the land of Rameses” {Genesis 47:11}."),
 dict(key="burial", title="Carried up to Machpelah", when="Genesis 50", cam="j", act=["atad", "hebron", "rameses"],
      text="“Do not bury me, please, in Egypt” {Genesis 47:29}. Jacob's sons carried him up, mourned seven days at the threshing floor of the Bramble across the Jordan {Genesis 50:10}, and buried him in the cave of Machpelah {Genesis 50:13}. Joseph made the sons of Israel swear: “you shall carry my bones up from here” {Genesis 50:25}. The map after Joshua 24 follows them out."),
]

# ---------------------------------------------------------------- route segments
# kind: camp (the family's moves), march (war), spies (others' journeys)
SEGS = [
 ("ur", "camp", ["ur", (45.0, 31.9), (43.6, 33.0), (42.0, 34.4), (40.6, 35.1), (39.6, 35.9), "harran"]),
 ("canaan", "camp", ["harran", (38.2, 36.3), (37.15, 36.15), (36.75, 35.15), (36.45, 34.3), "damascus",
                     (35.7, 32.95), "shechem", "bethel", (35.0, 31.5), (34.88, 31.15)]),
 ("egypt", "camp", [(34.88, 31.15), (34.4, 31.0), (33.6, 31.0), (32.6, 30.9), (31.9, 30.85)]),
 ("egypt", "camp", [(31.9, 30.85), (32.7, 30.75), (33.8, 30.8), (34.7, 31.0), (35.05, 31.45), "bethel"]),
 ("lot", "spies", ["bethel", (35.45, 31.85), (35.48, 31.5), "sodom"]),
 ("lot", "camp", ["bethel", (35.18, 31.75), "hebron"]),
 ("kings", "march", [(38.9, 33.4), (36.4, 33.1), "ashteroth", "ham", "shaveh", (35.65, 30.6), "elparan",
                     (34.7, 30.2), "kadesh", (35.0, 31.0), "hazazon", "sodom"]),
 ("kings", "march", ["sodom", (35.5, 31.9), (35.62, 32.8), "dan", "hobah"]),
 ("kings", "march", ["hebron", (35.2, 31.9), (35.5, 32.6), "dan"]),
 ("kings", "return", ["hobah", (35.7, 33.0), (35.4, 32.2), "salem"]),
 ("hagar", "spies", ["hebron", (34.6, 31.05), "shur"]),
 ("hagar", "spies", ["shur", (34.1, 30.85), "lahairoi"]),
 ("sodom", "spies", ["sodom", "zoar", (35.58, 31.2)]),
 ("gerar", "camp", ["hebron", (34.85, 31.45), "gerar", "beersheba"]),
 ("moriah", "camp", ["beersheba", (35.0, 31.45), "moriah"]),
 ("moriah", "return", ["moriah", (35.05, 31.5), "beersheba"]),
 ("machpelah", "camp", ["beersheba", "hebron"]),
 ("rebekah", "spies", ["hebron", (36.2, 33.4), (36.9, 35.2), "harran"]),
 ("rebekah", "spies", ["harran", (37.0, 35.0), (36.0, 33.2), (35.1, 31.6), "lahairoi"]),
 ("wells", "camp", ["lahairoi", "gerar", "rehoboth", "beersheba"]),
 ("jacobgoes", "camp", ["beersheba", (35.1, 31.6), "bethel", (35.6, 32.6), (36.3, 33.6), (36.8, 35.1), (37.9, 36.3), "harran"]),
 ("jacomes", "camp", ["harran", (37.9, 36.1), (37.0, 34.4), (36.3, 33.2), (35.95, 32.6), "galeed", "mahanaim",
                      "penuel", "succoth", "shechem"]),
 ("hebron2", "camp", ["shechem", "bethel", "bethlehem", "hebron"]),
 ("joseph", "spies", ["hebron", (35.25, 31.95), "shechem", "dothan"]),
 ("joseph", "spies", ["dothan", (35.05, 32.15), (34.9, 31.7), (34.6, 31.3), (34.0, 30.98), (33.0, 30.92), (32.0, 30.9)]),
 ("down", "camp", ["hebron", "beersheba", (34.3, 31.0), (33.2, 30.95), "rameses"]),
 ("burial", "camp", ["rameses", (33.0, 30.85), (34.6, 30.4), (35.25, 30.7), (35.65, 31.25), "atad", (35.3, 31.65), "hebron"]),
]

# Abram's view (Genesis 13:14), from between Bethel and Ai: north, south, east, toward the sea.
SIGHT_FROM = (35.25, 31.92)
SIGHT = [(35.25, 33.05), (35.25, 30.85), (36.35, 31.92), (34.55, 31.92)]
SIGHT_STAGE = "lot"

# "From the river of Egypt to the great river, the river Euphrates" (Genesis 15:18).
# Genesis has *nehar*, a river, so the line starts at the Nile, not the Brook of Egypt (Numbers 34:5).
PROMISE = [(31.676, 31.259), (32.6, 30.95), (33.8, 31.05), (34.85, 31.75), (35.45, 33.0), (36.45, 34.6),
           (37.3, 35.7), (38.08, 36.166)]
PROMISE_STAGE = "covenant"

# ---------------------------------------------------------------- water, mountains, labels
DEAD_SEA = [(35.50, 31.772), (35.535, 31.768), (35.565, 31.745), (35.578, 31.70),
            (35.588, 31.62), (35.588, 31.52), (35.578, 31.43), (35.565, 31.35),
            (35.545, 31.335), (35.50, 31.33), (35.465, 31.315), (35.445, 31.29),
            (35.46, 31.265), (35.505, 31.255), (35.53, 31.235), (35.53, 31.17),
            (35.515, 31.10), (35.49, 31.055), (35.46, 31.04), (35.43, 31.07),
            (35.41, 31.13), (35.395, 31.21), (35.385, 31.30), (35.39, 31.40),
            (35.395, 31.47), (35.42, 31.56), (35.45, 31.65), (35.475, 31.72)]
WADIS = [
 ("Jabbok", [(35.555, 32.105), (35.62, 32.17), (35.70, 32.195), (35.80, 32.19), (35.88, 32.17),
             (35.98, 32.135), (36.06, 32.09)], 3),
]
RIVERS_EXTRA = [[(39.05, 36.86), (39.07, 36.5), (39.05, 36.2), (39.02, 35.95)]]   # the Balikh, Harran's river

MOUNTAINS_J = [(31.5, 37.3, 15), (32.6, 37.1, 15), (33.7, 36.95, 15), (34.8, 37.25, 15), (35.9, 37.55, 15), (37.0, 37.8, 15), (38.3, 37.85, 15), (39.6, 37.7, 15), (40.9, 37.75, 15), (42.1, 37.6, 15), (43.3, 37.45, 15), (44.4, 37.2, 15), (45.2, 36.5, 15), (45.9, 35.7, 15), (46.4, 34.8, 15), (46.9, 34.0, 15), (47.5, 33.2, 15), (48.0, 32.4, 15), (36.35, 36.75, 15), (36.25, 34.1, 15), (36.0, 33.6, 15), (36.55, 34.5, 15), (33.95, 28.55, 15), (34.25, 28.9, 15), (33.6, 28.85, 15), (34.0, 29.3, 15), (35.55, 30.35, 15), (35.6, 30.9, 15), (35.25, 31.75, 15), (35.3, 32.25, 15)]
MOUNTAINS_L = [(35.86, 33.42, 3.4), (35.12, 31.48, 2), (35.18, 31.66, 2), (35.22, 31.99, 1.8), (35.30, 32.35, 1.8),
               (35.52, 30.10, 2.4), (35.58, 30.50, 2.4), (35.63, 30.88, 2.2), (35.76, 32.30, 2), (35.80, 32.45, 1.8),
               (36.20, 33.70, 2.6), (36.40, 33.90, 2.6)]

# text, lon, lat, class, from-stage, to-stage, rotate[, view]
LABELS = [
 ("EGYPT", 31.05, 29.9, "nation", None, None, 0),
 ("Goshen", 31.72, 30.55, "region", "down", None, 0),
 ("CANAAN", 35.0, 31.15, "nation", "canaan", "covenant", 0, "j"),
 ("the Negev", 34.75, 30.98, "region", "canaan", None, 0),
 ("SHINAR", 44.4, 32.6, "nation", "kings", None, 0, "j"),
 ("ELAM", 47.35, 32.15, "nation", "kings", None, 0, "j"),
 ("ARAM-NAHARAIM", 40.4, 36.3, "nation", "rebekah", None, 0, "j"),
 ("Paddan-aram", 39.6, 36.55, "region", "jacobgoes", None, 0, "j"),
 ("GILEAD", 36.2, 32.52, "nation", "jacomes", None, 0, "l"),
 ("Seir", 35.55, 30.30, "region", "kings", None, 0, "l"),
 ("EDOM", 35.72, 30.55, "nation", "hebron2", None, 0, "l"),
 ("MOAB", 35.80, 31.25, "nation", "sodom", None, 0, "l"),
 ("AMMON", 36.20, 32.0, "nation", "sodom", None, 0, "l"),
 ("land of the Philistines", 34.38, 31.45, "region", "gerar", None, 0, "l"),
 ("wilderness of Paran", 34.25, 29.9, "region", "gerar", "gerar", 0),
 ("Valley of Siddim", 35.66, 31.12, "region", "kings", "kings", 0, "l"),
 ("the plain of the Jordan", 35.62, 31.95, "region", "lot", "sodom", -80, "l"),
 ("THE GREAT SEA", 33.4, 33.4, "sea", None, None, 0, "j"),
 ("THE GREAT SEA", 34.25, 33.0, "sea", None, None, 0, "l"),
 ("Salt Sea", 35.49, 31.64, "water-s", None, None, -84, "l"),
 ("Euphrates", 42.7, 34.25, "river", None, None, -38),
 ("Tigris", 44.35, 34.6, "river", None, None, -50),
 ("Nile", 31.22, 29.40, "river", None, None, -80),
 ("Jordan", 35.565, 32.30, "river", None, None, -86, "l"),
 ("from the river of Egypt to the great river", 35.0, 32.95, "promise", "covenant", "covenant", -52, "j"),
]

# The peoples the kings struck (Genesis 14:5–6); three of them are giant peoples (Deuteronomy 2:10–11, 20).
GIANT_LABELS = [
 # text, lon, lat, from, to, kind, view, active stages
 ("Rephaim", 36.03, 32.92, "kings", "kings", "on", "l", ["kings"]),
 ("Zuzim", 35.90, 32.40, "kings", "kings", "on", "l", ["kings"]),
 ("Emim", 35.88, 31.67, "kings", "kings", "on", "l", ["kings"]),
 ("Horites", 35.88, 30.55, "kings", "kings", "name", "l", ["kings"]),
]
GIANT_TOWNS = [("ashteroth", "on", "kings", "kings"), ("ham", "on", "kings", "kings"), ("shaveh", "on", "kings", "kings")]

# ---------------------------------------------------------------- page text
CART = "The Journeys of the Fathers"
FROM = "Ur"
TITLE = "The Journeys of the Fathers"
ORDER = 2
OUT = "books/1-genesis/S2.md"
LINK_NOTE = "Map of the journeys of Abraham, Isaac and Jacob, from Ur to Egypt"
KEY = """      <li><svg viewBox="0 0 30 14"><path d="M2,7H28" stroke="#962a1b" stroke-width="3" stroke-linecap="round"/></svg>The family's journeys</li>
      <li><svg viewBox="0 0 30 14"><path d="M2,7H28" stroke="#b0442c" stroke-width="1.8" stroke-dasharray="6 3"/></svg>War: the kings and Abram's pursuit</li>
      <li><svg viewBox="0 0 30 14"><path d="M2,7H28" stroke="#6b5336" stroke-width="1.7" stroke-dasharray="1.5 3.5" stroke-linecap="round"/></svg>Other journeys: Lot, Hagar, the servant, Joseph</li>
      <li><svg viewBox="0 0 30 14"><circle cx="15" cy="7" r="3" fill="#3a2a1a"/></svg>Site known</li>
      <li><svg viewBox="0 0 30 14"><circle cx="15" cy="7" r="2.6" fill="#f4ead0" stroke="#3a2a1a" stroke-width="1.4"/></svg>Site not located; placed by the text</li>
      <li><svg viewBox="0 0 30 14"><circle cx="15" cy="7" r="5.5" fill="#9c1f3c" opacity=".85"/><circle cx="15" cy="7" r="2.3" fill="#3a2a1a"/></svg>A town of the giant peoples (Genesis 14:5)</li>
      <li><svg viewBox="0 0 30 14"><path d="M2,7H28" stroke="#a8801f" stroke-width="2.4" stroke-dasharray="9 4" stroke-opacity=".75"/></svg>The land promised (Genesis 15:18)</li>"""
SRC = """Coastlines, rivers and lakes: Natural Earth (public domain). Many places in Genesis have never been found; where a site is not known it is placed by what the text says. Quotations are from this rendering."""
