"""Content of the journey map: places, stages, territories, giants.
Coordinates are (lon, lat). Place names and quoted words follow the project's
rendering. `sure=False` marks a site whose location is not known; it is drawn as
an open ring and placed by the directions the text gives."""

# ---------------------------------------------------------------- places
# id: (name, lon, lat, sure, label position, tier, note)
#  tier 1: label shown from first appearance on; 2: label when active or zoomed in;
#  3: label only when active.
P = {}
def place(pid, name, lon, lat, sure=True, pos="e", tier=2, note=""):
    P[pid] = dict(id=pid, name=name, lon=lon, lat=lat, sure=sure, pos=pos, tier=tier, note=note)

# Egypt to the sea
place("rameses", "Rameses", 31.83, 30.80, pos="w", tier=1,
      note="Pi-Ramesses, the Delta capital of Ramesses II, at Qantir.")
place("succoth", "Succoth", 32.10, 30.55, False, pos="sw", tier=3,
      note="Usually placed at Tell el-Maskhuta in the Wadi Tumilat.")
place("etham", "Etham", 32.29, 30.67, False, pos="ne", tier=3,
      note="Not located. It lay “at the edge of the wilderness” {Exodus 13:20}.")
place("pihahiroth", "Pi-hahiroth", 32.27, 30.43, False, pos="w", tier=3,
      note="Not located, nor are Migdol and Baal-zephon {Exodus 14:2}.")
place("crossing", "the crossing", 32.43, 30.37, False, pos="s", tier=3,
      note="Where the sea was crossed is not known. Proposals run from the coastal lagoons in the north to the head of the Gulf of Suez.")
place("marah", "Marah", 32.92, 29.62, False, pos="e", tier=3, note="Not located.")
place("elim", "Elim", 33.03, 29.32, False, pos="e", tier=3,
      note="Not located; often placed at the springs of Wadi Gharandel.")
place("seacamp", "by the Sea of Reeds", 33.10, 29.06, False, pos="e", tier=3,
      note="An unnamed camp by the Sea of Reeds {Numbers 33:10}.")
place("dophkah", "Dophkah", 33.38, 29.03, False, pos="ne", tier=3, note="Not located.")
place("alush", "Alush", 33.55, 28.86, False, pos="ne", tier=3, note="Not located.")
place("rephidim", "Rephidim", 33.66, 28.70, False, pos="w", tier=3,
      note="Not located; often placed in the Wadi Feiran.")
place("sinai", "Mount Sinai", 33.975, 28.54, False, pos="se", tier=1,
      note="The traditional mountain, Jebel Musa. Other candidates stand in northern Sinai and in Arabia; the text does not fix the place.")
# Sinai to Kadesh
place("kibroth", "Kibroth-hattaavah", 34.21, 28.76, False, pos="e", tier=3, note="Not located.")
place("hazeroth", "Hazeroth", 34.43, 28.90, False, pos="e", tier=3,
      note="Not located; often placed at the oasis of Ain Khadra.")
place("kadesh", "Kadesh-barnea", 34.43, 30.63, pos="w", tier=1,
      note="The springs of Ain el-Qudeirat, on the edge of the Negev.")
place("hebron", "Hebron", 35.10, 31.53, pos="e", tier=2, note="Earlier Kiriath-arba, named for Arba, “the greatest man among the Anakim” {Joshua 14:15}.")
place("rehob", "Rehob", 35.80, 33.50, False, pos="e", tier=3,
      note="Not located. “Rehob, near Lebo-hamath” {Numbers 13:21}.")
place("lebohamath", "Lebo-hamath", 36.37, 34.20, False, pos="w", tier=3,
      note="Probably Lebweh in the northern Beqaa.")
place("hormah", "Hormah", 34.97, 31.21, False, pos="sw", tier=3, note="Not located for certain.")
place("arad", "Arad", 35.126, 31.28, pos="e", tier=3)
place("ezion", "Ezion-geber and Elath", 34.97, 29.55, False, pos="w", tier=3,
      note="At the head of the gulf; the exact sites are disputed.")
place("hor", "Mount Hor", 35.03, 30.88, False, pos="w", tier=3,
      note="Not located. The traditional site, Jebel Harun near Petra, lies inside Edom; the text puts the mountain “on the border of the land of Edom” {Numbers 20:23}, so the map sets it at Edom's western edge.")
# Around Edom and Moab
place("oboth", "Oboth", 35.95, 30.47, False, pos="e", tier=3, note="Not located.")
place("iyeabarim", "Iye-abarim", 36.02, 30.97, False, pos="e", tier=3,
      note="Not located. It lay “in the wilderness facing Moab, toward the sunrise” {Numbers 21:11}.")
place("arnoncamp", "beyond the Arnon", 36.08, 31.43, False, pos="n", tier=3,
      note="Camped in the wilderness on the far side of the Arnon {Numbers 21:13}.")
place("dibon", "Dibon", 35.78, 31.50, pos="e", tier=3)
place("aroer", "Aroer", 35.80, 31.465, pos="se", tier=3)
place("ar", "Ar", 35.74, 31.30, False, pos="e", tier=3, note="Ar of Moab; not located.")
place("kiriathaim", "Kiriathaim", 35.74, 31.62, False, pos="w", tier=2,
      note="Shaveh-kiriathaim, where the Emim were struck {Genesis 14:5}.")
place("jahaz", "Jahaz", 35.88, 31.60, False, pos="e", tier=3, note="Not located.")
place("medeba", "Medeba", 35.80, 31.72, pos="e", tier=3)
place("heshbon", "Heshbon", 35.81, 31.80, pos="e", tier=2)
place("jazer", "Jazer", 35.79, 31.97, False, pos="w", tier=3, note="Not located.")
place("rabbah", "Rabbah", 35.93, 31.955, pos="e", tier=2,
      note="Rabbah of the Ammonites, where Og's iron bed was kept {Deuteronomy 3:11}.")
place("edrei", "Edrei", 36.10, 32.62, pos="e", tier=2, note="One of Og's two cities, where he came out to battle {Deuteronomy 1:4} {Deuteronomy 3:1}.")
place("ashtaroth", "Ashtaroth", 36.02, 32.80, pos="e", tier=2,
      note="One of Og's two cities {Deuteronomy 1:4}; Ashteroth-karnaim, where the Rephaim were struck {Genesis 14:5}.")
