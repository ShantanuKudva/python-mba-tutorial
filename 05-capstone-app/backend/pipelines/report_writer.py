"""
Polished xlsx report generator.

🛠️  STUB — currently writes a minimal 2-sheet workbook. Improve in week 12:
     formatted headers, cell colors, embedded charts.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd


def write_report(
    metrics: dict[str, Any],
    summary: str,
    source_path: Path,
    out_path: Path,
) -> None:
    """
    Write a polished xlsx with metrics + AI summary + raw data.

    Sheets to include (week 12):
      - Summary   — AI narrative, model name, generated_at
      - Metrics   — flat key/value table of all metrics
      - Raw       — copy of the source workbook's first sheet
    """
    out_path.parent.mkdir(parents=True, exist_ok=True)

    flat = _flatten(metrics)
    metrics_df = pd.DataFrame(
        [{"metric": k, "value": v} for k, v in flat.items()]
    )

    summary_df = pd.DataFrame([{"section": "AI Summary", "text": summary or "(no summary)"}])

    try:
        raw = pd.read_excel(source_path)
    except Exception:
        raw = pd.DataFrame([{"info": "Could not read source workbook."}])

    with pd.ExcelWriter(out_path, engine="openpyxl") as writer:
        summary_df.to_excel(writer, sheet_name="Summary", index=False)
        metrics_df.to_excel(writer, sheet_name="Metrics", index=False)
        raw.to_excel(writer, sheet_name="Raw", index=False)


def _flatten(d: dict, prefix: str = "") -> dict:
    """Collapse nested dicts/lists into 'a.b.0.c' style keys for a flat table."""
    out: dict[str, Any] = {}
    for key, value in d.items():
        full = f"{prefix}{key}"
        if isinstance(value, dict):
            out.update(_flatten(value, prefix=full + "."))
        elif isinstance(value, list):
            for i, item in enumerate(value):
                if isinstance(item, dict):
                    out.update(_flatten(item, prefix=f"{full}.{i}."))
                else:
                    out[f"{full}.{i}"] = item
        else:
            out[full] = value
    return out
