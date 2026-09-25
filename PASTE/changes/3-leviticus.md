# Decision Making with Before/After: Leviticus

Changes to chapters already rendered, filed under the book the request started in (a word decision can reach into other books; its table lists every verse). Newest at the top. Each entry: the request, the options, and a `Where | Before | After` table.

## Leviticus readability sweep (2026-09-25): 308 changes made, 4 choices waiting

### Your request (chat, 2026-09-25, after midnight)

> Run through all of Leviticus THOROUGHLY; look for opportunities to smooth things out like we did with the majority of my 12 edits. Check for double words in close proximity and several short words like "for he had said". Look for vagueness with he, them, it… words that may not resonate with me. Also check your renders.md of Leviticus chapters.

### What was done

- **Every verse of all 27 chapters was read.** Every change that could touch the sense was checked against the Hebrew. 17 notes that quoted a changed phrase were updated to match.
- **308 changes**, listed chapter by chapter below. The kinds:
  - doubled words (*the sin he sinned*, *stone him with stones*, *salt with salt*, *swarming things that swarm*);
  - the object before the verb (*And all its fat he shall turn into smoke*);
  - strings of small words (*on the wood that is on the fire that is on the altar*);
  - an unclear *he*, *it* or *them* named;
  - hand and face idioms (*his hand cannot reach* → *he cannot afford*; *favor the face of the poor* → *show favor to the poor*);
  - older words (*talebearer*, *earthen vessel*).
- **One real error fixed.** 18:28 read *And the land will not vomit you out when you make it unclean*, which sounds like a promise. The Hebrew is a warning: *Otherwise, when you make the land unclean, it will vomit you out*.
- **Four consistency fixes.**
  - *judgments* → **rulings**: Exodus 21:1 and 24:3 already use *rulings* for the same Hebrew word, *mishpatim*.
  - *bears his guilt* → **carries his guilt**: the verb of the scapegoat (16:22) and of Exodus 28:38.
  - 16:3 *a bull calf* → **a young bull**: the same Hebrew as 4:3, and the 9:2 note depends on a calf not being a bull.
  - *go loose* → **hang loose** (10:6, 21:10), to match 13:45 and Numbers 5:18.
- **The render tables for 22–27 were checked.** Their stiff lines are in the tables below: 24:12 *by the mouth of the LORD*, 24:23 *stoned him with stones*, 26:5 *reach to the grape harvest*.
- **So this stops happening:** `RENDERING_SPEC.md` now has a section, *The readability pass*, with these eight patterns taken from your Exodus rulings, and `CLAUDE.md` points to it. The scheduled renders read both files, so Numbers 7 onward is written with it.

### Choices for you (nothing changed yet)

**1. "and here —" in the priest's inspections (Leviticus 13–14, 25 verses).** Your ruling keeps *And here —* for *hinneh*, the word that puts the reader inside someone's eyes. In these two chapters it sits in front of *if* (*and here — if the mark has spread*), and the pair stumbles. In a diagnosis, *hinneh* means *and if he sees that*.
- **A:** keep as it is.
- **B:** *the priest shall look, and if the mark has spread…*. Where there is no *if*: *and finds that there is no white hair…*.

**Recommend B, in these two chapters only.** Everywhere else, *And here —* stays.

| Verse | Reads now |
|---|---|
| 13:5 | And the priest shall look at him on the seventh day, and here — if the mark has stayed as it was and has not spread in the skin, the priest shall shut him away another seven days |
| 13:6 | And the priest shall look at him again on the seventh day, and here — if the mark has faded and has not spread in the skin, the priest shall declare him clean |
| 13:8 | And the priest shall look, and here — if the scab has spread in the skin, the priest shall declare him unclean |
| 13:10 | And the priest shall look, and here — if there is a white swelling in the skin and it has turned the hair white, and there is raw flesh in the swelling, |
| 13:13 | then the priest shall look, and here — if the blight has covered all his flesh, he shall declare the marked man clean |
| 13:17 | and the priest shall look at him, and here — if the mark has turned white, the priest shall declare the marked man clean |
| 13:20 | And the priest shall look, and here — if it looks lower than the skin and its hair has turned white, the priest shall declare him unclean |
| 13:21 | But if the priest looks at it, and here — there is no white hair in it, and it is not lower than the skin, and it is faded, then the priest shall shut him away seven days |
| 13:25 | the priest shall look at it, and here — if the hair in the bright spot has turned white and it looks deeper than the skin, it is blight that has broken out in the burn |
| 13:26 | But if the priest looks at it, and here — there is no white hair in the bright spot, and it is not lower than the skin, and it is faded, then the priest shall shut him away seven days |
| 13:30 | the priest shall look at the mark, and here — if it looks deeper than the skin and there is thin yellow hair in it, the priest shall declare him unclean |
| 13:31 | And when the priest looks at the mark of the scaly patch, and here — it does not look deeper than the skin, and there is no black hair in it, then the priest shall shut the marked person away for seven days |
| 13:32 | And the priest shall look at the mark on the seventh day, and here — if the scaly patch has not spread, and there is no yellow hair in it, and the patch does not look deeper than the skin, |
| 13:34 | And the priest shall look at the scaly patch on the seventh day, and here — if the patch has not spread in the skin and does not look deeper than the skin, the priest shall declare him clean |
| 13:36 | the priest shall look at him, and here — if the patch has spread in the skin, the priest does not need to look for the yellow hair |
| 13:39 | the priest shall look, and here — if the bright spots on the skin of their body are a faded white, it is a rash that has broken out in the skin |
| 13:43 | And the priest shall look at him, and here — if the swelling of the mark is reddish-white on his bald head or his bald forehead, looking like blight on the skin of the body, |
| 13:53 | But if the priest looks, and here — the mark has not spread in the garment, or in the warp or the weft, or in any leather object, |
| 13:55 | And the priest shall look after the mark has been washed, and here — if the mark has not changed its look, and the mark has not spread, it is unclean |
| 13:56 | But if the priest looks, and here — the mark has faded after it was washed, then he shall tear it out of the garment, or out of the leather, or out of the warp or the weft |
| 14:3 | And the priest shall look, and here — if the mark of blight has healed in the blighted man, |
| 14:37 | And he shall look at the mark, and here — if the mark is in the walls of the house, in greenish or reddish hollows that look lower than the wall, |
| 14:39 | And the priest shall come back on the seventh day and look, and here — if the mark has spread in the walls of the house, |
| 14:44 | the priest shall come and look, and here — if the mark has spread in the house, it is a malignant blight in the house |
| 14:48 | But if the priest comes and looks, and here — the mark has not spread in the house after the house was plastered, then the priest shall declare the house clean, because the mark has healed |

**2. *moshav*, "your dwellings" vs "the dwelling".** *The dwelling* is the fixed name for the tabernacle (*mishkan*). A different word, *moshav*, "where you live", is rendered *dwellings* in six verses and *settlements* in four, so *dwelling* ends up meaning two different things in the same books.

| Verse | Reads now |
|---|---|
| Exodus 10:23 | there was light in their **dwellings** |
| Exodus 12:20 | In all your **dwellings** you shall eat unleavened bread |
| Exodus 35:3 | You shall not kindle a fire in any of your **settlements** |
| Leviticus 3:17 | in all your **settlements**: you shall eat no fat and no blood |
| Leviticus 7:26 | in any of your **settlements** |
| Leviticus 23:3 | a sabbath to the LORD in all your **dwellings** |
| Leviticus 23:14, 21, 31 | a lasting statute… in all your **dwellings** |
| Leviticus 23:17 | From your **dwellings** you shall bring two loaves |

**Recommend** *wherever you live* in the formula, *from your homes* at Leviticus 23:17, and *where they lived* at Exodus 10:23.

**3. Leviticus 19:26: the Greek reads it differently.** It now reads *You shall not eat anything with the blood in it*. The Hebrew is *al ha-dam*, and the same phrase in 1 Samuel 14:32–34 describes soldiers eating meat with the blood still in it. The Greek reads *You shall not eat **on the mountains***. That is Ezekiel's phrase for eating at hill shrines: *he does not eat on the mountains* (Ezekiel 18:6). The rest of the verse forbids divination and omens, which fits the Greek.
- **A:** keep the Hebrew and add a note giving the Greek.
- **B:** follow the Greek, with a note giving the Hebrew.

**Recommend A.** The Hebrew phrase is attested in 1 Samuel, and eating blood is a running law of this book (3:17, 7:26, 17:10–14).

**4. *tevel*, "a mixing" (18:23, 20:12).** These read *It is a mixing.* and *They have done a mixing.* The note at 18:23 explains that the word means running together things that belong apart, the same idea as the *two kinds* of 19:19.
- **A:** keep.
- **B:** *It is a perversion* / *They have committed a perversion*, with the note keeping *mixing*.

**Recommend A**, because it keeps the link to 19:19. B reads more smoothly.

Still open from earlier: *qeri* (26:21–41), the shekel wording, and the optional 23:11 note.

### Left standing on purpose

- **"uncover the nakedness"** (chapters 18, 20): kept identical all 24 times. It carries *It is your father's nakedness* (18:8), and the note at 18:6 explains the idiom.
- **"whose hand was filled"** (16:32, 21:10): the ordination idiom, kept as in Exodus 29 and Numbers 3:3.
- **"the marked man"** (13:4 and after): the Hebrew calls the person *the mark*; the 13:4 note is built on it.
- **Notes built on the wording:** *a gathering of water* (11:36, which echoes Genesis 1:10), *produces seed* (12:2), *His own hands shall bring* (7:30), *the priest who offers it for sin* (6:26), *keep the LORD's watch* (8:35), *be paid its sabbaths… pay for their guilt* (26:34, 43), and *your staff of bread* (26:26).
- **"stand on the blood of your neighbor"** (19:16): the Hebrew is unclear, and the note gives the range.
- **"searched and searched"** (10:16): natural English, and the note explains the doubling.