place("salecah", "Salecah", 36.71, 32.49, pos="w", tier=3)
place("kenath", "Kenath", 36.62, 32.76, pos="w", tier=3)
place("nebo", "Mount Nebo", 35.725, 31.765, pos="e", tier=2, note="“Mount Nebo, the top of Pisgah” {Deuteronomy 34:1}.")
place("bethpeor", "Beth-peor", 35.69, 31.80, False, pos="ne", tier=3, note="Not located.")
place("shittim", "Shittim", 35.65, 31.85, False, pos="ne", tier=3,
      note="Abel-shittim, probably Tell el-Hammam.")
place("bethjeshimoth", "Beth-jeshimoth", 35.59, 31.78, False, pos="s", tier=3)
place("zoar", "Zoar", 35.47, 31.03, False, pos="w", tier=3, note="At the south end of the Salt Sea; not located for certain.")
# West of the Jordan
place("adam", "Adam", 35.55, 32.10, pos="w", tier=3, note="Tell ed-Damiyeh, where the Jabbok meets the Jordan.")
place("zarethan", "Zarethan", 35.58, 32.18, False, pos="e", tier=3, note="Not located.")
place("jericho", "Jericho", 35.444, 31.871, pos="n", tier=2)
place("gilgal", "Gilgal", 35.49, 31.85, False, pos="se", tier=3,
      note="Not located; “on the east edge of Jericho” {Joshua 4:19}.")
place("ai", "Ai", 35.26, 31.917, False, pos="n", tier=3, note="Usually placed at et-Tell; disputed.")
place("bethel", "Bethel", 35.235, 31.93, pos="w", tier=3)
place("shechem", "Shechem", 35.285, 32.213, pos="ne", tier=2, note="Between Mount Ebal and Mount Gerizim.")
place("ebal", "Mount Ebal", 35.274, 32.236, pos="n", tier=3)
place("gerizim", "Mount Gerizim", 35.273, 32.20, pos="s", tier=3)
place("gibeon", "Gibeon", 35.185, 31.847, pos="n", tier=3)
place("kjearim", "Kiriath-jearim", 35.10, 31.805, pos="w", tier=3)
place("jerusalem", "Jerusalem", 35.235, 31.777, pos="e", tier=1, note="Jebus, the city of the Jebusites {Joshua 15:63} {Joshua 18:28}.")
place("bethhoron", "Beth-horon", 35.12, 31.88, pos="nw", tier=3)
place("aijalon", "Aijalon", 35.03, 31.84, pos="s", tier=3)
place("azekah", "Azekah", 34.94, 31.70, pos="w", tier=3)
place("jarmuth", "Jarmuth", 34.97, 31.71, pos="e", tier=3)
place("makkedah", "Makkedah", 34.92, 31.625, False, pos="e", tier=3, note="Not located.")
place("libnah", "Libnah", 34.86, 31.60, False, pos="w", tier=3, note="Not located.")
place("lachish", "Lachish", 34.85, 31.565, pos="w", tier=3)
place("eglon", "Eglon", 34.92, 31.50, False, pos="w", tier=3, note="Not located.")
place("debir", "Debir", 35.02, 31.44, False, pos="e", tier=2,
      note="Earlier Kiriath-sepher {Joshua 15:15}; probably Khirbet Rabud. A town of the Anakim {Joshua 11:21}.")
place("anab", "Anab", 34.93, 31.40, pos="w", tier=2, note="A town of the Anakim {Joshua 11:21}.")
place("gezer", "Gezer", 34.92, 31.86, pos="w", tier=3)
place("gaza", "Gaza", 34.46, 31.50, pos="w", tier=2, note="Where some of the Anakim remained {Joshua 11:22}.")
place("ashkelon", "Ashkelon", 34.55, 31.665, pos="w", tier=3)
place("ashdod", "Ashdod", 34.65, 31.75, pos="w", tier=2, note="Where some of the Anakim remained {Joshua 11:22}.")
place("gath", "Gath", 34.85, 31.70, pos="w", tier=2, note="Where some of the Anakim remained {Joshua 11:22}.")
place("ekron", "Ekron", 34.85, 31.78, pos="w", tier=3)
place("beersheba", "Beersheba", 34.84, 31.245, pos="w", tier=2)
place("halak", "the bare mountain", 34.93, 30.92, False, pos="w", tier=3,
      note="The southern limit of Joshua's conquest, “the bare mountain that rises toward Seir” {Joshua 11:17}; not located for certain.")
place("hazor", "Hazor", 35.568, 33.017, pos="e", tier=2)
place("merom", "waters of Merom", 35.43, 33.00, False, pos="w", tier=3, note="Not located.")
place("madon", "Madon", 35.45, 32.80, False, pos="w", tier=3, note="Not located.")
place("shimron", "Shimron", 35.22, 32.70, False, pos="w", tier=3, note="Not located for certain.")
place("achshaph", "Achshaph", 35.13, 32.90, False, pos="w", tier=3, note="Not located.")
place("sidon", "Sidon", 35.37, 33.56, pos="w", tier=2, note="“Great Sidon” {Joshua 11:8}.")
place("tyre", "Tyre", 35.20, 33.27, pos="w", tier=3)
place("misrephoth", "Misrephoth-maim", 35.12, 33.08, False, pos="w", tier=3, note="Not located.")
place("mizpeh", "Valley of Mizpeh", 35.75, 33.30, False, pos="e", tier=3, note="Not located.")
place("baalgad", "Baal-gad", 35.70, 33.38, False, pos="e", tier=3,
      note="The northern limit of Joshua's conquest, “in the Valley of Lebanon under Mount Hermon” {Joshua 11:17}; not located.")
place("hermon", "Mount Hermon", 35.86, 33.42, pos="e", tier=2)
place("dor", "Dor", 34.92, 32.62, pos="w", tier=3)
place("megiddo", "Megiddo", 35.185, 32.585, pos="w", tier=3)
place("taanach", "Taanach", 35.22, 32.52, pos="e", tier=3)
place("bethshean", "Beth-shean", 35.50, 32.50, pos="e", tier=3)
place("shiloh", "Shiloh", 35.29, 32.055, pos="e", tier=2)
place("timnath", "Timnath-serah", 35.11, 32.01, False, pos="w", tier=3,
      note="Probably Khirbet Tibnah.")
