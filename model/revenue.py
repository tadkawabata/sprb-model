"""US and ex-US end-market net sales ($M)."""
from __future__ import annotations

import math

from .config import to_year


def _interp(series: dict[int, float], t: float) -> float:
    lo = math.floor(t)
    w = t - lo
    return series.get(lo, 0.0) * (1 - w) + series.get(lo + 1, 0.0) * w


def _decay(year: int, loe: float, erosion: float) -> float:
    return (1 - erosion) ** max(0.0, year + 0.5 - loe)


def build_revenue(patients: list[dict], epi: dict, pricing: dict, tl: dict) -> list[dict]:
    approval = to_year(tl["approval"])
    launch = approval + tl["launch_lag_years"]
    us_loe = approval + tl["us_exclusivity_years"]
    exus_lag = tl["exus_launch_lag_years"]
    exus_loe = launch + exus_lag + tl["exus_exclusivity_years"]
    erosion = tl["post_loe_erosion"]

    net_price0 = pricing["us_wac_k"] / 1000 * (1 - pricing["gross_to_net"])   # $M / patient-year
    growth = pricing["annual_price_increase"]

    us_pre_loe = {}
    for p in patients:
        price = net_price0 * (1 + growth) ** max(0, p["year"] - int(launch))
        us_pre_loe[p["year"]] = p["treated_avg"] * epi["compliance"] * price

    rows = []
    for p in patients:
        y = p["year"]
        us = us_pre_loe[y] * _decay(y, us_loe, erosion)
        # ex-US follows the US launch curve, shifted by the launch lag
        exus = pricing["exus_sales_pct_of_us"] * _interp(us_pre_loe, y - exus_lag) * _decay(y, exus_loe, erosion)
        rows.append({
            "year": y,
            "us_net_price_k": net_price0 * 1000 * (1 + growth) ** max(0, y - int(launch)),
            "us_sales": us,
            "exus_sales": exus,
            "ww_sales": us + exus,
        })
    return rows
