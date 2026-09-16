# SPRB — Spruce Biosciences: Research Pack for Revenue & Valuation Model

*Compiled Sept 16, 2026. Sources: five livestream transcripts (speaker is Martin Shkreli, based on self-references to Retrophin, Godel Terminal, prison) + web research. Everything tagged **[src]** is from a filing/press release/analyst note; **[MS]** is Shkreli's claim; **[assumption]** is mine and should be treated as an editable model input.*

> Archived as received. Corrections against SEC filings are in [errata.md](errata.md); `inputs/` uses the corrected figures.

---

## 0. TL;DR for the model builder

- **One asset:** tralesinidase alfa (TA-ERT), an ICV-delivered enzyme replacement therapy for **Sanfilippo syndrome type B (MPS IIIB)**. No approved therapy exists.
- **Regulatory path:** accelerated approval on **CSF HS-NRE** (heparan sulfate non-reducing end) as a reasonably-likely surrogate. BLA submission **Q4 2026**; analysts expect approval **~mid-2027**. Confirmatory study (TrAnsform, n≈14) starts Q4 2026.
- **US patient pool is small:** bottom-up epidemiology gives roughly **~110–375 living US patients** (base ~220), and far fewer diagnosed + treatable. Company only states "<1 in 200,000" (an upper bound of ≤~1,700 US).
- **Peak sales estimates in the wild:** H.C. Wainwright >$150M US (~$800k/yr price); Craig-Hallum >$500M WW; CEO says peak could exceed $1B; Shkreli models $400M peak.
- **Economics drag:** high-single to low-double-digit **royalty to BioMarin**, up to $25.5M regulatory milestone for first MPS IIIB product, up to $100M sales milestones.
- **Kicker:** Rare Pediatric Disease **PRV** on approval (recent sales $150–200M).
- **Cap table (6/30/26):** 2,752,810 common shares, $96.3M cash, runway into 2H27 → **expect another raise** before/around approval.

---

## 1. What Shkreli said (condensed across all 5 transcripts)

### Timeline of the streams (inferred from context)
| Transcript | Approx. date | Context |
|---|---|---|
| Doc 3 + Doc 1 (near-duplicates) | ~Oct 6, 2025 | Day of FDA Breakthrough Therapy Designation news; stock halted repeatedly |
| Doc 2 | Late Feb 2026 | Right after Feb 18 news that BLA slipped from Q1 → Q4 2026 (same stream as NVDA earnings preview) |
| Doc 4 | ~Late Aug 2026 | Hot Chips week; Spruce pre-BLA meeting news (Aug 24) |
| Doc 5 | Undated, likely near Doc 4 | Shows portfolio: long Abivax, BioCryst, Spruce; buys SPRB on pullback |

### Thesis points [MS]
- **Price target:** $500/share, range $500–$800; cautious case ~$400, high case ~$1,000. Said a 10x+ outcome is possible. Said it could hit $200–300 within a week or two of the Oct 2025 news (it did spike; 52-wk high was $240 [src]).
- **Market cap framing:** stock was ~$20M market cap before BTD news, ~$77M during the halt. "Realistic" market cap = ~$1B. Rare disease drugs selling $100–200M should command ≥$1B.
- **His DCF:** ~$554/share assuming 1M shares; ~$900 with 1.75M shares; still ~$500 even with 3M shares (note: that last one is internally inconsistent — 3M × $500 = $1.5B).
- **Revenue ramp he modeled:** $120M → $165M → $200M → … → $400M peak.
- **Peak-sales sanity check:** used a company slide of lysosomal storage disorder (LSD) drug peak sales: 169, 740, 30, 311, 635, 480 ($M) → average/median ≈ $400M. Noted Vimizim sells the most despite being one of the rarest.
- **Alt TAM math:**
  - ~500 patients × $750k/yr (≈$375M).
  - "PE/pharma buyer" framing: ~1,000 patients × $500k = $500M sales × 4x sales = ~$2B acquisition value.
