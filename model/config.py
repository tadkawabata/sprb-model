"""Load YAML inputs and resolve {bear, base, bull} scenario nodes."""
from __future__ import annotations

import copy
import datetime as dt
from pathlib import Path

import yaml

SCENARIOS = ("bear", "base", "bull")
ROOT = Path(__file__).resolve().parent.parent
INPUT_FILES = ("epidemiology", "pricing", "company", "deal_terms", "timeline")


def load_inputs(inputs_dir: Path | None = None) -> dict:
    d = Path(inputs_dir) if inputs_dir else ROOT / "inputs"
    return {name: yaml.safe_load((d / f"{name}.yaml").read_text()) for name in INPUT_FILES}


def is_scenario_node(node) -> bool:
    return isinstance(node, dict) and set(node) == set(SCENARIOS)


def resolve(node, scenario: str):
    """Replace every {bear, base, bull} node with its value for `scenario`."""
    if is_scenario_node(node):
        return resolve(node[scenario], scenario)
    if isinstance(node, dict):
        return {k: resolve(v, scenario) for k, v in node.items()}
    if isinstance(node, list):
        return [resolve(v, scenario) for v in node]
    return node


def scenario_paths(node, prefix: tuple = ()):
    """Yield the key path of every scenario node (these are the tornado drivers)."""
    if is_scenario_node(node):
        yield prefix
    elif isinstance(node, dict):
        for k, v in node.items():
            yield from scenario_paths(v, prefix + (k,))
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from scenario_paths(v, prefix + (i,))


def get_path(node, path):
    for key in path:
        node = node[key]
    return node


def with_override(inputs: dict, path, value) -> dict:
    out = copy.deepcopy(inputs)
    get_path(out, path[:-1])[path[-1]] = value
    return out


def to_year(value) -> float:
    """Date (or ISO string, or number) -> decimal year."""
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        value = dt.date.fromisoformat(value)
    start = dt.date(value.year, 1, 1)
    days = (dt.date(value.year + 1, 1, 1) - start).days
    return value.year + (value - start).days / days


def overlap(year: int, start: float, end: float = float("inf")) -> float:
    """Fraction of calendar `year` that falls inside [start, end)."""
    return max(0.0, min(year + 1, end) - max(year, start))