place("gibeahph", "Gibeah of Phinehas", 35.31, 32.15, False, pos="sw", tier=3, note="Not located.")
place("kedesh", "Kedesh", 35.53, 33.11, pos="w", tier=3)
place("dan", "Dan", 35.652, 33.249, pos="e", tier=2, note="Earlier Leshem {Joshua 19:47}.")
place("bezer", "Bezer", 35.88, 31.70, False, pos="e", tier=3, note="Not located.")
place("ramoth", "Ramoth in Gilead", 36.03, 32.53, False, pos="e", tier=3, note="Probably Tell er-Rumeith.")
place("golan", "Golan", 35.84, 32.80, False, pos="w", tier=3, note="Not located for certain.")
place("witness", "the altar Witness", 35.53, 32.07, False, pos="ne", tier=3,
      note="Built “at the frontier of the land of Canaan, in the region of the Jordan” {Joshua 22:11}; the place is not known.")

# ---------------------------------------------------------------- stages
# cam: "j" whole journey, "l" the land.  Caption refs in {Book c:v}.
STAGES = [
 dict(key="egypt", title="Out of Egypt", when="Year 1 · month 1 · day 15", cam="j",
      act=["rameses", "succoth"],
      text="On the day after the Passover the sons of Israel set out from Rameses toward Succoth, “about six hundred thousand men on foot, besides children” {Exodus 12:37} {Numbers 33:3}. Moses took the bones of Joseph with him {Exodus 13:19}. God did not lead them by the way of the land of the Philistines, though it was near {Exodus 13:17}."),
 dict(key="etham", title="To the edge of the wilderness, and back", when="Year 1 · month 1", cam="j",
      act=["etham", "pihahiroth"],
      text="From Succoth they camped at Etham, “at the edge of the wilderness” {Exodus 13:20}. Then they turned back and camped before Pi-hahiroth, between Migdol and the sea {Exodus 14:2} {Numbers 33:7}. None of these camps has been found; the map follows the directions the text gives: out to the edge of the wilderness, then back to the water."),
 dict(key="sea", title="Through the sea", when="Year 1 · month 1", cam="j",
      act=["crossing"],
      text="Pharaoh's army overtook them camped by the sea {Exodus 14:9}. The sons of Israel “went into the middle of the sea on dry ground” {Exodus 14:22}. Where they crossed is not known: proposals run from the coastal lagoons in the north to the head of the Gulf of Suez. The map puts the crossing at the Bitter Lakes, on the line of the camps."),
 dict(key="marah", title="Marah and Elim", when="Year 1 · months 1–2", cam="j",
      act=["marah", "elim", "seacamp"],
      text="Three days in the wilderness of Shur without water {Exodus 15:22}, then the bitter water of Marah {Exodus 15:23}, then Elim, with “twelve springs of water and seventy palm trees” {Exodus 15:27}. After Elim they camped by the Sea of Reeds {Numbers 33:10}, so the route runs south along the gulf."),
 dict(key="sin", title="Manna, water, and Amalek", when="Year 1 · month 2 · day 15", cam="j",
      act=["dophkah", "alush", "rephidim"],
      text="They came to the wilderness of Sin, between Elim and Sinai, one month after leaving Egypt {Exodus 16:1}, and the manna began {Exodus 16:15}. At Rephidim there was no water to drink {Exodus 17:1} until Moses struck “the rock at Horeb” {Exodus 17:6}, and there the Amalekites fought against Israel {Exodus 17:8}."),
 dict(key="sinai", title="Mount Sinai", when="Year 1 · month 3, to year 2", cam="j",
      act=["sinai"],
      text="In the third month they came to the wilderness of Sinai and camped in front of the mountain {Exodus 19:1} {Exodus 19:2}. They stayed almost a year: the dwelling was raised on the first day of the second year {Exodus 40:17}. The mountain shown is the traditional one, in the south of the peninsula; the text does not fix its place."),
 dict(key="paran", title="From Sinai to Kadesh", when="Year 2 · month 2 · day 20", cam="j",
      act=["kibroth", "hazeroth", "kadesh"],
      text="The cloud lifted on the twentieth day of the second month of the second year {Numbers 10:11}. They went by Taberah, Kibroth-hattaavah and Hazeroth into the wilderness of Paran {Numbers 11:35} {Numbers 12:16}, and came to Kadesh. “It is eleven days' journey from Horeb by the way of Mount Seir to Kadesh-barnea” {Deuteronomy 1:2}."),
 dict(key="spies", title="The twelve spies", when="Year 2 · the first ripe grapes", cam="j",
      act=["kadesh", "hebron", "rehob", "hormah"],
      text="From Kadesh twelve men went up through the Negev to Hebron, where Ahiman, Sheshai and Talmai, the descendants of Anak, lived, and on as far as Rehob, near Lebo-hamath {Numbers 13:21} {Numbers 13:22}. After forty days they came back saying, “There we saw the Nephilim — the sons of Anak are from the Nephilim — and we were like grasshoppers in our own eyes” {Numbers 13:33}. The people refused to go up. When they went up anyway, they were beaten down as far as Hormah {Numbers 14:45}."),
 dict(key="years", title="Thirty-eight years", when="Years 2 to 40", cam="j",
      act=["ezion"],
      text="A year for each of the forty days of scouting {Numbers 14:34}. As Moses tells it, “we went around Mount Seir for many days” {Deuteronomy 2:1}. Numbers names seventeen camps between Hazeroth and Ezion-geber, none of them located {Numbers 33:18} {Numbers 33:35}. From Kadesh-barnea to the Brook Zered took thirty-eight years {Deuteronomy 2:14}."),
 dict(key="hor", title="Kadesh again; Edom refuses", when="Year 40 · months 1 to 5", cam="j",
      act=["kadesh", "hor", "arad", "hormah"],
      text="In the first month the whole congregation came to Kadesh, and Miriam died there {Numbers 20:1}. Edom refused to let Israel pass along the King's Highway {Numbers 20:17} {Numbers 20:21}, and Moab refused too {Judges 11:17}. Aaron died on Mount Hor, “on the border of the land of Edom,” on the first day of the fifth month of the fortieth year {Numbers 20:23} {Numbers 33:38}. The king of Arad attacked; Israel destroyed his towns, and the place was named Hormah {Numbers 21:1} {Numbers 21:3}."),
 dict(key="edom", title="Around Edom and Moab", when="Year 40", cam="j",
      act=["ezion", "oboth", "iyeabarim", "arnoncamp"],
      text="They went “by the way of the Sea of Reeds, to go around the land of Edom” {Numbers 21:4}, past Elath and Ezion-geber, then turned and went by the way of the wilderness of Moab {Deuteronomy 2:8}. The bronze serpent was raised on this road {Numbers 21:9}. They crossed the Brook Zered {Deuteronomy 2:13} and camped beyond the Arnon, in the wilderness: “They did not enter the territory of Moab” {Judges 11:18}. Numbers 33 names other camps on this leg, Zalmonah and Punon among them {Numbers 33:41}. Moab and Ammon had once been held by giants, the Emim and the Zamzummim {Deuteronomy 2:10} {Deuteronomy 2:20}."),
 dict(key="sihon", title="Sihon and Og", when="Year 40", cam="l",
      act=["dibon", "jahaz", "heshbon", "jazer", "edrei", "ashtaroth", "rabbah", "nebo"],
      text="Sihon king of the Amorites would not let Israel pass and fought them at Jahaz; Israel took his land “from the Arnon to the Jabbok” {Numbers 21:23} {Numbers 21:24}. Then they went up by the road to Bashan, and Og came out to battle at Edrei {Numbers 21:33}. Og “was left of the remnant of the Rephaim”; his iron bed was kept in Rabbah of the Ammonites {Deuteronomy 3:11}. Bashan, with sixty walled towns, “is called a land of Rephaim” {Deuteronomy 3:4} {Deuteronomy 3:13}."),
 dict(key="moab", title="The plains of Moab", when="Year 40 · month 11 · day 1", cam="l",
      act=["shittim", "bethjeshimoth"],
      text="Israel camped in the plains of Moab, across the Jordan from Jericho {Numbers 22:1}, from Beth-jeshimoth to Abel-shittim {Numbers 33:49}. Balak brought Balaam to curse them, and he blessed them three times {Numbers 24:10}. Moses gave the kingdoms of Sihon and Og to Reuben, Gad and half the tribe of Manasseh {Numbers 32:33}. On the first day of the eleventh month of the fortieth year he began the words of Deuteronomy {Deuteronomy 1:3}."),
 dict(key="nebo", title="Moses sees the land", when="Year 40", cam="l",
      act=["nebo", "bethpeor", "dan", "zoar", "jericho"],
      text="Moses went up Mount Nebo, the top of Pisgah, and the LORD showed him all the land: Gilead as far as Dan, Naphtali, Ephraim and Manasseh, all Judah as far as the western sea, the Negev, and the valley of Jericho as far as Zoar {Deuteronomy 34:1} {Deuteronomy 34:3}. “I have let you see it with your eyes, but you shall not cross over there” {Deuteronomy 34:4}. He died there in the land of Moab, and no one knows his burial place {Deuteronomy 34:5} {Deuteronomy 34:6}."),
 dict(key="jordan", title="Across the Jordan", when="Year 41 · month 1 · day 10", cam="l",
      act=["shittim", "adam", "zarethan", "jericho", "gilgal"],
      text="From Shittim they came to the Jordan {Joshua 3:1}. The waters coming down stood still, “very far away, from Adam, the city beside Zarethan,” and the people crossed opposite Jericho {Joshua 3:16}. They came up on the tenth day of the first month and camped at Gilgal {Joshua 4:19}, kept the Passover, and the manna ceased {Joshua 5:10} {Joshua 5:12}. Counting from the fifteenth day of the first month, when they left Rameses {Numbers 33:3}, the journey took forty years less five days."),
 dict(key="ai", title="Jericho, Ai, and Mount Ebal", when="Joshua 6–9", cam="l",
      act=["jericho", "ai", "bethel", "ebal", "gerizim", "gibeon", "kjearim"],
      text="Jericho was burned {Joshua 6:24}, then Ai, made “a heap forever” {Joshua 8:28}. On Mount Ebal Joshua built an altar, and all Israel stood, half in front of Mount Gerizim and half in front of Mount Ebal {Joshua 8:30} {Joshua 8:33}. The Hivites of Gibeon won a covenant by a trick; their cities were Gibeon, Chephirah, Beeroth and Kiriath-jearim {Joshua 9:7} {Joshua 9:17}."),
 dict(key="south", title="The southern campaign", when="Joshua 10", cam="l",
      act=["gibeon", "bethhoron", "aijalon", "azekah", "makkedah", "libnah", "lachish", "gezer",
           "eglon", "hebron", "debir", "jarmuth", "jerusalem", "kadesh", "gaza"],
      text="The five kings of the Amorites, of Jerusalem, Hebron, Jarmuth, Lachish and Eglon, camped against Gibeon {Joshua 10:5}. Joshua marched up all night from Gilgal and chased them by the ascent of Beth-horon as far as Azekah and Makkedah, under the hailstones, while the sun stood still {Joshua 10:9} {Joshua 10:11} {Joshua 10:13}. Makkedah, Libnah, Lachish, Eglon, Hebron and Debir fell in turn {Joshua 10:28} {Joshua 10:39}: “from Kadesh-barnea to Gaza, and all the land of Goshen as far as Gibeon” {Joshua 10:41}."),
 dict(key="north", title="The northern campaign", when="Joshua 11", cam="l",
      act=["hazor", "merom", "madon", "shimron", "achshaph", "sidon", "misrephoth", "mizpeh",
           "baalgad", "halak", "hebron", "debir", "anab", "gaza", "gath", "ashdod"],
      text="Jabin king of Hazor gathered the kings of the north at the waters of Merom {Joshua 11:1} {Joshua 11:5}. Joshua fell on them there and chased them as far as Great Sidon and Misrephoth-maim, and east to the Valley of Mizpeh; Hazor alone he burned {Joshua 11:8} {Joshua 11:13}. He cut off the Anakim from Hebron, Debir and Anab: “only in Gaza, in Gath and in Ashdod did some remain” {Joshua 11:21} {Joshua 11:22}. The war took “many days” {Joshua 11:18}. “Then the land had rest from war” {Joshua 11:23}."),
 dict(key="divide", title="The land divided", when="Year 47 · Caleb is 85", cam="l",
      act=["shiloh", "hebron", "debir", "dan", "timnath", "jerusalem", "gezer", "megiddo",
           "taanach", "bethshean", "dor"],
      text="The LORD told Joshua that “very much of the land remains to be possessed”: the Philistine coast, the Sidonians and Lebanon {Joshua 13:1} {Joshua 13:6}. Caleb, eighty-five years old and forty-five years after Kadesh, asked for the hill country of the Anakim and drove the three sons of Anak out of Hebron {Joshua 14:10} {Joshua 14:12} {Joshua 15:14}. Judah and Joseph drew their lots first {Joshua 15:1} {Joshua 16:1}; the other seven tribes drew theirs at Shiloh, where the tent of meeting was set up {Joshua 18:1} {Joshua 18:10}. The Jebusites kept Jerusalem, and the Canaanites kept Gezer and the cities of the valleys {Joshua 15:63} {Joshua 16:10} {Joshua 17:12}. Dan lost its land and took Leshem in the north {Joshua 19:47}."),
 dict(key="rest", title="Rest", when="Joshua 20–22", cam="l",
      act=["kedesh", "shechem", "hebron", "bezer", "ramoth", "golan", "witness", "shiloh"],
      text="Six cities of refuge were set apart: Kedesh, Shechem and Hebron west of the Jordan; Bezer, Ramoth in Gilead and Golan east of it {Joshua 20:7} {Joshua 20:8}. The Levites received forty-eight towns {Joshua 21:41}. “Not one word failed of all the good word that the LORD had spoken to the house of Israel. It all came to pass” {Joshua 21:45}. The eastern tribes went home and built an altar by the Jordan, which they called Witness {Joshua 22:9} {Joshua 22:34}."),
 dict(key="bones", title="The bones of Joseph", when="Joshua 24 · Joshua is 110", cam="j",
      act=["shechem", "timnath", "gibeahph", "rameses"],
      text="Joshua gathered all the tribes of Israel to Shechem, and there he made a covenant with the people {Joshua 24:1} {Joshua 24:25}. He died a hundred and ten years old and was buried at Timnath-serah {Joshua 24:29} {Joshua 24:30}. “The bones of Joseph, which the sons of Israel brought up from Egypt, they buried at Shechem” {Joshua 24:32}: Joseph's request {Genesis 50:25}, carried out of Egypt by Moses {Exodus 13:19}, kept at the end of the road."),
]