- **Dilution view:** Company only needed ~$50M; ideally sells 250k–500k shares, not 1M. Modeled up to 3M total shares. (Actual: $50M PIPE Oct 2025, $66.5M offering Apr 2026, $5.5M Aug 2026 — share count went ~0.6M → 2.75M+.)
- **Regulatory view:** HS normalization to below upper limit of normal is "enough for approval"; "slam dunk." FDA confirmed CSF HS-NRE as reasonably likely surrogate. Breakthrough designation right before filing is a positive signal.
- **CMC risk acknowledged:** manufacturing is "tricky"; could get a CMC-only CRL (cited Scholar Rock as precedent) but viewed it as a quarters-long delay, not thesis-breaking. (This is exactly what happened: BLA pushed to Q4 2026 for PPQ batches.)
- **Feb 2026 reaction to delay:** Filing a clean BLA in Q4 beats filing Q1 and getting a CRL. Still 10x thesis. **PRV could be flipped for ~$100M.**
- **Aug 2026:** Bought more. Still 5–10x. Acknowledged "market is telling you you're wrong" but held conviction; "I know orphan drugs better than almost anybody."
- **Science points he made (mostly accurate):**
  - MPS IIIB = missing NAGLU enzyme → heparan sulfate builds up → neurodegeneration ("starts like autism, ends like Alzheimer's"); death typically in teens.
  - Enzymes don't cross BBB → drug delivered via Ommaya reservoir, intracerebroventricular (ICV).
  - Published data: patients with CSF HS at 200–500 dropped to below lower limit of quantification; liver/spleen volumes normalized; some cognitive stabilization.
  - Existing damage likely not reversed → value is in treating young/early patients.
- **Deal history:** BioMarin originally developed it and let it go (he compared to BioMarin passing Firdapse to Catalyst, which he says became a ~$2.5B company). Actual chain: BioMarin → Allievex (2019) → Allievex wound down → Spruce bought it out of liquidation [src].
- **Comps he name-dropped:** Genzyme (Sanofi hostile takeover), TKT (→ Shire → Takeda), Alexion/Synageva (he said Alexion overpaid ~$8B), Soliris-era Alexion.
- **Other SPRB-adjacent bits:** Short Capricor (CAPR); mentioned Denali-style HS surrogate implicitly; he was promoting his Godel Terminal throughout — **he has a disclosed long position and a commercial incentive to generate attention; weight accordingly.**

---

## 2. Company facts (verified)

### Asset
- TA-ERT = recombinant human NAGLU fused to an IGF2 peptide (to get into cells via the M6P receptor), dosed ICV. Expanded access program plans **weekly** ICV dosing [src].
- Designations: Breakthrough Therapy (Oct 2025), Fast Track, Rare Pediatric Disease, Orphan (US + EU) [src].
- Clinical base: 22 patients dosed across studies 201/202/401, up to ~6 years follow-up; CSF HS-NRE normalized durably; stabilization of cognition, communication, motor vs natural history [src].
- Rare Pediatric PRV program reauthorized through Sept 30, 2029 → TA-ERT eligible for a voucher if approved [src].

### Regulatory timeline
| Date | Event |
|---|---|
| Oct 2024 | Spruce acquires asset from Allievex liquidation |
| Mar 2025 | Pivot announced; BLA guided 1H26 |
| Oct 6, 2025 | Breakthrough Therapy Designation → stock explodes |
| Oct 2025 | $50M PIPE (~502k shares @ $68 + pre-funded warrants) |
| Dec 2025 | Type B (clinical): FDA says integrated data + natural history could serve as adequate & well-controlled evidence for CSF HS-NRE surrogate; confirmatory study to start during BLA review |
| Jan 2026 | Type B (CMC): FDA wants 1 PPQ batch at submission, 2nd PPQ batch data before mid-cycle |
| Feb 18, 2026 | BLA pushed to **Q4 2026** |
| Apr 2026 | $60M offering @ $50 (+180k greenshoe exercised; $64.4M net) |
| Jun 2026 | 6-year data at MPS Symposium; multiple analyst initiations |
| Aug 24, 2026 | Two pre-BLA meetings positive: FDA found CMC comparability strategy reasonable after tech transfer to a commercial-scale CDMO; aligned on BLA format |
| **Q4 2026** | **BLA submission; TrAnsform confirmatory study + EAP (~10 pts) start** |
| ~mid-2027 | Expected approval decision (analyst consensus) |

