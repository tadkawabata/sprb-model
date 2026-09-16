"""Cohort-based US patient model.

Pools, updated annually:
  eligible  — diagnosed, still early enough to benefit, not yet on drug.
              Seeded at launch with the prevalent bolus; fed by incident cohorts;
              drains through starts and through disease progression.
  treated   — on drug; seeded with trial/EAP rollovers at launch; drains at 1 / years_on_therapy (death + discontinuation).

Because treated attrition is slow when the drug extends survival, the treated pool
accumulates for 10-20 years — the mechanism behind the ">$1B peak" claims.
"""
from __future__ import annotations

import math

from .config import overlap


def annual_cases(epi: dict) -> float:
    return epi["us_live_births"] * epi["incidence_per_100k"] / 1e5


def start_rate(tau: float, epi: dict) -> float:
    """Logistic ramp of the annual start rate from `start_rate_at_launch` x mature to ~mature by ramp_years."""
    ramp = epi["start_ramp_years"]
    floor = epi["start_rate_at_launch"]
    logistic = 1 / (1 + math.exp(-(8 / ramp) * (tau - ramp / 2)))
    return epi["annual_start_rate_mature"] * (floor + (1 - floor) * logistic)


def build_patients(epi: dict, launch: float, years) -> list[dict]:
    cases = annual_cases(epi)
    prevalent = cases * epi["untreated_life_years"]
    bolus = prevalent * epi["dx_rate_prevalent"] * epi["eligible_frac_prevalent"]
    attrition = 1 / epi["years_on_therapy"]
    loss = epi["eligibility_loss_rate"]

    eligible = treated = 0.0
    rows = []
    for y in years:
        on = overlap(y, launch)
        row = {"year": y, "annual_cases": cases, "prevalent_at_launch": prevalent,
               "eligible_pool": 0.0, "starts": 0.0, "treated_end": 0.0, "treated_avg": 0.0}
        if on == 0:
            rows.append(row)
            continue
        if y <= launch < y + 1:
            eligible += bolus
            treated += epi["rollover_patients_at_launch"]
        tau = (y + 1 - launch) - on / 2          # years since launch at mid on-market period
        dx = epi["dx_rate_prevalent"] + (epi["dx_rate_incident_mature"] - epi["dx_rate_prevalent"]) * min(
            1.0, tau / epi["years_to_mature_dx"])

        starts = eligible * start_rate(tau, epi) * on
        begin = treated
        treated = treated * (1 - attrition * on) + starts
        eligible = (eligible - starts) * (1 - loss * on) + cases * dx * epi["eligible_frac_incident"] * on

        row.update(eligible_pool=eligible, starts=starts, treated_end=treated,
                   treated_avg=(begin + treated) / 2 * on)
        rows.append(row)
    return rows