# ---------------------------------------------------------------- route segments
# kind: camp (the people's line of march), march (a campaign), spies, wander, return
SEGS = [
 ("egypt", "camp", ["rameses", (31.97, 30.70), "succoth"]),
 ("etham", "camp", ["succoth", (32.20, 30.63), "etham", (32.33, 30.57), "pihahiroth"]),
 ("sea", "camp", ["pihahiroth", "crossing", (32.53, 30.32)]),
 ("marah", "camp", [(32.53, 30.32), (32.68, 30.02), (32.82, 29.80), "marah", "elim", "seacamp"]),
 ("sin", "camp", ["seacamp", (33.24, 28.97), "dophkah", "alush", "rephidim"]),
 ("sinai", "camp", ["rephidim", (33.84, 28.63), "sinai"]),
 ("paran", "camp", ["sinai", "kibroth", "hazeroth", (34.62, 29.25), (34.78, 29.62),
                    (34.72, 29.98), (34.55, 30.33), "kadesh"]),
 ("spies", "spies", ["kadesh", (34.80, 31.00), "hebron", (35.24, 31.98), (35.33, 32.50),
                     (35.55, 33.00), "rehob"]),
 ("spies", "march", ["kadesh", (34.78, 30.98), "hormah"]),
 ("years", "wander", ["kadesh", (34.30, 30.28), (34.50, 29.88), (34.76, 29.62), "ezion",
                      (35.13, 29.92), (35.20, 30.32), (34.92, 30.62), "kadesh"]),
 ("hor", "camp", ["kadesh", (34.75, 30.80), "hor"]),
 ("hor", "march", ["hor", (35.06, 31.10), "arad"]),
 ("edom", "camp", ["hor", (35.12, 30.45), (35.06, 29.95), (35.02, 29.66), (35.30, 29.70),
                   (35.62, 29.95), (35.88, 30.20), "oboth", (36.04, 30.75), "iyeabarim",
                   (36.10, 31.18), "arnoncamp"]),
 ("sihon", "camp", ["arnoncamp", (35.97, 31.48), "dibon", (35.77, 31.64), "nebo"]),
 ("sihon", "march", [(35.98, 31.48), "jahaz"]),
 ("sihon", "march", ["jahaz", "heshbon", "jazer"]),
 ("sihon", "march", ["heshbon", (35.95, 32.15), (36.04, 32.43), "edrei"]),
 ("moab", "camp", ["nebo", (35.66, 31.80), "shittim"]),
 ("jordan", "camp", ["shittim", (35.57, 31.86), "gilgal"]),
 ("ai", "march", ["gilgal", "jericho"]),
 ("ai", "march", ["gilgal", (35.36, 31.89), "ai"]),
 ("ai", "march", ["ai", (35.25, 32.07), "ebal"]),
 ("ai", "march", ["gilgal", (35.30, 31.87), "gibeon"]),
 ("south", "march", ["gilgal", (35.33, 31.86), "gibeon", "bethhoron", "azekah", "makkedah",
                     "libnah", "lachish", "eglon", "hebron", "debir"]),
 ("south", "return", ["debir", (35.20, 31.62), (35.38, 31.78), "gilgal"]),
 ("north", "march", ["gilgal", (35.55, 32.30), (35.56, 32.72), (35.50, 32.95), "merom"]),
 ("north", "march", ["merom", (35.28, 33.25), "sidon"]),
 ("north", "march", ["merom", "misrephoth"]),
 ("north", "march", ["merom", (35.62, 33.18), "mizpeh"]),
 ("north", "march", ["merom", "hazor"]),
 ("divide", "camp", ["gilgal", (35.38, 31.96), "shiloh"]),
 ("divide", "march", [(34.97, 31.80), (35.02, 32.30), (35.27, 32.75), (35.55, 33.08), "dan"]),
 ("rest", "return", ["shiloh", (35.47, 32.06), (35.72, 32.12)]),
 ("bones", "camp", ["shiloh", "shechem"]),
]