### Financials (Q2 2026, 10-Q)
| Item | Value |
|---|---|
| Cash & equivalents (6/30/26) | $96.3M |
| Aug 2026 private placement (Cure Sanfilippo Foundation + National MPS Society) | $5.5M (terms not detailed) |
| Term loan | $15.0M drawn Jan 2026 (balance sheet carries $7.1M total debt — likely net of discount/warrant allocation; **verify in 10-Q**). Facility reportedly $50M with $35M undrawn as of Mar 2026 |
| Warrant liability | $3.3M |
| Q2 R&D / G&A | $12.2M / $4.3M |
| Q2 net loss | $16.2M |
| H1 2026 operating cash burn | $30.9M |
| Common shares outstanding (6/30/26) | **2,752,810** (vs 1,372,043 at 12/31/25) |
| Q2 weighted avg shares | 2,431,075 |
| Accumulated deficit (NOL proxy) | $317.7M |
| Runway guidance | Into 2H 2027 (excludes product revenue / PRV) |
| ATM | $75M Jefferies ATM, unused as of 6/30/26 |

**TODO for Claude Code:** pull latest 10-Q cover-page share count, outstanding pre-funded warrants (Oct 2025 PIPE PFWs), common warrants, options/RSUs, and Aug 2026 placement share count to get fully diluted shares.

### License economics owed to BioMarin (critical for model)
- **Royalties:** high-single-digit to low-double-digit **tiered** royalties on annual net sales of MPS IIIB products (subject to customary reductions/floors) [src]. Model input: **8%–12% blended, tiered by sales band** [assumption on exact tiers].
- **Dev/regulatory milestones:** up to $88M aggregate across products; **up to $25.5M for first MPS IIIB product** [src].
- **Sales milestones:** up to **$100M per licensed product** [src] (tiers undisclosed — [assumption] spread across e.g. $100M/$250M/$500M net sales thresholds).

### Stock / Street context
- 52-week range ~$7 to $240; ~$50–64 through Jul–Aug 2026 [src]. B.Riley noted shares down ~75% from Q4 2025 highs [src]. **Pull live price.**
- Analyst price targets span **$104 (Guggenheim) → $230 (Oppenheimer)**; others: H.C. Wainwright $150, B.Riley $160, Craig-Hallum $140, Citizens $144, Jones $135 [src].
- Jones assumptions: **85% probability of US accelerated approval**, approval ~mid-2027, PRV ~$180M; ex-US could double the opportunity; diagnosis rates likely rise post-approval [src].
- Illustrative: at $60/share × 2.75M shares ≈ $165M market cap; net cash ≈ $96M + $5.5M − $15M ≈ $87M (before Q3 burn) → EV ≈ **~$80M**.

---

## 3. Patient count — raw numbers

### Published epidemiology
| Metric | Value | Source |
|---|---|---|
| Company statement | MPS IIIB affects **<1 in 200,000** people in US; true numbers unclear (no newborn screening) | Spruce PR |
| MPS IIIB birth incidence (average) | **~1 in 280,000** (range 1:125k to 1:500k); higher in Southern European & Middle Eastern ancestry | Myriad carrier screen |
| MPS IIIB global incidence | **~0.52 per 100,000** live births | PMC (Ecuador cluster paper) |
| MPS IIIB by country (per 100k births) | Australia 0.43; France 0.10; Germany 0.36; **Greece 0.78**; Netherlands 0.42; **N. Portugal 0.72**; Sweden 0.03; Taiwan 0.28; UK 0.21; Brazil 0.12 | PMC narrative review table |
| All MPS III (A–D) combined | 1:50,000 to 1:250,000 depending on population | NORD / Medscape |
| MPS III US registry incidence / prevalence | 0.26 per 100k births; ~0.70 per million population (all subtypes, diagnosed) | Medscape |
| Worldwide living with MPS III A/B/C | ~12,000–19,000 | Medscape |
| Geographic skew | IIIA dominates NW Europe/US/Australia; **IIIB dominates Southern Europe, Taiwan, Japan, Brazil**; much of global IIIB burden may sit in India (access-limited) | NORD, SciELO, ISPOR poster |
| Life expectancy (severe) | ~15–19 years | Spruce PR |

### Derived US patient funnel [assumption — editable inputs]
Constants: US live births ≈ **3.6M/yr**; US population ≈ **340M**.

