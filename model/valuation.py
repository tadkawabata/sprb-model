"""Valuation: rNPV, EV/peak-sales grid, market-implied value, per-share bridge."""
from __future__ import annotations

from .config import to_year


def diluted_shares(company: dict, price: float, change_of_control: bool = False) -> float:
    """Treasury-stock-method fully diluted shares at `price` (options counted in full)."""
    s = company["shares"]
    total = s["basic"] + s["rsus"] + s["options"] + s["espp"]
    for w in s["warrants"]:
        if change_of_control and w["free_on_change_of_control"]:
            total += w["shares"]
        elif price > w["strike"]:
            total += w["shares"] * (1 - w["strike"] / price)
    for c in s["convertibles"]:
        if price > c["conversion_price"]:
            total += c["principal"] * 1e6 / c["conversion_price"]
    return total


def balance_sheet_today(company: dict, tl: dict) -> dict:
    cash = company["cash"]
    elapsed = to_year(tl["valuation_date"]) - to_year(cash["as_of"])
    gross = cash["balance"] + cash["subsequent_inflows"] - cash["quarterly_burn"] * 4 * elapsed
    debt = company["debt"]["principal"] + company["debt"]["final_payment"]
    return {"cash": gross, "debt": debt, "net_cash": gross - debt}


def raise_terms(company: dict) -> dict:
    r = company["financing"]["pre_approval_raise"]
    if not r["enabled"]:
        return {"date": None, "gross": 0.0, "net": 0.0, "price": None, "new_shares": 0.0}
    return {"date": to_year(r["date"]), "gross": r["gross"], "net": r["gross"] * (1 - r["fees_pct"]),
            "price": r["price"], "new_shares": r["gross"] * 1e6 / r["price"]}


def present_value(rows: list[dict], key: str, rate: float, val: float, terminal_growth: float | None = None) -> float:
    pv = 0.0
    for r in rows:
        y = r["year"]
        t = (max(y, val) + y + 1) / 2 - val
        pv += r[key] / (1 + rate) ** t
    if terminal_growth is not None and rows and rows[-1][key] > 0:
        last = rows[-1]
        tv = last[key] * (1 + terminal_growth) / (rate - terminal_growth)
        pv += tv / (1 + rate) ** (last["year"] + 1 - val)
    return pv


def min_cash(rows: list[dict], key: str, start_cash: float, raise_: dict) -> tuple[float, int]:
    cash, low, low_year = start_cash, start_cash, rows[0]["year"]
    for r in rows:
        if raise_["date"] is not None and r["year"] <= raise_["date"] < r["year"] + 1:
            cash += raise_["net"]
        cash += r[key]
        if cash < low:
            low, low_year = cash, r["year"]
    return low, low_year


def rnpv(pnl: list[dict], company: dict, deal: dict, tl: dict) -> dict:
    val = to_year(tl["valuation_date"])
    rate = tl["discount_rate"]
    pos = tl["probability_of_approval"]
    terminal_g = -tl["post_loe_erosion"] if tl["terminal_value"] else None

    pv_success = present_value(pnl, "fcf_success", rate, val, terminal_g)
    pv_acquirer = present_value(pnl, "fcf_acquirer", rate, val, terminal_g)
    pv_failure = present_value(pnl, "fcf_failure", rate, val)
    bs = balance_sheet_today(company, tl)
    rz = raise_terms(company)
    shares = diluted_shares(company, company["price"]) + rz["new_shares"]

    def per_share(ev: float) -> float:
        return (ev + bs["net_cash"] + rz["net"]) * 1e6 / shares

    risked_ev = pos * pv_success + (1 - pos) * pv_failure
    # limited liability: each branch's equity is floored at zero before probability-weighting
    success_ps, failure_ps = max(0.0, per_share(pv_success)), max(0.0, per_share(pv_failure))
    acquirer_ps = max(0.0, per_share(pv_acquirer))
    cash_low_success, cash_low_year = min_cash(pnl, "fcf_success", bs["net_cash"], rz)
    return {
        "discount_rate": rate, "pos": pos,
        "pv_success": pv_success, "pv_acquirer": pv_acquirer, "pv_failure": pv_failure, "risked_ev": risked_ev,
        **bs, "raise_net": rz["net"], "raise_price": rz["price"], "new_shares": rz["new_shares"],
        "fd_shares_post_raise": shares,
        "per_share": pos * success_ps + (1 - pos) * failure_ps,
        "per_share_success": success_ps,
        # strategic value: the drug in a buyer's hands after approval (no takeover premium, no CoC share adjustments)
        "per_share_acquirer": pos * acquirer_ps + (1 - pos) * failure_ps,
        "per_share_acquirer_success": acquirer_ps,
        "per_share_failure": failure_ps,
        "min_net_cash_success": cash_low_success, "min_net_cash_year": cash_low_year,
    }


def after_tax_prv(deal: dict) -> float:
    return deal["prv"]["value"] * (1 - deal["tax"]["rate"])


def multiples_grid(company: dict, deal: dict, tl: dict) -> dict:
    """Per-share value = (peak x multiple x (1-haircut) x PoS + risked after-tax PRV + net cash + raise) / FD shares."""
    g = tl["multiples_grid"]
    pos = tl["probability_of_approval"]
    bs = balance_sheet_today(company, tl)
    rz = raise_terms(company)
    shares = diluted_shares(company, company["price"]) + rz["new_shares"]
    other = pos * after_tax_prv(deal) + bs["net_cash"] + rz["net"]
    table = {peak: {m: (peak * m * (1 - g["royalty_haircut"]) * pos + other) * 1e6 / shares for m in g["multiples"]}
             for peak in g["peak_sales"]}
    return {"table": table, "multiples": g["multiples"], "pos": pos, "shares": shares}


def market_implied(company: dict, deal: dict, tl: dict) -> dict:
    """What today's price says the drug (ex-PRV, ex-cash) is worth."""
    pos = tl["probability_of_approval"]
    bs = balance_sheet_today(company, tl)
    shares = diluted_shares(company, company["price"])
    market_cap = company["price"] * shares / 1e6
    ev = market_cap - bs["net_cash"]
    prv = pos * after_tax_prv(deal)
    drug = ev - prv
    haircut = tl["multiples_grid"]["royalty_haircut"]
    implied_peak = {m: drug / (m * pos * (1 - haircut)) for m in tl["multiples_grid"]["multiples"]}
    return {"price": company["price"], "fd_shares": shares, "market_cap": market_cap, **bs, "ev": ev,
            "risked_after_tax_prv": prv, "implied_drug_value": drug, "implied_peak_sales": implied_peak}