# Moses' view from Nebo (Deuteronomy 34:1-3).
SIGHT = [(35.652, 33.249), (35.45, 33.0), (35.22, 32.25), (34.95, 31.62), (34.45, 31.80),
         (34.85, 31.10), (35.45, 31.87), (35.47, 31.03), (35.80, 32.30)]

# ---------------------------------------------------------------- geography
DEAD_SEA = [(35.50, 31.772), (35.535, 31.768), (35.565, 31.745), (35.578, 31.70),
            (35.588, 31.62), (35.588, 31.52), (35.578, 31.43), (35.565, 31.35),
            (35.545, 31.335), (35.50, 31.33), (35.465, 31.315), (35.445, 31.29),
            (35.46, 31.265), (35.505, 31.255), (35.53, 31.235), (35.53, 31.17),
            (35.515, 31.10), (35.49, 31.055), (35.46, 31.04), (35.43, 31.07),
            (35.41, 31.13), (35.395, 31.21), (35.385, 31.30), (35.39, 31.40),
            (35.395, 31.47), (35.42, 31.56), (35.45, 31.65), (35.475, 31.72)]
HULEH = [(35.595, 33.095), (35.615, 33.105), (35.635, 33.095), (35.638, 33.07),
         (35.625, 33.052), (35.603, 33.058)]
