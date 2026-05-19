# B1KE · Thread v0.1

## Engineering feasibility study · Ryobi-powered ebike, cargo trike, and ebike cart for M1ND.Industries Skunkworks.

**Date:** 2026-05-18 (afternoon build)
**Status:** Engineering feasibility study v0.1 · Ryobi-as-universal-power thesis extended to mobility
**Codename:** B1KE (M1ND.Industries Skunkworks designation, number-letter substitution following M1ND/T1NY/B1RN family)
**Parent:** M1ND.studio · M1ND.Industries Skunkworks division
**Companion documents:** GROW01-OG-spec-v0.2 (the sister project that proved Ryobi-as-portable-power thesis), MICROSYSTEM-thread-v0.1
**This document:** the engineering feasibility brief for a Ryobi-powered electric mobility platform

---

## § 0 · The thesis

The studio has already proven the Ryobi-as-universal-power thesis at fixed-base scale: GROW01-OG-spec-v0.2 demonstrates that a $40 third-party AC inverter or the studio's existing Ryobi 800W inverter runs the entire microsystem (iDOO + BDRC + auxiliary loads) off Ryobi One+ 18V batteries indefinitely with solar supplementation.

**B1KE extends the thesis to electric mobility.** Ryobi 40V batteries — which are 36V nominal under load and 40V peak when freshly charged — are a near-perfect voltage match for standard 36V ebike motor systems. The conversion is already a solved problem in the DIY community; multiple builders have shipped working setups including a University of Pittsburgh engineering student team who open-sourced their CAD files, BOM, and wiring documentation on GitHub. **The engineering risk is low; the thesis is proven; the studio's contribution is editorial integration into the M1ND.studio catalogue plus the cargo trike and ebike cart feasibility extensions.**

What B1KE adds to the existing DIY landscape:

1. **System-level integration with the broader studio Ryobi ecosystem** — the same batteries power the GROW01-OG microsystem, the BDRC rice cooker (via inverter), and now the B1KE platform. One battery investment, multiple deployments.
2. **A studio editorial wrapper** — the spec, the build documentation, the published catalogue position. Same architectural move as GROW01-OG: commodity components, studio curation.
3. **Three product variants** — not just the ebike, but cargo trike and ebike cart configurations for different use cases (commuting, errands, micro-business logistics).
4. **The Toronto urban context** — Canadian regulations, Toronto-specific use cases, integration with the studio's broader thesis about distributed living and small-footprint logistics.

---

## § 1 · The electrical match · why this works

### 1.1 Ryobi 40V specifications, confirmed

| Battery | Capacity | Nominal V | Peak V | Energy | Weight | Price CAD |
|---|---|---|---|---|---|---|
| OP4020 (2.0Ah Compact) | 2.0 Ah | 36V | 40V | 72 Wh | 2.0 lb | ~$90 |
| OP4040 (4.0Ah) | 4.0 Ah | 36V | 40V | 144 Wh | 2.9 lb | ~$140 |
| OP4050 (5.0Ah) | 5.0 Ah | 36V | 40V | 180 Wh | 3.2 lb | ~$165 |
| OP4060 (6.0Ah HP) | 6.0 Ah | 36V | 40V | 216 Wh | 3.6 lb | ~$190 |
| OP4080 (8.0Ah HP, 21700) | 8.0 Ah | 36V | 40V | 288 Wh | 4.2 lb | ~$250 |

The Ryobi "40V" naming is marketing — peak voltage off the charger. **Operational voltage is 36V**, which is the standard for legal-class ebikes in most jurisdictions including Canada (where pedal-assisted ebikes are limited to 500W and 32 km/h).

### 1.2 Ebike motor system compatibility

Standard ebike voltage tiers:
- **36V systems:** 250W-500W motors, typical for commuters and Class 1 pedal-assist. Direct Ryobi-40V compatibility.
- **48V systems:** 500W-1000W motors, more aggressive performance. **Not compatible** — would require boost converter, not recommended.
- **52V/72V systems:** High-performance / off-road. Out of scope for B1KE.

