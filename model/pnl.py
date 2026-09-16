"""Annual P&L and unlevered free cash flow ($M), success and failure branches.

Success branch: approval on the scenario date, full commercial build.
Acquirer branch: same as success, but from US approval a strategic owner strips G&A and part of SG&A.
Failure branch: costs run until the approval decision date, then a one-time wind-down.
Only the part of each year after the valuation date is counted.
Opex scales down with sales erosion after US LOE.
Simplifications: no working capital or capex; debt handled at face in the valuation bridge.
"""
from __future__ import annotations

from .config import overlap, to_year


def tiered_royalty(sales: float, tiers: list[dict], shift: float = 0.0) -> float:
    owed, lower = 0.0, 0.0
    for tier in tiers:
        upper = float("inf") if tier["up_to"] is None else tier["up_to"]
        owed += max(0.0, min(sales, upper) - lower) * max(0.0, tier["rate"] + shift)
        if sales <= upper:
            break
        lower = upper
    return owed


def _by_year(schedule: dict, thereafter: float, growth: float, year: int) -> float:
    if year in schedule:
        return schedule[year]
    return thereafter * (1 + growth) ** max(0, year - (max(schedule) + 1))


def build_pnl(revenue: list[dict], company: dict, pricing: dict, deal: dict, tl: dict) -> list[dict]:
    val = to_year(tl["valuation_date"])
    approval = to_year(tl["approval"])
    launch = approval + tl["launch_lag_years"]
    exus_launch = launch + tl["exus_launch_lag_years"]
    prv_date = approval + deal["prv"]["months_after_approval"] / 12
    oc = company["operating_costs"]
    bmrn = deal["biomarin"]
    tax = deal["tax"]
    direct = pricing["exus_mode"] == "direct"
    us_loe = approval + tl["us_exclusivity_years"]
    erosion = tl["post_loe_erosion"]

    restricted_nol, unrestricted_nol = tax["pre_change_nol"], 0.0
    paid_sales_milestones: set[float] = set()
    rows = []
    for r in revenue:
        y = r["year"]
        frac = overlap(y, val)
        if frac == 0:
            continue

        us, exus, ww = r["us_sales"] * frac, r["exus_sales"] * frac, r["ww_sales"] * frac
        exus_revenue = exus if direct else exus * pricing["exus_partner_royalty"]
        cogs = oc["cogs_pct"] * (us + (exus if direct else 0.0))
        royalty = tiered_royalty(r["ww_sales"], bmrn["royalty_tiers"], bmrn["royalty_tier_shift"]) * frac

        in_year = lambda t: y <= t < y + 1 and t >= val  # noqa: E731
        reg_ms = sum(m["amount"] for m in bmrn["regulatory_milestones"]) if in_year(approval) else 0.0
        sales_ms = 0.0
        for m in bmrn["sales_milestones"]:
            if r["ww_sales"] >= m["threshold"] and m["threshold"] not in paid_sales_milestones:
                paid_sales_milestones.add(m["threshold"])
                sales_ms += m["amount"]
        prv = deal["prv"]["value"] if in_year(prv_date) else 0.0

        rd_rate = _by_year(oc["rd_by_year"], oc["rd_thereafter"], 0.0, y)
        ga_rate = _by_year(oc["ga_by_year"], oc["ga_thereafter"], oc["ga_growth"], y)
        sga_growth = (1 + oc["sga_growth"]) ** max(0, y - int(launch))
        sga_us = (overlap(y, max(val, launch - 1), launch) * oc["us_commercial_sga_prelaunch"]
                  + overlap(y, max(val, launch)) * oc["us_commercial_sga"] * sga_growth)
        sga_exus = (overlap(y, max(val, exus_launch - 0.5)) * oc["exus_sga_direct"]
                    * (1 + oc["sga_growth"]) ** max(0, y - int(exus_launch))) if direct else 0.0
        # after US loss of exclusivity, overhead is cut in line with sales erosion
        loe_scale = (1 - erosion) ** max(0.0, y + 0.5 - us_loe)
        sga_us, sga_exus = sga_us * loe_scale, sga_exus * loe_scale
        rd, ga = rd_rate * frac * loe_scale, ga_rate * frac * loe_scale

        revenue_total = us + exus_revenue
        pretax = revenue_total + prv - cogs - royalty - reg_ms - sales_ms - rd - ga - sga_us - sga_exus

        if pretax <= 0:
            unrestricted_nol += -pretax
            tax_paid = 0.0
        else:
            cap = tax["nol_taxable_income_cap"] * pretax
            use_r = min(restricted_nol, tax["section_382_annual_limit"] * frac, cap)
            use_u = min(unrestricted_nol, cap - use_r)
            restricted_nol -= use_r
            unrestricted_nol -= use_u
            tax_paid = tax["rate"] * (pretax - use_r - use_u)

        acq = company["acquirer_view"]
        owned = overlap(y, max(val, approval)) / frac     # share of this period after the buyer takes over
        synergies = owned * (acq["ga_synergy"] * ga + acq["sga_synergy"] * (sga_us + sga_exus))
        pretax_acq = pretax + synergies
        tax_acq = tax_paid * (1 - owned) + owned * acq["tax_rate"] * max(0.0, pretax_acq)

        pre_decision = overlap(y, val, approval)
        fail_fcf = -(rd_rate * pre_decision + ga_rate * pre_decision
                     + overlap(y, max(val, launch - 1), min(launch, approval)) * oc["us_commercial_sga_prelaunch"])
        if in_year(approval):
            fail_fcf -= oc["failure_wind_down"]

        rows.append({
            "year": y, "year_fraction": frac,
            "us_sales": us, "exus_sales": exus, "ww_sales": ww,
            "exus_revenue_to_spruce": exus_revenue, "total_revenue": revenue_total,
            "cogs": cogs, "biomarin_royalty": royalty,
            "regulatory_milestones": reg_ms, "sales_milestones": sales_ms,
            "rd": rd, "ga": ga, "sga_us": sga_us, "sga_exus": sga_exus,
            "prv_proceeds": prv, "pretax_income": pretax, "tax": tax_paid,
            "fcf_success": pretax - tax_paid, "fcf_acquirer": pretax_acq - tax_acq, "fcf_failure": fail_fcf,
        })
    return rows