TIMSAH = [(32.255, 30.585), (32.29, 30.595), (32.325, 30.582), (32.318, 30.562), (32.28, 30.558)]

# Watercourses drawn by hand: name, points, label position index, seasonal?
WADIS = [
 ("Arnon", [(35.565, 31.465), (35.63, 31.462), (35.70, 31.455), (35.77, 31.445), (35.84, 31.42),
            (35.92, 31.38), (36.02, 31.335), (36.13, 31.30)], 3),
 ("Brook Zered", [(35.47, 31.06), (35.55, 31.035), (35.65, 30.99), (35.75, 30.965), (35.85, 30.95),
                  (35.95, 30.93), (36.05, 30.885), (36.15, 30.83)], 4),
 ("Jabbok", [(35.555, 32.105), (35.62, 32.17), (35.70, 32.195), (35.80, 32.19), (35.88, 32.17),
             (35.98, 32.135), (36.06, 32.09), (36.08, 32.04), (36.02, 31.99), (35.95, 31.96)], 3),
 ("", [(35.575, 32.645), (35.65, 32.69), (35.75, 32.71), (35.85, 32.72), (35.95, 32.70),
       (36.03, 32.68)], None),                                                      # Yarmuk
 ("", [(35.36, 32.50), (35.25, 32.58), (35.15, 32.65), (35.10, 32.72), (35.05, 32.80),
       (35.03, 32.815)], None),                                                     # Kishon
 ("Kanah", [(35.20, 32.15), (35.10, 32.165), (35.00, 32.14), (34.93, 32.105)], 1),
 ("", [(34.93, 32.105), (34.86, 32.10), (34.79, 32.10)], None),                     # Yarkon
 ("Brook of Egypt", [(33.80, 31.13), (33.83, 31.00), (33.86, 30.84), (33.82, 30.62),
                     (33.74, 30.40), (33.66, 30.16), (33.62, 29.92)], 3),
]

ROADS = [
 ("the way of the land of the Philistines", "egypt", "etham",
  [(32.30, 30.88), (32.55, 30.99), (32.82, 31.03), (33.10, 31.03), (33.45, 31.06),
   (33.80, 31.10), (34.10, 31.20), (34.25, 31.29), (34.46, 31.50)]),
 ("the King's Highway", "hor", None,
  [(35.01, 29.56), (35.30, 29.90), (35.46, 30.30), (35.60, 30.73), (35.64, 31.00),
   (35.70, 31.18), (35.76, 31.36), (35.79, 31.48), (35.80, 31.72), (35.81, 31.80),
   (35.90, 31.98), (35.98, 32.20), (36.03, 32.53), (36.10, 32.62), (36.22, 33.05),
   (36.30, 33.50)]),
]

