# CODEX · Thread v0.1

## The studio's card-based publishing practice.

**Date:** 2026-05-18 (CODEX practice founding)
**Status:** Practice established · flagship Tao Te Ching CODEX in design
**Codename:** CODEX (real word, all-caps, from the Latin *caudex* — originally a wooden writing tablet bound together at one edge, the historical precursor to the bound book; the word predates the modern book by ~1,500 years)
**Parent:** M1ND.studio
**Sister practice:** KEEP (archive/research counterpart at the same scale)
**Companion documents:** KEEP-thread-v0.4, the 1646 cell standard, the Wowlive shelving spec
**This document:** establishes CODEX as the studio's build practice for card-based publishing

---

## § 0 · The discovery moment

On 2026-05-18, while working on KEEP and the 1646 cell standard, the studio identified a sourcing fact with structural implications: **blank 4×6 index cards at $0.022 per card** (Amazon: B09GWBJ97Y, 500-pack at $11 CAD). At this price, material cost ceases to be a design constraint anywhere in the 1646 ecosystem.

Within minutes of running the math, a question emerged: *how much text fits on a 4×6 card, double-sided?* The answer, at book-classic typesetting (9pt body, 11pt leading, 0.4" margins):

- **~286 words per side**
- **~572 words per card double-sided**
- **~57,000 words per 100-card 1646 cell**

That number — 57,000 words — is the entire word-count of *The Old Man and the Sea*, *Of Mice and Men*, *Animal Farm*, *The Stranger*, *Slaughterhouse-Five*, *The Great Gatsby*, *Hamlet*, *Siddhartha*, *Heart of Darkness*, *Notes from Underground*, *Fahrenheit 451*, *The Bhagavad Gita*, and *Meditations*. **The majority of the literary canon's shorter works each fit in a single 1646 cell.** A complete personal library of "100 short canonical books" fits in roughly one Wowlive shelving unit.

The studio had been quietly accumulating every piece of infrastructure required for a card-based publishing format — the 1646 cell, the Wowlive shelves, KEEP's editorial standards, the studio's typography stack, the BDRC recipe-deck design pattern already operating as a working card-as-document format. **The format already existed across the studio's catalogue. What was missing was the practice that explicitly produced for it.** CODEX is that practice.

---

## § 1 · The format

### 1.1 · Physical specification

- **Card:** 4×6 inches, light cardstock (~110 lb / 60 lb cover stock equivalent), blank both sides
- **Typesetting area:** 3.2" wide × 5.2" tall (0.4" margins all around)
- **Body type:** EB Garamond at 9pt, 11pt leading (classical book typography, scaled to the card)
- **Display type:** Space Grotesk for headings, chapter numbers, front-matter
- **Mono type:** IBM Plex Mono for technical notes, footnotes, page numbers
- **Page numbering convention:** card 1 = recto + verso (2 pages per card)
- **Storage:** 100 cards per 1646 cell, with 10-card front-matter pocket plus 10-card back-matter pocket allowing ~80 cards (~160 pages) of body content per single-cell book

### 1.2 · The reading experience

A CODEX is *not* a book pretending to be a card-deck, and not a card-deck pretending to be a book. It is a third thing: a **card-bound text**, designed to be read in sequence but also to be navigable out of sequence, to be mixed with the reader's own notes and annotations on additional blank cards, and to be archived in a 1646 cell on a Wowlive shelf alongside the rest of the reader's library.

The historical reference is genuine: the *codex* as a textual form predates the modern bound book by ~1,500 years. Pre-Gutenberg codices were card-bound, sheet-bound, or scroll-rolled — the bound spine with sewn signatures is a much later innovation. **CODEX is not a regression to a primitive form; it is a return to a form the modern book replaced for industrial production reasons that no longer apply to small-batch personal publishing.**

### 1.3 · What CODEX is NOT

- **Not a substitute for the bound book.** Reading *Pride and Prejudice* on cards is a different experience than reading it bound. Some readers will prefer one; some the other; many will keep both. CODEX is a complement, not a replacement.
- **Not a Kindle-killer or POD-killer.** These markets exist for different reasons. CODEX is a small-batch, high-craft, physically-rooted format.
- **Not a publishing rebellion.** The studio isn't trying to disrupt publishing. It's adding a format to the catalogue.

---

## § 2 · The publishing pipeline

CODEX operates as a four-stage pipeline:

### Stage 1 · Source
The studio identifies a text worth publishing in CODEX format. Sources include:

- **Public-domain canonical works** — anything pre-1929 in the US, pre-1949 in Canada, with regional variation. The bulk of the literary canon.
- **Studio-original writing** — T1NY essays, MHYC profiles, MEAL reports, KEEP research can all ship as CODEX in addition to web/PDF.
- **Commissioned typesetting** — a customer who owns the rights to a text (their own writing, public-domain translations, or licensed works) can commission the studio to typeset it.
- **Reader's own writing** — journals, notes, family records, project logs. The studio publishes blank-CODEX templates; the reader fills them.

### Stage 2 · Typeset
The studio designs the CODEX to its visual standard:

- EB Garamond body, 9pt / 11pt leading
- Front matter: studio mark, title card, copyright/source attribution, table of contents
- Body content with chapter-opening cards (display type, generous whitespace)
- Back matter: colophon, blank reading-note cards, archive label for the 1646 cell

Output: a print-ready PDF where each page in the PDF = one card face (recto or verso), sized to 4×6 inches at print resolution (typically 300dpi).

### Stage 3 · Print
The customer prints the PDF on a home or commercial printer:

- **Inkjet:** works for color-rich CODEX (covers, illustrations); slow on cardstock
- **Laser:** works for text-heavy CODEX (most works); faster and cheaper per page
- **Commercial print:** for higher-volume runs (50+ CODEX of same title), worth considering

Material cost per CODEX (100 cards): **~$2.20 in blank cards + ~$1-3 in printing = $3-5 CAD all-in.**

### Stage 4 · File
The CODEX lives in a 1646 cell, slotted into a Wowlive shelf, alongside the reader's other CODEX library and personal archive.

The reader can:
- Read in sequence (the default)
- Read out of sequence (random-access by chapter or by page number)
- Add their own blank-card notes interspersed with the original
- Remove and replace cards if they wear out
- Lend a CODEX without losing it permanently (cards can be reprinted from the source PDF)

---

## § 3 · Relationship to KEEP

KEEP and CODEX are sibling practices at the archive scale. The pair completes the studio's 2×2 architecture:

| Pair | Research | Build |
|---|---|---|
| Dwelling | T1NY | BXBX |
| Network | MHYC | MESH |
| Food | MEAL | STOCK |
| **Archive** | **KEEP** | **CODEX** |

**KEEP** is the research practice and the archival storage standard — the 1646 cell, the Wowlive shelf, the architectural argument for personal archival in 2026. KEEP produces *infrastructure* and *editorial about how to organize an archive*.

**CODEX** is the build practice that produces *content* for the archive — books, recipe decks, journal templates, research-as-cards, reference works. CODEX produces *things to put inside the 1646 cells that KEEP defines.*

The practices reinforce each other:

- A KEEP customer who buys a 1646 cell system has a use case for CODEX immediately (what fills the cells?)
- A CODEX customer who buys a book in card-format has a use case for KEEP immediately (where do the cards live?)
- The studio's research practices (T1NY, MHYC, MEAL) can publish into the CODEX format and become physical objects in the customer's KEEP archive.

**The catalogue's loop closes.** Studio research → CODEX → physical book → KEEP archive → customer's library. Every stage of the loop is the studio's own infrastructure.

---

## § 4 · The flagship · CODEX-001 · Tao Te Ching

The studio's inaugural CODEX is the **Tao Te Ching**, Lao Tzu, translated by James Legge (1891 translation, firmly public domain in all jurisdictions, classical scholarly translation).

### Why this work, first

1. **Length is ideal.** At ~5,000 words, the Tao Te Ching fits in roughly 9 cards. This leaves ~91 cards of room in a single 1646 cell for: front matter, chapter-opening cards (one per the 81 chapters), translator's notes, blank journaling cards for the reader's own reflections, archive labels. **The Tao Te Ching CODEX is a complete reading-and-meditation kit in a single cell**, not just a book.

2. **The text wants random-access reading.** The 81 chapters of the Tao Te Ching are aphoristic — many readers cycle through chapters rather than reading start-to-finish. Card format suits this natively. *Reading one chapter per day for 81 days* is a real practice; the CODEX format supports it physically.

3. **Public domain everywhere.** The Legge translation (1891) is firmly public domain in the US, Canada, UK, EU, everywhere. No licensing complications.

4. **The voice matches the studio.** Aphoristic, design-conscious, philosophical, measured. The Tao Te Ching is the kind of text the studio's editorial register reads as naturally adjacent.

5. **It's been typeset thousands of times.** The studio isn't typesetting a difficult text from scratch — the studio is bringing its design judgment to a text that has many existing reference editions.

### CODEX-001 specifications

- **Title:** Tao Te Ching
- **Translator:** James Legge (1891)
- **Length:** ~5,000 words in the body, plus front and back matter
- **Card count:** ~100 cards total (front matter + 81 chapter-opening cards + body + reading-note blanks + back matter)
- **Format:** 4×6 cards, double-sided, 9pt EB Garamond body, Space Grotesk display
- **Storage:** 1 × 1646 cell
- **Studio designation:** CODEX-001
- **Edition:** Studio Classics Series · Volume 01

### CODEX-001 design moves

- **Cover card:** brutal minimalism — large display type ("TAO TE CHING"), translator credit, studio mark
- **Verso of cover:** colophon-style metadata (translator, year, public-domain source, studio CODEX edition designation)
- **Chapter cards:** each chapter gets its own opening recto with chapter number in display type, chapter text on the verso and following cards as needed
- **Reading-note cards:** every 10 chapters, a blank card with a single light header ("Reflections · Chapters 1–10") for the reader's own writing
- **Back matter:** translator's biographical note, a brief history of the text, a blank "first read" card with date/place fields, an archive label for the 1646 cell exterior

---

## § 5 · Future CODEX titles · Studio Classics Series

The CODEX-001 Tao Te Ching launches what the studio is calling **the Studio Classics Series**: 12 short canonical works typeset to CODEX standard over the studio's first year, with one CODEX per month from the practice's founding.

### Working CODEX-002 through CODEX-012 list

| # | Title | Author | Translator | Words | Cards | Rationale |
|---|---|---|---|---|---|---|
| 001 | Tao Te Ching | Lao Tzu | Legge 1891 | 5,000 | 9 body | Inaugural · short, aphoristic, public domain |
| 002 | The Art of War | Sun Tzu | Giles 1910 | 8,500 | 15 body | Aphoristic · companion to Tao |
| 003 | Meditations | Marcus Aurelius | Long 1862 | 50,000 | 88 body | Single-cell stoic classic |
| 004 | The Old Man and the Sea | Hemingway | — | 27,000 | 48 body | *(if rights cleared; otherwise skip)* |
| 005 | Letters to a Young Poet | Rilke | Hull 1934 | 18,000 | 32 body | *(check pub-domain status)* |
| 006 | The Metamorphosis | Kafka | Wyllie 1915 | 22,000 | 39 body | Single-cell, short, dense |
| 007 | Heart of Darkness | Conrad | — | 38,000 | 67 body | Single cell, canonical novella |
| 008 | The Bhagavad Gita | — | Edwin Arnold 1885 | 27,000 | 48 body | Companion to Tao + Meditations |
| 009 | Notes from Underground | Dostoyevsky | Garnett 1918 | 45,000 | 79 body | Long single-cell |
| 010 | Siddhartha | Hesse | Rosner 1951 | 32,000 | 56 body | *(check pub-domain status)* |
| 011 | The Stranger | Camus | — | 37,000 | 64 body | *(rights issue — skip or commission)* |
| 012 | Alice in Wonderland | Carroll | — | 26,000 | 47 body | Public domain, beloved, illustrated |

**Honest copyright note:** Several of the titles above (Hemingway, Camus, Hesse for Siddhartha translations younger than 1949) are NOT cleanly public domain depending on jurisdiction. The Studio Classics Series should explicitly stick to pre-1929 (US) / pre-1949 (Canada) sources or to translations that are themselves public domain. The actual final 12 will be the longest-runway public-domain candidates. **Tao, Sun Tzu, Marcus Aurelius, Bhagavad Gita, Notes from Underground (Garnett), Dostoyevsky's earlier works, Conrad, Kafka in early English translations, Carroll, Dickens, Austen, Melville short works, Wilde, Shakespeare, the King James Bible, Thoreau** are all firmly public domain everywhere relevant.

---

## § 6 · Operating questions

**Q1 · Print quality and reader expectations.** A CODEX printed on a home laser or inkjet won't match offset-printed book quality. **Is the studio's bet that the format (card-bound, archivable, personally-printable) wins over the production quality?** My read: yes, but the studio's design judgment in the typesetting has to be unimpeachable, because the design is what justifies the format. **Investment: real typesetting attention per CODEX.**

**Q2 · Commercial printing partnership.** For higher-volume CODEX runs (50+ copies of same title), a print-on-demand or short-run printing partner makes sense. **Does the studio establish a relationship now or wait?** My read: wait until CODEX-003 or CODEX-004. The early CODEX titles are best printed by the studio itself for tight quality control during format establishment.

**Q3 · Pricing strategy for CODEX-as-product.** The materials cost is ~$3-5 per CODEX. **What does the studio charge?** Options: (a) sell the PDF only at $5-15 per title and let customers print themselves; (b) sell finished printed CODEX at $35-65 per title; (c) both — PDF tier and printed tier. My read: (c). PDF tier funds the format's distribution; printed tier funds the studio's labor and design margin.

**Q4 · Customer's first CODEX experience.** A customer encountering CODEX for the first time needs to understand: this isn't a book in the conventional sense, the cards are meant to live in a 1646 cell, the format rewards specific reading practices. **How is this communicated?** My read: every CODEX ships with a one-card insert at the front ("How to read this CODEX") explaining the format briefly. Plus CODEX product pages explain the format clearly.

**Q5 · Studio-original CODEX vs canonical works.** The Studio Classics Series is the visible inaugural product, but the larger long-term value is studio-original work (T1NY essays, MHYC profiles, MEAL reports) shipping as CODEX. **What's the priority order?** My read: Studio Classics first establishes the format and the studio's typesetting standard. Studio-original CODEX follows once T1NY.0001 and MHYC.0002 are ready to publish.

**Q6 · The blank CODEX templates.** Beyond published works, the studio can publish **CODEX templates** — designed-but-blank card sets for journaling, household inventory, project tracking, recipe collection. **Is this a real product line?** My read: yes, but Phase 2. Once the format is established with finished CODEX titles, blank templates become the higher-margin product. The customer pays for the design judgment, prints the cards themselves.

---

## § 7 · Closing

CODEX is the most architecturally significant catalogue addition since the original 12-practice scaffolding got locked. It does three things at once:

1. **Closes the catalogue's loop** — studio editorial work can now ship as physical objects that live in studio archive systems. Research → physical book → archive → reader's library, all studio infrastructure.
2. **Completes the KEEP partnership** — KEEP now has a build counterpart at the same scale. The 2×2 catalogue architecture is structurally clean: Dwelling/Network/Food/Archive each get a research practice and a build practice.
3. **Unlocks a publishing format that's genuinely the studio's own** — not a Kindle, not a POD, not a zine. A card-bound codex at $3-5 in materials per book. The studio owns the format because the studio owns the infrastructure that makes it work.

The flagship Tao Te Ching CODEX (CODEX-001) is in design and will ship as the first real CODEX product. Studio Classics Series follows monthly. Studio-original CODEX (T1NY, MHYC, MEAL) follows as those texts complete.

---

*CODEX Thread v0.1 captured 2026-05-18. Practice founding. Companion to KEEP-thread-v0.4. Flagship in design: CODEX-001 Tao Te Ching, Legge 1891 translation, public domain. Next: typeset the PDF, print-test on Pixma + future laser, publish the catalogue page.*
