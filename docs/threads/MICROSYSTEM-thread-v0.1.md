# MICROSYSTEM · Integration Thread v0.1

## The micro-domestic-production architecture · cross-practice spec.

**Date:** 2026-05-18
**Status:** Integration architecture · first cross-practice specification
**Component practices:** BDRC (grain meals) + GROW (hydroponic herbs) + SPORE (mushrooms) + STOCK (cuisine refills)
**Companion documents:** BDRC-thread, GROW-thread, SPORE-thread, STOCK-thread, MEAL.0001
**Deferred companion:** HAKO-deployment-thread (next session)
**This document:** the spec for how the four practices live together as one system

---

## § 0 · What this document is

The studio's catalogue now contains four practices that produce or process food at apartment scale: **BDRC** (toggle-switch grain meals), **GROW** (hydroponic herbs and greens), **SPORE** (cultivated mushrooms), and **STOCK** (cuisine refill cells and COOK single-meal kits). Each has its own working thread. What hasn't been documented yet is **how they work together as one system.**

This document captures that integration. Not how each practice operates independently — that's already specified — but how they share infrastructure, compound in value, and deploy as a coherent micro-domestic-production module. The document also prepares the ground for the eventual Hako-deployment spec by establishing what the "complete system" looks like before figuring out how to fit it inside a dwelling envelope.

**The work in this document is integration architecture, not new product specification.** No new cells are proposed; no new practices are launched. The catalogue's existing parts are arranged into a system.

---

## § 1 · The thesis · what's being integrated and why

Each of the four practices follows the same M1ND.studio architectural move:

> Pick a commodity envelope. Design what fills it. Let the customer source the envelope from anywhere. Earn margin through curation, design, and editorial work — not through manufacturing what's already commoditized.

When deployed individually, each practice is valuable. When deployed together in one household, **they compound in a way no single practice could achieve alone.** This compounding is the integration's reason to exist:

| Combined practices | What becomes possible |
|---|---|
| **BDRC + GROW** | Fresh herbs finish toggle-switch grain meals. *"Grow your finish."* |
| **BDRC + SPORE** | Fresh mushrooms upgrade BDRC's dried-porcini cells and add sautéed fresh toppings. |
| **GROW + SPORE** | Spent SPORE substrate composts into soil amendment for GROW's overflow plants (potted backup). |
| **BDRC + STOCK** | Refill cells back-stop the BDRC catalogue with deeper cuisine specificity. |
| **All four** | A complete cooking practice from grain to herb to mushroom to cuisine. One household, four catalogues, four-way compounding. |

This is the catalogue's structural advantage. **No incumbent in any of these categories operates the others.** Hello Fresh ships herbs because they have to assume the customer doesn't grow them. AeroGarden makes hydroponics but doesn't sell recipes or grain bases. North Spore sells mushroom kits but doesn't make cookbooks. **The studio's distinctive position is operating across categories that no single competitor connects** — and designing the catalogues to talk to each other deliberately.

---

## § 2 · The shared infrastructure

### 2.1 The 1646 envelope is the atomic unit

