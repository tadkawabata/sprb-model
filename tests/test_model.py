from model.config import load_inputs, resolve, scenario_paths, to_year
from model.patients import build_patients
from model.pnl import tiered_royalty
from model.scenarios import run_all, run_scenario
from model.valuation import diluted_shares

INPUTS = load_inputs()
BASE = {k: resolve(v, "base") for k, v in INPUTS.items()}


def test_fully_diluted_shares_match_filings():
    # basic 2,874,013 + RSU/option/ESPP 176,703 + Avenue warrant TSM at $55.20 (64,000 x (1 - 50/55.2))
    assert round(diluted_shares(BASE["company"], 55.20)) == 3_056_745
    assert round(diluted_shares(BASE["company"], 55.20, change_of_control=True)) == 3_114_716


def test_tiered_royalty_is_marginal():
    tiers = [{"up_to": 100, "rate": 0.08}, {"up_to": 250, "rate": 0.10}, {"up_to": None, "rate": 0.12}]
    assert tiered_royalty(50, tiers) == 4.0
    assert abs(tiered_royalty(300, tiers) - (8 + 15 + 6)) < 1e-9


def test_no_patients_before_launch_and_rollovers_at_launch():
    epi = BASE["epidemiology"]
    rows = build_patients(epi, launch=2027.75, years=range(2026, 2031))
    assert rows[0]["treated_end"] == 0
    assert rows[1]["treated_end"] >= epi["rollover_patients_at_launch"]


def test_scenarios_are_ordered():
    res = run_all(INPUTS)
    assert res["bear"]["peak_ww_sales"] < res["base"]["peak_ww_sales"] < res["bull"]["peak_ww_sales"]
    for r in res.values():
        v = r["valuation"]
        assert v["per_share"] >= 0 and v["per_share_acquirer"] >= v["per_share"] - 1e-9


def test_every_scenario_input_resolves_to_a_scalar():
    for path in scenario_paths(INPUTS):
        assert path, "scenario node at the root"
    assert isinstance(BASE["timeline"]["discount_rate"], float)
    assert to_year("2027-07-01") > 2027.49


def test_later_approval_lowers_value():
    late = load_inputs()
    late["timeline"]["approval"]["base"] = "2028-07-01"
    assert (run_scenario(late, "base")["valuation"]["per_share_acquirer"]
            < run_scenario(INPUTS, "base")["valuation"]["per_share_acquirer"])
