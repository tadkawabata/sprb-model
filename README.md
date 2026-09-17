# sprb-model

Revenue and valuation model for **Spruce Biosciences (SPRB)**. Its one asset is tralesinidase alfa (TA-ERT), an ICV enzyme replacement therapy for Sanfilippo syndrome type B (MPS IIIB). The BLA is guided for Q4 2026.

> Research artifact, not investment advice. Most inputs are editable assumptions. The source research pack leans partly on livestreams by Martin Shkreli, who is long the stock and promotional, so weight those claims accordingly.

## Run

```bash
pip install -r requirements.txt
python run.py          # regenerates outputs/summary.md and outputs/charts/
python -m pytest -q
```

Read the results in **[outputs/summary.md](outputs/summary.md)**. For a full walkthrough (reading the output, editing inputs, refreshing after filings, what-ifs), see **[docs/GUIDE.md](docs/GUIDE.md)**.

## Layout

```
inputs/                 every number lives here; {bear, base, bull} nodes are scenario inputs
  company.yaml          price, FD share build, cash/debt, opex, acquirer synergies, pre-approval raise
  epidemiology.yaml     incidence, prevalent pool, diagnosis, eligibility, uptake, survival on therapy
  pricing.yaml          WAC, gross-to-net, price growth, ex-US size and mode (direct / partner)
  deal_terms.yaml       BioMarin royalty tiers + milestones, PRV, tax / Sec. 382 NOLs
  timeline.yaml         approval date, PoS, discount rate, exclusivity, grid + sensitivity axes
model/
  patients.py           cohort model: prevalent bolus + trial/EAP rollovers + incident cohorts,
                        logistic uptake, eligibility loss, attrition = 1 / years_on_therapy
  revenue.py            US net sales; ex-US follows US curve with lag; post-LOE erosion
  pnl.py                COGS, tiered royalty, milestones, R&D/G&A/SG&A, PRV, tax with NOL limits;
                        FCF for standalone-success, acquirer-success and failure branches
  valuation.py          TSM diluted shares, rNPV bridge, EV/peak-sales grid, market-implied value
  scenarios.py          bear/base/bull runs, automatic tornado over every scenario input, 2-D sensitivity
  report.py             writes outputs/
```

## Method notes

- **Units:** $M; shares are raw counts, post the 1:75 reverse split (Aug 2025).
- **rNPV** = PoS × max(0, success equity) + (1 − PoS) × max(0, failure equity). Both are per share, after the modeled pre-approval raise.
  - The failure branch spends cash up to the approval decision date, then pays a wind-down cost.
- **Standalone vs acquirer.** At base-case scale (~$100M peak worldwide), standalone overhead uses up the product's contribution. The *acquirer* view assumes a strategic owner takes over at approval, removes G&A and part of SG&A, and pays full tax. It includes no takeover premium. On a change of control, the Avenue warrant delivers 64k shares for free.
- **The multiples grid** applies EV/peak-sales multiples meant for an *approved* asset, then applies PoS once. (The source pack's grid applied PoS on top of late-stage multiples, which counts approval risk twice.)
- **Tornado:** every `{bear, base, bull}` input is swung to its bear and bull value while everything else stays at base. Add a scenario node anywhere and it appears in the tornado automatically.
- **Simplifications:**
  - No working capital or capex.
  - Debt is taken at face (principal + final payment); interest is ignored.
  - Options are counted in full, since strikes are undisclosed.
  - Unused Sec. 382 limits don't carry forward.

## Keeping it current

Price, share count and cash go stale fast. Before relying on an output, re-pull these into `inputs/company.yaml`:
- Price
- The 10-Q cover-page share count
- Cash
- Any new raises or ATM usage

See [docs/errata.md](docs/errata.md) for the corrections made to the original research pack.