### A question, not a change

Almost every verse opens with *And*, which is Hebrew's joining letter. In the laws it piles up: *And the priest shall… And he shall… And…*. Dropping it where it adds nothing is the biggest smoothing left. But it would change every book, including Genesis, which is closed. Should I try it on one chapter so you can see it?

### Changes made (308)

#### Leviticus 1 (11)

| Verse | Before | After |
|---|---|---|
| 2 | you shall bring **your offering** from the livestock | you shall bring **it** from the livestock |
| 3 | He shall bring it to the entrance of the tent of meeting, **for his acceptance** before the LORD. | He shall bring it to the entrance of the tent of meeting, **so that he may be accepted** before the LORD. |
| 5 | shall bring the blood and dash **the blood** against the altar all around | shall bring the blood and dash **it** against the altar all around |
| 6 | And he shall skin the burnt offering and cut it into **its** pieces. | And he shall skin the burnt offering and cut it into pieces. |
| 8, 12 | on the wood **that is on the fire that is** on the altar. | on the wood **burning** on the altar. |
| 9 | **And** its entrails and its legs **he shall wash** with water, and the priest | **He shall wash** its entrails and its legs with water, and the priest |
| 10 | And if his offering is from the flock, from the sheep or from the goats, **for a burnt offering,** he shall bring | And if his **burnt** offering is from the flock, from the sheep or from the goats, he shall bring |
| 12 | And he shall cut it into **its** pieces, with its head | And he shall cut it into pieces, with its head |
| 13 | **And** the entrails and the legs **he shall wash** with water, and the priest | **He shall wash** the entrails and the legs with water, and the priest |
| 15 | against the **wall** of the altar. | against the **side** of the altar. |
| 17 | on the altar, on the **wood that is on the fire.** | on the altar, on the **burning wood.** |

#### Leviticus 2 (8)

| Verse | Before | After |
|---|---|---|
| 1 | brings **an offering of** a grain offering to the LORD | brings a grain offering to the LORD |
| 2 | and one shall scoop out **from it his** handful of its fine flour and **of its** oil, with all its frankincense, | and one **of them** shall scoop out **a** handful of its fine flour and oil, with all its frankincense, |
| 3, 10 | most holy, from the offerings by **fire of the LORD.** | most holy, from the **LORD's** offerings by **fire.** |
| 4 | bring **an offering of** a grain offering baked in an oven | bring a grain offering baked in an oven |
| 8 | the grain offering **that is** made from these | the grain offering made from these |
| 9 | And the priest shall lift **up** from the grain offering **its memorial portion** and turn it | And the priest shall lift **its memorial portion** from the grain offering and turn it |
| 13 | And every **offering of your** grain offering **you shall salt** with salt. | And **you shall season** every grain offering with salt. |
| 14 | crushed **grain of the** fresh **ear,** as your grain offering | crushed fresh **grain,** as your grain offering |

#### Leviticus 3 (3)

| Verse | Before | After |
|---|---|---|
| 3, 9, 14 | the fat **that covers** the **entrails,** and all the fat **that is** on the entrails, | the fat **covering** the **entrails** and all the fat on the entrails, |
| 4, 10, 15 | and the two kidneys **and** the fat **that is** on **them, which is on** the **loins;** and the lobe **on** the liver, which he shall remove with the kidneys | and the two kidneys **with** the fat on **them at** the **loins,** and the lobe **of** the liver, which he shall remove with the kidneys |
| 5 | on top of the burnt offering **that is** on the wood **that is on the fire** | on top of the burnt offering on the **burning** wood |

#### Leviticus 4 (20)

| Verse | Before | After |
|---|---|---|
| 3 | then **he shall bring** for the sin he has **sinned** an unblemished young bull to the LORD as a sin offering. | then for the sin he has **committed he shall bring** an unblemished young bull to the LORD as a sin offering. |
| 4 | and lean his hand on **the** head **of the bull,** and slaughter **the bull** before the LORD. | and lean his hand on **its** head and slaughter **it** before the LORD. |
| 6 | and sprinkle some of **the blood** seven times before the LORD | and sprinkle some of **it** seven times before the LORD |
| 7 | on the horns of the altar of fragrant incense before the **LORD, which is** in the tent of meeting; and all the rest of the bull's blood **he shall pour out** at the base of the altar of burnt **offering, which is** at the entrance of the tent of meeting. | on the horns of the altar of fragrant incense **that stands** before the **LORD** in the tent of meeting; and **he shall pour out** all the rest of the bull's blood at the base of the altar of burnt **offering** at the entrance of the tent of meeting. |
| 8 | And all the fat of the bull of the sin **offering he shall lift off it:** the fat **that covers** the entrails and all the fat **that is** on the entrails, | And **he shall lift off** all the fat of the bull of the sin **offering:** the fat **covering** the entrails and all the fat on the entrails, |
| 9 | and the two kidneys **and** the fat **that is** on **them, which is on** the **loins;** and the lobe **on** the liver, which he shall remove with the kidneys | and the two kidneys **with** the fat on **them at** the **loins,** and the lobe **of** the liver, which he shall remove with the kidneys |
| 12 | and burn it on wood **with** fire. | and burn it on **a** wood fire. |
| 14 | when the sin they **sinned** becomes known, the congregation shall **bring** a young bull as a sin offering and bring it before the tent of meeting. | when the sin they **have committed** becomes known, the congregation shall **offer** a young bull as a sin offering and bring it before the tent of meeting. |
| 15 | lean their hands on the head **of the bull** before the LORD, and **the bull** shall be slaughtered before the LORD. | lean their hands on the **bull's** head before the LORD, and **it** shall be slaughtered before the LORD. |
| 18 | on the horns of the altar that **is** before the **LORD, which is** in the tent of meeting; and all the rest of the blood **he shall pour out** at the base of the altar of burnt **offering, which is** at the entrance of the tent of meeting. | on the horns of the altar that **stands** before the **LORD** in the tent of meeting; and **he shall pour out** all the rest of the blood at the base of the altar of burnt **offering** at the entrance of the tent of meeting. |
| 19 | And **all its fat** he shall lift off **it** and turn into smoke on the altar. | And he shall lift off **all its fat** and turn **it** into smoke on the altar. |
| 20 | **And he** shall do **to the** bull as he did **to** the bull of the sin **offering; so shall he do to it.** | **He** shall do **with this** bull **just** as he did **with** the bull of the sin **offering.** |
| 23, 28 | or if **his** sin **that** he **sinned** is made known to him | or if **the** sin he **has committed** is made known to him |
| 25 | and its blood **he shall pour out** at the base of the altar of burnt offering. | and **pour out** its blood at the base of the altar of burnt offering. |
| 26 | **And** all its fat **he shall turn** into smoke on the altar, | **He shall turn** all its fat into smoke on the altar, |
| 27 | And if **one person** from the people of the land sins by mistake | And if **anyone** from the people of the land sins by mistake |
| 28 | an unblemished female goat for **the sin he sinned.** | an unblemished female goat for **his sin.** |
| 30, 34 | and all the rest of its blood **he shall pour out** at the base of the altar. | and **pour out** all the rest of its blood at the base of the altar. |
| 31 | **And** all its **fat he shall remove,** as the fat is removed from the peace offering, | **He shall remove** all its **fat,** as the fat is removed from the peace offering, |
| 35 | **And** all its **fat he shall remove,** as the fat of the sheep is removed from the peace offering, and the priest shall turn **them** into smoke on the altar, on the offerings by **fire of the LORD.** And the priest shall make atonement for him for **his** sin **that** he **sinned,** | **He shall remove** all its **fat,** as the fat of the sheep is removed from the peace offering, and the priest shall turn **it** into smoke on the altar, on **top of** the **LORD's** offerings by **fire.** And the priest shall make atonement for him for **the** sin he **has committed,** |

#### Leviticus 5 (15)

| Verse | Before | After |
|---|---|---|
| 1 | if he does not tell it, he **bears** his guilt. | if he does not tell it, he **carries** his guilt. |
| 2 | whether the carcass of an unclean wild **animal or the carcass** of unclean **livestock** or **the carcass** of an unclean swarming thing, | whether the carcass of an unclean wild **animal,** of unclean **livestock,** or of an unclean swarming thing, |
| 5 | he shall confess **what** he has **sinned in,** | he shall confess **how** he has **sinned,** |
| 6 | to the LORD for the sin he **sinned** — | to the LORD for the sin he **has committed** — |
| section heading above v7 | ## If **His Hand** Cannot **Reach It** | ## If **He** Cannot **Afford a Lamb** |
| 7 | And if **his hand** cannot **reach the cost of** a lamb, he shall bring as his guilt offering for **what he sinned** two turtledoves | And if **he** cannot **afford** a lamb, he shall bring as his guilt offering for **his sin** two turtledoves |
| 9 | on the **wall** of the altar | on the **side** of the altar |
| 10 | And the second **he shall make** a burnt **offering** according to the rule. And the priest shall make atonement for him for the sin he **sinned,** | And **he shall offer** the second **as** a burnt **offering,** according to the rule. And the priest shall make atonement for him for the sin he **has committed,** |
| 11 | And if **his hand** cannot **reach** two turtledoves or two young pigeons, he shall bring as his offering for **what he sinned** a tenth | And if **he** cannot **afford** two turtledoves or two young pigeons, he shall bring as his offering for **his sin** a tenth |
| 12 | and the priest shall scoop out **from** it **his handful** as its memorial portion and turn it into smoke on the altar, on the offerings by **fire of the LORD.** | and the priest shall scoop out **a handful of** it as its memorial portion and turn it into smoke on the altar, on **top of** the **LORD's** offerings by **fire.** |
| 13 | for the sin he **sinned** in any one of these, and he shall be forgiven. And **it** shall be the priest's, like the grain offering. | for the sin he **has committed** in any one of these, and he shall be forgiven. And **the rest** shall be the priest's, like the grain offering. |
| 15 | he shall bring his guilt offering **to the LORD —** an unblemished ram from the flock, at **your valuation** in silver **shekels** by the shekel of the holy **place — as a guilt offering.** | he shall bring **to the LORD as** his guilt offering an unblemished ram from the flock, at **the set value** in silver **shekels,** by the shekel of the holy **place.** |
| 16 | And **what he sinned against the holy thing he shall repay, and he shall** add a fifth to it **and** give it to the priest. | And **he shall make restitution for his sin against the holy thing,** add a fifth to it, **and** give it to the priest. |
| 17 | he is guilty and **bears** his guilt. | he is guilty and **carries** his guilt. |
| 18 | And he shall bring an unblemished ram from the flock, at **your valuation,** as a guilt **offering, to the priest.** | And he shall bring **to the priest** an unblemished ram from the flock, at **the set value,** as a guilt **offering.** |

