"""Scenario runner, probability weighting, tornado, and 2-D sensitivity."""
from __future__ import annotations

from .config import (SCENARIOS, get_path, resolve, scenario_paths, to_year,
                     with_override)
from .patients import build_patients
from .pnl import build_pnl
from .revenue import build_revenue
from .valuation import rnpv


def run_scenario(inputs: dict, scenario: str) -> dict:
    r = {name: resolve(node, scenario) for name, node in inputs.items()}
    tl = r["timeline"]
    years = range(int(to_year(tl["valuation_date"])), tl["horizon_end"] + 1)
    launch = to_year(tl["approval"]) + tl["launch_lag_years"]

    patients = build_patients(r["epidemiology"], launch, years)
    revenue = build_revenue(patients, r["epidemiology"], r["pricing"], tl)
    pnl = build_pnl(revenue, r["company"], r["pricing"], r["deal_terms"], tl)
    peak = max(revenue, key=lambda row: row["ww_sales"])
    return {
        "scenario": scenario, "inputs": r, "launch": launch,
        "patients": patients, "revenue": revenue, "pnl": pnl,
        "valuation": rnpv(pnl, r["company"], r["deal_terms"], tl),
        "peak_ww_sales": peak["ww_sales"], "peak_year": peak["year"],
        "peak_us_treated": max(p["treated_end"] for p in patients),
    }


def run_all(inputs: dict) -> dict:
    return {s: run_scenario(inputs, s) for s in SCENARIOS}


def weighted_per_share(results: dict, weights: list[float], key: str = "per_share") -> float:
    return sum(w * results[s]["valuation"][key] for s, w in zip(SCENARIOS, weights))


def per_share(result: dict) -> float:
    return result["valuation"]["per_share"]


def per_share_acquirer(result: dict) -> float:
    return result["valuation"]["per_share_acquirer"]


def tornado(inputs: dict, metric=per_share) -> list[dict]:
    """Swing each scenario input to its bear and bull value, holding everything else at base."""
    rows = []
    for path in scenario_paths(inputs):
        node = get_path(inputs, path)
        low = metric(run_scenario(with_override(inputs, path, node["bear"]), "base"))
        high = metric(run_scenario(with_override(inputs, path, node["bull"]), "base"))
        rows.append({"driver": ".".join(map(str, path)), "bear_input": node["bear"], "base_input": node["base"],
                     "bull_input": node["bull"], "bear_value": low, "bull_value": high, "swing": abs(high - low)})
    return sorted(rows, key=lambda row: row["swing"], reverse=True)


def sensitivity(inputs: dict, row_path, row_values, col_path, col_values, metric=per_share) -> dict:
    table = {}
    for rv in row_values:
        overridden = with_override(inputs, row_path, rv)
        table[rv] = {cv: metric(run_scenario(with_override(overridden, col_path, cv), "base")) for cv in col_values}
    return table