| Step | Bear | Base | Bull |
|---|---|---|---|
| Birth incidence (per 100k) | 0.21 (UK-like) | 0.36 (≈1:280k) | 0.52 (global est.) |
| New US cases / yr | ~7.6 | ~13 | ~19 |
| Avg living span of cohort (yrs) | 15 | 17 | 20 |
| **US prevalent (living)** | **~115** | **~220** | **~375** |
| Diagnosed | 60% | 70% | 85% |
| Eligible (before advanced neuro disease) | 50% | 60% | 75% |
| Treated (uptake) | 70% | 80% | 85% |
| Compliance / persistence | 90% | 90% | 90% |
| **US patients on drug (launch-era peak, static)** | **~21** | **~66** | **~180** |

Cross-checks:
- Company upper bound: 340M / 200k = **≤1,700 US** (regulatory boilerplate, not an estimate).
- Registry floor: 0.70/million × 340M ≈ ~240 diagnosed MPS III (all types) in US; IIIB share in US maybe 25–35% → **~60–85 registry-visible IIIB patients**.
- Shkreli's 500–1,000 patient numbers only reconcile if they're **global** or assume large undiagnosed/attenuated populations.
- H.C. Wainwright's >$150M US at ~$800k implies **~190+ paying US patients** ≈ this file's bull case.

### Dynamic (long-run) view — why peak depends on survival extension
If the drug stabilizes disease, treated patients live much longer and the pool **accumulates**:
`Steady-state treated ≈ annual new US cases × diagnosis rate × uptake × years on therapy`
| | Bear | Base | Bull |
|---|---|---|---|
| Years on therapy (with ERT) | 15 | 25 | 30 |
| Steady-state US treated | ~7.6×0.6×0.7×15 ≈ **48** | ~13×0.7×0.85×25 ≈ **190** | ~19×0.85×0.9×30 ≈ **435** |

This is the main mechanism behind "peak >$1B" claims (plus ex-US and earlier diagnosis). It takes 10–20 years to build.

### Ex-US [assumption]
- EU27 + UK births ≈ **4.3M/yr**; incidence plausibly similar to US on average but higher in Greece/Portugal/Italy/Spain.
- Japan, Taiwan, Brazil, Turkey, Middle East: IIIB is the dominant subtype there.
- Pricing typically **40–60% of US** in Europe; launch lag 1–2 yrs after US; Spruce has mentioned exploring **Asia partnerships** (would mean royalties, not full revenue).
- Jones: ex-US could roughly **double** the US opportunity.

---

## 4. Pricing & revenue inputs

### Price comps
| Drug | Disease / route | Price | Notes |
|---|---|---|---|
| **Brineura** (BioMarin) | CLN2 Batten, **ICV** every 2 wks | List ~$702k/yr at 2017 launch (~$716k by 2020); **net ~$486k** after gov't discounts (~31% GTN) | Closest analog: ultra-rare, pediatric, ICV ERT. CLN2 ≈ 20 US births/yr. Brineura sales **$48M in Q4 2024** (~$190M annualized, ~7.5 yrs post-launch) |
| Brineura (Canada) | same | ~CA$844k/yr | CADTH |
| **Avlayah** (Denali, tividenofusp alfa) | MPS II (Hunter), IV, brain-penetrant | $5,200/150mg vial → ~$270k–$811k/yr by weight | Approved Mar 25, 2026 on **CSF HS** surrogate; ~500 US prevalent MPS II; Denali targets ~75% |
| H.C. Wainwright TA-ERT assumption | — | ~$800k/yr | — |
| Shkreli assumption | — | $500k–$750k/yr | — |
| Spruce CEO | — | Not weight-based; priced "accordingly but sensibly" | Mar 2026 Oppenheimer conf. |

### Suggested revenue inputs [assumption]
| Input | Bear | Base | Bull |
|---|---|---|---|
| US WAC ($/yr) | 650k | 750k | 850k |
| Gross-to-net | 35% | 25% | 20% |
| US net price | ~$420k | ~$560k | ~$680k |
| Annual price increase | 0% | 2% | 3% |
| Launch (first revenue) | 1H 2028 (CRL/delay) | 2H 2027 | mid-2027 |
| Years to launch-pool peak | 6 | 5 | 4 |
| Ex-US revenue as % of US | 30% (partner royalty) | 60% | 100% |
| COGS % of net sales | 15% | 12% | 10% |
| BioMarin royalty (blended) | 12% | 10% | 9% |
| Probability of approval | 65% | 80% | 90% |
| PRV sale value | $120M | $160M | $200M |