#### Leviticus 6 (13)

| Verse | Before | After |
|---|---|---|
| 2 | or something he seized by **force;** or he **has defrauded** his neighbor; | or something he seized by **force,** or he **defrauds** his neighbor; |
| 3 | or he **found** something lost and **lied** about it, and **swore** falsely — in any one of all the things a man may do and **sin by doing:** | or he **finds** something lost and **lies** about it, and **swears** falsely — in any one of all the things a man may do and **so sin:** |
| 6 | And he shall bring his guilt offering to the **LORD —** an unblemished ram from the **flock,** at **your valuation — to** the **priest, as a guilt offering.** | And he shall bring **to the priest, as** his guilt offering to the **LORD,** an unblemished ram from the **flock** at the **set value.** |
| 7 | and he shall be forgiven for any **one** of **all** the things a man may do **and incur guilt by."** | and he shall be forgiven for any of the things a man may do **to become guilty."** |
| 9 | This is the instruction for the burnt **offering. The burnt offering itself** shall stay on the hearth | This is the instruction for the burnt **offering: it** shall stay on the hearth |
| 11 | And he shall take off **his** garments and put on **other garments,** | And he shall take off **these** garments and put on **others,** |
| 12 | And the fire on the altar shall be kept **burning on it;** it shall not go out. **And** the priest shall burn wood on **it morning by morning, and arrange** the burnt offering on it, and turn **into smoke on it** the fat of the peace **offerings.** | And the fire on the altar shall be kept **burning;** it shall not go out. **Every morning** the priest shall burn wood on **it, lay out** the burnt offering on it, and turn the fat of the peace **offerings into smoke on it.** |
| 15 | And one shall lift **from it his** handful **—** of the fine flour of the grain **offering and of its oil, and** all the frankincense **that is** on **the grain offering —** and turn | And one **of them** shall lift **out a** handful of the fine flour **and oil** of the grain **offering, with** all the frankincense on **it,** and turn |
| 16 | **And what is left of it** Aaron and his sons shall **eat.** It shall be eaten unleavened in a holy place; in the court of the tent of **meeting they shall eat it.** | Aaron and his sons shall **eat what is left of it.** It shall be eaten unleavened in a holy place; **they shall eat it** in the court of the tent of **meeting.** |
| 18 | from the offerings by **fire of the LORD.** | from the **LORD's** offerings by **fire.** |
| 22 | It is a lasting statute: **to the LORD** it shall go up in smoke whole. | It is a lasting statute: it shall go up in smoke **to the LORD,** whole. |
| 25 | **In** the place where the burnt offering is **slaughtered the sin offering shall be slaughtered, before the LORD.** | **The sin offering shall be slaughtered before the LORD in** the place where the burnt offering is **slaughtered.** |
| 28 | **And an earthen vessel** in which it was boiled shall be broken; and if it was boiled in a bronze **vessel,** | **A clay pot** in which it was boiled shall be broken; and if it was boiled in a bronze **pot,** |

#### Leviticus 7 (13)

| Verse | Before | After |
|---|---|---|
| 2 | **In** the place where they slaughter the burnt **offering they shall slaughter the guilt** offering, | **They shall slaughter the guilt offering in** the place where they slaughter the burnt offering, |
| 3 | **And** all its **fat he shall bring from it:** the fat tail, **and** the fat **that covers** the entrails, | **He shall offer** all its **fat:** the fat tail, the fat **covering** the entrails, |
| 4 | and the two kidneys **and** the fat **that is** on **them, which is on** the **loins;** and the lobe **on** the liver, which he shall remove with the kidneys | and the two kidneys **with** the fat on **them at** the **loins,** and the lobe **of** the liver, which he shall remove with the kidneys |
| 8 | And the priest who presents **any** man's burnt offering **—** the hide of the burnt offering he **presented belongs to that priest himself.** | And the priest who presents **a** man's burnt offering **shall have for himself** the hide of the burnt offering he **presented.** |
| 18 | and the person who eats it **bears** his guilt. | and the person who eats it **carries** his guilt. |
| 19 | **As for the flesh,** anyone who is clean may eat **it.** | **Otherwise,** anyone who is clean may eat **the flesh.** |
| 20 | while **his uncleanness** is **on him** | while **he** is **unclean** |
| 29 | Whoever **brings his** peace offering to the LORD shall bring his offering to the **LORD from his peace offering.** | Whoever **offers a** peace offering to the LORD shall bring **from it** his offering to the **LORD.** |
| 30 | His own hands shall bring the offerings by **fire of the LORD.** | His own hands shall bring the **LORD's** offerings by **fire.** |
| 32 | **And** the right thigh **you shall give** to the priest as a contribution from your peace offerings. | **You shall give** the right thigh to the priest as a contribution from your peace offerings. |
| 33 | The **one among Aaron's sons** who presents the blood of the peace **offering and the fat — the right thigh shall be his as his share.** | The **right thigh shall be the share of the son of Aaron** who presents the blood **and the fat** of the peace **offering.** |
| 34 | For the breast that is waved and the thigh that is lifted off **I have taken** from the sons of Israel, from their peace offerings, and **I** have given them | For **I have taken** the breast that is waved and the thigh that is lifted off from the sons of Israel, from their peace offerings, and have given them |
| 35 | This is the share that comes with the anointing of Aaron and **the anointing** of his sons, **out of** the offerings by **fire of the LORD,** | This is the share that comes with the anointing of Aaron and of his sons, **from** the **LORD's** offerings by **fire,** |

#### Leviticus 8 (12)

| Verse | Before | After |
|---|---|---|
| 7 | And he put the tunic on **him** and tied | And he put the tunic on **Aaron** and tied |
| 9 | And he set the turban on his head, and **on the turban, at the front, he** set the gold plate, the holy crown, | And he set the turban on his head, and set the gold plate, the holy crown, **on the front of the turban,** |
| 14 | leaned their hands on **the head of the bull of the sin offering.** | leaned their hands on **its head.** |
| 15 | and he poured out the blood at the base of the **altar, and** set **it** apart, to make atonement for it. | and he poured out the blood at the base of the **altar. So he** set **the altar** apart, to make atonement for it. |
| 17 | And the bull **and** its **hide and** its flesh and its dung **he burned** in the fire outside the camp, | And **he burned** the bull **—** its **hide,** its flesh and its dung **—** in the fire outside the camp, |
| 20 | And the ram **he cut** into **its** pieces, and Moses turned the **head and** the pieces and the suet into smoke. | And **he cut** the ram into pieces, and Moses turned the **head,** the pieces and the suet into smoke. |
| 25 | the fat tail and all the fat **that was** on the entrails, | the fat tail and all the fat on the entrails, |
| 26 | And **out of** the basket of unleavened bread **that was** before the LORD he took one unleavened **loaf and** one loaf of oiled bread and one wafer, | And **from** the basket of unleavened bread before the LORD he took one unleavened **loaf,** one loaf of oiled bread and one wafer, |
| 29 | **From** the ram of **ordination it was Moses' share,** | **It was Moses' share of** the ram of **ordination,** |
| 30 | and sprinkled it on **Aaron, on** his garments, and on his sons and **on his sons' garments with him; and** he set apart **Aaron,** his garments, and his sons and **his sons'** garments with him. | and sprinkled it on **Aaron and** his garments, and on his sons and **their garments; so** he set apart **Aaron and** his garments, and his sons and **their** garments with him. |
| 32 | And **what** is left of the flesh and **of** the **bread you shall burn in the fire.** | And **you shall burn in the fire whatever** is left of the flesh and the **bread.** |
| 34 | **As** has been done **this day, the LORD has commanded to be done,** to make atonement for you. | **The LORD commanded what** has been done **today,** to make atonement for you. |

#### Leviticus 9 (10)

| Verse | Before | After |
|---|---|---|
| 5 | And they **took** what Moses commanded to the front of the tent of meeting, | And they **brought** what Moses **had** commanded to the front of the tent of meeting, |
| 7 | Come near to the altar and **make** your sin offering and your burnt offering, and make atonement for yourself and for the people; **and make** the offering **of the people** and make atonement for them, | Come near to the altar and **offer** your sin offering and your burnt offering, and make atonement for yourself and for the people; **then offer** the **people's** offering and make atonement for them, |
| 8 | slaughtered the calf of **the** sin **offering that was his own.** | slaughtered the calf of **his own** sin **offering.** |
| 9 | and put it on the horns of the altar, and poured out the **blood** at the base of the altar. | and put it on the horns of the altar, and poured out the **rest** at the base of the altar. |
| 10 | **And** the **fat and** the kidneys and the lobe from the **liver of the** sin **offering he turned into smoke on the altar,** | **He turned into smoke on** the **altar the fat,** the kidneys and the lobe **of the liver** from the sin **offering,** |
| 11 | And the flesh and the hide **he burned** in the fire outside the camp. | And **he burned** the flesh and the hide in the fire outside the camp. |
| 15 | **And** he **brought** the people's offering. He took the goat **of** the sin **offering that was for the people, and** slaughtered it, and offered it **for** sin like the **first one.** | **Then** he **presented** the people's offering. He took the **people's** goat **for** the sin **offering,** slaughtered it, and offered it **as a** sin **offering** like the **first.** |
| 16 | and **made** it according to the rule. | and **offered** it according to the rule. |
| 20 | and he turned **the fat pieces** into smoke on the altar. | and he turned **them** into smoke on the altar. |
| 21 | And the breasts and the right thigh **Aaron waved** before the LORD, | And **Aaron waved** the breasts and the right thigh before the LORD, |

