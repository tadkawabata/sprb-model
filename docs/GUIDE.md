# How to use sprb-model

This guide covers running the model, reading its output, changing assumptions, and keeping it current. For the one-page overview, see the [README](../README.md). For how the source research pack was corrected, see [errata.md](errata.md).

---

## 1. Setup and first run

```bash
cd ~/sprb-model
pip install -r requirements.txt      # pyyaml, matplotlib, pytest
python run.py                        # writes outputs/summary.md + outputs/charts/*.png
python -m pytest -q                  # 6 sanity tests
```

`run.py` runs the bear, base and bull scenarios. It then runs every tornado swing and the sensitivity grid. It takes about a second.

**The workflow is always the same:** edit a YAML file in `inputs/`, run `python run.py`, read `outputs/summary.md`, then commit. Don't edit `outputs/` by hand, because the next run overwrites it.

---

## 2. Reading `outputs/summary.md`

The report has these sections, top to bottom:

| Section | What it tells you | How to use it |
|---|---|---|
| **Cap table** | Basic → fully diluted (FD) shares at the current price, plus the count on a change of control | Check this first after any new filing |
| **What the market is pricing** | Market cap − net cash = EV, minus the risked after-tax PRV = what the market is paying for the drug itself | The quickest read on whether the stock is cheap. Near zero or negative means you're getting TA-ERT for free |
| **rNPV by scenario** | Peak sales, peak patients and per-share values for each scenario | The main answer. See below |
| **Charts** | US patients on therapy; worldwide and US net sales | Sanity-check the curve shapes |
| **EV / peak-sales grid** | Per-share value for peak-sales × multiple combinations | Compare to Street or Shkreli targets. "What peak is $X/share assuming?" |
| **Tornado** | Every scenario input swung to its bear and bull value, ranked by impact | Tells you which assumptions to spend research time on |
| **Sensitivity** | Per-share value across incidence × US list price (WAC) | The two biggest single levers on the US side |
| **Base case annual detail** | Line-by-line P&L and FCF | Audit trail. Check here when a number looks wrong |

### The rNPV columns

Every per-share figure is **after the modeled pre-approval raise**, divided by FD shares plus the new raise shares.

- **Success: standalone** means the drug is approved and Spruce commercializes it alone, carrying all of its own G&A and SG&A.
- **Success: acquirer** means the drug is approved and a strategic buyer takes it over at approval. The buyer removes G&A and part of SG&A (`acquirer_view` in `company.yaml`). No takeover premium is included.
- **Failure** means no approval: cash burns until the decision date, then a wind-down cost is paid.
- **rNPV** = PoS × success + (1 − PoS) × failure. Each branch is floored at $0 first.
- **Low point of net cash** is the lowest cumulative cash in the standalone-success path. **A negative number means the modeled raise isn't enough**, so real dilution would be worse than modeled.

**Why two versions?** At base-case scale (~$100M peak worldwide sales), a standalone Spruce spends about everything the drug earns. So the standalone value mostly reflects failure-case cash, and the acquirer value is the more realistic view of what the asset is worth to someone. If the two views are far apart, the question is whether Spruce gets bought, not whether the drug works.

---

## 3. The input files

All money is in **$M**. Shares are raw counts (post the 1:75 reverse split). Dates are `YYYY-MM-DD`.

| File | What's in it |
|---|---|
| `company.yaml` | Price, share build (basic, RSUs, options, warrants, convertibles), cash, debt, opex schedule, acquirer synergies, pre-approval raise |
| `epidemiology.yaml` | Births, incidence, prevalent pool, diagnosis and eligibility rates, uptake ramp, survival on therapy, trial rollovers, compliance |
| `pricing.yaml` | US WAC, gross-to-net, price growth, ex-US size and mode (`direct` or `partner`) |
| `deal_terms.yaml` | BioMarin royalty tiers, milestones, PRV value and timing, tax and NOL limits |
| `timeline.yaml` | Approval date, PoS, discount rate, exclusivity, scenario weights, grid and sensitivity axes |

Comments tag each value as `[src]` (from a filing) or `[assumption]` (editable judgment).

### Scenario nodes

Any value written like this is a **scenario input**:

```yaml
incidence_per_100k: {bear: 0.21, base: 0.36, bull: 0.52}
```