### Revenue anchors in the wild
| Source | Peak / estimate |
|---|---|
| H.C. Wainwright (Dec 2025) | >$150M **US** at ~$800k/yr |
| Craig-Hallum | >$500M **worldwide** |
| Spruce CEO (Mar 2026) | Peak could **exceed $1B** (better diagnosis + life extension) |
| Shkreli | Ramp $120M → $165M → $200M → **$400M peak** |
| LSD drug peak sales (company slide via MS) | 30 / 169 / 311 / 480 / 635 / 740 ($M); avg ≈ $395M |
| Brineura (closest analog) | ~$190M/yr run-rate after ~7.5 yrs |
| Kanuma (cautionary) | Analysts forecast $600M–$1B peak; did **$29M in 2016**, year 1 |

**My read of the numbers:** Shkreli's $120M first-year revenue is aggressive vs. the bottom-up US funnel (base ~66 patients × ~$560k ≈ $37M US at launch-pool peak). A $150–300M WW peak is supportable with Brineura-like execution; $400M+ requires the survival-extension/accumulation dynamic plus meaningful ex-US.

---

## 5. Valuation research (for your multiples work)

### Heuristics (secondary sources — rules of thumb, not law)
- Phase III / near-approval orphan asset: **~3–5x peak sales** EV (DrugPatentWatch; DealStream).
- De-risked, approved, first-in-class: **~4–6x peak sales** (low end friendly tuck-in, high end competitive auction) (Substack explainer — low-quality source).
- Typical biotech takeover premium: 60–120%.
- EU price ≈ 40–60% of US; ex-US partner royalties typically 10–20%.

### Precedent transactions
| Deal | Price | Implied multiple | Lesson |
|---|---|---|---|
| Alexion ← Synageva (2015) | $8.4B (140% premium), Kanuma pre-approval, BTD + priority review | **10–14x** analyst peak sales | Buyer overpaid; Kanuma sold $29M in 2016. Shows what a strategic *will* pay for an ultra-rare ERT, and the downside of trusting peak-sales hype |
| BioMarin ← Amicus (Dec 2025, closed Apr 2026) | $4.8B equity | ~8x trailing revenue (~$600M from Galafold + Pombiliti); ~2.4x mgmt's combined ~$2B peak | Current-era LSD M&A, commercial & growing |
| BioMarin ← Inozyme (2025) | $270M | pre-commercial | BioMarin actively buying rare assets |
| BioCryst (2026) | — | — | Publicly hunting ~$300M-peak rare assets to plug into its commercial engine → natural buyer universe for SPRB |

### PRV market
- 2025 sales ~$150M typical; Jazz sold one for **$200M in Jan 2026**; historical range $21M → $350M.
- BioMarin sold its Voxzogo PRV for $110M (BioMarin also received PRVs for Brineura and Vimizim).

### Illustrative EV → per-share grid [assumption: PoS 85%, net cash $87M, 2.75M shares, PRV excluded, pre-future-dilution]
| WW peak sales | 3x | 4x | 5x |
|---|---|---|---|
| $150M | ~$171 | ~$217 | ~$264 |
| $300M | ~$310 | ~$403 | ~$495 |
| $500M | ~$495 | ~$650 | ~$804 |

- PRV at $180M × 85% PoS adds roughly **+$56/share** (pre-tax; NOLs likely shield it).
- Royalty burden (~10%) argues for trimming the multiple ~10% vs. an unencumbered asset.
- **Shkreli's $500–$800 ≈ ~$300–500M WW peak at 4–5x.** Street's $104–230 ≈ ~$100–200M peak at 3–4x, or higher peak with heavier risk/dilution haircuts.
- Recompute with fully diluted shares and a pre-approval raise.

---

## 6. Key risks & catalysts