#### Leviticus 10 (8)

| Verse | Before | After |
|---|---|---|
| 1 | each took his fire pan, **and** put fire in **them, and** laid incense on it, and **brought near** before the LORD strange fire, | each took his fire pan, put fire in **it,** laid incense on it, and **offered** before the LORD strange fire, |
| 3 | This is what the LORD **spoke, saying:** | This is what the LORD **spoke of when He said:** |
| 6 | Do not let your hair **go** loose | Do not let your hair **hang** loose |
| 6 | may weep for **the burning** the LORD has burned. | may weep for **those** the LORD has burned. |
| 10 | and so that you can separate **between** the holy **and** the ordinary, and **between** the unclean **and** the clean, | and so that you can separate the holy **from** the ordinary, and the unclean **from** the clean, |
| 12, 13 | from the offerings by fire **of the LORD** | from the **LORD's** offerings by fire |
| 14 | **And** the breast that was waved and the thigh that was lifted off **you shall eat** in a clean place | **You shall eat** the breast that was waved and the thigh that was lifted off in a clean place |
| 15 | **The** thigh that **was** lifted off and the breast that **was waved they shall bring** with the offerings by **fire of the fat pieces,** to wave before the LORD; | **They shall bring the** thigh that **is** lifted off and the breast that **is waved, together** with **the fat pieces for** the offerings by **fire,** to wave **them** before the LORD; |

#### Leviticus 11 (22)

| Verse | Before | After |
|---|---|---|
| 3 | **Whatever parts** the **hoof and** has **the hoof cleft** in **two** and brings up the **cud, among animals — that you may eat.** | **Among** the **animals, you may eat any that** has **a divided hoof, split** in **two,** and brings up the **cud.** |
| 4 | But **these** you shall not **eat, of** those that bring up the cud or **part the** hoof: the camel, because it brings up the cud but does not **part the** hoof | But you shall not **eat these, among** those that bring up the cud or **have a divided** hoof: the camel, because it brings up the cud but does not **have a divided** hoof |
| 5, 6 | because it brings up the cud but does not **part the** hoof — it is unclean for you; | because it brings up the cud but does not **have a divided** hoof — it is unclean for you; |
| 7 | because it **parts the hoof and** has **the hoof cleft** in two, but does not chew the cud | because it has **a divided hoof, split** in two, but does not chew the cud |
| 9 | **These** you may eat **of all that is in the water:** anything in the **water, in** the **seas and in the streams,** that has fins and **scales — those you may eat.** | **Of all that lives in the water** you may eat **these:** anything in the **seas or** the **streams** that has fins and **scales.** |
| 13 | And these you shall **loathe among the birds —** they shall not be eaten, they are loathsome: | And **among the birds,** these you shall **loathe;** they shall not be eaten, they are loathsome: |
| 15 | every **raven** of **every kind,** | every **kind** of **raven,** |
| 20 | that **goes** on **four** is loathsome to you. | that **walks** on **all fours** is loathsome to you. |
| 21 | But **these** you may eat **of every winged swarming thing that goes on four:** those that have jointed legs above their **feet,** for leaping **with them** on the ground. | But **among the winged swarming things that walk on all fours,** you may eat those that have jointed legs above their **feet** for leaping on the ground. |
| 22 | **These of them** you may eat: | **Of these** you may eat: |
| 26 | every animal that **parts the** hoof but **does** not **have it cleft** in two, | every animal that **has a divided** hoof but not **split** in two, |
| 27 | And every creature that **goes** on its paws, among all the creatures that **go** on **four,** | And every creature that **walks** on its paws, among all the creatures that **walk** on **all fours,** |
| 29 | among the **swarming** things that swarm on the ground: | among the things that swarm on the ground: |
| 31 | These are the unclean for you among all the swarming things. | These are the **ones** unclean for you among all the swarming things. |
| 32 | any **vessel** of wood, or clothing, or hide, or **sackcloth,** any **vessel that work is done with.** | any **article** of wood, or clothing, or hide, or **sackcloth —** any **article used for work.** |
| 33 | And **every earthen vessel that** any of them falls into **—** everything in it becomes unclean, and you shall break **it.** | And **if** any of them falls into **a clay pot,** everything in it becomes unclean, and you shall break **the pot.** |
| 37 | on any seed **for sowing** that is to be sown, | on any seed that is to be sown, |
| 41 | And **every swarming thing** that swarms on the ground is loathsome. | And **everything** that swarms on the ground is loathsome. |
| 42 | Whatever **goes** on its belly, **and** whatever **goes** on **four, up to** whatever has many feet — **every swarming thing** that swarms on the ground — | Whatever **moves** on its belly, whatever **walks** on **all fours,** whatever has many feet — **anything** that swarms on the ground — |
| 43 | with **any swarming thing** that swarms, | with **anything** that swarms, |
| 45 | to be **God to you.** | to be **your God.** |
| 47 | to separate **between** the unclean **and** the clean, and **between** the creature that may be eaten **and** the creature that may not be eaten. | to separate the unclean **from** the clean, and the creature that may be eaten **from** the creature that may not be eaten. |

#### Leviticus 12 (1)

| Verse | Before | After |
|---|---|---|
| 8 | And if **her hand** cannot **find enough for** a lamb, | And if **she** cannot **afford** a lamb, |

#### Leviticus 13 (13)

| Verse | Before | After |
|---|---|---|
| 2 | When a person has **on the skin of his body** a swelling or a scab or a bright **spot, and it becomes** on the skin of his **body** a mark of **blight,** | When a person has a swelling or a scab or a bright **spot** on the skin of his **body, and it becomes** a mark of **blight on his skin,** |
| 5, 54 | **a second** seven days | **another** seven days |
| 11 | **He** shall not shut him away, because he is unclean. | **The priest** shall not shut him away, because he is unclean. |
| 12 | and **the blight** covers all the skin of the marked man | and covers all the skin of the marked man |
| 13 | he shall declare the **mark** clean. It has all turned white | he shall declare the **marked man** clean. It has all turned white |
| 16 | **Or** if the raw flesh **turns** back and **becomes** white, | **But** if the raw flesh **changes** back and **turns** white, |
| 17 | the priest shall declare the **mark** clean. He is clean. | the priest shall declare the **marked man** clean. He is clean. |
| 24 | Or when **there is** a burn **from fire** on the skin of **someone's** body, | Or when **someone has** a burn on the skin of **his** body, |
| 33 | and the priest shall shut **the patch** away **a second** seven days. | and the priest shall shut **him** away **another** seven days. |
| 35 | But if the scaly patch **does keep** spreading in the skin | But if the scaly patch **keeps** spreading in the skin |
| 54 | then the priest shall **give orders, and they shall wash** the thing **that has** the mark on **it,** and he shall shut it away | then the priest shall **order that** the thing **with** the mark on **it be washed,** and he shall shut it away |
| 57 | You shall burn in the fire **the thing that** has the mark on it. | You shall burn in the fire **whatever** has the mark on it. |
| 58 | And the garment, or the warp or the weft, or any leather **object that you wash** and the mark leaves it, shall be washed a second time, and it **is** clean. | And **if you wash** the garment, or the warp or the weft, or any leather **object,** and the mark leaves it, **it** shall be washed a second time, and it **will be** clean. |

#### Leviticus 14 (27)

