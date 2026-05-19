# M1ND.studio

A personal media network and family company operating from Toronto. Twelve practices spanning archive infrastructure, food research and production, dwelling design, cultural programming, and design systems. Everything in this repo is the canonical source for the public catalogue at [m1nd.co](https://m1nd.co).

---

## What this is

M1ND.studio is structured as a 2×2 of paired research-and-build practices, plus an elaborated food family, plus supporting infrastructure practices. The pairing creates a clean editorial structure: every "research" practice produces written work (essays, profiles, reports); every "build" practice produces shippable objects (cells, kits, hardware, software). The catalogue is the integrated surface across all of it.

| Pair        | Research                    | Build                              |
|-------------|------------------------------|-------------------------------------|
| Dwelling    | **T1NY** · housing research  | **BXBX** · industrial design firm   |
| Network     | **MHYC** · neighborhood research | **MESH** · digital network design |
| Food        | **MEAL** · food research      | **STOCK** · food products (COOK / BDRC / GROW / SPORE) |
| Archive     | **KEEP** · 1646 cell envelope | **CODEX** · card-based publishing |

Supporting practices: **.Studio** (design systems), **NOLO** (cultural production), **B1KE** (mechanical skunkworks), plus **BASE**, **SQMX**, **F1XR** (scoping).

The studio's central architectural commitment is the **1646 cell** — a 4×6 inch photo-storage envelope (Novelinks 24-pack base) standardized as the universal storage unit across every practice. Every product, every kit, every published title fits this dimension. The cell architecture is what makes the catalogue cohere as a system rather than a collection.

---

## Repository structure

```
m1nd-studio/
├── index.html              · Top-level catalogue landing
├── CNAME                   · Custom-domain config for GitHub Pages (m1nd.co)
│
├── studio/                 · .Studio · design-systems practice
├── keep/                   · KEEP · archive infrastructure
├── codex/                  · CODEX · card-based publishing
├── stock/                  · STOCK · food build (COOK / BDRC / GROW / SPORE)
├── meal/                   · MEAL · food research + curated kits store
├── bxbx/                   · BXBX · industrial design firm
├── t1ny/                   · T1NY · dwelling research
├── mhyc/                   · MHYC · neighborhood research
├── mesh/                   · MESH · digital network design
├── nolo/                   · NOLO · cultural production
├── b1ke/                   · B1KE · mechanical skunkworks
├── base/, sqmx/, f1xr/     · Supporting practices (scoping)
│
├── shared/                 · Shared CSS variables (studio.css)
├── assets/                 · Fonts, images, future static assets
│
├── docs/                   · Working documentation
│   ├── threads/            · Practice founding documents
│   ├── architecture/       · Cross-practice specs and inventories
│   ├── brainstorms/        · Working ideation docs (not yet productized)
│   └── editorial/          · Published .000X essays
│
└── scripts/                · Python utilities for the build process
```

---

## Running locally

The site is hand-written static HTML — no build step, no framework, no JavaScript dependencies. Any local HTTP server will serve it correctly.

```bash
# Python (built into macOS and most Linux distributions)
python3 -m http.server 8000
# Then open http://localhost:8000

# Or with Node, if you prefer
npx serve .

# Or with PHP
php -S localhost:8000
```

Every link in the site is relative, so the site can be hosted at any path — locally at `localhost:8000`, on GitHub Pages at `your-username.github.io/m1nd-studio`, or at a custom domain like `m1nd.co`.

---

## Typography stack

The site uses four typefaces in disciplined combinations:

- **Display** — Space Grotesk (Regular 400 / Medium 500 / Bold 700)
- **Serif body (web)** — Inter (Regular 400 / Medium 500)
- **Classical body (editorial)** — EB Garamond (Regular 400 / Medium 500 / Italic 400)
- **Monospace** — IBM Plex Mono (Regular 400)

All four are loaded from Google Fonts in production. Local copies of the TTF files are committed under `assets/fonts/` for offline development and for CODEX print-pipeline use.

## Palette

Three foundation colors plus per-practice accents. See [`shared/studio.css`](shared/studio.css) for the canonical CSS variables.

| Foundation | Hex | Use |
|------------|-----|-----|
| Paper | `#F4F1E8` | Page ground |
| Ink | `#1A1814` | Body text |
| Hanko | `#B85540` | Studio accent (used sparingly) |

Per-practice accents are documented at [`studio/index.html`](studio/index.html) (the .Studio practice landing).

---

## Status

The catalogue MVP is at **v0.8** as of 2026-05-19. 46 HTML files across 12 practices. Most practice landing pages and product cards are complete; "in design" and "coming soon" labels appear on specific products that haven't yet shipped. The honesty about status is intentional — the studio's editorial voice runs on transparent disclosure rather than vapor-marketing.

The CODEX-001 Tao Te Ching PDF generator is currently deferred pending a PDF pipeline rebuild. The KEEP Cards organizational tool (a customer-facing web app for cell-level archive management) is scoped but implementation is deferred to late 2026 / early 2027.

---

## Building in the open

This repo is public from day one. The thinking is on display, including the working brainstorms, the pricing math, and the implementation roadmaps that haven't yet shipped. The bet is that the work itself is the marketing — and that customers who'd care about a studio operating in this register will find it more compelling than a glossy promotional surface.

Issues and discussions are welcome via GitHub. Pull requests for typo fixes or clarifications are appreciated. Substantive editorial changes go through the studio.

---

## License

Copyright © 2026 M1ND.studio. All rights reserved.

The source is open for viewing — you can read every page, every thread document, every brainstorm. Reuse, redistribution, derivative works, and commercial use require written permission from the studio. Third-party content (fonts, public-domain texts) retains its original licensing.

See [LICENSE](LICENSE) for the full text.

---

## Contact

Toronto, Ontario.  
[m1nd.co](https://m1nd.co)
