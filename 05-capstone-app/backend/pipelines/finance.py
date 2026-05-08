"""
Finance pipeline.

🛠️  STUB — currently returns mock data so the frontend works end-to-end.
     Replace `run` with real logic from `03-mba-analytics/finance/health.py`.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any


def run(xlsx_path: Path) -> dict[str, Any]:
    """
    Read an Excel file and compute financial-health metrics.

    Expected return shape:
        {
            "metrics": {
                "current_ratio": 1.85,
                "quick_ratio": 1.20,
                "debt_to_equity": 1.05,
                "gross_margin": 0.40,
                "operating_margin": 0.16,
                "net_margin": 0.11,
                "score": 72.5,
                "verdict": "Stable",
            },
            "headline": "Healthy liquidity, watch leverage.",
        }
    """
    # TODO(week 11): port `health.py`. Read the workbook, compute ratios,
    # composite score, and a one-line verdict. Return the dict above.
    return {
        "metrics": {
            "current_ratio": 1.85,
            "quick_ratio": 1.20,
            "debt_to_equity": 1.05,
            "gross_margin": 0.40,
            "operating_margin": 0.16,
            "net_margin": 0.11,
            "score": 72.5,
            "verdict": "Stable",
        },
        "headline": "(MOCK) Healthy liquidity, watch leverage.",
    }