| Verse | Before | After |
|---|---|---|
| 4 | the priest shall **give orders, and** two live clean birds **shall** be taken for the one being cleansed, **and** cedar wood, **and** scarlet **yarn,** and hyssop. | the priest shall **order that** two live clean birds be taken for the one being cleansed, **with** cedar wood, scarlet **yarn** and hyssop. |
| 5 | And the priest shall **give orders, and** one **bird shall** be slaughtered into **an earthen vessel** over fresh running water. | And the priest shall **order that** one **of the birds** be slaughtered into **a clay pot,** over fresh running water. |
| 6 | He shall take the live **bird, and** the cedar wood, **and** the scarlet **yarn,** and the hyssop, and dip them **and the live bird** in the blood | He shall take the live **bird with** the cedar wood, the scarlet **yarn** and the hyssop, and dip them **all** in the blood |
| 9 | all his **hair:** his **head and** his beard and his **eyebrows — all his hair he shall shave.** | all his **hair —** his **head,** his beard and his **eyebrows, every hair.** |
| 14 | And the priest shall take some of the blood of the guilt **offering,** and **the priest shall** put it on | And the priest shall take some of the blood of the guilt **offering** and put it on |
| 15, 26 | into **the priest's** own left palm, | into **his** own left palm, |
| 16 | and **the priest shall** dip his right finger in the oil **that is** on his left palm and sprinkle some of **the oil** with his finger seven times | and dip his right finger in the oil on his left palm and sprinkle some of **it** with his finger seven times |
| 17 | And **some of the rest of** the oil **on** his palm the priest shall put on the lobe | And **from** the oil **left in** his palm the priest shall put **some** on the lobe |
| 18, 29 | And what is left of the oil **on the priest's** palm **he shall put** on the head | And **he shall put** what is left of the oil **in his** palm on the head |
| 19 | And the priest shall **make** the sin offering | And the priest shall **offer** the sin offering |
| 21 | And if he is poor and **his hand** cannot **reach** so **far,** | And if he is poor and cannot **afford** so **much,** |
| 22 | whichever **his hand** can **reach** — one shall be | whichever **he** can **afford** — one shall be |
| 24 | and **the priest shall** wave them before the LORD. | and wave them before the LORD. |
| 27 | and **the priest shall sprinkle** with his right finger some of the oil **that is on** his left palm seven times before the LORD. | and with his right finger **sprinkle** some of the oil **in** his left palm seven times before the LORD. |
| 28 | And the priest shall put some **of the oil on his palm** on the lobe | And **from the oil in his palm** the priest shall put some on the lobe |
| 30 | And he shall offer **one of** the turtledoves or **of** the young pigeons, whichever **his hand** can **reach** — | And he shall offer the turtledoves or the young pigeons, whichever **he** can **afford** — |
| 31 | **whichever his hand can reach,** one as a sin offering | one as a sin offering |
| 32 | **whose hand** cannot **reach** the **cost of** his cleansing. | **who** cannot **afford** the **full offering for** his cleansing. |
| 35 | the **one who owns** the house shall come and tell the priest, **saying,** 'Something like a mark has appeared **to me** in **the** house.' | the **owner of** the house shall come and tell the priest, 'Something like a mark has appeared in **my** house.' |
| 36 | And the priest shall **give orders, and they shall empty** the house before **the priest comes** in to look at the mark, so that **everything** in the house **does not become** unclean. **And after** that the priest shall **come** in to look at the house. | And the priest shall **order** the house **emptied** before **he goes** in to look at the mark, so that **nothing** in the house **becomes** unclean. **After** that the priest shall **go** in to look at the house. |
| 38 | the priest shall go out of the house to **the** doorway **of the house** and shut **the house** up for seven days. | the priest shall go out of the house to **its** doorway and shut **it** up for seven days. |
| 40 | the priest shall **give orders, and they shall pull out** the stones **that have** the mark in them and **throw them** outside the city, to an unclean place. | the priest shall **order that** the stones **with** the mark in them **be pulled out and thrown** outside the city, to an unclean place. |
| 41 | scraped all **round** inside | scraped all **around** inside |
| 42 | And they shall take other stones and put them in place of **those stones,** and he shall take **other** plaster and **plaster** the house. | And they shall take other stones and put them in place of **the old ones,** and he shall take **fresh** plaster and **replaster** the house. |
| 48 | But if the priest **does come** and **look,** | But if the priest **comes** and **looks,** |
| 50 | And he shall slaughter one **bird** into **an earthen vessel** over fresh running water, | And he shall slaughter one **of the birds** into **a clay pot,** over fresh running water, |
| 57 | to **give direction on the day** something is unclean and **on the day** it is clean. | to **teach when** something is unclean and **when** it is clean. |

#### Leviticus 15 (9)

| Verse | Before | After |
|---|---|---|
| 3 | And this is his **uncleanness in his discharge:** whether his body runs with **the discharge** or **his body** is stopped up **from the discharge, it** is **his uncleanness.** | And this is **how** his **discharge makes him unclean:** whether his body runs with **it** or is stopped up **by it, he** is **unclean.** |
| 11 | And **anyone** the man with the discharge touches without **having rinsed** his hands in **water** shall wash his clothes | And **if** the man with the discharge touches **anyone** without **first rinsing** his hands in **water, that person** shall wash his clothes |
| 12 | **And an earthen vessel** the man with the discharge touches shall be broken, | **A clay pot that** the man with the discharge touches shall be broken, |
| 15 | and **the priest shall** make atonement for him before the LORD for his discharge. | and make atonement for him before the LORD for his discharge. |
| 18 | And **a woman** a man lies **with,** with an emission of **semen —** they shall both bathe in water, | And **when** a man lies with **a woman and has** an emission of **semen,** they shall both bathe in water, |
| 23 | **And if it** is on **the bed,** or on whatever she is sitting on, **when he** touches **it, he** shall be unclean until evening. | **If anything** is on **her bed** or on whatever she is sitting on, **whoever** touches **it** shall be unclean until evening. |
| 24 | And if a man **does lie** with her | And if a man **lies** with her |
| 27 | And anyone who touches **them** shall be unclean, | And anyone who touches **these things** shall be unclean, |
| 30 | and **the priest shall** make atonement for her before the LORD for her unclean flow. | and make atonement for her before the LORD for her unclean flow. |

#### Leviticus 16 (15)

| Verse | Before | After |
|---|---|---|
| 2 | **Speak to** Aaron your **brother,** that he **is** not **to** come at just any time into the holy place inside the veil, in front of the cover **that is** on the ark, | **Tell** Aaron your **brother** that he **must** not come at just any time into the holy place inside the veil, in front of the cover on the ark, |
| 3 | **With this** Aaron shall come into the holy place: with a bull **calf** for a sin offering | **This is how** Aaron shall come into the holy place: with a **young** bull for a sin offering |
| 6 | And Aaron shall present **the** bull **of** the sin offering **that is his own,** and make atonement for himself and for his household. | And Aaron shall present **his own** bull **for** the sin offering and make atonement for himself and for his household. |
| 9 | and **make** it a sin offering. | and **offer** it **as** a sin offering. |
| 11 | And Aaron shall present **the** bull **of** the sin offering **that is his own,** and make atonement for himself and for his **household, and** he shall slaughter **the** bull **of** the sin **offering that is his own.** | And Aaron shall present **his own** bull **for** the sin offering and make atonement for himself and for his **household;** he shall slaughter **his own** bull **for** the sin **offering.** |
| 12 | a fire pan full of coals **of fire** from the altar before the LORD, and **his** two **hands full** of finely ground fragrant incense, | a fire pan full of **burning** coals from the altar before the LORD, and two **handfuls** of finely ground fragrant incense, |
| 13 | and the cloud of the incense shall **cover** the cover that is over the Testimony, | and the cloud of the incense shall **hide** the cover that is over the Testimony, |
| 14 | and **in front of the cover** he shall sprinkle some of the blood seven times with his **finger.** | and he shall sprinkle some of the blood seven times with his **finger in front of the cover.** |
| 15 | And he shall slaughter the goat **of** the sin offering **that is for the people** | And he shall slaughter the **people's** goat **for** the sin offering |
| 16 | because of the **uncleannesses** of the sons of Israel | because of the **uncleanness** of the sons of Israel |
| 16 | in the middle of their **uncleannesses.** | in the middle of their **uncleanness.** |
| 19 | and cleanse it **and set it apart** from the **uncleannesses** of the sons of **Israel.** | and cleanse it from the **uncleanness** of the sons of **Israel and set it apart.** |
| 24 | and come out and **make** his burnt offering and the burnt **offering of the people,** | and come out and **offer** his burnt offering and the **people's** burnt **offering,** |
| 25 | And the fat of the sin offering **he shall turn** into smoke on the altar. | And **he shall turn** the fat of the sin offering into smoke on the altar. |
| 33 | and make atonement for the most holy **place; and** for the tent of meeting and for the **altar** he shall make **atonement; and** for the priests and for all the people of the **assembly he shall make atonement.** | and make atonement for the most holy **place,** for the tent of meeting and for the **altar; and** he shall make **atonement** for the priests and for all the people of the **assembly.** |

#### Leviticus 17 (7)

| Verse | Before | After |
|---|---|---|
| 5 | This is so that the sons of Israel will **bring their sacrifices, which** they have been **sacrificing** out in the open **field,** and bring them to the LORD, to the entrance of the tent of meeting, to the priest, and **sacrifice** them as peace offerings to the LORD. | This is so that the sons of Israel will **take the sacrifices** they have been **making** out in the open **field** and bring them to the LORD, to the entrance of the tent of meeting, to the priest, and **offer** them as peace offerings to the LORD. |
| 7 | And they shall no longer **sacrifice** their sacrifices to the goat-spirits they have been **whoring after.** | And they shall no longer **offer** their sacrifices to the goat-spirits they have been **prostituting themselves to.** |
| 9 | to **make** it **for** the LORD | to **offer** it **to** the LORD |
| 11 | **Because** the life of the flesh is in the blood, | **For** the life of the flesh is in the blood, |
| 11 | ; **because** it is the blood that makes atonement by the life. | ; **for** it is the blood that makes atonement by the life. |
| 14 | **Because** the life of all flesh — its blood is its life. | **For** the life of all flesh — its blood is its life. |
| 16 | he **bears** his guilt. | he **carries** his guilt. |

#### Leviticus 18 (9)

| Verse | Before | After |
|---|---|---|
| 4 | You shall **do** My **judgments** and keep My statutes**, to walk** in them. | You shall **carry out** My **rulings** and keep My statutes**, and walk** in them. |
| 5 | My statutes and My **judgments, which a** person shall **do and** live by them. | My statutes and My **judgments; the** person **who does them** shall live by them. |
| 5 | And you shall keep My statutes and My **judgments**; | And you shall keep My statutes and My **rulings**; |
| 20 | And you shall not **give your emission to** your neighbor's **wife, to** become unclean by her. | And you shall not **lie with** your neighbor's **wife and so** become unclean by her. |
| 23 | And you shall not **give your emission to** any **animal, to** become unclean by it; | And you shall not **lie with** any **animal and so** become unclean by it; |
| 25 | and I **called** its **guilt to account upon it,** | and I **punished it for** its **guilt,** |
| 26 | But you shall keep My statutes and My **judgments**, | But you shall keep My statutes and My **rulings**, |
| 28 | **And** the land will **not** vomit you out **when you make it unclean,** as it vomited out the nation that was before you. | **Otherwise, when you make** the land **unclean, it** will vomit you out as it vomited out the nation that was before you. |
| 29 | **Because anyone who** does any of these detestable things — **the people** who do them shall be cut off from among their people. | **For whoever** does any of these detestable things — **those** who do them shall be cut off from among their people. |

