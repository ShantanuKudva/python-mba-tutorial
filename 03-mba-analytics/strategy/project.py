"""
Week 9 Project — Scenario Model with Tornado Chart.

Concepts: revenue modelling, sensitivity analysis, pandas, matplotlib.
Lesson: 03-mba-analytics/strategy/project.md
Difficulty: Hard

Goal: model three scenarios (base/best/worst), run a ±20% sensitivity analysis
on all four inputs, and draw a tornado chart.

Expected output:
    === SCENARIO TABLE ===
    best   → $17,890,000  (+41% vs base)
    base   → $12,675,000
    worst  →  $7,902,000  (-38% vs base)

    === SENSITIVITY TABLE ===
    (sorted by abs_swing descending)

    A horizontal tornado chart displayed in the output area.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Setup — model function.
def revenue_model(starting_units, price, growth_rate, churn_rate, years=5):
    total = 0.0
    units = starting_units
    for _ in range(years):
        units = units * (1 + growth_rate - churn_rate)
        total += units * price
    return total

base = {
    "starting_units": 1_000,
    "price":          2_400,
    "growth_rate":    0.12,
    "churn_rate":     0.05,
}

# 🛠️ Step 1: define scenarios_table(base) → pd.DataFrame.
#    Build best, base, worst dicts.
#    Return a DataFrame with columns: scenario, revenue, vs_base_pct.

# 🛠️ Step 2: print the scenario table.

# 🛠️ Step 3: define sensitivity_table(base, delta=0.20) → pd.DataFrame.
#    For each key in base, vary it by ±delta while keeping others fixed.
#    Compute low_rev, high_rev, swing = high - low, abs_swing = abs(swing).
#    Return sorted by abs_swing descending.

# 🛠️ Step 4: print the sensitivity table.

# 🛠️ Step 5: draw the tornado chart.
#    base_rev = revenue_model(**base)
#    fig, ax = plt.subplots(figsize=(8, 4))
#    sens = sensitivity_table(base)
#    y = range(len(sens))
#    ax.barh(list(y), sens["high"] - base_rev, left=base_rev, color="steelblue", label="+20%")
#    ax.barh(list(y), sens["low"]  - base_rev, left=base_rev, color="tomato",    label="-20%")
#    ax.set_yticks(list(y)); ax.set_yticklabels(sens["input"].tolist())
#    ax.axvline(base_rev, color="black", linewidth=1, linestyle="--")
#    ax.set_title("Tornado Chart — 5-Year Revenue Sensitivity")
#    ax.legend(); plt.tight_layout(); plt.show()
