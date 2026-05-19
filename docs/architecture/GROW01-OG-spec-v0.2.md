# GROW01 · Ryobi One+ Off-Grid Conversion Spec · v0.2

## The corrected thesis · the iDOO doesn't need a conversion at all.

**Date:** 2026-05-18 (afternoon revision)
**Status:** Engineering spec v0.2 · architecture revised
**Codename:** GROW01·OG (off-grid variant of the GROW01 standard)
**Supersedes:** GROW01-OG-spec-v0.1 (DC-bus thesis, now deprecated)
**Companion documents:** GROW-thread-v0.1, MICROSYSTEM-thread-v0.1, BXBX commodity-envelopes thesis
**Future reference:** HAKO-deployment-thread (next session) — power architecture revised by this document
**This document:** the corrected engineering brief

---

## § 0 · What changed since v0.1, and why

The v0.1 spec proposed two paths to power the iDOO from a Ryobi battery: (A) the official Ryobi 120W DC Power Source plus a custom cable to the iDOO's 12V barrel jack, or (B) a DIY buck converter build at $40-50 BOM. The thesis was that the conversion is "DC-to-DC voltage step-down."

**That thesis is wrong.** The conversion isn't DC-to-DC — it's *get-AC-mains-from-the-battery*, after which the iDOO uses its own stock AC adapter unchanged. The Chinese third-party Ryobi-compatible AC inverter market is mature and competitive ($40-50 CAD on Amazon for a 150-200W pure-sine-wave unit with a Ryobi battery slot built in). The studio's catalogue should default to this path because:

1. **It's cheaper than the official Ryobi DC Power Source** ($40 vs $80-100)
2. **No cable modification needed** — the iDOO uses its stock 12V adapter, no custom barrel-jack assembly
3. **Universal compatibility** — the same inverter runs the BDRC rice cooker, charges phones, runs fans, takes any AC device
4. **No electronics knowledge required** — plug battery into inverter, plug iDOO into inverter, done
5. **The studio doesn't need to ship anything custom** — both the inverter and the iDOO are sourced independently by the customer

The studio also owns a Ryobi 800W Automotive Inverter (P/N referenced in the prompt). At 800W AC output that single unit powers the entire microsystem simultaneously — iDOO (40W AC), BDRC rice cooker (350W AC during cook), fan, phone charger, lamp — with significant headroom.

**The right framing isn't "off-grid iDOO." It's "off-grid microsystem."** A single Ryobi inverter is the studio's actual power deployment standard.

This document is the corrected spec. v0.1 is archived for reference.

---

## § 1 · The corrected architecture

### 1.1 What needs to be true for this to work

The iDOO IG301 expects 12V DC from its stock barrel-jack adapter. The stock adapter is a universal AC-to-DC switching brick rated for 100-240V AC input @ 50/60 Hz. **Any reliable AC source within that range powers the iDOO unchanged.**

Ryobi-compatible AC inverters convert 18V DC battery output to 110-120V AC. Pure-sine-wave units are required for sensitive electronics (the iDOO has a switching power supply that prefers clean AC); modified-sine-wave units may work but introduce harmonic distortion that stresses the iDOO's adapter. **Spec: pure-sine output only.**

The chain: Ryobi battery → AC inverter → iDOO stock adapter → iDOO 12V input. Each step is a commodity component. No custom electronics, no DIY assembly, no risk of damaging the iDOO from polarity mistakes.

### 1.2 The two relevant inverter products