### Catalysts
- **Sept 19, 2026 — Ultragenyx UX111 PDUFA** (AAV gene therapy for MPS **IIIA**, resubmitted after a July 2025 CMC-driven CRL). Not a competitor (different subtype) but a direct **sentiment read-through for Sanfilippo accelerated approvals.**
- Q4 2026: BLA submission; TrAnsform + EAP start.
- ~60 days post-submission: BLA acceptance / priority review designation.
- 2nd PPQ batch data before mid-cycle.
- ~Mid-2027: PDUFA; PRV award and sale.
- Financing event (runway into 2H27).

### Risks
- **Surrogate/natural-history risk:** FDA rejected Regenxbio's RGX-121 (MPS II) in Feb 2026, citing reliance on a natural-history control and use of a **single form of heparan sulfate** as surrogate. Spruce's package leans on natural history + CSF **HS-NRE**. Mitigants: FDA explicitly said (Dec 2025) Spruce's integrated data + natural history could serve as adequate evidence, and Denali won approval on CSF HS in Mar 2026.
- **CMC:** already caused one delay; tech transfer to new CDMO; UX111 precedent of CMC CRL.
- **Tiny patient pool / diagnosis gap:** no newborn screening; many kids diagnosed after irreversible damage.
- **Launch execution:** ICV device implant + weekly dosing burden; limited treating centers.
- **Dilution:** already ~4–5x share count since Oct 2025; more coming.
- **Royalties + milestones** to BioMarin.
- **Future competition:** Denali's DNL126 (brain-penetrant ERT for Sanfilippo) could read across; gene therapies for other MPS III subtypes.
- **Source bias:** Shkreli is long and promotional; Kanuma shows ultra-rare ERT peak-sales forecasts can miss badly.

---

## 7. Spec for Claude Code model (suggested repo structure)

```
sprb-model/
  inputs/
    epidemiology.yaml   # incidence, births, survival, dx, eligibility, uptake, compliance (bear/base/bull)
    pricing.yaml        # WAC, GTN, price growth, ex-US price ratio
    company.yaml        # cash, debt, shares (basic + PFW + warrants + options), burn, runway
    deal_terms.yaml     # royalty tiers, milestones, PRV value
    timeline.yaml       # BLA date, PDUFA, launch dates US/EU/RoW, PoS
  model/
    patients.py         # cohort model: prevalent bolus at launch + annual incident cohorts,
                        # diagnosis lag, uptake curve (logistic), treated survival extension
    revenue.py          # patients x net price x compliance; US + ex-US (direct or royalty)
    pnl.py              # COGS, royalty, milestones, SG&A launch build, R&D (confirmatory trial), tax w/ NOLs
    valuation.py        # (a) rNPV w/ PoS + discount rate, (b) EV/peak-sales multiple grid,
                        # (c) per-share bridge: EV + net cash + PRV - milestones, / FD shares after raise
    scenarios.py        # bear/base/bull + tornado on key drivers
  outputs/
    summary.md, charts/
```

Key modeling rules:
1. Run 2027–2045 annually (long horizon needed for the accumulation effect).
2. Patient model must be **cohort-based**, not a static prevalence × share — the survival-extension parameter is the single biggest driver of peak.
3. Exclusivity: US biologic exclusivity 12 yrs from approval; US orphan 7 yrs; EU orphan 10 yrs [general regulatory facts — verify].
4. Discount rate 10–15%; PoS 65–90%.
5. Include a pre-approval equity raise (size + price as inputs) before computing per-share value.
6. Output a sensitivity table: peak sales vs. multiple, and per-share value vs. (US prevalence × net price).

---

