"""
Marketing pipeline.

🛠️  STUB — replace with logic from `03-mba-analytics/marketing/segmentation.py`.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any


def run(xlsx_path: Path) -> dict[str, Any]:
    """
    Read orders + customers, return segmentation summary.

    Expected return shape:
        {
            "metrics": {
                "total_revenue": 1_240_000,
                "customer_count": 412,
                "segments": [
                    {"name": "Champions", "customers": 48, "revenue": 540_000, "avg_spend": 11_250},
                    ...
                ],
                "top_cohort_retention_pct_m1": 62.3,
            },
            "headline": "Champions segment drives 43% of revenue.",
        }
    """
    # TODO(week 11): port segmentation logic. RFM scoring + segment counts + cohort.
    return {
        "metrics": {
            "total_revenue": 1_240_000,
            "customer_count": 412,
            "segments": [
                {"name": "Champions", "customers": 48, "revenue": 540_000, "avg_spend": 11_250},
                {"name": "Loyal", "customers": 92, "revenue": 320_000, "avg_spend": 3_478},
                {"name": "At Risk", "customers": 75, "revenue": 180_000, "avg_spend": 2_400},
                {"name": "Lost", "customers": 197, "revenue": 200_000, "avg_spend": 1_015},
            ],
            "top_cohort_retention_pct_m1": 62.3,
        },
        "headline": "(MOCK) Champions segment drives 43% of revenue.",
    }
