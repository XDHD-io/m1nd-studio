# .Studio · Thread v0.1

## The studio's design-systems practice.

**Date:** 2026-05-19 (.Studio practice founding)
**Status:** Practice established · 4×6 print envelope locked · labeling system migrated from KEEP · organizational tool concept scoped
**Codename:** .Studio (the leading dot is intentional; reads as "dot-studio," signals system-level work)
**Parent:** M1ND.studio
**Sister practices:** KEEP (archive infrastructure), CODEX (publishing pipeline)
**Companion documents:** KEEP-thread-v0.4, KEEP-1646-mods-thread-v0.1, CODEX-thread-v0.1
**This document:** establishes .Studio as the design-systems practice that the rest of the catalogue inherits from

---

## § 0 · Why this practice exists

The studio has been quietly accumulating a design system for the last several months. Typography (Space Grotesk + Inter + EB Garamond + IBM Plex Mono). Palette (paper, ink, hanko vermillion, practice-specific accents). The 1646 cell envelope and its 4×6 dimensions. The CODEX format spec. The label slot on every cell. The print register for the studio's editorial work.

This design system has been distributed across practices without an explicit owner. KEEP holds the 1646 physical standard. CODEX holds the editorial typography. STOCK holds the product-card visual register. The studio's own front-page sets the typographic anchor. **Each practice has been using the design system; no practice has owned maintaining it.**

This worked when the design system was small enough to live in everyone's head. It is no longer that small. The studio now has:

- A canonical typography stack across 9 practices
- A locked color palette with per-practice accents
- A 4×6 physical print envelope used by CODEX, COOK recipe cards, MEAL kit inserts, and now booklets
- A labeling convention applied across CELL, KEEP, STOCK, CODEX, MEAL
- A visual register used in every page of the catalogue MVP

**.Studio is the practice that owns this system as a system.** Not the practice that uses it (every practice does). Not the practice that ships it (every practice does). The practice that *defines, maintains, evolves, and documents* it.

---

## § 1 · What .Studio owns

### 1.1 · The typography stack
- **Display:** Space Grotesk (Regular 400, Medium 500, Bold 700)
- **Serif:** Inter for web body, EB Garamond for classical/editorial body
- **Mono:** IBM Plex Mono
- **Sizing:** body 14.5px / leading 1.55 on web, 9pt/11pt for CODEX, 9pt/11pt for booklet bodies