## 8. Sources
- Spruce PR — Type B meetings / BLA to Q4 2026 (Feb 18, 2026): https://finance.yahoo.com/news/spruce-biosciences-announces-positive-type-120000056.html
- Spruce Q2 2026 results + balance sheet (Aug 12, 2026): https://www.businesswire.com/news/home/20260812480178/en/Spruce-Biosciences-Reports-Second-Quarter-2026-Financial-Results-and-Provides-Corporate-Updates
- Spruce 10-Q Q2 2026: https://www.sec.gov/Archives/edgar/data/1683553/000119312526345876/sprb-20260630.htm
- Spruce 10-K FY2025 (BioMarin royalty/milestones): https://www.sec.gov/Archives/edgar/data/1683553/000119312526097558/sprb-20251231.htm
- Pre-BLA meetings (Aug 24, 2026): https://investors.sprucebio.com/news-releases/news-release-details/spruce-biosciences-announces-positive-pre-bla-meetings-fda-and
- April 2026 offering: https://finance.yahoo.com/markets/stocks/articles/spruce-biosciences-announces-pricing-public-034500198.html
- Oct 2025 $50M PIPE: https://trial.medpath.com/news/f293b7ea5611ba6b/spruce-biosciences-secures-50m-to-advance-sanfilippo-syndrome-type-b-therapy-toward-bla-submission
- Breakthrough designation coverage: https://sanfilipponews.com/news/tralesinidase-alfa-ert-sanfilippo-type-b-children-fast-tracked/
- CEO at Oppenheimer conf (peak >$1B, pricing, debt facility): https://finance.yahoo.com/news/spruce-biosciences-touts-mps-iiib-223758695.html
- H.C. Wainwright ($800k price, >$150M US): https://www.investing.com/news/analyst-ratings/spruce-biosciences-stock-rating-resumed-at-buy-by-hc-wainwright-93CH-4419089
- Jones Trading (85% PoS, PRV $180M): https://www.investing.com/news/analyst-ratings/jones-trading-initiates-spruce-biosciences-stock-with-buy-rating-on-therapy-potential-93CH-4731634
- Craig-Hallum (>$500M WW): https://www.investing.com/news/company-news/spruce-presents-sixyear-data-on-mps-iiib-therapy-candidate-93CH-4731459
- B.Riley initiation: https://www.investing.com/news/analyst-ratings/briley-initiates-spruce-biosciences-stock-with-buy-rating-on-therapy-potential-93CH-4787542
- HCW reiterate / Guggenheim $104: https://www.investing.com/equities/spruce-biosciences-inc
- Epidemiology: Myriad https://myriad.com/womens-health/diseases/mucopolysaccharidosis-type-iiib/ ; Medscape https://emedicine.medscape.com/article/948540-overview ; NORD https://rarediseases.org/rare-diseases/mucopolysaccharidosis-type-iii/ ; country table https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11087936/ ; global 0.52/100k https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12468815/ ; ISPOR subtype poster https://www.ispor.org/docs/default-source/euro2019/pro60-prevalence-of-sanfilippo-syndrome-and-sub-types-in-major-geographical-regions-pdf.pdf
- Brineura pricing: https://www.fiercepharma.com/pharma/biomarin-picks-up-fda-approval-for-orphan-drug-brineura ; sales: https://finance.yahoo.com/news/biomarin-q4-earnings-sales-top-142300658.html
- Denali Avlayah approval & price: https://finance.yahoo.com/sectors/healthcare/articles/denali-therapeutics-wins-fda-accelerated-210536622.html ; RGX-121 CRL reasons: https://www.fiercepharma.com/pharma/fda-approves-denali-hunter-syndrome-drug-breaking-streak-rare-disease-rejections
- UX111 PDUFA Sept 19, 2026: https://ir.ultragenyx.com/news-releases/news-release-details/ultragenyx-announces-us-fda-acceptance-bla-resubmission-ux111
- PRV prices: https://www.pharmaceutical-technology.com/news/fda-seeks-permanent-future-for-rare-pediatric-priority-review-vouchers/
- Synageva: https://www.thestreet.com/investing/stocks/alexion-pays-hefty-84b-to-acquire-synageva-expand-rare-disease-drug-business-13140427 ; Kanuma sales: https://www.thestreet.com/investing/stocks/alexion-pharma-s-bloated-blockbuster-deal-still-haunts-14005166
- Amicus: https://pharmaphorum.com/news/biomarin-ends-year-48bn-play-amicus
- Multiples heuristics: https://www.drugpatentwatch.com/blog/value-a-biotech-like-a-pro-the-metrics-that-actually-move-price-targets/ ; https://dealstream.com/industry-guides/biotechnology-businesses/rules-of-thumb
- BioCryst as rare-asset buyer: https://www.cnbc.com/2026/08/28/biocryst-is-profitable-now-it-wants-to-buy-more-rare-disease-drugs.html