A plain value applies to all three scenarios:

```yaml
compliance: 0.90
```

Rules:
- The keys must be **exactly** `bear`, `base` and `bull`. Leave one out, or add a fourth, and it's treated as an ordinary dictionary, which breaks the model.
- **Every scenario node shows up in the tornado automatically.** To take an input out of the tornado, turn it into a plain value.
- To make a plain input scenario-dependent, just rewrite it as `{bear: …, base: …, bull: …}`. No code change is needed.

---

## 4. Common tasks

### Refresh after a new 10-Q, raise, or price move

This matters most, because cap-table numbers go stale fast. In `inputs/company.yaml`:

1. `price` and `price_date`: today's close.
2. `shares.basic`: from the **10-Q cover page** ("As of [date], the registrant had X shares…").
3. `shares.rsus`, `shares.options`, `shares.espp`: from the "potentially dilutive securities" table in the EPS note.
4. `shares.warrants`: check for new warrants or exercises.
5. `cash.as_of`, `cash.balance`, `cash.subsequent_inflows`: cash from the balance sheet, plus any raise closed after quarter-end.
6. `cash.quarterly_burn`: operating cash used in the quarter.
7. `debt.principal`: use **face value**, not the balance-sheet carrying value, which is net of discount.
8. `financing.pre_approval_raise`: once a raise actually happens, fold its shares into `basic`. Then either set `enabled: false` or resize the raise to whatever funding is still needed.

In `inputs/timeline.yaml`, update `valuation_date`. Cash is rolled forward from `cash.as_of` to this date at the burn rate.

Then:

```bash
python run.py && python -m pytest -q
```

`test_fully_diluted_shares_match_filings` pins the 9/16/26 share count, so it **will fail after an update**. That's expected: change the two numbers in `tests/test_model.py` to the new counts.

### React to regulatory news

| News | Edit |
|---|---|
| BLA accepted, priority review | Tighten `timeline.approval` dates; raise `probability_of_approval` |
| CRL (e.g. CMC) | Push `approval` out 9–12 months; lower PoS; consider a bigger raise at a lower price |
| Approval | Set PoS to `1.0` for all scenarios; set `approval` to the actual date |
| PRV sold | Set `prv.value` to the actual price and `months_after_approval` to match; once cash is received, fold it into `cash` and set `value: 0` so it isn't counted twice |
| Ex-US partnership signed | `pricing.exus_mode: partner`, `exus_partner_royalty` to the deal rate; add any upfront to `cash.subsequent_inflows` |
| Actual list price announced | `pricing.us_wac_k` (in $K per patient-year) |

### Test a what-if without editing files

```python
from model.config import load_inputs, with_override
from model.scenarios import run_scenario

inputs = load_inputs()
base = run_scenario(inputs, "base")
print(base["peak_ww_sales"], base["valuation"]["per_share_acquirer"])     # 111, 43.29

late = with_override(inputs, ("timeline", "approval"), "2028-07-01")       # replaces the whole bear/base/bull node
print(run_scenario(late, "base")["valuation"]["per_share_acquirer"])       # 32.95

no_raise = with_override(inputs, ("company", "financing", "pre_approval_raise", "enabled"), False)
print(run_scenario(no_raise, "base")["valuation"]["per_share_acquirer"])   # 41.18
```

`with_override` takes a path of keys and returns a modified copy. If the path points at a scenario node, the override applies to all three scenarios.

A `run_scenario` result contains these keys:
- `patients`, `revenue`, `pnl`: lists of annual rows.
- `valuation`: a dict of `per_share`, `per_share_acquirer`, `pv_success`, `net_cash`, `fd_shares_post_raise`, `min_net_cash_success`, and more.
- `peak_ww_sales`, `peak_year`, `peak_us_treated`, `launch`.

### Change the grid, sensitivity axes, or scenario weights

All of these live in `timeline.yaml`:

```yaml
scenario_weights: [0.25, 0.50, 0.25]   # order is bear, base, bull; should sum to 1
multiples_grid:
  peak_sales: [150, 300, 500, 750]
  multiples: [3, 4, 5, 6]
sensitivity:
  incidence_per_100k: [...]
  us_wac_k: [...]
```

The sensitivity table always crosses incidence with WAC. To cross different inputs, edit the `sensitivity(...)` call in `model/report.py`.