# ---------------------------------------------------------------- territories
# Tribal lots, after Joshua 13-19, drawn approximately. Coastal and Jordan sides
# run past the shore or river and are trimmed to it.
WEST = dict(
 judah=[(35.60, 31.765), (35.50, 31.795), (35.42, 31.80), (35.35, 31.80), (35.30, 31.78),
        (35.27, 31.77), (35.24, 31.765), (35.215, 31.765), (35.20, 31.775), (35.19, 31.795),
        (35.14, 31.80), (35.10, 31.805), (35.06, 31.785), (35.02, 31.765), (34.975, 31.75),
        (34.91, 31.775), (34.86, 31.795), (34.80, 31.83), (34.74, 31.87), (34.69, 31.925),
        (34.60, 31.97), (34.30, 31.75), (33.90, 31.35), (33.70, 31.20), (33.80, 31.13),
        (33.85, 31.00), (33.95, 30.85), (34.25, 30.70), (34.33, 30.62), (34.43, 30.58),
        (34.75, 30.68), (35.00, 30.80), (35.17, 30.92), (35.25, 30.95), (35.43, 31.02),
        (35.50, 31.10), (35.55, 31.40), (35.58, 31.70)],
 simeon=[(34.62, 31.42), (34.80, 31.45), (34.98, 31.38), (35.08, 31.28), (35.05, 31.12),
         (34.85, 31.05), (34.62, 31.12), (34.50, 31.25)],
 benjamin=[(35.60, 31.765), (35.62, 31.93), (35.45, 31.89), (35.38, 31.91), (35.30, 31.925),
           (35.24, 31.925), (35.20, 31.895), (35.15, 31.885), (35.10, 31.88), (35.09, 31.845),
           (35.10, 31.805), (35.14, 31.80), (35.19, 31.795), (35.20, 31.775), (35.215, 31.765),
           (35.24, 31.765), (35.27, 31.77), (35.30, 31.78), (35.35, 31.80), (35.42, 31.80),
           (35.50, 31.795)],
 dansouth=[(35.10, 31.88), (35.09, 31.845), (35.10, 31.805), (35.06, 31.785), (35.02, 31.765),
           (34.975, 31.75), (34.91, 31.775), (34.86, 31.795), (34.80, 31.83), (34.74, 31.87),
           (34.69, 31.925), (34.60, 31.97), (34.70, 32.13), (34.79, 32.10), (34.86, 32.10),
           (34.93, 32.105), (34.92, 32.05), (34.89, 31.95), (34.915, 31.852), (35.02, 31.87)],
 ephraim=[(35.62, 31.93), (35.62, 32.08), (35.50, 32.09), (35.42, 32.12), (35.38, 32.17),
          (35.32, 32.235), (35.25, 32.24), (35.22, 32.19), (35.19, 32.15), (35.10, 32.165),
          (35.00, 32.14), (34.93, 32.105), (34.92, 32.05), (34.89, 31.95), (34.915, 31.852),
          (35.02, 31.87), (35.10, 31.88), (35.15, 31.885), (35.20, 31.895), (35.24, 31.925),
          (35.30, 31.925), (35.38, 31.91), (35.45, 31.89)],
 manasseh=[(34.93, 32.105), (35.00, 32.14), (35.10, 32.165), (35.19, 32.15), (35.22, 32.19),
           (35.25, 32.24), (35.32, 32.235), (35.38, 32.17), (35.42, 32.12), (35.50, 32.09),
           (35.62, 32.08), (35.62, 32.36), (35.50, 32.38), (35.40, 32.42), (35.30, 32.42),
           (35.22, 32.50), (35.12, 32.55), (35.00, 32.58), (34.89, 32.53), (34.80, 32.55),
           (34.70, 32.15), (34.79, 32.10), (34.86, 32.10)],
 issachar=[(35.62, 32.36), (35.62, 32.70), (35.47, 32.70), (35.39, 32.69), (35.28, 32.68),
           (35.17, 32.65), (35.08, 32.61), (35.12, 32.55), (35.22, 32.50), (35.30, 32.42),
           (35.40, 32.42), (35.50, 32.38)],
 zebulun=[(35.11, 32.66), (35.17, 32.65), (35.28, 32.68), (35.39, 32.69), (35.43, 32.74),
          (35.42, 32.80), (35.35, 32.84), (35.25, 32.86), (35.17, 32.82), (35.12, 32.76)],
 asher=[(34.80, 32.55), (34.89, 32.53), (35.00, 32.58), (35.08, 32.61), (35.11, 32.66),
        (35.12, 32.76), (35.17, 32.82), (35.25, 32.86), (35.30, 32.98), (35.35, 33.10),
        (35.42, 33.30), (35.50, 33.55), (35.55, 33.66), (35.30, 33.72), (34.95, 33.20),
        (34.85, 32.80)],
 naphtali=[(35.62, 32.70), (35.66, 33.00), (35.68, 33.20), (35.70, 33.34), (35.58, 33.42),
           (35.50, 33.55), (35.42, 33.30), (35.35, 33.10), (35.30, 32.98), (35.25, 32.86),
           (35.35, 32.84), (35.42, 32.80), (35.43, 32.74), (35.47, 32.70)],
 dannorth=[(35.60, 33.205), (35.70, 33.215), (35.72, 33.29), (35.62, 33.31)],
)
EAST = dict(
 reuben=[(35.50, 31.465), (35.50, 31.84), (35.70, 31.84), (35.81, 31.81), (35.97, 31.79),
         (36.03, 31.60), (36.06, 31.38), (35.95, 31.37), (35.84, 31.42), (35.77, 31.445),
         (35.70, 31.455), (35.63, 31.462), (35.565, 31.465)],
 gad=[(35.50, 31.84), (35.50, 32.10), (35.52, 32.40), (35.55, 32.70), (35.635, 32.70),
      (35.63, 32.40), (35.63, 32.20), (35.68, 32.19), (35.85, 32.30), (35.98, 32.48),
      (36.06, 32.60), (36.10, 32.40), (36.06, 32.20), (36.02, 32.08), (35.92, 32.00),
      (35.90, 31.88), (35.97, 31.79), (35.81, 31.81), (35.70, 31.84)],
 manassehE=[(35.63, 32.20), (35.63, 32.40), (35.635, 32.70), (35.80, 32.71), (35.80, 32.90),
            (35.79, 33.05), (35.82, 33.30), (35.86, 33.44), (36.00, 33.46), (36.25, 33.25),
            (36.50, 33.00), (36.72, 32.86), (36.82, 32.60), (36.79, 32.43), (36.50, 32.42),
            (36.25, 32.58), (36.06, 32.60), (35.98, 32.48), (35.85, 32.30), (35.68, 32.19)],
)
GESHUR = [(35.55, 32.70), (35.80, 32.71), (35.80, 32.90), (35.79, 33.05), (35.62, 33.05), (35.58, 32.90)]
MAACAH = [(35.62, 33.05), (35.79, 33.05), (35.82, 33.30), (35.72, 33.36), (35.66, 33.25)]
MOAB = [(35.565, 31.465), (35.63, 31.462), (35.70, 31.455), (35.77, 31.445), (35.84, 31.42),
        (35.95, 31.37), (36.06, 31.38), (36.12, 31.10), (36.05, 30.885), (35.95, 30.93),
        (35.85, 30.95), (35.75, 30.965), (35.65, 30.99), (35.55, 31.035), (35.47, 31.06),
        (35.45, 31.25)]
AMMON = [(35.90, 31.88), (35.92, 32.00), (36.02, 32.08), (36.06, 32.20), (36.28, 32.18),
         (36.32, 31.86), (36.10, 31.74), (35.97, 31.79)]
ANAKIM = [(34.86, 31.38), (34.93, 31.58), (35.05, 31.66), (35.18, 31.61), (35.22, 31.47),
          (35.12, 31.33), (34.96, 31.31)]
PHILISTIA = [(33.70, 31.20), (34.30, 31.75), (34.60, 31.97), (34.69, 31.925), (34.74, 31.87),
             (34.80, 31.83), (34.86, 31.795), (34.885, 31.70), (34.80, 31.55), (34.66, 31.36),
             (34.40, 31.20), (34.18, 31.08), (33.95, 30.94), (33.85, 31.00), (33.80, 31.13)]
SIDON = [(35.10, 33.08), (35.25, 33.20), (35.42, 33.30), (35.50, 33.42), (35.62, 33.33),
         (35.72, 33.37), (35.87, 33.47), (36.12, 33.72), (36.50, 34.30), (36.20, 34.55),
         (35.70, 34.55), (35.40, 33.85), (34.90, 33.30)]