Every cell across all four practices ships in the same physical envelope: a 1646-spec storage cell (4.7" × 6.6" × 1.2"). Multiple manufacturer sources, ~$2-3 per cell at retail. The cells stack and label uniformly regardless of which practice they belong to.

This is the most important shared standard in the entire catalogue. **A customer who buys a KEEP case (originally for personal-archive use) can later use the same cells for BDRC, then SPORE, then GROW.** The customer's investment in 1646 cases is one-time; the catalogue draws margin from what fills them.

### 2.2 The Wowlive STD-S01 3-tier shelf is the deployment standard

Shelf dimensions: 33.75" W × 9.84" D per tier, three tiers, ~$35 CAD from Wowlive or generic equivalents. **One Wowlive 3-tier holds the complete studio kitchen module** — verified during the GROW spec work (GROW-thread §2):

```
┌──────────────────────────────────────────────────┐
│  TOP TIER  ·  active appliances                  │
│  ┌──────────────────┐  ┌──────────┐              │
│  │ iDOO GROW01      │  │ B&D RC503│   ~12"       │
│  │ 13.6" × 7.7"     │  │  ~8"×8"  │   slack      │
│  └──────────────────┘  └──────────┘              │
├──────────────────────────────────────────────────┤
│  MIDDLE TIER  ·  active SPORE fruiting + cells   │
│  ┌──────────────┐  ┌──┐┌──┐┌──┐                  │
│  │ SBT shoebox  │  │ 1646 cells   │              │
│  │ tote 14"×8"  │  │ (3-4 fit)    │              │
│  └──────────────┘  └──┘└──┘└──┘                  │
├──────────────────────────────────────────────────┤
│  BOTTOM TIER  ·  cell library                    │
│  ┌──┐ ┌──┐ ┌──┐ ┌──┐ ┌──┐ ┌──┐                   │
│  │  │ │  │ │  │ │  │ │  │ │  │  (6 cells)        │
│  └──┘ └──┘ └──┘ └──┘ └──┘ └──┘                   │
└──────────────────────────────────────────────────┘
```

**Why this matters:** the shelf isn't just storage. It's the deployment unit. Each tier has a specific role; the three tiers together produce a complete operating system for the kitchen. **The shelf is the system's form factor.**

Worth noting: the middle tier accommodates an active SPORE fruiting tote (a shoebox-sized SBT is ~14" × 8" × 6" with the lid on). This was the missing piece during the GROW spec. **Middle tier becomes the active biological zone** — fruiting mushrooms on one side, cell library on the other.

### 2.3 The hanko system

Every cell across all four practices carries the M1ND.studio hanko mark in the bottom-right corner of every card. The letter content varies — BXBX, KEEP, COOK, BDRC, STOCK, GROW, SPORE — but the visual treatment is identical: vermillion outlined square, 5-character cap inside, same dimensions, same placement on every card.

A customer's catalogue thus reads as a unified visual artifact regardless of which practices they own. **The studio's identity is consistent across practices in a way no multi-product retailer typically achieves.** This is meaningful brand equity that doesn't require ongoing investment to maintain — it's baked into the card system.

### 2.4 The card system v0.2 — three modes, fixed chrome

Documented in earlier sessions (1646 Card v0.2). Three layout modes (A image-led / B text-led / C text-only with sketch box). Fixed chrome (ID, date, title, hanko, brand strip). The four practices all use this same card vocabulary:

- **BDRC** uses Mode A for meal cards, Mode B for ingredient/method/finish cards
- **GROW** uses Mode A for crop showpiece, Mode B for planting/care/harvest cards
- **SPORE** uses Mode A for species identity, Mode B for workflow steps, Mode C as troubleshooting card
- **STOCK** uses all three across various cell types

A customer browsing their catalogue sees consistent typography, consistent hierarchy, consistent design language. **The system is the brand.**

---

## § 3 · The compounding effects, named explicitly

Each cross-practice compounding effect deserves its own naming and documentation. The catalogue's value proposition increasingly lives in these intersections, not in any single practice.

### 3.1 Grow your finish (BDRC + GROW)

**The headline integration.** BDRC cells specify finishing herbs that the customer can grow in their iDOO GROW01. The studio's published cross-references:

| BDRC cell | GROW cell that supports it |
|---|---|
| 01 · Jasmine + Lemongrass + Ginger | 02 · Asian Aromatics |
| 02 · Saffron Basmati + Cardamom | 01 · Mediterranean Garden (dill, parsley) |
| 03 · Coconut Pandan Rice | 02 · Asian Aromatics (cilantro, Thai basil) |
| 04 · Hainanese Chicken Rice | 02 · Asian Aromatics (scallion, cilantro) |
| 05 · Lemon-Dill Pilaf | 01 · Mediterranean Garden (dill, parsley) |
| 06 · Mujadara | 03 · Levantine Herb Box (parsley, mint) |
| 07 · Khichdi | 02 · Asian Aromatics (cilantro) |
| 08 · Tomato-Basil Risotto | 01 · Mediterranean Garden (basil) |
| 09 · Mushroom Farro | 01 · Mediterranean Garden (thyme, parsley) |
| 10 · Greek Lemon-Orzo | 01 · Mediterranean Garden (dill, oregano, parsley) |
| 13 · Bibimbap Rice | 02 · Asian Aromatics (scallion, cilantro, perilla) |
| 14 · Quinoa Za'atar | 03 · Levantine Herb Box (parsley, mint) |

Each BDRC recipe card's "Finish" section will name the specific GROW cell that delivers the herbs. The relationship runs in both directions: each GROW cell's "Cross-references" card lists the BDRC cells the harvest serves.

### 3.2 Fresh from the fruit (BDRC + SPORE)

Fresh mushrooms upgrade or substitute into multiple BDRC cells. Specifically:

| BDRC cell | SPORE harvest that upgrades it |
|---|---|
| 09 · Mushroom Farro | Fresh oyster or lion's mane (in place of/in addition to dried porcini) |
| 05 · Lemon-Dill Pilaf | Sautéed king trumpets on top |
| 07 · Khichdi | Sautéed oysters folded in |
| 13 · Bibimbap Rice | Fresh oyster mushrooms as a canonical topping |
| 16 · Smoky Black Bean | Pulled lion's mane "carnitas" as a vegetarian protein |

The studio's cross-reference cards should make these explicit, treating fresh mushrooms as **a finishing ingredient parallel to fresh herbs** — same role in the cooking architecture, different production practice.

### 3.3 Spent substrate as soil amendment (SPORE + outdoor/houseplant gardens)

SPORE's fruited substrate (the CVG cake after the second flush) is rich in mycelial matter and partially digested organic material — **excellent soil amendment for any soil-based gardening.** While GROW is hydroponic and doesn't use soil, customers with houseplants, outdoor gardens, or balcony pots benefit from spent substrate as compost.

The studio's catalogue position: **nothing in the system goes to waste.** Spent substrate becomes a flagged use-case in the SPORE recipe deck — not a separate product, just an instruction on how to use the by-product.

### 3.4 Cuisine cells back-stop daily cooking (STOCK + BDRC + GROW + SPORE)

The STOCK cuisine refill cells (Italian / Sichuan / Levantine / Moroccan / Mexican / Indian etc.) provide the specialty ingredients that make any of the daily-cooking practices regionally specific. A customer cooking BDRC Cell 14 (Quinoa Za'atar) tonight uses za'atar that may have come from the STOCK Levantine refill cell, herbs from the GROW Levantine Herb Box, no mushrooms needed for this particular dish but the option is there.

**STOCK is the catalogue's depth dimension.** BDRC, GROW, and SPORE provide the daily-rhythm production. STOCK provides the cuisine-specific specialty layer that elevates daily output to restaurant-quality.

### 3.5 The integrated meal · proof of concept

The clearest demonstration of the system is **one dinner that touches all four practices**:

> **A weeknight grain bowl, Mediterranean-Italian.**
> 
> - **Grain:** BDRC Cell 09 Mushroom Farro, started 45 minutes before dinner. Toggle pressed, walk away.
> - **Hot fresh mushrooms:** SPORE Cell 01 Blue Oysters harvested earlier today (or earlier this week), sliced, sautéed in olive oil with garlic until golden, set aside warm.
> - **Fresh herbs:** GROW Cell 01 Mediterranean Garden — fresh thyme and parsley snipped 5 minutes before serving.
> - **Cuisine specialty:** STOCK Italian refill cell — finishing olive oil and aged balsamic, drizzled at the table.
> - **Hardware:** Everything assembled from the Wowlive shelf in the customer's kitchen, ~30 sq ft of total footprint.

This meal is the catalogue's central thesis demonstrated in one plate. **No single competitor in any of the component categories — meal kits, herb subscriptions, mushroom kits, spice services — can deliver this meal at this quality, at this price, with this little waste.**

The integrated meal is also the catalogue's most photographable artifact. The hero image for stock.m1nd.co could be this exact bowl, photographed in the customer's actual kitchen with the Wowlive shelf visible in the background. **The image sells the system, not any individual product.**

---

## § 4 · Daily, weekly, monthly · the system in motion

The four practices operate on different cycles. The integration deserves naming the temporal pattern, because it informs how customers actually live with the system.

### Daily (every day or every other day)
- **GROW:** Check water level in iDOO reservoir (30 seconds). Snip herbs as needed for that night's cooking.
- **SPORE:** Twice-daily misting if a tote is in active fruiting phase (30 seconds each). Otherwise nothing.
- **BDRC:** Toggle-switch a grain cell for dinner (5 minutes setup, walk away).

Total daily time investment when all systems are active: **~5-7 minutes of active engagement plus 30-50 minutes of hands-off cooking time.**

### Weekly
- **GROW:** Top up nutrient solution (5 minutes once a week or so).
- **SPORE:** Inspect colonization progress on any active jars or totes (1 minute).
- **BDRC/STOCK:** Plan the week's grain cells; restock any depleted spice mixes from STOCK refills.

Total weekly investment: **~15-20 minutes.**

### Monthly
- **GROW:** Mid-cycle reset — clean iDOO reservoir, replace any failed pods.
- **SPORE:** Spawn-to-bulk cycle for a new tote (~30 minutes of active work).
- **STOCK:** Consider next refill cells or new cuisine to add to the rotation.

Total monthly investment: **~1 hour.**

### What this rhythm tells us

The system rewards customers who develop a daily rhythm. Five minutes a day of micro-engagement keeps the entire system productive. **Compare with meal kits:** Hello Fresh requires no daily attention but generates no compounding value either. The studio's system trades a small daily commitment for ongoing freshness, customization, and accumulated household productivity.

**The system is closer to keeping plants alive than to subscribing to a service.** That positioning matters for customer acquisition — *"if you can keep a houseplant, you can run this system"* is the catalogue's honest customer-fit statement.

---

## § 5 · Sourcing map · the full Toronto procurement spec

The studio's complete sourcing needs across all four practices. Useful as a Phase 0 procurement working document.

### Grains and pulses (BDRC + occasional STOCK)
- **Long-grain rice (jasmine, basmati):** T&T Supermarket, Pacific Mall vendors, Sahid Halal Foods (Indian grocery)
- **Short-grain rice (Korean, sushi-style):** PAT Mart, Galleria Supermarket
- **Specialty grains (farro, freekeh):** Whole Foods bulk, ASA Tea & Foods (Italian)
- **Quinoa, lentils, mung dal:** Bulk Barn, Indian grocery (Brar's)
- **Black beans, freeze-dried beans:** Costco wholesale, Latin grocery (Latino Grocer Toronto)

### Spices and aromatics (BDRC + STOCK + COOK)
- **Specialty spice imports (ras el hanout, za'atar, gochugaru):** Naseem Foods (Levantine), PAT Mart (Korean), Galleria Supermarket
- **Saffron, dried mushrooms (porcini), high-end specialty:** Eataly Toronto, ASA Tea & Foods
- **Bulk standard spices:** Bulk Barn for cumin, coriander, oregano, etc.
- **Specialty Asian botanicals (lemongrass, kaffir lime leaf, pandan):** Asian groceries on Spadina + Chinatown, T&T

### Hydroponic supplies (GROW)
- **Seeds:** Stokes Seeds (St. Catharines), William Dam (Dundas), Veseys (PEI), specialty herb seeds from Renee's Garden
- **Nutrient solution:** General Hydroponics MaxiGrow + MaxiBloom from Toronto hydroponic suppliers (Modern Hydroponics, Brite-Lite)
- **Sponges / growing media:** Same hydroponic suppliers, or direct order from iDOO accessory line
- **Mineral additives (cal-mag, pH solutions):** Modern Hydroponics

### Mushroom cultivation supplies (SPORE)
- **Spawn strains (initial culture purchase):** North Spore (Maine, ships cross-border), Smug Bug Ontario (Toronto), Mycelio (Quebec)
- **Mason jars and modified lids:** Canadian Tire, Home Hardware
- **Substrate ingredients (coco coir, vermiculite, gypsum):** Modern Hydroponics, Home Depot, Canadian Tire garden centre
- **Shoebox totes:** Canadian Tire, Walmart, Dollarama
- **Sterilization supplies (pressure cooker, alcohol):** Restaurant supply, Canadian Tire

### Packaging and shipping (all practices)
- **1646 cells:** Simply Tidy via Michaels or Amazon, Novelinks via Amazon, IRIS / ALINK / Lifewit via Amazon
- **Outer shipping boxes:** Canada Post Small Flat Rate Box (~$14 fixed cost in Canada)
- **Vac-pac equipment + bags:** FoodSaver basic unit ($150) + bulk bags from Costco
- **Archival labels and stickers:** Avery, custom-printed via Vistaprint or Moo
- **Padding (kraft paper, tissue):** Uline Canada

**Total relationships to establish for Phase 0:** approximately 15-20 active supplier touchpoints, mostly in Toronto's grocery, hydroponic, and bulk-supply ecosystems. Many overlap (Bulk Barn covers grains + spices; Canadian Tire covers jars + totes + some grain). **The actual supplier-relationship count is more like 8-10 vendors who can supply across practice categories.**

---

## § 6 · The portable enclosure question · preparing for HAKO deployment

Jordan's note in the original prompt frames the eventual vision: *"all getting designed to fit into a Hako flagship model."* This integration thread doesn't fully specify that — that's the next session's work — but the question can be scoped here.

### What "the complete microsystem in a portable enclosure" means

The Wowlive shelf deployment described in § 2.2 is **the static apartment-friendly version.** A Hako deployment is the **mobile dwelling-integrated version.** Same practices, same cells, same compounding effects — but designed to live inside the dwelling envelope itself, not on a separate shelf in someone's existing kitchen.

The architecture that needs spec work in the Hako-deployment thread:

1. **How the iDOO mounts inside a Hako** — does it sit on a built-in shelf, hang from a wall fixture, integrate into a custom millwork panel?
2. **How the SPORE fruiting tote lives in the dwelling** — needs darkness during colonization, humidity during fruiting, neither of which is a default condition in a dwelling
3. **How the BDRC rice cooker is stored** — countertop, drawer, built-in? Power requirements (uses 350W during cook cycle)
4. **How the 1646 cell library deploys** — wall-mounted shelving, drawer storage, modular slot system built into the Hako interior
5. **Power, water, ventilation requirements** — the iDOO uses ~25W constant during operation; the rice cooker uses 350W intermittently; SPORE needs air exchange; GROW needs water access. Cumulative: how does this affect Hako infrastructure spec?
6. **The total floor footprint inside the Hako** — the current Wowlive deployment is ~3 sq ft. Inside a Hako that's roughly 56 sq ft of total floor area, the microsystem would occupy ~5% of dwelling floor space. **Feasible.**

### The thesis worth naming in advance

**A Hako with the microsystem built in is the studio's flagship BXBX product.** Every M1ND.studio practice converging into one dwelling that fits in a U-Box logistics envelope.

- BXBX produces the dwelling
- KEEP produces the storage architecture inside it
- STOCK + COOK + BDRC + GROW + SPORE produce the daily-life sustenance from inside it
- The whole thing fits in a single shipping container and deploys anywhere

That's the studio's most internally-consistent product vision to date. **A complete designed life inside one commodity logistics envelope.** Worth real spec work in its own session. **HAKO-deployment-thread.md to come.**

---

## § 7 · Open questions · cross-practice integration

**Q1 · The "Studio Kitchen v1" bundle, revisited.** GROW-thread §7 proposed a single SKU bundling Wowlive + iDOO + B&D + GROW starter + BDRC starter + STOCK trial. Should the bundle now also include a **SPORE starter cell** to make all four practices represented in the introductory offer? My read: **yes for a "Studio Kitchen v2" SKU that follows Studio Kitchen v1 by 6 months.** v1 launches with 3 practices, v2 adds SPORE once that practice has bedded in.

**Q2 · The cross-reference card design.** When a BDRC Cell 05 recipe card says *"finish with fresh dill from your GROW Cell 01"*, the wording is straightforward when the customer owns both. But what about the customer who only owns BDRC? Should the cross-reference appear at all, or is it noise for that customer? My read: **always include the cross-reference**, formatted as a small note in the recipe deck. Functions as an upgrade prompt without being pushy. Customers who don't own GROW will read it and either ignore it or eventually buy in.

**Q3 · The integrated meal photograph.** The hero image described in § 3.5 is the catalogue's most important marketing asset. **Should the studio commission a professional food photographer for Phase 0 documentation, or photograph it in-house?** A real food photographer in Toronto with editorial credentials runs $1,500-3,500/day. For one definitive system image — probably worth it. Especially since it'd be reusable for years.

**Q4 · The system's name.** "M1ND.studio microsystem" is descriptive but generic. Working candidates: **"the Studio Kitchen,"** **"the M1ND module,"** **"the food module,"** **"M1ND.studio · domestic stack."** My instinct: **"the Studio Kitchen"** — direct, accessible, what customers will actually call it.

**Q5 · Onboarding flow for the integrated customer.** A customer buying their first single cell (say a BDRC cell) experiences the catalogue as that one product. A customer buying the Studio Kitchen experiences the full system. **The two onboarding paths need meaningfully different welcome materials.** The Studio Kitchen v1 ships with what? A printed welcome book? A folded card? An emailed start-here guide? Worth designing as a deliberate artifact rather than letting it emerge ad hoc.

**Q6 · The deployment guide.** A customer who buys all the components needs an actual physical-arrangement guide. Where does the iDOO go? Where does the rice cooker live? Which tier of the Wowlive holds what? **This is a real deliverable** — a small printed guide that ships with any Studio Kitchen bundle, walking the customer through deployment. Mode A image-led cards showing the Wowlive layout. Two or three cards' worth of work, but essential.

---

## § 8 · Closing

Four practices. One coherent micro-domestic-production system. Documented across five thread documents (BDRC, GROW, SPORE, STOCK, this one). Roughly 20,000 words of catalogue specification produced across the May 2026 work cycle. The studio's editorial register has a clearly identifiable shape now — and **the catalogue produces real artifacts whose value compounds in the customer's home** in a way that no single-category competitor can match.

The studio's path from here is:

1. **Phase 0 work in summer 2026:** bench-test SPORE in Toronto, verify GROW cells, finalize BDRC pricing and recipes, build the spawn-production area in the Dupont Arts studio
2. **The Hako-deployment spec next session:** integrate this entire microsystem into a BXBX flagship
3. **Phase 1 launch in autumn 2026:** the Studio Kitchen v1 bundle becomes available; ~25 selected Toronto customers receive the complete system
4. **Phase 2 expansion in 2027:** public catalogue launch, retail partnerships, eventual east-coast distribution

The integration story is complete enough to begin photographing the artifact. The Hako story is the next ambitious step. **The studio's catalogue is genuinely becoming a system that no incumbent competitor can replicate** — because the system's value lives in the intersections between practices, not in any single product.

That's the most important thing the studio has demonstrated in this work cycle. The catalogue is a system. The system is a thesis. **The thesis is producing real artifacts now.** What remains is the operational work of getting them into customers' hands.

---

*MICROSYSTEM Integration Thread v0.1 captured 2026-05-18. The first cross-practice spec for M1ND.studio's indoor food-production catalogue. Companion to BDRC, GROW, SPORE, STOCK threads. Next session: HAKO-deployment-thread — the entire microsystem inside a BXBX flagship dwelling envelope.*
