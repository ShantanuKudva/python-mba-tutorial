"""
Strategy pipeline.

🛠️  STUB — replace with logic from `03-mba-analytics/strategy/scenarios.py`.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any


def run(xlsx_path: Path) -> dict[str, Any]:
    """
    Read base assumptions, return scenario + sensitivity tables.

    Expected return shape:
        {
            "metrics": {
                "scenarios": [
                    {"name": "best", "revenue_5y": 38_000_000},
                    {"name": "base", "revenue_5y": 25_000_000},
                    {"name": "worst", "revenue_5y": 14_000_000},
                ],
                "sensitivity": [
                    {"input": "growth_rate", "low": 18_000_000, "high": 32_000_000, "swing": 14_000_000},
                    ...
                ],
            },
            "headline": "Growth rate is the dominant driver.",
        }
    """
    # TODO(week 11): port scenarios.py. Build best/base/worst + sensitivity table.
    return {
        "metrics": {
            "scenarios": [
                {"name": "best", "revenue_5y": 38_000_000},
                {"name": "base", "revenue_5y": 25_000_000},
                {"name": "worst", "revenue_5y": 14_000_000},
            ],
            "sensitivity": [
                {"input": "growth_rate",   "low": 18_000_000, "high": 32_000_000, "swing": 14_000_000},
                {"input": "price",         "low": 21_000_000, "high": 29_000_000, "swing":  8_000_000},
                {"input": "churn_rate",    "low": 22_500_000, "high": 27_500_000, "swing":  5_000_000},
                {"input": "starting_units","low": 23_000_000, "high": 27_000_000, "swing":  4_000_000},
            ],
        },
        "headline": "(MOCK) Growth rate is the dominant driver.",
    }