WANDER = [(34.18, 30.72), (34.70, 30.92), (35.20, 30.88), (35.36, 30.50), (35.28, 29.85),
          (35.04, 29.55), (34.72, 29.45), (34.42, 29.72), (34.12, 30.12), (34.02, 30.45)]

# Tribe label anchors (lon, lat).
TRIBE_LABELS = dict(
 judah=("Judah", 35.03, 31.25), simeon=("Simeon", 34.72, 31.20), benjamin=("Benjamin", 35.33, 31.835),
 dansouth=("Dan", 34.86, 31.94), ephraim=("Ephraim", 35.18, 32.03), manasseh=("Manasseh", 35.15, 32.36),
 issachar=("Issachar", 35.38, 32.635), zebulun=("Zebulun", 35.28, 32.76), asher=("Asher", 35.17, 33.0),
 naphtali=("Naphtali", 35.42, 33.19),
 reuben=("Reuben", 35.84, 31.56), gad=("Gad", 35.80, 31.98), manassehE=("Manasseh", 36.40, 32.93),
)

# Area and water labels: text, lon, lat, class, from-stage, to-stage, rotate[, view "j" or "l"]
LABELS = [
 ("EGYPT", 31.05, 30.05, "nation", None, None, 0),
 ("Goshen", 31.72, 30.62, "region", "egypt", "sea", 0),
 ("wilderness of Shur", 32.80, 30.18, "region", "marah", "marah", 0),
 ("wilderness of Sin", 33.20, 28.78, "region", "sin", "sin", 0),
 ("wilderness of Sinai", 34.12, 28.45, "region", "sinai", "sinai", 0),
 ("wilderness of Paran", 34.10, 29.70, "region", "paran", "years", 0),
 ("wilderness of Zin", 34.85, 30.48, "region", "spies", "hor", 0),
 ("SINAI", 33.65, 29.35, "nation", "egypt", "sinai", 0),
 ("the Negev", 34.75, 31.00, "region", "spies", None, 0),
 ("CANAAN", 35.10, 32.10, "nation", "egypt", "nebo", 0),
 ("EDOM", 35.68, 30.40, "nation", "paran", None, 0),
 ("Seir", 35.53, 30.18, "region", "paran", None, 0),
 ("the Arabah", 35.18, 30.40, "region", "years", None, -70),
 ("MOAB", 35.80, 31.24, "nation", "hor", None, 0),
 ("AMMON", 36.20, 32.01, "nation", "edom", None, 0),
 ("Kingdom of Sihon", 35.92, 31.76, "kingdom", "edom", "edom", 0),
 ("Kingdom of Og", 36.30, 33.05, "kingdom", "edom", "edom", 0),
 ("BASHAN", 36.33, 33.13, "nation", "sihon", None, 0),
 ("GILEAD", 35.82, 32.28, "nation", "sihon", None, 0),
 ("PHILISTINES", 34.30, 31.36, "nation", "egypt", None, 0, "l"),
 ("Amalekites", 34.62, 30.82, "people", "spies", "spies", 0),
 ("Amalekites", 33.92, 28.80, "people", "sin", "sin", 0),
 ("Jebusites", 35.24, 31.74, "people", "south", None, 0, "l"),
 ("Hivites", 35.13, 31.83, "people", "ai", "ai", 0, "l"),
 ("Amorites", 35.10, 31.635, "people", "south", "south", 0, "l"),
 ("Canaanites", 35.27, 32.85, "people", "north", "north", 0, "l"),
 ("SIDONIANS", 35.56, 33.63, "nation", "north", None, 0),
 ("GESHUR", 35.69, 32.92, "people", "sihon", None, 0, "l"),
 ("MAACAH", 35.79, 33.17, "people", "sihon", None, 0, "l"),
 ("LEBANON", 35.95, 33.90, "nation", "north", None, 0),
 ("Gebalites", 35.65, 34.12, "people", "divide", None, 0, "l"),
 ("THE GREAT SEA", 33.55, 32.45, "sea", None, None, 0, "j"),
 ("THE GREAT SEA", 34.40, 33.05, "sea", None, None, 0, "l"),
 ("Sea of Reeds", 32.88, 29.58, "water", None, None, -58),
 ("Sea of Reeds", 34.70, 28.80, "water", None, None, -66),
 ("Salt Sea", 35.485, 31.48, "water-s", None, None, -84),
 ("Sea of Chinnereth", 35.585, 32.81, "water-s", None, None, -78),
 ("Nile", 31.22, 29.40, "river", None, None, -80),
 ("Jordan", 35.565, 32.30, "river", None, None, -86),
]

# Giant peoples. state: on (they hold it), gone (driven out), former (gone before the Exodus)
GIANT_LABELS = [
 # text, lon, lat, from, to, kind, view ("j" journey only, "l" land only, None both), active stages
 ("ANAKIM", 35.02, 31.33, "egypt", "south", "on", None, ["spies"]),
 ("Anakim cut off", 35.02, 31.33, "north", None, "gone", "l", ["north"]),
 ("REPHAIM", 36.40, 32.70, "egypt", "edom", "on", None, []),
 ("Rephaim · Og defeated", 36.40, 32.70, "sihon", None, "gone", "l", ["sihon"]),
 ("Emim (formerly)", 35.80, 31.11, "egypt", None, "former", None, ["edom"]),
 ("Zamzummim (formerly)", 36.20, 31.89, "egypt", None, "former", None, ["edom"]),
 ("Valley of Rephaim", 35.14, 31.725, "divide", None, "name", "l", ["divide"]),
 ("Perizzites and Rephaim", 35.27, 32.29, "divide", None, "name", "l", ["divide"]),
]
# Giant towns: place id, from, to (the stages they are drawn as giant towns)
GIANT_TOWNS = [
 ("hebron", "on", "egypt", "south"), ("hebron", "gone", "north", None),
 ("debir", "on", "egypt", "south"), ("debir", "gone", "north", None),
 ("anab", "on", "egypt", "south"), ("anab", "gone", "north", None),
 ("ashtaroth", "on", "egypt", "edom"), ("ashtaroth", "gone", "sihon", None),
 ("edrei", "on", "egypt", "edom"), ("edrei", "gone", "sihon", None),
 ("kiriathaim", "former", "egypt", None),
 ("gaza", "on", "north", None), ("gath", "on", "north", None), ("ashdod", "on", "north", None),
]