#### Leviticus 19 (14)

| Verse | Before | After |
|---|---|---|
| 6 | and what is left **over to** the third day | and what is left **until** the third day |
| 8 | And whoever eats it **bears** his guilt, | And whoever eats it **carries** his guilt, |
| 15 | You shall not favor **the face of** the poor **and you shall not** defer to the **face of the** great. | You shall not **show** favor **to** the poor **or** defer to the great. |
| 16 | You shall not go **about as a talebearer** among your people. | You shall not go **around spreading slander** among your people. |
| 17 | You shall **surely** correct your neighbor, | You shall **be sure to** correct your neighbor, |
| 19 | You shall not sow your field with two **kinds.** And a garment woven of two kinds **shall not come on you.** | You shall not sow your field with two **kinds of seed.** And **you shall not put on** a garment woven of two kinds **of material.** |
| 21 | — a ram **of** guilt offering. | — a ram **for a** guilt offering. |
| 22 | for the sin he **sinned;** and he shall be forgiven **of the sin he sinned.** | for the sin he **has committed;** and he shall be forgiven **for it.** |
| 26 | You shall not eat **over** the **blood.** | You shall not eat **anything with** the **blood in it.** |
| 27 | You shall not round off the **edge** of your head, | You shall not round off the **hair at the sides** of your head, |
| 29 | or the land will **become a prostitute** and **the land will** be **full of** depravity. | or the land will **turn to prostitution** and be **filled with** depravity. |
| 31 | **to be made** unclean by them. | **and so become** unclean by them. |
| 32 | You shall rise **before a gray head** and **give** honor **to** the **face of an old man;** | You shall rise **in the presence of the gray-haired** and honor the **old;** |
| 37 | and all My **judgments** and do them. | and all My **rulings** and do them. |

#### Leviticus 20 (15)

| Verse | Before | After |
|---|---|---|
| 2 | **"And** to the sons of **Israel you shall say:** | **"Say** to the sons of **Israel:** |
| 2 | The people of the land shall stone **him with stones.** | The people of the land shall stone **him.** |
| 3 | because he gave of his children to Molech, **to make** My sanctuary unclean and **to profane** My holy name. | because he gave of his children to Molech, **and so made** My sanctuary unclean and **profaned** My holy name. |
| 5 | him and all who **go whoring after him,** to **whore after** Molech. | him and all who **follow him in prostituting themselves** to Molech. |
| 6 | And the person who turns to ghosts and to spirits, **to whore after** them — | And the person who turns to ghosts and to spirits, **prostituting himself by following** them — |
| 9 | his blood is on **him.** | his blood is on **his own head.** |
| 11, 12, 13, 16, 27 | their blood is on **them.** | their blood is on **their own heads.** |
| 15 | And a man who **gives his emission to** an animal | And a man who **lies with** an animal |
| 17 | in the sight **of the sons** of their people. He has uncovered his sister's nakedness; he **bears** his guilt. | in the sight of their people. He has uncovered his sister's nakedness; he **carries** his guilt. |
| 19 | because that **is laying** bare his own flesh. They shall **bear** their guilt. | because that **lays** bare his own flesh. They shall **carry** their guilt. |
| 20 | They shall **bear** their sin; | They shall **carry** their sin; |
| 22 | and all My **judgments** and do them, | and all My **rulings** and do them, |
| 24 | and I will give it to you **to possess** — | and I will give it to you **as your own** — |
| 25 | And you shall separate **between** the clean animal **and** the unclean, and **between** the unclean bird **and** the clean, | And you shall separate the clean animal **from** the unclean, and the unclean bird **from** the clean, |
| 27 | They shall stone **them with stones;** | They shall stone **them;** |

#### Leviticus 21 (8)

| Verse | Before | After |
|---|---|---|
| 1 | **"Say** to the priests, the sons of Aaron, and say to them: | **"Speak** to the priests, the sons of Aaron, and say to them: |
| 2 | except for his **close** flesh — | except for his **own** flesh **closest to him** — |
| 6 | because they present the offerings by **fire of the LORD,** | because they present the **LORD's** offerings by **fire,** |
| 10 | shall not let his hair **go** loose | shall not let his hair **hang** loose |
| 11 | And he shall not go **in to** any dead body. | And he shall not go **near** any dead body. |
| 13 | And he shall take a **wife in her virginity.** | And he shall take **as his wife** a **woman who is a virgin.** |
| 21 | to present the offerings by **fire of the LORD.** | to present the **LORD's** offerings by **fire.** |
| 22 | **from** the most holy and **from** the holy. | **both** the most holy and the holy. |

#### Leviticus 22 (13)

| Verse | Before | After |
|---|---|---|
| 3 | while **his uncleanness** is **on him** | while **he** is **unclean** |
| 6 | the person who touches **it** shall be unclean until evening, | the person who touches **any of these** shall be unclean until evening, |
| 8 | **One** that died on its own or **one** torn by **beasts he shall not eat,** and so make himself unclean by it. | **He shall not eat an animal** that died on its own or **was** torn by **beasts,** and so make himself unclean by it. |
| 9 | so that they do not carry sin because of it and die for **it when they profane** it. | so that they do not carry sin because of it and die for **profaning** it. |
| 11 | But if a priest buys a **person, bought** with his money, **he** may eat of it, and those born in his **house —** they may eat of his bread. | But if a priest buys a **person** with his money, **that person** may eat of it, and **so may** those born in his **house;** they may eat of his bread. |
| 14 | and give the holy thing to the priest. | and give the holy thing **back** to the priest. |
| 19 | **so that it is** accepted for you, it must be an unblemished male, | **to be** accepted for you, it must be an unblemished male, |
| 23 | **An** ox or a sheep with a limb too long or too **short you may make into a freewill offering,** but **for a vow** it will not be **accepted.** | **You may offer as a freewill offering an** ox or a sheep with a limb too long or too **short,** but it will not be **accepted for a vow.** |
| 24 | **One** whose testicles are bruised, or crushed, or torn, or cut, **you shall not bring to the LORD,** | **You shall not offer to the LORD an animal** whose testicles are bruised, or crushed, or torn, or cut, |
| 25 | And **from the hand of a foreigner** you shall not **bring** any of these as the bread of your God, | And you shall not **take** any of these **from a foreigner and offer them** as the bread of your God, |
| 27 | it shall **be** seven days **under** its mother, | it shall **stay** seven days **with** its mother, |
| 28 | **And an** ox or **a sheep —** you shall not slaughter it and its young on the same day. | **Whether** ox or **sheep,** you shall not slaughter it and its young on the same day. |
| 29 | And when you **sacrifice** a thanksgiving sacrifice to the LORD, **sacrifice** it so that it is accepted for you. | And when you **offer** a thanksgiving sacrifice to the LORD, **offer** it so that it is accepted for you. |

#### Leviticus 23 (10)

| Verse | Before | After |
|---|---|---|
| 3 | **Six days work** may be **done,** | **Work** may be **done for six days,** |
| 8 | And you shall present an offering by fire to the LORD seven days. | And you shall present an offering by fire to the LORD **for** seven days. |
| 10 | you shall bring the sheaf **of the first** of your harvest to the priest. | you shall bring the **first** sheaf of your harvest to the priest. |
| 14 | **And** bread, **and** roasted **grain, and** fresh grain **you shall not eat** until that very day, | **You shall eat no** bread, roasted **grain or** fresh grain until that very day, |
| 15 | seven full **sabbaths there shall be.** | **there shall be** seven full **sabbaths.** |
| 20 | And the priest shall wave them with the bread of the **firstfruits as a wave offering before the LORD,** with the two lambs. | And the priest shall wave them **before the LORD** with the bread of the **firstfruits, together** with the two lambs. |
| 22 | you shall not reap all the way to the edge of your **field as you reap,** and you shall not gather the gleanings of your harvest. **For** the poor and for the **guest you shall leave them.** | you shall not reap all the way to the edge of your **field,** and you shall not gather the gleanings of your harvest. **You shall leave them for** the poor and for the **guest.** |
| 29 | For any person who **is** not **afflicted** on that very day | For any person who **does** not **afflict himself** on that very day |
| 36 | **Seven** days you shall present an offering by fire to the LORD. | **For seven** days you shall present an offering by fire to the LORD. |
| 42 | **In booths you** shall live seven days. Every native **in Israel** shall live in booths, | **You** shall live **in booths for** seven days. Every native **Israelite** shall live in booths, |

#### Leviticus 24 (3)

| Verse | Before | After |
|---|---|---|
| 9 | from the offerings by fire **of the LORD** — a lasting due. | from the **LORD's** offerings by fire — a lasting due. |
| 12 | until the **answer** should be made clear to **them by the mouth of the LORD.** | until the **LORD's decision** should be made clear to **them.** |
| 23 | and stoned **him with stones.** | and stoned **him.** |

#### Leviticus 25 (10)