**B1KE targets 36V motor systems exclusively.** This keeps the studio on the legal side of Canadian ebike regulations and matches the Ryobi battery output natively without any voltage conversion electronics.

### 1.3 The current-draw question · why parallel matters

The single failure mode in this conversion is the Ryobi battery's BMS (battery management system) tripping under heavy current draw. A 250W motor at 36V draws roughly 7A continuous; a 500W motor draws ~14A; peak draws during acceleration or hill climbing can spike to 20-25A.

**Real-world reports from the DIY community:**
- Single Ryobi 40V battery on 250W motor: works, but BMS occasionally trips on hard accelerations or extended hills
- Single Ryobi 40V battery on 500W motor: BMS trips reliably under load; effective range cut to 5-8 km before forced cycling
- **Two Ryobi 40V batteries in parallel (via Y-harness):** current draw split between packs, BMS never trips at 250-500W operation. **This is the validated configuration.**

The University of Pittsburgh student team converged on the same answer through full engineering analysis: 2× Ryobi 40V in parallel via 3D-printed mounts and a Y-harness is the right configuration. **Their open-source documentation is the studio's starting point.**

---

## § 2 · Three product variants

### 2.1 · B1KE-001 · The Commuter (standard ebike)

**Use case:** Single-rider urban commuting, errands, neighborhood mobility within Toronto. Replaces a car for distances under ~15 km.