**Product 1 · Third-party 150-200W Ryobi-compatible AC inverter** (e.g., Amazon B0DHZSTBSD, $40-50 CAD)
- Built-in Ryobi 18V battery slot
- Pure-sine-wave AC output, 110-120V, 150-200W continuous
- Multiple output: 1× AC outlet, 2× USB-A, 1× USB-C
- Compact form factor (~6" × 4" × 3")
- No warranty backing (Chinese manufacturer)
- Adequate for iDOO solo operation OR iDOO + small auxiliary loads (laptop charger, fan)

**Product 2 · Ryobi 800W Automotive Power Inverter** (P/N RYi800)
- Accepts Ryobi 18V One+ batteries OR 12V vehicle outlet
- Pure-sine-wave AC output, 110-120V, 800W continuous, 1600W peak
- Multiple output: 2× AC outlets, 2× USB ports
- Larger form factor (~10" × 7" × 4")
- Ryobi warranty
- Runs the entire microsystem simultaneously — iDOO + BDRC + ancillary

**The studio's catalogue position:** Product 1 for customers who need to power only the iDOO and don't already own Ryobi infrastructure. Product 2 for customers who already own Ryobi tools, want margin for the full microsystem, or are setting up Hako-deployable studio kitchens. **Most studio customers already in the Ryobi ecosystem will use Product 2; new entrants will start with Product 1.**

### 1.3 What this means for the engineering content of the spec

**There isn't any.** The studio's "GROW01·OG" product is no longer an electrical engineering exercise — it's a sourcing recommendation. The studio specifies the chain of commodity components, runtime expectations, deployment patterns, and integration with the rest of the microsystem. It does not manufacture, assemble, or ship electrical hardware.

This is consistent with the broader M1ND.studio commodity-envelope thesis: **the studio names which commodity components to source and how to deploy them; the customer assembles from any retailer.** Same logic as the 1646 cell having five interchangeable manufacturer sources, or the RC503 being one of several toggle-switch rice cookers the studio endorses.

---

## § 2 · The corrected runtime math

### 2.1 iDOO power consumption (unchanged from v0.1)

Source: iDOO IG301 User Manual

| Parameter | Value |
|---|---|
| Stock adapter input | 100-240V AC, 50/60 Hz |
| Stock adapter output | 12V DC @ 3A (36W max) |
| LED panel | ~22-23W (16 hours/day) |
| Pump | 1.5W (cycling 30 min on / off) |
| Daily energy consumption | **~360 Wh** at the 12V DC point |
| 24-hour average draw | ~15W DC |

### 2.2 Chain efficiency · the cost of the AC path

The DC path (v0.1) was ~88% efficient end-to-end (battery → buck converter → iDOO). The AC path adds an inverter stage, which costs efficiency:

| Stage | Efficiency |
|---|---|
| Battery → AC inverter (DC-to-AC conversion) | ~85% |
| AC inverter → iDOO stock adapter (AC-to-DC conversion) | ~90% |
| **Combined chain efficiency** | **~76%** |

Daily battery energy required:
- DC path (v0.1 spec): 360 Wh ÷ 0.88 = **~409 Wh from battery per day**
- AC path (v0.2 spec, current): 360 Wh ÷ 0.76 = **~474 Wh from battery per day**

**The AC path costs about 15-20% in efficiency** compared to direct DC, in exchange for plug-and-play simplicity and zero modification. This tradeoff is worth it for the studio's catalogue — the convenience gain dwarfs the efficiency loss at the small scale of a single iDOO.

### 2.3 Runtime per Ryobi battery, corrected

Usable battery energy = nominal Wh × 0.85 (battery low-voltage cutoff buffer)

iDOO 24h average via AC path = 15W DC / 0.76 chain efficiency = **20W drawn from battery, averaged across 24 hours**

| Ryobi battery | Nominal Wh | Usable Wh | Runtime (continuous iDOO operation) |
|---|---|---|---|
| P102 (1.3Ah) | 23 Wh | ~20 Wh | ~1 hour |
| P190 (2.0Ah) | 36 Wh | ~31 Wh | ~1.5 hours |
| P192 (4.0Ah) | 72 Wh | ~61 Wh | **~3 hours** |
| PBP004 (6.0Ah) | 108 Wh | ~92 Wh | **~4.5 hours** |
| PBP005 (8.0Ah) | 144 Wh | ~122 Wh | **~6 hours** |
| PBP007 (12.0Ah XL) | 216 Wh | ~184 Wh | **~9 hours** |

A 12Ah XL battery now delivers ~9 hours instead of ~11 hours (the difference is the inverter overhead). Still no single battery sustains a full 24-hour iDOO cycle. **Multi-battery rotation remains required for continuous off-grid operation.** This is unchanged from v0.1.

---

## § 3 · Deployment strategies, revised

### 3.1 Strategy A · Tactical short-term (1-2 days off-grid)

**Configuration:**
- 1× $40 third-party Ryobi-compatible AC inverter (e.g., Amazon B0DHZSTBSD)
- 2-3× Ryobi 8Ah or 12Ah HP batteries fully charged in advance
- iDOO operates only during daylight (8-10 hour photoperiod instead of full 16)
- Result: 2-3 days of plant survival on stored battery capacity

**Use cases:** Apartment power outage. Weekend cabin trip. Brief field deployment. Demonstrating GROW01 at a market or trade show. Transporting living plants between locations.

**Total spend:** $40 inverter + ~$200-450 for 2-3 batteries (assuming customer doesn't already own them). For customers in the Ryobi ecosystem, just $40 plus whatever batteries they already have.

### 3.2 Strategy B · Solar-supplemented continuous (indefinite off-grid)

**Configuration:**
- 1× Ryobi 800W inverter (or two of the $40 third-party inverters in parallel for redundancy)
- 2× Ryobi 12Ah XL batteries on rotation
- 1× Ryobi 18V Solar Battery Charger (~$120-150) OR third-party MPPT charger with 100W solar panel
- Solar panel: 100W minimum, 200W recommended for cloudy-day buffer
- A weatherproof outdoor enclosure for the solar charger/panel

**Daily energy:** iDOO uses 474 Wh/day via the AC chain. 100W solar in Toronto summer produces 400-500 Wh/day at the panel; account for ~80% MPPT charger efficiency = 320-400 Wh/day reaching the battery. **Summer: barely sufficient.** Winter: insufficient — needs 200W solar or grid supplementation.

**Sustained off-grid summer operation in Toronto:** feasible on 200W solar. Winter operation: requires either 400W solar (which is large for a residential setup) or accept that the iDOO doesn't run continuously off-grid in deep winter without grid charging.

### 3.3 Strategy C · The Ryobi 800W full kitchen module

**Configuration:**
- 1× Ryobi 800W Automotive Inverter (already in the studio's hardware inventory)
- 3-4× Ryobi 12Ah XL batteries on rotation
- Solar charging as in Strategy B
- The inverter powers: iDOO continuously, BDRC rice cooker per-meal, fan during fruiting (if SPORE setup is active), phone/laptop charging, lighting

**This is the studio's actual deployment standard.** A single 800W inverter is overprovisioned for the iDOO alone but appropriately sized for the integrated microsystem. **One inverter, multiple appliances, no per-appliance conversion electronics.**

The 800W headroom matters for the BDRC rice cooker specifically. The RC503 draws 350W during cook cycles; running it through a 150W third-party inverter (Strategy A) would either fail at the cook cycle's peak draw or trip the inverter's overload protection. **The Ryobi 800W handles the rice cooker comfortably with margin for everything else.**

Energy budget at Strategy C scale:
- iDOO daily: ~474 Wh
- BDRC rice cooker, one meal/day: ~140 Wh (24 min × 350W ÷ 0.76 efficiency)
- Phone/laptop charging: ~50 Wh
- Misc: ~30 Wh
- **Daily total: ~700 Wh from battery bank**

A pair of 12Ah XL batteries (432 Wh total nominal, ~368 Wh usable) covers half a day at Strategy C scale. **Four 12Ah XL batteries cover a full day with no charging input.** With 200W solar in summer, the system is genuinely indefinite-off-grid.

### 3.4 Strategy D · Hako-integrated (deferred to HAKO-deployment-thread)

For the eventual BXBX flagship Hako deployment, the right architecture is **a dedicated marine deep-cycle battery (100Ah, ~1200 Wh useful) plus permanent 200-400W roof solar, with a fixed inverter mounted in the Hako's millwork providing standard 110V receptacles throughout the dwelling.**

The Hako interior wiring becomes **standard residential AC, just powered by an inverter behind the wall.** Every receptacle accepts any standard plug. Customer can use Ryobi One+ batteries as backup or for transport between Hako sites, but the primary battery is a fixed deep-cycle unit sized to the dwelling's actual daily load.

This is the right answer for the Hako spec, but it's a different document. **This GROW01·OG spec covers the interim (pre-Hako) off-grid path — which is the $40-150 Ryobi-inverter approach documented above.**

---

## § 4 · Updated bill of materials

### 4.1 The "Quick & Cheap" build (for casual off-grid GROW01)

| Item | Cost CAD | Source |
|---|---|---|
| Third-party Ryobi 18V → AC inverter, 150-200W pure-sine (e.g., Amazon B0DHZSTBSD) | $40-50 | Amazon |
| Stock iDOO 12V adapter | $0 (included with iDOO) | — |
| Ryobi 8Ah or 12Ah battery (customer-supplied) | $130-220 | Home Depot |
| **Total beyond iDOO itself** | **$40-50** for inverter | |
| **Total with one battery** | **$170-270** | |

### 4.2 The "Studio Kitchen" build (full microsystem off-grid)

| Item | Cost CAD | Source |
|---|---|---|
| Ryobi 800W Automotive Inverter | $200-260 | Home Depot, Amazon |
| 2× Ryobi 12Ah XL batteries (for rotation) | $440-500 | Home Depot |
| Ryobi 18V Solar Battery Charger | $120-150 | Home Depot |
| 100W or 200W solar panel | $130-280 | Renogy via Amazon, Canadian Tire |
| Cables, mounting brackets, weatherproofing | $50-80 | Princess Auto |
| **Total** | **~$940-1,270** | |

This is the indefinite-off-grid version of the studio kitchen. Not the right spend for a customer testing the catalogue for the first time, but the right spend for someone deploying the studio kitchen in a cabin, RV, or pre-Hako off-grid arrangement.

### 4.3 The DC Power Source path (former Path A, now an alternate)

The Ryobi 120W DC Power Source ($80-100) + custom barrel-jack cable ($5-15) approach from v0.1 still works and is marginally more efficient (88% chain vs 76%). **It remains documented as an alternative** for customers who:

- Want maximum battery efficiency (~20% more runtime per battery vs AC path)
- Don't need to power AC-only appliances
- Don't already own a Ryobi inverter

For most customers, the AC path is simpler, cheaper, and more flexible. The DC path is a footnote.

### 4.4 The DIY buck converter build (former Path B, now deprecated)

Documented in v0.1 §2.2 for completeness. **Effectively obsolete.** No customer should choose the $40-50 DIY assembly over the $40-50 third-party AC inverter unless they specifically want the educational experience. The DIY path is retained in the appendix for the small subset of builders integrating the conversion into Hako millwork where ready-made enclosures don't fit the dwelling architecture.

---

## § 5 · Microsystem power architecture, revised

This is the section that needed the most substantial rewriting. v0.1 proposed a centralized 12V DC bus for the studio kitchen module. **The correct architecture is a centralized AC bus from a Ryobi-compatible inverter.**

### 5.1 The architecture, in one diagram

```
┌────────────────────────────────────────────────────────────┐
│                                                            │
│   Ryobi One+ battery(ies)                                 │
│   18V DC, hot-swappable                                   │
│         │                                                  │
│         ▼                                                  │
│   ┌──────────────────────────────────┐                    │
│   │  AC Inverter                     │                    │
│   │  150W (basic) or 800W (full)     │                    │
│   │  Pure-sine output                │                    │
│   │  110-120V AC, 60Hz               │                    │
│   └──────┬───────────────────────────┘                    │
│          │                                                 │
│          ▼ AC mains, standard 110V receptacles            │
│   ┌──────┴──────┬──────┬──────┬──────┐                    │
│   │             │      │      │      │                    │
│   ▼             ▼      ▼      ▼      ▼                    │
│  iDOO       B&D     fan   phone   lamp                    │
│  GROW01    RC503  (SPORE)  USB   (any)                    │
│   │             │                                          │
│   │             └─ via stock 350W AC plug                  │
│   │                                                        │
│   └─ via stock 12V/3A AC adapter (unchanged)              │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

Every appliance uses its stock power cord. The inverter provides standard AC outlets. The customer plugs things in normally.

### 5.2 Why this is better than the DC-bus thesis

**v0.1's DC-bus thesis assumed every appliance would be ported to native 12V DC operation.** That's true for the iDOO (12V native via its adapter), partially true for the rice cooker (which uses AC), and unnecessary for everything else.

**The AC-bus thesis works for all appliances unchanged.** No conversion electronics per appliance. No custom cables. No risk of polarity mistakes. The inverter is a single point of conversion that the entire kitchen module shares.

**The efficiency tradeoff is real but small.** ~20% less battery efficiency on the iDOO via AC vs direct DC. For other appliances (rice cooker, fan, phone charging) the AC path is *more* efficient than the DC alternative because those appliances are AC-native to begin with.

**Composability is much better.** A customer who later adds an espresso machine, electric kettle, hot plate, or any other appliance can do so without any per-appliance integration work. **The kitchen module is genuinely flexible.**

### 5.3 What this changes for the Hako-deployment spec

The Hako flagship's electrical architecture is now much simpler:

- A dedicated marine deep-cycle battery (or two) in the Hako's wall cavity
- A fixed pure-sine inverter mounted permanently
- Standard 110V residential wiring to a small number of outlets in the Hako interior
- Solar panel(s) on the Hako roof feeding an MPPT charger that maintains the battery

**The Hako interior is just an apartment from the power perspective.** Everything plugs in normally. The off-grid infrastructure is invisible to the appliances. The customer can swap any appliance for any other appliance without rethinking the power architecture.

This is also a meaningfully easier spec to build (and to insure, and to maintain). Standard residential AC is well-understood by electricians, inspectors, and customers themselves. A custom DC bus would require Hako-specific knowledge from anyone servicing the dwelling — a real burden.

**The Hako-deployment-thread (next session) inherits this architecture as its starting point.**

---

## § 6 · Safety considerations, updated

Most of the v0.1 safety rules go away because the DIY electronics build is no longer the recommended path. The remaining rules:

### 6.1 Inverter operation

- **Pure-sine-wave inverters only.** Modified-sine-wave inverters produce harmonic distortion that stresses switching power supplies (like the iDOO's stock adapter). Some cheap inverters claim "pure sine" but produce only modified sine — verify before purchase via product reviews or specification sheets.
- **Don't exceed continuous load rating.** A 150W inverter running an iDOO (40W AC) has plenty of headroom. Adding a rice cooker (350W) to a 150W inverter will trip overload protection or damage the inverter. **Match inverter capacity to total simultaneous load** with at least 30% headroom.
- **Don't operate inverters in sealed enclosures.** They produce heat at load and need ventilation. The Ryobi 800W in particular benefits from open-air operation; mounting it in a closed cabinet without ventilation will trip its thermal protection.

### 6.2 Battery handling (unchanged from v0.1)

- Store batteries at 40-60% charge if not used for >1 month
- Avoid temperatures above 30°C during storage
- Inspect for swelling, deformation, or leakage before each use
- Damaged batteries are not safe to use — recycle at Home Depot

### 6.3 Water-safety considerations (unchanged)

The iDOO has an open water reservoir near its electronics. Off-grid operation does not change this. The Ryobi battery and inverter should be positioned away from the iDOO's water reservoir with sufficient elevation that overflow cannot reach the battery contacts or inverter outlets. **A Wowlive top tier with the inverter mounted to the side or on a separate small shelf above is the recommended physical arrangement.**

### 6.4 Insurance and code considerations

Standard 110V AC operation is well-understood by insurance and code authorities. Running an inverter-fed appliance is no different from running it from a generator or any other backup AC source. **No special insurance rider is typically required** beyond standard residential coverage.

The Hako-deployment spec will need to verify this with local electrical authorities (ESA in Ontario), but the foundation is much cleaner than a custom DC bus would have been.

---

## § 7 · What this enables for the studio catalogue

### 7.1 The GROW01·OG product is now a paragraph, not a product

The studio's GROW01 catalogue page can simply include this section:

> **Going off-grid.**
> The GROW01 standard works equally well on-grid and off-grid. For off-grid deployment, source a pure-sine-wave AC inverter that accepts your existing battery system. Two recommendations:
>
> - **Quick & Cheap:** A third-party Ryobi 18V → AC inverter at 150-200W from Amazon (~$40-50 CAD). Plug your iDOO's stock adapter into the inverter, plug a charged Ryobi battery into the inverter, walk away. Single 8Ah battery: ~6 hours. Single 12Ah XL: ~9 hours.
>
> - **Full Studio Kitchen:** The Ryobi 800W Automotive Inverter (~$200-260) runs the entire microsystem simultaneously — iDOO, rice cooker, fan, charging. Pair with 2-4 12Ah XL batteries and 100-200W solar for indefinite off-grid operation.

That's the catalogue copy. **No special product to ship. No engineering risk to manage. Just a sourcing recommendation that any customer can act on independently.**

### 7.2 The off-grid path now applies to the full microsystem

v0.1 framed off-grid as an iDOO-specific question. v0.2 reframes it as the whole microsystem's question — and answers it the same way: one inverter, multiple appliances, standard AC throughout.

**This is the right answer for the Hako flagship.** It's also the right answer for customers who don't have a Hako but want their studio kitchen to work during power outages, in cabins, in RVs, or anywhere off-grid. **The catalogue gains a "Going off-grid" section that applies to every cooking practice the studio offers**, not just GROW.

### 7.3 The studio's R&D content of this spec is zero

This is worth saying directly. The studio didn't engineer anything. The studio identified that commodity inverters solve the problem, named the two relevant products, did the runtime math, and wrote it down. **That's the entire studio contribution.**

This is consistent with the catalogue's broader thesis. The studio doesn't manufacture rice cookers, iDOO hydroponic systems, 1646 cells, Wowlive shelves, mushroom spawn, or now AC inverters. The studio's value is editorial — curation, integration, design — applied to commodity components anyone can source. The off-grid power story is just another expression of the same architectural move.

---

## § 8 · Open questions, revised

**Q1 · Should the studio recommend specific inverter SKUs or stay generic?** Naming specific Amazon products (e.g., B0DHZSTBSD) creates dependency on those listings remaining available. Staying generic ("any 150W+ pure-sine Ryobi-compatible AC inverter") gives customers flexibility but more decision burden. My read: **name 2-3 specific options as examples** with the generic guidance, refreshed periodically as listings change.

**Q2 · Does the studio bench-test a specific inverter for catalogue endorsement?** Bench-testing a B0DHZSTBSD-class third-party inverter with an actual iDOO would verify the math, identify edge cases (does the iDOO's switching adapter produce inrush current that trips the inverter? does the inverter produce clean enough sine wave?), and produce a small studio-credibility artifact. **My read: yes, before publishing the off-grid section of the catalogue.** ~$60 in test hardware, half a day of testing.

**Q3 · The Hako-deployment power architecture, now substantially revised.** v0.1 proposed a centralized 12V DC bus inside the Hako. v0.2 proposes a centralized AC bus from a fixed inverter. **The Hako spec needs to start from this AC-bus architecture**, not the DC-bus one. Marine deep-cycle battery + fixed inverter + roof solar + standard interior wiring is the simpler and more correct design.

**Q4 · BDRC off-grid spec.** Now that the AC inverter approach is the catalogue standard, the BDRC rice cooker just works on the same inverter without modification. **No separate BDRC·OG spec is needed** — it falls out of the Studio Kitchen build automatically. This is a meaningful simplification.

**Q5 · Solar charger recommendation.** Ryobi's own 18V solar charger ($120-150) is the obvious choice for ecosystem coherence. But third-party MPPT chargers with adjustable output voltages can charge Ryobi batteries via the same battery-adapter approach the DIY buck-converter path used. **My read: recommend Ryobi's own product for catalogue simplicity; document the third-party alternative for builders.**

**Q6 · Liability framing.** Much smaller surface in v0.2 than v0.1 because there's no DIY electrical work. The studio's catalogue can include a brief note: *"The studio does not manufacture electrical hardware. All off-grid components are sourced independently by the customer from established retailers (Home Depot, Amazon). Follow manufacturer instructions for inverter operation, battery storage, and solar panel installation."* That's enough.

---

## § 9 · Closing

The architecture got simpler. The customer experience got better. The studio's R&D burden went to zero. **All three are signs the v0.1 thesis was overcomplicated.**

The corrected path: **commodity Ryobi-compatible AC inverter ($40 third-party or $200+ official Ryobi 800W) + stock appliances + Ryobi battery infrastructure = off-grid microsystem with no studio engineering required.** The studio's job is to name the components, do the math, and write the catalogue copy. Nothing else.

This is also the right foundation for the Hako-deployment spec next session. **The Hako's interior is just an apartment from the power perspective** — standard residential AC fed by an inverter behind the wall, with a deep-cycle battery in the wall cavity and solar on the roof. Familiar architecture, well-understood by trades, easy to insure, easy to maintain, easy to modify.

The studio's catalogue has gained an "off-grid" dimension across every practice without adding any new product, any new manufacturing burden, or any new electrical engineering risk. **That's the right kind of catalogue expansion.**

---

*GROW01·OG Engineering Spec v0.2 captured 2026-05-18. Supersedes v0.1's DC-bus thesis. AC-inverter-as-default architecture documented. Companion to GROW-thread-v0.1 and MICROSYSTEM-thread-v0.1. Next session: HAKO-deployment-thread now inherits the AC-bus power architecture as its foundation.*
