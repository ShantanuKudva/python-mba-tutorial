"""
Week 8 Project — 1-Page Financial Health Report.

Concepts: ratios, weighted scoring, conditionals, io.BytesIO, openpyxl/pandas.
Lesson: 05-mba-analytics/finance/project.md
Difficulty: Hard

Goal: compute all six ratios, produce a health score, and write a two-sheet
Excel workbook to an in-memory buffer (Ratios sheet + Score sheet).

Expected output:
    === RATIOS ===
    Current ratio     : 1.88x   (Benchmark ≥ 1.5)  Strong
    ...
    === HEALTH SCORE ===
    Score: 78 / 100 — Stable
    Key drivers: ...
"""

import io
import pandas as pd

# Setup — P&L and balance sheet in memory.
pl = {
    "Revenue":           5_400_000,
    "COGS":              3_240_000,
    "Gross Profit":      2_160_000,
    "Operating Income":  1_000_000,
    "Net Income":          605_000,
}
bs = {
    "Current Assets":      3_200_000,
    "Inventory":           1_200_000,
    "Current Liabilities": 1_700_000,
    "Total Debt":          2_100_000,
    "Shareholders Equity": 2_900_000,
}

# 🛠️ Step 1: define all_ratios(pl, bs) → dict of six ratios.
#    Reuse the formulas from ex01.

# 🛠️ Step 2: define benchmark(name, value) → "Strong" | "OK" | "Weak".
#    Use simple thresholds:
#    current_ratio ≥ 1.5 → Strong, ≥ 1.0 → OK, else Weak
#    gross_margin  ≥ 0.30 → Strong, ≥ 0.15 → OK, else Weak
#    (define similar rules for the other 4 ratios)

# 🛠️ Step 3: define health_score(ratios) → (score, verdict).
#    Reuse the scoring heuristic from ex04.

# 🛠️ Step 4: print the ratios table and health score.
#    print("=== RATIOS ===")
#    for name, value in ratios.items():
#        ...
#    print("\n=== HEALTH SCORE ===")
#    print(f"Score: {score} / 100 — {verdict}")

# 🛠️ Step 5 (stretch): write a two-sheet Excel workbook to io.BytesIO.
#    buf = io.BytesIO()
#    with pd.ExcelWriter(buf, engine="openpyxl") as writer:
#        ratios_df.to_excel(writer, sheet_name="Ratios", index=False)
#        score_df.to_excel(writer, sheet_name="Score", index=False)
#    buf.seek(0)
#    print(f"\nExcel buffer ready: {len(buf.read()):,} bytes")