| Verse | Before | After |
|---|---|---|
| 3 | **Six** years you shall sow your field, and six years you shall prune your vineyard and gather in its produce. | **For six** years you shall sow your field, and **for** six years you shall prune your vineyard and gather in its produce. |
| 4 | **Your field you** shall not **sow, and** your **vineyard you shall not prune.** | **You** shall not **sow** your **field or prune your vineyard.** |
| 5 | **What** grows by itself from your **harvest you shall not reap, and** the grapes of your untrimmed **vine you shall not gather.** | **You shall not reap what** grows by itself from your **harvest, or gather** the grapes of your untrimmed **vine.** |
| 10 | and you shall **return, each man** to his **holding,** and **each man** to his **family you shall return.** | and **each of** you shall **return** to his **holding** and to his **family.** |
| 14 | or buy from your **neighbor's hand,** | or buy from your **neighbor,** |
| 18 | and keep My **judgments** and do them, | and keep My **rulings** and do them, |
| 41 | and he shall return to his family, and **to the holding of his fathers he shall return.** | and he shall return to his family **and to the holding of his fathers.** |
| 44 | **As for your** male and female slaves **whom** you may have **—** from the nations around **you,** from them you may buy male and female slaves. | **The** male and female slaves you may have **are to come** from the nations around **you;** from them you may buy male and female slaves. |
| 50 | **As the days of a hired man it shall be with him.** | **His time with him shall be counted like the days of a hired man.** |
| 53 | **As** a man hired year by **year he shall be with him. He** shall not rule over him with crushing harshness in your sight. | **He shall be with the buyer like** a man hired year by **year, and the buyer** shall not rule over him with crushing harshness in your sight. |

#### Leviticus 26 (10)

| Verse | Before | After |
|---|---|---|
| 5 | Your threshing will **reach to** the grape harvest, and the grape harvest **will reach to** the sowing. You will eat your bread **to the full** | Your threshing will **last until** the grape harvest, and the grape harvest **until** the sowing. You will eat your **fill of** bread |
| 15 | and your soul abhors My **judgments**, | and your soul abhors My **rulings**, |
| 21 | I will **add blows to** you seven times over, as your sins deserve. | I will **strike** you **again,** seven times over, as your sins deserve. |
| 23 | And if **by** these things you will not **be corrected by Me,** | And if **even after** these things you will not **accept My discipline,** |
| 26 | ten women will bake your bread in one oven and **hand** out **your bread** by weight, | ten women will bake your bread in one oven and **ration it** out by weight, |
| 33 | And **you** I will scatter among the nations, | And I will scatter **you** among the nations, |
| 39 | and **also in** the guilt of their fathers they will rot away with them. | and **because of** the guilt of their fathers they will rot away with them. |
| 41 | if **then** their uncircumcised heart is **humbled,** and they **then** pay for their guilt, | if their uncircumcised heart is **humbled then,** and they pay for their guilt, |
| 43 | they rejected My **judgments** | they rejected My **rulings** |
| 46 | These are the statutes and the **judgments** and the laws | These are the statutes and the **rulings** and the laws |

#### Leviticus 27 (9)

| Verse | Before | After |
|---|---|---|
| 7 | And if **from** sixty years old **and up, if a male,** the valuation shall be fifteen shekels, and **for** a female ten shekels. | And if **the person is** sixty years old **or more,** the valuation **of a male** shall be fifteen shekels, and **of** a female ten shekels. |
| 16 | its valuation shall be by its seed: a homer of barley **seed at fifty shekels of silver.** | its valuation shall be by its seed: **fifty shekels of silver for** a homer of barley **seed.** |
| 17 | If he sets apart his field from the year of jubilee, | If he sets apart his field **starting** from the year of jubilee, |
| 18 | the priest shall **reckon** the **silver** for him by the years that remain until the year of jubilee, and it shall be **taken off** the valuation. | the priest shall **calculate** the **price** for him by the years that remain until the year of jubilee, and it shall be **deducted from** the valuation. |
| 20 | or if he has sold **the field** to another man, | or if he has sold **it** to another man, |
| 23 | the priest shall **reckon** for him the amount of the valuation up to the year of jubilee, and he shall **give** the valuation **on** that day as a holy **thing** to the LORD. | the priest shall **calculate** for him the amount of the valuation up to the year of jubilee, and he shall **pay** the valuation that **same** day as a holy **gift** to the LORD. |
| 26 | But a **firstling,** which as a **firstling** already belongs to the **LORD among the animals — no man shall set it apart.** | But **no one may set apart** a **firstborn animal,** which as a **firstborn** already belongs to the **LORD.** |
| 28 | But nothing **devoted** that a man devotes to the LORD from anything he has, | But nothing that a man devotes to the LORD from anything he has, |
| 30 | of the seed of the land and of the fruit of the tree, | **whether grain or the fruit of the trees,** |

#### Also changed, to match

| Where | Before | After |
|---|---|---|
| Numbers 5:17 | holy water in a clay **vessel** | holy water in a clay **pot** |

---

## *ger* = guest (2026-09-24)

### Your request (chat, 2026-09-24)

> I think guest is the right word here… a person staying inside someone's personal space… versatile enough for the law and for someone known to you.

### Changes made

**Tested against every verse first.** It holds, and in the stories it fits better than any alternative:
- Lot in Sodom: *This one came here as a guest* (Genesis 19:9).
- Jacob: *I have lived as a guest with Laban* (Genesis 32:4).
- Moses, taken in and fed by Jethro: *I have been a guest in a foreign land* (Exodus 2:22).
- Israel, which came into Egypt by Pharaoh's invitation (Genesis 45:18, 47:4): *you were guests in the land of Egypt* (Exodus 22:21).
- *You are guests and residents with Me* (Leviticus 25:23).

The core of *ger* is someone living under another people's protection, which is what a guest is.

**One weakness, carried in a note:** a *ger* could stay for generations (Leviticus 25:45), and "guest" usually sounds short-term. The Genesis 23:4 note now says "a guest who may stay for generations."