---

## 5. How the model works (for auditing)

```
epidemiology ─▶ patients.py ─▶ revenue.py ─▶ pnl.py ─▶ valuation.py ─▶ report.py
                (cohorts)      (US, ex-US)   (FCF x3)   (rNPV, grid)    (summary.md)
```

**`patients.py`** tracks two US pools year by year:
- **Eligible:** diagnosed patients who haven't started treatment.
  - At launch, it's seeded with prevalent patients × diagnosis rate × eligible fraction.
  - Each year it gains new cases × a rising diagnosis rate × incident eligibility.
  - It loses the patients who start, and `eligibility_loss_rate` of the rest as their disease progresses.
- **Treated:** seeded with `rollover_patients_at_launch`, then gains new starts. Each year it loses `1 / years_on_therapy`.
- The start rate ramps on a logistic curve from `start_rate_at_launch` up to `annual_start_rate_mature` over `start_ramp_years`.
- Slow attrition makes the treated pool keep growing for 10–20 years. That's the accumulation effect behind the high peak-sales claims.

**`revenue.py`**
- US sales = average treated patients × compliance × net price (price grows each year).
- Ex-US sales follow the same US curve, scaled by `exus_sales_pct_of_us` and shifted later by the launch lag.
- After exclusivity ends (US: approval + 12 yrs; ex-US: launch + 10 yrs), sales decline at `post_loe_erosion` per year.

**`pnl.py`** builds each year's P&L and three free-cash-flow streams:
- **Revenue:** US sales, plus ex-US sales (direct mode) or a royalty on them (partner mode).
- **Costs:** COGS, the tiered BioMarin royalty on worldwide sales, milestones, R&D, G&A, and US and ex-US SG&A. Overhead shrinks along with sales after US exclusivity ends.
- **PRV proceeds** arrive `months_after_approval` after approval.
- **Tax:** pre-change NOLs are capped at the annual Sec. 382 limit. Losses generated inside the model can offset later income without that cap. Either way, NOLs can offset at most 80% of taxable income.
- **The three FCF streams:** `fcf_success` (standalone), `fcf_acquirer` (buyer from approval) and `fcf_failure`.
- **2026** counts only the rest of the year after `valuation_date`.

**`valuation.py`**
- Discounts each year at mid-period.
- Adds a terminal value at the end of the horizon (a decaying perpetuity at −erosion), if final-year FCF is positive.
- Bridge: EV + net cash today + net raise proceeds, divided by FD shares plus raise shares.
- FD shares use the treasury-stock method at the current price. Options are counted in full because their strikes aren't disclosed.

**Known simplifications:**
- No working capital or capex.
- Debt is taken at face, and interest is ignored.
- Unused Sec. 382 limits don't carry forward.
- The acquirer view has no takeover premium.
- Per-share values ignore that the TSM share count should move with the modeled value.

---

## 6. Extending the model

- **Add an input:** put it in the right YAML (as a scenario node if it should vary), then read it in the module that needs it via `epi[...]`, `oc[...]`, etc. Inputs reach each module already resolved for the scenario being run.
- **Add a P&L line:** compute it in `pnl.py`, include it in `pretax`, add it to the row dict, then add it to the `keys` list in `report.py` so it appears in the annual table.
- **Add a test:** add to `tests/test_model.py`. The existing tests check share math, royalty tiers, scenario ordering, and that later approval lowers value.

---

## 7. Gotchas

- **Don't use the balance-sheet debt figure.** The 10-Q carries debt net of a $9.5M discount; the model needs face value.
- **Always use the cover-page share count.** It's more recent than the balance-sheet count.
- **A $0.00 per-share value isn't a bug.** It means that branch's equity went negative and was floored.
- **The tornado and sensitivity tables use the acquirer metric;** the standalone metric is floored so often it hides the swings. To switch, change `metric=per_share_acquirer` in `report.py`.
- **Weighted averages are dominated by the bull case,** because values are floored near zero on the downside and unbounded on the upside. Look at the scenarios individually.
- **Outputs are only as good as the `[assumption]` inputs.** The royalty tiers, milestone timing, opex levels and raise terms are all estimates.
- **Not investment advice.** Some source material comes from a promotional long holder; see the pack's caveats.