### 1.2 · The palette
- **Paper:** `#F4F1E8` (warm cream, the studio's base ground)
- **Ink:** `#1A1814` (warm black, never pure black)
- **Hanko:** `#B85540` (vermillion, the studio's signature accent, used sparingly)
- **Per-practice accents:** locked in `/shared/studio.css`
  - STOCK / MEAL family · `#8A6B3A` (warm ochre)
  - BXBX · `#1A1814` (ink)
  - KEEP · `#5C5A56` (slate)
  - CODEX · `#7A3F2E` (burnt brick)
  - T1NY · `#3D5A6C` (deep blue)
  - MHYC · `#2E5C4F` (deep teal)
  - MESH · `#6E4A7E` (deep aubergine)
  - B1KE · `#6E4A2E` (engine brown)

### 1.3 · The print envelope · 4×6
**The studio's first formal design standard under .Studio is the 4×6 print envelope.** Every printed surface in the catalogue conforms to this dimension:

- **The 1646 cell** is 4×6 (its dimensions define the envelope)
- **CODEX cards** are 4×6 (a stack of 100 = one book in a cell)
- **MEAL kit insert cards** are 4×6
- **COOK recipe cards** are 4×6
- **Folded booklets** (new under .Studio) are 4×3 when folded from a 4×6 sheet
- **Cell labels** (migrated from KEEP) are designed against the 4×6 cell exterior

The envelope creates economies of scale across the catalogue. One print spec serves every product line. One paper stock (the Oxford 4×6 ruled/blank cards, sourced from the standard office-supply channel — Made in Mexico) serves every practice. **The 4×6 envelope is .Studio's most important design decision and its primary deliverable.**

### 1.4 · The labeling system *(migrated from KEEP)*
Previously held under KEEP as part of the 1646 cell standard, the labeling system formally moves to .Studio under this practice founding. The migration logic:

- KEEP owns the *physical envelope* (the cell as object, the shelf as object, the mod kit as physical accessory)
- .Studio owns the *design system that the envelope inhabits* (typography, color, label format, the visual register that makes a labeled cell legible)

The two practices remain tightly coupled. A KEEP customer who buys 1646 cells gets cell labels designed by .Studio. A .Studio update to the label spec propagates to every KEEP product. Practical effect on the catalogue: the *cell label* product spec lives at `.studio.m1nd.co/labels` instead of `keep.m1nd.co/labels`.

### 1.5 · The CODEX format spec
CODEX is a .Studio-defined format that CODEX-the-practice publishes into. Card dimensions, body typography, chapter-card layout, colophon convention, table-of-contents pattern — all .Studio decisions. CODEX-the-practice picks the works, does the typesetting, runs the publishing pipeline. **CODEX is one consumer of the .Studio format; the booklet (next section) is another.**

---

## § 2 · The folded-card booklet · .Studio's first new format

### 2.1 · The discovery

A 4×6 card folded in half along its short axis creates a **4×3 booklet page** with 4 page-faces (2 outer + 2 inner). This is the natural folding pattern — landscape orientation, comfortable thumb-and-finger grip, fits a pocket.

| Booklet format | Cards per booklet | Page faces | Per 100-pack of cards |
|---|---|---|---|
| **Mini Field Notes** (~28 pages) | 7 | 28 | **14 booklets** |
| **Standard Field Notes** (~52 pages) | 13 | 52 | **7 booklets** |
| **Big Pocket** (~100 pages) | 25 | 100 | **4 booklets** |
| **Quarter-pack chunk** (28 pages) | 7 | 28 | **4 booklets** (exactly) |
| **Half-pack chunk** (52 pages) | 13 | 52 | **2 booklets** (exactly) |

The natural unit: a single 100-pack of cards = **2 × 50-page booklets OR 4 × 25-page booklets.** This is too clean a number to be coincidence; it's the design constraint .Studio should build around.

### 2.2 · Text capacity per booklet

At the studio's standard book-typography spec (9pt EB Garamond body, 11pt leading, 0.25" margins on the 4×3 page):

- **~118 words per page face**
- **25-page mini booklet: ~3,300 words total / ~2,600 content** (after ~6 pages of front/back matter)
- **50-page standard booklet: ~6,100 words total / ~5,400 content**
- **100-page big booklet: ~11,800 words total / ~11,000 content**

For comparison: a typical Field Notes notebook is 48 pages of dot-grid blank for writing. The studio's standard booklet matches Field Notes' page count almost exactly. **The studio's booklet is not competing with Field Notes — it's complementary.** Field Notes is a writing surface; the studio's booklet is a writing surface AND a printable substrate for studio-original short-form content (essays, manuals, reference works, single-author chapbooks).

### 2.3 · Booklet product line — initial SKUs

Living under the .Studio practice, sold through the catalogue:

**Blank booklets** (the writing-surface tier)
- **STUDIO-BL-01 · 4 × Mini Notebooks** — One 100-pack of cards folded and stapled into 4 × 25-page notebooks. Studio-branded covers (paper-and-hanko palette, Space Grotesk wordmark). $18.
- **STUDIO-BL-02 · 2 × Standard Notebooks** — Same pack, folded into 2 × 50-page notebooks. $16.
- **STUDIO-BL-03 · Year-One Studio Journal** — 4 × 25-page booklets pre-printed with quarterly journal prompts, one per quarter of the customer's first year with the studio. $24.

**Printed manuals** (the studio-content tier)
- **STUDIO-PR-01 · BXBX Hako Owner's Manual** — 50-page booklet, ~5,000 words covering build, install, maintenance, expansion. Ships with every Hako; available separately at $18.
- **STUDIO-PR-02 · KEEP 1646 Mods Manual** — 50-page booklet, the full case study from KEEP-1646-mods-thread typeset to the studio's booklet format. $18.
- **STUDIO-PR-03 · CODEX-001 Pocket Edition (Tao Te Ching)** — 25-page condensed version of CODEX-001 in booklet format. A different reading experience than the full CODEX card-stack — sequential, traditional, pocketable. $12. *Companion product to CODEX-001 rather than a replacement.*
- **STUDIO-PR-04 · The Studio Almanac · Year One** — 50-page booklet, year-end summary of the catalogue's first year. $20.

**Limited / commissioned**
- **STUDIO-LM-01 · Custom booklet typesetting** — Customer brings text (their own writing, public-domain work, family records); studio typesets to spec and prints a small run. $80-200 per booklet depending on length and quantity.

### 2.4 · Why the booklet matters

Three reasons this isn't just a side-product:

1. **It uses cards the customer already has.** A customer with a 100-pack of 1646 cards can immediately make 4 mini notebooks. The studio doesn't need to source different paper or invest in new inventory — the booklet is a *transformation* of an existing product.

2. **It opens a new content surface.** Studio editorial work that's too long for a single card and too short for a CODEX (the 5,000-word manual range) now has a natural home. The KEEP 1646 mods case study, the Hako owner's manual, the year-end almanac — all of these become real physical products instead of just web pages.

3. **It compounds with everything else.** A MEAL kit can ship with a booklet insert. A CODEX product can have a companion booklet. A BXBX Hako delivery includes its booklet manual. The booklet is a unifying format that connects practices that previously didn't have a shared deliverable.

---

## § 3 · The master organizational tool

The hardest unresolved question in the studio's catalogue: **how does a customer who's filled 20-30 cells in a Wowlive shelf find any specific thing again?**

The current answer is "label the cell." That works at small scale. It breaks at any scale beyond ~20 cells, and breaks completely for cells the customer fills *without* explicit itemization (kitchen drawer cleanup, project parts dump, mixed-receipt cell). The studio needs a clever pattern, not just better labels.

### 3.1 · The pattern · cells remember themselves

Three layered approaches under one architecture:

**Layer 1 · The QR sticker.** Every 1646 cell ships with a pre-printed QR sticker on the exterior label slot, encoding a unique cell ID. The customer doesn't print this; .Studio does. Cell IDs are sequential within a customer account (CELL-001, CELL-002, etc.) but globally unique across the studio's customer base.

**Layer 2 · The personal KEEP web app.** Each customer has a personal account at `keep.m1nd.co/me` (working URL spec). The app holds a record for each of their cells, keyed by QR ID. Records can be:

- **Photo-only** — customer scans the QR, takes one photo of the cell contents, app stores the photo against the ID. No typing required. Searchable later by *date received* or by reverse-image-search keyword.
- **Voice-memo** — customer scans the QR, records a 10-second voice note ("everything from the kitchen drawer cleanup, May 19"), app stores the audio and an auto-transcript. Searchable by transcript keyword.
- **Just-in-time text** — customer scans the QR, types a quick note or list ("invoices Q2 2026" or "screws, hinges, brackets"). The most labor-intensive option, but searchable as text.
- **Mixed / nothing** — customer scans, dumps stuff in, doesn't add a record. Cell still has its ID. Later searches can find it by "cells I scanned but never described" if the customer needs that.

**Layer 3 · The retrieval interface.** Customer searches their KEEP library by:
- *What they remember about content* ("kitchen", "Q2 invoices", "screws")
- *When they put it away* ("April-May 2026")
- *Where on the shelf* (Wowlive shelves can also have QR IDs; cells get a "shelf-position" attribute when scanned at the shelf location)
- *Photos they took* (visual scan of thumbnails)
- *Voice memos they recorded* (audio playback or transcript search)

### 3.2 · Why this works architecturally

The key insight: **the customer pays a tiny cost at filling time, gets a large benefit at retrieval time.** Most labeling systems get this backwards — they require effort up front and offer marginal benefit later. The studio's pattern asks for ~5 seconds of effort per cell (scan + photo OR voice note OR brief text) and returns full-library search later.

The pattern also degrades gracefully. A customer who scans nothing still has cells with unique IDs — they can search by ID, by shelf position, or by physical inspection. A customer who scans everything has a fully-indexed personal archive. **Most customers will fall in between, and that's fine.**

### 3.3 · Implementation status · honest

This is a real software product. Building it requires:

- Customer account infrastructure (Stripe Customer model + custom backend)
- QR generation pipeline at studio shipping time
- Photo / audio / text storage backend (~$50/month at small scale on Cloudflare R2)
- Search infrastructure (initially: simple SQL full-text; eventually: vector embeddings for photos)
- Mobile-friendly web app (mobile-first, scan-and-stash UX)
- Voice-to-text transcription pipeline (Whisper API at OpenAI ~$0.006/minute)

**Realistic timeline:** scoped for late 2026 / early 2027. Not a year-one deliverable. The studio's catalogue can launch and operate at small scale without this — manual labeling works for the first 50 customers each with <30 cells. The tool becomes necessary at the scale where it becomes obviously necessary.

**Year-one substitute:** ship every cell with a pre-printed unique ID anyway. Sticker says "CELL-001-AB47" or similar. Customer can write this ID on a paper register or in a notes app. This is the *manual-labeling* version of the same architecture and doesn't require any studio backend work. When the web app launches, the IDs already exist on the customer's cells and migrate cleanly.

### 3.4 · What this tool is called

**Working name: KEEP Cards** — the personal KEEP web app that tracks the customer's cells. Each cell ID is a "card" in the database (the term "card" doubles back to the studio's existing card-and-cell language).

Alternative names worth considering: **CellCard, KEEPing, the Library, the Catalogue (customer-side).** The studio should pick before the app gets built. *Worth a design decision in a future session.*

---

## § 4 · The Made-in-Mexico note

The Oxford brand 4×6 ruled/blank index cards that the studio standardized on (B09GWBJ97Y and adjacent SKUs) are manufactured in Mexico. The Novelinks 24-pack photo cases are Made in USA. **Both origins should appear in catalogue documentation** consistent with the studio's transparent-sourcing register.

Surface treatment:
- KEEP's 1646 spec page mentions Novelinks USA
- .Studio's 4×6 envelope spec page mentions Oxford Mexico
- The cell catalogue page lists both alongside each cell SKU
- No marketing-language treatment ("crafted in Mexico" etc.) — just honest geographic attribution in the studio's standard documentation register

This matters because the studio's editorial voice has been consistently honest about supply chains (MEAL.0001 names where ingredients come from; BXBX commits to telling people where hardware is made). The cards being Made in Mexico is not a story; it's a fact, surfaced at the appropriate level of detail.

---

## § 5 · How .Studio relates to the rest of the catalogue

### 5.1 · Practices that .Studio defines for

Every practice in the catalogue inherits design from .Studio. Specifically:

- **KEEP** — receives the cell labeling system, the cell-ID architecture, the typography for cell labels. KEEP-the-practice keeps the physical envelope.
- **CODEX** — receives the CODEX format spec, the typography for body and display, the card-bound book structure. CODEX-the-practice keeps the editorial work and publishing pipeline.
- **STOCK / MEAL** — receives the product card visual register, the kit insert card spec, the recipe card format. These practices keep the food work.
- **BXBX** — receives the deck system (already established at v0.1), the booklet manual format, the studio's visual register for industrial-design contexts.
- **All practices** — receive the per-practice accent color, the typography stack, the paper-and-hanko palette.

**.Studio's customers are the studio's other practices.** The catalogue customer interacts with .Studio mostly through its products (booklets, labels, manuals) — but the architectural function is internal.

### 5.2 · What .Studio does NOT own

To keep boundaries clean:
- **Physical product manufacturing** lives in the practice that ships it (KEEP for cells, BXBX for Hako, etc.)
- **Editorial content** lives in the practice that writes it (CODEX for canonical works, MEAL for food research, T1NY for dwelling research)
- **Customer-facing storefront UX** is shared studio infrastructure; .Studio sets visual standards but doesn't own the cart/checkout/account systems
- **Sourcing decisions** for non-design inputs (food ingredients, mushroom spawn, seed varieties) live with the practice that needs them

### 5.3 · Inheritance pattern

The clean way to describe .Studio's role: **it's the parent class.** Every other practice inherits from .Studio's typography, palette, and format conventions. Practices can override (CODEX uses EB Garamond at editorial scale where other practices use Inter at web scale), but they inherit the substrate.

---

## § 6 · Sister-practice relationship · .Studio and KEEP

KEEP and .Studio are the studio's two infrastructure practices. The split:

**KEEP** — physical archive infrastructure
- The 1646 cell
- The Wowlive shelf
- The mod kit
- The cell-as-platform thesis

**.Studio** — design-systems infrastructure
- The 4×6 print envelope
- The typography stack
- The labeling system
- The folded-card booklet
- The organizational tool spec

The two practices complete each other. KEEP without .Studio = unlabeled boxes on shelves. .Studio without KEEP = a beautiful design system with nothing to design for. **Together, they form the substrate everything else in the catalogue inherits from.**

There's a clean naming convention worth establishing: **infrastructure practices use full uppercase (KEEP); design practice uses leading-dot notation (.Studio).** This subtle typographic signal communicates that .Studio operates at a different layer than other practices — it's *meta* to them rather than peer with them, while still being a real practice with its own surface area and products.

---

## § 7 · Open questions

**Q1 · Should .Studio have its own subdomain?** Working assumption: `studio.m1nd.co` for the practice landing, even though the leading-dot is non-standard in URL form. Alternative: `dot-studio.m1nd.co` or `system.m1nd.co`. Worth deciding before public catalogue launch.

**Q2 · Does the booklet format need a name?** Field Notes has a brand. Moleskine has a brand. The studio's booklet probably needs a name beyond "the booklet" — something that distinguishes it as the studio's specific format rather than a generic notebook. Working candidates: **Fold** (descriptive), **Brick** (because it's small and dense), **Pocket** (literal), **Folio** (classical, slightly pretentious), **Half** (because it's the cards folded in half). My instinct is **Fold** — short, descriptive, sits well next to CODEX in the catalogue.

**Q3 · How is the cell-ID encoded?** Working spec: 12-character base32 string like `CELL-001-AB47K3` where the first 3 digits are sequential per-customer and the rest is randomized for uniqueness. Encoded into the QR. Worth confirming the format scales — 12 characters of base32 = ~10^12 unique IDs which is overkill but cheap.

**Q4 · Does the labeling system include physical printing?** I.e., does .Studio ship adhesive label sheets that customers can print at home, or are labels exclusively studio-applied at shipment? **My recommendation:** both. Studio-applied at shipment for the default cell. Adhesive sheets (Avery template-compatible) for customers who want to re-label or label cells they bought separately. The sheets become a small .Studio SKU.

**Q5 · Does .Studio do work for non-studio clients?** I.e., the design-systems practice as consulting service. *Probably yes, eventually* — but Year 1 it should focus on serving the studio's own practices. Once stable, .Studio could offer brand-system design as a commission service in the same register that BXBX offers industrial-design commissions.

**Q6 · How does .Studio relate to the .Studio file extensions used in domain naming?** Slight terminology conflict — practices in the catalogue are at `[practice].m1nd.co`, but the practice itself is called `.Studio`. Worth confirming this isn't visually confusing. *Resolution:* the leading-dot is part of the practice name and only appears in branded contexts; URLs and paths use `studio` without the dot. So: practice = `.Studio`, subdomain = `studio.m1nd.co`, filesystem path = `studio/`.

---

## § 8 · What ships in v0.1

Concretely, the .Studio practice founding delivers:

1. **This thread document** — the founding statement and architectural definition
2. **.Studio practice landing page** at `/studio/index.html` in the MVP
3. **Folded booklet product line page** at `/studio/booklets.html` with SKU specifications for STUDIO-BL-01 through STUDIO-PR-04
4. **The CELL comparison essay/infographic** at `/studio/cell-comparison.html` — the 1646 cell against other standard-sized objects (CD jewel case, VHS, MiniDisc, iPhone, common EDC, the studio's charger-cell SKU candidate)
5. **Cross-references from KEEP and CODEX** to acknowledge the practice migration
6. **Catalogue index update** — .Studio appears in the catalogue grid alongside other practices

What does NOT ship in v0.1 (deferred):
- The customer-facing KEEP Cards web app (organizational tool implementation)
- The label spec sheet (Avery template files)
- A redesigned labeling page for KEEP that delegates to .Studio
- The charger-cell SKU page (ships separately as a STOCK SKU, referenced in the comparison essay)

---

## § 9 · Closing

.Studio is the catalogue's first formally-named design-systems practice. Its function is to own the substrate every other practice inherits from — typography, color, format envelopes, labeling conventions, and the organizational tooling that makes the studio's archive platform legible at scale.

Its first new product is the folded-card booklet — a transformation of existing 4×6 cards into a Field Notes-style pocket notebook format. Its first new architectural deliverable is the personal KEEP organizational tool spec. Its first migration is the labeling system from KEEP.

Most importantly: **.Studio names something that was already true.** The studio has been operating with a design system for months. It just didn't have a practice that owned the system as a system. Now it does. The catalogue becomes structurally cleaner; the design system becomes maintainable rather than scattered; and the studio gains a practice whose surface area is precisely the things that have been making everything else feel coherent.

---

*.Studio Thread v0.1 captured 2026-05-19. Practice founding. Sister to KEEP. Companion to CODEX-thread-v0.1 and KEEP-1646-mods-thread-v0.1. Next: ship the practice landing, the booklet product line page, and the cell comparison essay. Deferred: the organizational tool web app implementation, the Avery label template files, and the labeling-spec page migration from KEEP.*