| Where | Before | After |
|---|---|---|
| Genesis 12:10; 15:13; 17:8; 19:9; 20:1; 21:23, 34; 23:4; 26:3; 28:4; 32:4; 35:27; 36:7; 37:1; 47:4, 9 | live(d) as a foreigner / foreigners | live(d) as a **guest** / **guests** |
| Exodus 2:22; 18:3 | I have been a foreigner in a foreign land | I have been a **guest** in a foreign land ("foreign" stays: it's a different word, *nokhriyyah*) |
| Exodus 6:4; 12:19, 48, 49; 20:10; 22:21; 23:9, 12 | foreigner(s) | **guest(s)** |
| Leviticus 16:29; 17:8, 10, 12, 13, 15; 18:26; 19:10, 33, 34; 20:2; 22:18; 23:22; 24:16, 22; 25:6, 23, 35, 45, 47 | foreigner(s) | **guest(s)** |
| Notes: Genesis 16:6, 23:4, 36:6–7; Exodus 2:19, 2:22, 12:49, 18:3–4, 22:21, 23:9; Leviticus 17, 19 (×2), 22:25, 25:23 | foreigner | guest (Exodus 2:22 and 22:21 notes rewritten; the old 22:21 note had a behind-the-curtain line, now removed) |
| RENDERING_SPEC | *gur* = live as a foreigner | ***ger* = guest; *gur* = live as a guest**; *ben nekhar* = foreigner |

**Unchanged on purpose:** the *ben nekhar* verses keep "foreigner" (Genesis 17:12, 17:27; Exodus 12:43; Leviticus 22:25), and so do "foreign gods" (Genesis 35:2, 4), "made himself a stranger" (Genesis 42:7) and "a foreign people" (Exodus 21:8). Those are all the *nekhar* word.

---

## *ger*: the verse list and word options (2026-09-24)

### Your request (chat, 2026-09-24)

> List the verses [for *ger*], and also give me a list of other possible words.

### Answer (nothing changed)

### Every *ger* verse rendered so far, and how it reads now

Two forms:
- **the noun** *ger*: a person
- **the verb** *gur*: to live as a *ger*, marked "(verb)"

| Verse | Reads now |
|---|---|
| Genesis 15:13 | your seed will **live as foreigners** in a land not theirs |
| Genesis 23:4 | "A **foreigner** and a resident I am among you" |
| Genesis 35:27 | where Abraham and Isaac had **lived as foreigners** (verb) |
| Exodus 2:22 | "I have been a **foreigner** in a foreign land" (Gershom's name) |
| Exodus 6:4 | the land where they **lived as foreigners** (verb) |
| Exodus 12:19 | whether a **foreigner** or a native of the land |
| Exodus 12:48 | when a **foreigner** lives with you and would keep the Passover |
| Exodus 12:49 | one law for the native and for the **foreigner** living among you |
| Exodus 18:3 | "I have been a **foreigner** in a foreign land" (Gershom again) |
| Exodus 20:10 | the **foreigner** who is inside your gates (Sabbath command) |
| Exodus 22:21 | you shall not wrong a **foreigner**… for you were **foreigners** in the land of Egypt |
| Exodus 23:9 | you shall not press down a **foreigner**, for you yourselves know |
| Exodus 23:12 | the son of your slave woman and the **foreigner** may draw breath |
| Leviticus 16:29 | neither the native nor the **foreigner** living among you |
| Leviticus 17:8, 10, 13 | of the **foreigners** living among them |
| Leviticus 17:12 | the **foreigner** living among you shall not eat blood |
| Leviticus 18:26 | neither the native nor the **foreigner** living among you |
| Leviticus 19:10 | for the poor and for the **foreigner** |
| Leviticus 19:33 | when a **foreigner** lives with you in your land |
| Leviticus 19:34 | the **foreigner** living with you shall be to you as a native… (you were **foreigners** in Egypt) |
| Leviticus 20:2 | of the **foreigners** living in Israel |
| Leviticus 22:18 | of the **foreigners** living in Israel |
| Leviticus 23:22 | for the poor and for the **foreigner** |
| Leviticus 24:16 | the **foreigner** as well as the native |
| Leviticus 24:22 | one law, for the **foreigner** and for the native alike |
| Leviticus 25:6 | your resident, who **live with you as foreigners** |
| Leviticus 25:23 | you are **foreigners** and residents with Me |
| Leviticus 25:35 | as a **foreigner** and a resident, he shall live with you |
| Leviticus 25:45 | the residents who **live with you as foreigners** |
| Leviticus 25:47 | if a **foreigner** or a resident with you prospers… sells himself to the **foreigner** |

Two more notes on the list:
- **Exodus 2:22 and 18:3.** Moses names his son *Gershom* from this word: *ger sham*, "a *ger* there". Whatever English word is chosen will sit in the pun on his name, and the note explains it.
- **The other languages.** The Greek mostly has *prosēlytos*, "one who has come over", in the laws, and *paroikos*, "one living beside", in the stories (Genesis 23:4; Exodus 20:10). The Latin has *advena*, "one who has come", or *peregrinus*, "pilgrim".

### Possible English words for *ger*

| Word | Fits? |
|---|---|
| **stranger** | the classic English word ("love the stranger, for you were strangers in Egypt"); reads naturally in laws and in Gershom's name; modern ear also hears "someone I don't know" |
| **immigrant** | exact modern meaning (came from elsewhere to live here); politically loaded today, and too modern for the text's style |
| **alien / resident alien** | legally exact; "alien" now suggests outer space; "resident" is taken by *toshav* |
| **newcomer** | captures "one who has come" (the Greek and Latin sense); too casual for law |
| **guest** | captures "living on someone else's land" (Leviticus 25:23, "you are guests with Me"); too light for the laws |
| **sojourner** | ruled out earlier: Bible English |
| **foreigner** | now taken by *ben nekhar* |
| **settler** | freed up; but "settler" suggests someone who takes land, the opposite of a *ger* |

**Recommendation: stranger.** It is the only candidate that works in all three places: the laws ("one law for the native and the stranger"), the stories ("strangers in a land not theirs"), and the verb ("where Abraham and Isaac lived as strangers"). It keeps the book's style. The verb would become "live as a stranger" everywhere, including the ruled phrase in RENDERING_SPEC ("live as a foreigner" → "live as a stranger").

---

## 23:24 and *ben nekhar* (2026-09-24)

### Your request (chat, 2026-09-24)

> 23:24 yes. For ben nekhar do we have any other possible words, and what do other languages translate it as?

### Changes made

| Where | Before | After |
|---|---|---|
| Leviticus 23:24 | a remembrance by a blast | a remembrance **with horn blasts** (note: the word also means a great shout) |

### ben nekhar: the other languages (checked in our Greek and Latin texts)

| Verse | Hebrew | Greek (Septuagint) | Latin (Vulgate) |
|---|---|---|---|
| Genesis 17:12 | *ben nekhar* | *allotrios*, "belonging to another" | *de stirpe* (paraphrased: "not of your stock") |
| Genesis 17:27 | *ben nekhar* | *allogenēs*, "of another birth" | *alienigena*, "born elsewhere" |
| Exodus 12:43 | *ben nekhar* | *allogenēs* | *alienigena* |
| Leviticus 22:25 | *ben nekhar* | *allogenēs* | *alienigena* |

For comparison, the other two words:
- ***ger*:** the Greek has *prosēlytos*, "one who has come over" (Exodus 12:48; Leviticus 19:34), which gives English *proselyte*, or *paroikos*, "one living beside" (Genesis 23:4). The Latin has *advena*, "one who has come", or *peregrinus*, the root of English *pilgrim*.
- ***zar* (Leviticus 22:10):** the Greek uses the same *allogenēs*. So the Greek blurs *zar* and *ben nekhar*, and the Hebrew keeps them apart.

Jesus uses *allogenēs* once: of the one healed leper who came back to give thanks, *this foreigner* (Luke 17:18).

**All three ancient languages say the same thing: *a person born of another people*.** It carries no sense of traveling and no sense of being unauthorized.

### English candidates for ben nekhar

| Word | Fits? |
|---|---|
| **foreigner** | exactly the meaning; plain; what the Greek and Latin say |
| alien | Latin's word, but modern English hears legal status or outer space |
| outlander | accurate, but old-fashioned |
| man of another nation | exact but wordy; could be used where a verse needs it |
| stranger | taken, if *ger* becomes "stranger" |
| outsider | taken by *zar* |
| gentile | wrong word: that is *goy*, "nation" |

**Recommendation:** ***ben nekhar* = foreigner** (as it is now in all four verses), and ***ger* = stranger**, which frees "foreigner" to mean only *ben nekhar*. The Greek *proselyte* ("one who has come over") is why "stranger" fits *ger*: someone who came in from outside and lives among you.

That still needs your go before I list the *ger* verses and change them.

### Changes made: *ben nekhar*

| Where | Before | After |
|---|---|---|
| RENDERING_SPEC fixed terms | — | *ben nekhar* = foreigner (already the wording in Genesis 17:12, 17:27; Exodus 12:43; Leviticus 22:25, so no verse changes) |

Still open: ***ger*** is also "foreigner" today (Exodus 12:48, 49; Leviticus 22:18 and others). Until *ger* gets its own word ("stranger" is the recommendation), the two stay blurred.

---

## Round of rulings: 15:1 note, wart, resident, soothing aroma, servant (2026-09-24)

### Your request (chat, 2026-09-24 afternoon)

> Yes on the Exodus 15:1 note. 22:22 wart. 23:11 … the day after Saturday … Sunday. 23:24 – is there a different word instead of blast? toshav = resident. Soothing aroma if I have to choose, but perhaps "pleasing aroma"? ger = resident; ben nekhar = traveler or outsider? All word choices work with servant. Lev 25:42 … "For they are slaves, whom I brought out…"?

### Changes made

| Where | Before | After |
|---|---|---|
| Exodus 15 notes | — | New note at v1: the song retold (Isaiah 51:10, Psalm 77:19, 1 Corinthians 10:2, Revelation 15:3) |
| Leviticus 22:22 | or with a running sore | or with a **wart** (the Greek literally says "warted"; note updated) |
| Genesis 23:4 | A foreigner and a **settler** I am among you | A foreigner and a **resident** I am among you |
| Leviticus 25:23 note | quoted "settler" | quotes "resident" |
| Genesis 8:21 | the **quieting smell** | the **soothing aroma** (note updated) |
| Exodus 29:18, 25, 41 | a **quieting smell** | a **soothing aroma** (note updated) |
| Leviticus 25:42 | For they are **My slaves** | For they are **My servants** (… "sold as a slave is sold" stays) |
| Leviticus 25:55 | slaves to Me… My slaves | **servants** to Me… My **servants** (note rewritten) |
| RENDERING_SPEC fixed terms | — | *toshav* = resident; *re'ach nichoach* = soothing aroma; *eved* (God the master) = servant |

### Your questions

**23:11 "the day after the sabbath" (no change made).** The Hebrew says *the sabbath*, with no "day" and no "seventh". Two readings are old:
- **The weekly Sabbath (your reading):** the sheaf is waved on a Sunday. Then Pentecost, fifty days later, also always falls on a Sunday.
- **The first day of Unleavened Bread (v7):** that day is kept like a sabbath, so the sheaf would fall on a fixed date, whatever the weekday.

Your reading has a New Testament echo. Jesus rose *on the first day of the week* after the Sabbath (Matthew 28:1), and Paul calls Him *the firstfruits of those who have fallen asleep* (1 Corinthians 15:20): the firstfruits sheaf of v10–11. If you want, the v11 note can add that.

**23:24 "a remembrance by a blast" (no change made).** *Teru'ah* covers two sounds:
- **a great shout** (the shout at Jericho, Joshua 6:5)
- **the blast of a horn** (Leviticus 25:9, *shofar teru'ah*)

Options:
- *a remembrance by shouting*
- *a remembrance with horn blasts*
- *a day of remembrance and shouting*
- keep *a blast*

Numbers 29:1 calls the same day *yom teru'ah*. My recommendation: **"a remembrance with horn blasts"**, which is clear, and Leviticus 25:9 shows horns were what sounded on these days. The note would say the word is also "shout."

**"Pleasing aroma" vs "soothing aroma".** Both are honest translations. *Nichoach* is built from *nuach*, rest. "Soothing" keeps that; "pleasing" is the more common English but loses the rest idea, and the Genesis 8:21 note ties this word to Noah's name. You chose soothing if you had to choose, so that's applied. Say the word if you'd rather have "pleasing" everywhere.

**Lev 25:42 "For they are slaves, whom I brought out…"** Dropping "My" isn't possible: the Hebrew is *avadai*, "My servants", and the "My" is the point. "Servant" is a fully legitimate meaning of *eved*, and it fits the context, so the text now reads **"For they are My servants… They shall not be sold as a slave is sold."** The note says the Hebrew uses one word for both.

**ger = resident, ben nekhar = traveler or outsider: it doesn't quite work, for two reasons.**
1. **"Resident" is now *toshav*.** *Ger* and *toshav* stand side by side in Genesis 23:4 and Leviticus 25:23, 35 and 47. Both can't be "resident."
2. **"Outsider" is already *zar*,** the word for a non-priest or an unauthorized person (Exodus 29:33, 30:33; Leviticus 22:10, 12, 13; Numbers 1:51). "Traveler" isn't what *ben nekhar* means: it means a person of a foreign nation, whether or not he travels.

What each word actually means:

| Hebrew | Meaning | Candidates |
|---|---|---|
| *ger* | someone living long-term in a land not his own, without land or inheritance rights (Israel was *gerim* in Egypt) | **stranger** ("you were strangers in the land of Egypt"), immigrant, alien, foreigner (now) |
| *ben nekhar* | a person of another nation | **foreigner** |
| *toshav* | a settled resident without land of his own | resident (decided) |
| *zar* | anyone not entitled (a non-priest, a non-family member) | outsider (now) |

**My recommendation:**
- *ger* = **stranger**: the old English word that means exactly this, and it reads naturally in the famous verses.
- *ben nekhar* = **foreigner**, the plainest word for a person of another nation.

That changes every *ger* in Genesis–Numbers from "foreigner" to "stranger", a few dozen verses (my quick count also caught the name Hagar, which is spelled the same way, so the exact number still needs checking). I will list every verse before changing anything, if you say go.