**Configuration:**
- Donor bicycle (standard adult bike, ideally with rack mount points and 26" or 700c wheels)
- 36V 250-350W rear hub motor conversion kit (~$200-300 CAD from Amazon: Ebikeling, AW, or similar)
- 2× Ryobi 40V batteries in parallel (recommend OP4060 6Ah HP at ~$190 each = $380)
- Y-harness with appropriate fusing (3D-printable or fabricated)
- 3D-printed Ryobi battery mounts on the frame (Pittsburgh CAD files as starting point)
- LCD display + thumb throttle + PAS (pedal-assist sensor) — included with most kits
- Optional: front rack basket for grocery / cargo capacity

**Performance:**
- Range: 45-55 km on flat urban terrain, 30-35 km mixed
- Speed: 32 km/h legal Canadian limit (pedal-assist class)
- Acceleration: smooth and adequate, no BMS trips at 250-350W
- Hot-swap capability: empty battery off, fresh battery on, no downtime

**BOM total:** ~$650-800 CAD all-in (donor bike + kit + 2 batteries + harness + mounts)
**Time to build:** ~8-12 hours for a competent home mechanic

### 2.2 · B1KE-002 · The Cargo Trike

**Use case:** Studio logistics — moving 1646 cells between Dupont Arts studio and partner sites, BXBX work site deliveries, STOCK customer drop-offs in the GTA, NOLO event load-in. **The studio's actual operational vehicle.**

**Configuration:**
- Donor cargo trike (Bullitt-style front-loader OR delta trike with rear cargo bed). Used cargo trikes in Toronto: $800-2000 for a decent donor.
- 36V 500W rear hub motor OR mid-drive (Bafang BBS01B 250W mid-drive recommended for hill-climbing torque)
- **3× Ryobi 40V OP4060 batteries in parallel** (18Ah equivalent, 648 Wh) — extra capacity for cargo weight + longer trip patterns
- Y-harness with 3-way split
- Custom battery mount in a weatherproof case below the cargo bed
- LCD display with cargo-optimized PAS levels (gentler power curves to extend range)
- Studio-branded cargo box (designed to carry 1646 cells in their standard envelopes — direct compatibility with KEEP)

**Performance:**
- Range: 50-65 km with cargo
- Speed: 32 km/h max (still pedal-assist class even with cargo)
- Payload capacity: ~80-100 kg cargo plus rider
- Hill capability: solid with mid-drive (Bafang BBS01B handles Toronto's modest hills with cargo)

**BOM total:** ~$1,800-2,500 CAD all-in
**Time to build:** ~20-30 hours including custom cargo-mount fabrication

**Strategic value:** This is the studio's actual operational vehicle for the STOCK fulfillment phase. Avoids fuel costs, parking issues, and the carbon load of a cargo van for the typical 1-2 deliveries per week the studio will run during Phase 1.

### 2.3 · B1KE-003 · The Ebike Cart (push or pull configuration)

**Use case:** A *separate* electric-assisted cart that attaches to or follows a standard bike. Useful for transporting larger 1646 case loads, COOK/BDRC/STOCK fulfillment runs to nearby drop-off points, BXBX site visits where the trike doesn't fit.

**Configuration:**
- Standard bike trailer base (Burley or similar, ~$300 used)
- 36V 250W rear-wheel hub motor on the trailer's wheels (single-wheel or dual-wheel configuration)
- Integration: motor activates with bike's PAS to provide assist *to the trailer load* rather than to the bike
- 2× Ryobi 40V OP4060 batteries on the trailer chassis
- Communication: simple wireless throttle on bike handlebar triggers cart motor; or pressure-sensor on hitch detects bike acceleration and matches

**Performance:**
- Range: 30-40 km with cart fully loaded
- Speed: matches bike's pedal-assist speed (32 km/h max)
- Payload: ~50-80 kg in cart

**BOM total:** ~$700-1,000 CAD all-in
**Time to build:** ~15-20 hours including the cart-motor integration

**Strategic value:** Modular — the studio's existing bikes don't need conversion; the cart provides assist on demand for cargo runs and detaches for normal riding. Lower commitment than the trike for customers/operators who already have a primary bike.

---

## § 3 · The University of Pittsburgh open-source build · what we inherit

The reference build documented on Hackaday.io and GitHub (pittxprojects/ebike repo) provides:

- **3D-printable battery mounts** for Ryobi 40V packs in dual-pack-parallel configuration
- **Y-harness wiring diagram** with appropriate fuse specifications
- **BOM** (partial — community notes indicate the GitHub BOM is incomplete, motor source needs separate sourcing)
- **Written installation documentation**
- **Video walkthrough** (YouTube link: youtu.be/FgjxSFlo72g)
- **MIT/open-source licensing** — free to use, modify, redistribute

**The studio's Phase 0 work starts with this baseline** rather than from scratch. Specific tasks:

1. Download and review the Pittsburgh team's CAD and documentation
2. Adapt the battery mount to a specific donor bike geometry (B1KE-001 prototype)
3. Verify the wiring harness specs are still current with 2026 controller standards
4. Source a 36V 250-350W conversion kit (Toronto Amazon delivery: 2-3 days)
5. Source 2× Ryobi OP4060 batteries (Jordan's existing Ryobi ecosystem or Home Depot Canada)
6. Build the prototype, document the build, refine the studio's spec

**No academic-grade engineering work required.** The thesis is proven; the studio's task is build-and-refine, not invent-from-scratch.

---

## § 4 · Studio differentiation · what B1KE adds beyond the DIY landscape

Plenty of DIY builders have done Ryobi-ebike conversions. **What does the studio bring that's worth adding to the catalogue?**

### 4.1 · Editorial integration with the M1ND.studio ecosystem

B1KE is a leaf node of the studio's broader Ryobi-as-universal-power thesis. A customer who buys into the studio's catalogue gets:

- Hako flagship dwelling with off-grid Ryobi-powered microsystem (per HAKO-deployment-thread-v0.1)
- BDRC + GROW + SPORE + STOCK practices running off the same Ryobi battery ecosystem
- B1KE mobility built on the same Ryobi infrastructure
- **One battery investment, four+ deployment surfaces.**

This integration is the differentiator. **The studio sells the system, not the parts.** Same architectural move as the broader catalogue: commodity components, studio curation, system-level coherence.

### 4.2 · Design and build quality

DIY ebike builds in 2026 are still typically ugly, exposed-wiring, function-only. **The studio's contribution is design judgment** — clean battery mounting, integrated cable routing, finished surfaces, studio typography on the LCD display housing, weatherproof enclosures that match the BXBX deck system visual register.

A studio-built B1KE looks like a studio product, not a hackathon project. **That's the visible difference customers pay for.**

### 4.3 · Documentation, support, and the studio publishing surface

A full build spec at b1ke.m1nd.co (or similar) including:
- Step-by-step build documentation with photographs
- Sourcing recommendations with current pricing
- Troubleshooting guide
- Modification options for different use cases (commuter / cargo / cart)
- Integration notes with the broader Ryobi microsystem
- Open invitation for customer builds with editorial coverage

This is the **MESH-style publishing infrastructure** applied to a hardware build. The studio's editorial credibility makes the spec usable by people who couldn't follow a Hackaday writeup.

### 4.4 · Cargo trike + ebike cart variants — genuinely new

While the basic ebike conversion is well-trodden DIY territory, the **cargo trike** and **ebike cart** configurations specifically tuned for studio logistics (1646 cell envelopes, BDRC fulfillment, BXBX site work) are genuinely new. **No published builds combine the Ryobi battery infrastructure with cargo-optimized configurations in the way the studio plans to.**

This is where B1KE earns its place in the catalogue beyond being a re-publication of existing work.

---

## § 5 · Toronto regulatory context

Ontario ebike regulations as of 2026:

- **Class 1 (pedal-assist only, no throttle, max 32 km/h, max 500W):** Treated as bicycles. No license, no insurance, no registration required. Can use bike lanes and paths.
- **Class 2 (throttle-capable, max 32 km/h, max 500W):** Similar regulatory treatment but some municipalities restrict throttle use on multi-use paths.
- **Class 3 (faster, >32 km/h):** Treated more like mopeds, requires registration, license restrictions vary.

**B1KE targets Class 1 explicitly.** 250-350W motors, PAS-only operation, 32 km/h max, no throttle on the consumer build (an optional throttle accessory exists but isn't installed by default). This keeps B1KE in the bicycle regulatory category and avoids licensing/registration friction.

**Cargo trikes** are treated identically to bicycles under Ontario law as long as they meet the same power and speed specs. **The B1KE-002 cargo trike is legally a bicycle**, even with 500W mid-drive, as long as the PAS cuts out above 32 km/h. Most cargo bike builds use a different power class for hill capability but de-tune the speed limit electronically.

**The ebike cart (B1KE-003) is more ambiguous.** A trailer with its own motor providing assist may or may not be regulated as part of the bicycle — current interpretation varies. **Worth a real conversation with an Ontario transportation lawyer before publishing B1KE-003 as a consumer spec.** For studio internal use, the cart is fine; for sale to customers, it needs regulatory clarification.

---

## § 6 · Bench testing plan

The studio's Phase 0 validation requires real bench testing rather than just spec confidence. Proposed sequence:

### Phase 0a · Single-battery proof (1 weekend)
- Acquire a basic donor bike + 36V 250W hub motor kit + 1× Ryobi OP4060 + battery adapter
- Wire it up per Pittsburgh student documentation
- Test: ride 10-15 km routes around Toronto; document BMS trip frequency, perceived power, range, hot-swap experience
- Outcome: confirms the basic thesis works in practice for studio use; identifies failure modes

### Phase 0b · Dual-battery parallel (1 weekend)
- Add second Ryobi OP4060, fabricate Y-harness, mount second battery
- Repeat test routes; document range improvement and BMS-trip elimination
- Outcome: confirms the recommended configuration and BOM

### Phase 0c · Studio build (~2-3 weeks part-time)
- Take the validated configuration and rebuild it with studio design judgment applied:
  - Custom battery mount in BXBX-style minimal design
  - Cable routing internalized where possible
  - Studio typography / minimal branding on the LCD display housing
  - Photography for catalogue documentation
- Outcome: the B1KE-001 v1 reference build, documented end-to-end

### Phase 1 · Cargo trike prototype (timing depends on Phase 0 outcomes)
- Source used cargo trike (Bullitt, Yuba Sweet Curry, or DIY delta-style)
- Apply B1KE-001 learnings + Bafang mid-drive + 3-battery parallel configuration
- Outcome: B1KE-002 working prototype = studio's operational vehicle

### Phase 1b · Ebike cart (lower priority, contingent on regulatory clarity)
- Build a trailer-motor integration on a used Burley
- Test with cargo loads up to 50 kg
- Hold publication of consumer spec pending regulatory review
- Outcome: B1KE-003 internal use; consumer release pending legal clarity

---

## § 7 · BOM summary · all three variants

### B1KE-001 · Commuter ebike

| Item | Cost CAD | Notes |
|---|---|---|
| Donor bicycle (used quality bike) | $200-400 | Kijiji / Facebook Marketplace, ideally with rack mounts |
| 36V 250-350W rear hub motor conversion kit | $200-300 | Ebikeling, AW, Bafang — Amazon |
| 2× Ryobi OP4060 6Ah HP batteries | $380 | Home Depot Canada or Amazon |
| 2× Ryobi battery adapters (with leads) | $30 | Amazon third-party |
| Y-harness fabrication (wire, fuse holder, connectors) | $30 | Princess Auto |
| 3D-printed battery mounts (Pittsburgh CAD adapted) | $20 | Filament cost, fab via local print shop or Jordan's network |
| Misc cable management, fasteners | $30 | Princess Auto |
| **TOTAL** | **~$890-1,190** | |

### B1KE-002 · Cargo trike

| Item | Cost CAD | Notes |
|---|---|---|
| Donor cargo trike (used Bullitt-style) | $800-2,000 | Kijiji / specialist resellers |
| Bafang BBS01B 36V 250W mid-drive kit | $500-700 | Amazon or specialist ebike retailer |
| 3× Ryobi OP4060 batteries | $570 | Home Depot Canada |
| 3× Ryobi battery adapters | $45 | Amazon |
| 3-way Y-harness with fusing | $50 | Custom fab |
| Custom battery mount + weatherproof case | $200 | Studio fabrication time + materials |
| Studio cargo box (sized for 1646 cells) | $150 | Studio fabrication, plywood + finish |
| Misc | $50 | |
| **TOTAL** | **~$2,365-3,765** | |

### B1KE-003 · Ebike cart (internal use spec)

| Item | Cost CAD | Notes |
|---|---|---|
| Used Burley or equivalent trailer | $200-400 | Kijiji |
| 36V 250W single-wheel hub motor kit | $200 | Amazon |
| 2× Ryobi OP4060 batteries | $380 | Or share batteries with another B1KE build |
| Adapters, Y-harness | $50 | |
| Custom motor mount + battery housing | $100 | Studio fabrication |
| Wireless throttle integration with bike | $50 | Optional |
| **TOTAL** | **~$980-1,180** | |

---

## § 8 · Strategic position within the studio

### 8.1 · B1KE is operational tooling first, customer product second

The studio needs a cargo vehicle. Phase 1 STOCK fulfillment will involve delivering 1646 cell orders to Toronto-area customers and visiting BXBX work sites. **Without a cargo bike or trike, the studio is dependent on a car or rental van for every fulfillment run** — which conflicts with the studio's stated environmental and operational values.

**B1KE-002 cargo trike is the studio's actual operational vehicle.** Build it for studio use first. Customer interest in similar builds is a secondary outcome; the primary outcome is that the studio's logistics work better.

### 8.2 · B1KE extends the Ryobi ecosystem thesis credibly

The studio's broader argument — *"one battery investment serves multiple deployments"* — is much more credible with B1KE in the catalogue than without it. A customer evaluating the Hako or the GROW01-OG microsystem can see that the same Ryobi batteries also power transportation, and the overall ecosystem value-per-battery goes up significantly.

This is the same architectural move as the BDRC + GROW + SPORE catalogue working off shared infrastructure (Wowlive shelf, 1646 cells, KEEP storage). **B1KE makes the studio's universal-power thesis fully visible.**

### 8.3 · The publishing position

A studio publishing serious engineering specs (B1KE) alongside research reports (T1NY, MHYC, MEAL) and consumer products (BDRC, GROW, SPORE) demonstrates **range of capability** that's hard to fake. Most studios publish in one register; M1ND.studio publishes across editorial-research, engineering-specification, product-catalogue, and dwelling-spec registers. **Each register reinforces the others.**

B1KE-thread is the studio's engineering register on full display. Worth being legibly good at this category.

---

## § 9 · Open questions

**Q1 · Donor bike vs purpose-built B1KE platform.** Phase 0 uses a donor bike. **Should later phases offer a studio-designed B1KE platform** (a complete bike built around the Ryobi system rather than a conversion)? My read: not in Phase 0-1. Conversion preserves the commodity-envelopes thesis (use existing bikes the customer already owns or buys used). A purpose-built B1KE platform is a Phase 3+ decision dependent on demand.

**Q2 · The trike specifically · open-source the design?** Once B1KE-002 cargo trike is validated, the studio could open-source the custom cargo box design, battery mount, and integration documentation. This builds studio credibility and enables other cargo bike builders to adopt the Ryobi approach. **My read: yes, with attribution required.** Same pattern as the Pittsburgh team's contribution to the studio.

**Q3 · Insurance and liability.** Selling B1KE as a consumer product carries product-liability exposure. **Should the studio sell complete B1KEs, sell build kits + documentation, or only publish the spec and let customers build their own?** My read: publish the spec, sell custom builds on commission only with explicit liability disclosure. Same model as BXBX dwellings — the studio designs and may build to order, but the customer accepts the bespoke nature of each unit.

**Q4 · Sister project · Ryobi-powered scooter / skateboard / etc.** The same battery architecture works for any 36V e-mobility platform. **Does the studio expand B1KE into a broader micro-mobility series?** My read: not in Phase 0-1. Focus on the ebike + trike + cart trinity, then evaluate expansion.

**Q5 · Connection to MHYC's distributed living thesis.** A customer rotating between Toronto and Mexico City could plausibly travel with their Ryobi batteries (TSA-permitted as carry-on under proper conditions for small packs) and pair them with locally-sourced ebike conversion kits in each city. **Worth a specific MHYC piece exploring this.** My read: B1KE feeds an interesting MHYC angle; flag for the inaugural MHYC editorial cycle.

**Q6 · Branding overlap with "B1RN" identity work.** B1KE and B1RN both use the same letter-substitution idiom in the studio family. **Worth verifying these don't conflict in customer perception.** My read: they don't — B1KE is engineering-mobility, B1RN is cultural-identity, contexts are distinct enough. But Jordan should confirm.

---

## § 10 · Closing

B1KE is a feasibility-proven engineering project that extends the studio's Ryobi-as-universal-power thesis from fixed-base infrastructure into electric mobility. The DIY community has already demonstrated that the basic conversion works; the University of Pittsburgh student team open-sourced their build documentation; **the studio's role is to integrate this proven technology into the M1ND.studio catalogue with editorial coherence, design quality, and the cargo trike + ebike cart extensions that are genuinely new.**

The strategic value to the studio:
1. **Operational tooling** — the studio needs a cargo vehicle for Phase 1 STOCK fulfillment, and B1KE-002 is that vehicle
2. **Catalogue coherence** — B1KE makes the Ryobi ecosystem thesis visible across dwelling, food, and mobility surfaces
3. **Engineering credibility** — publishing a serious engineering spec alongside research reports and consumer products demonstrates range

The work from here:
1. Acquire Phase 0a hardware (donor bike + kit + 1 Ryobi battery + adapter) — ~$650 total budget
2. Build the single-battery prototype, document the build, validate the basic thesis
3. Phase 0b — add second battery, validate parallel configuration
4. Phase 0c — studio rebuild with full design judgment applied; ship as B1KE-001 reference build
5. Phase 1 — cargo trike prototype as operational vehicle
6. Phase 1b — ebike cart pending regulatory clarification

**Total budget for Phase 0a/b/c (B1KE-001 only):** ~$1,000-1,400 CAD including studio-build time
**Total budget through Phase 1 (B1KE-002 cargo trike):** ~$3,500-5,000 CAD additional

The thesis is proven. The math works. The studio's operational logistics get solved. **The work is to build it.**

---

*B1KE Thread v0.1 captured 2026-05-18 (afternoon build). Engineering feasibility study for M1ND.Industries Skunkworks. Companion to GROW01-OG-spec-v0.2. Next session: acquire Phase 0a hardware budget approval, OR continue catalogue-architecture work, OR proceed with bench testing once hardware arrives.*
