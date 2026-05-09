"""
Exercise 3 — Sensitivity table and tornado chart.

Concepts: sensitivity analysis, pandas DataFrame, matplotlib barh.
Lesson: 03-mba-analytics/strategy/lessons/02-sensitivity.md
Difficulty: Hard
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: vary each of the four inputs by ±20%, compute the resulting revenue swing,
build a sorted DataFrame, print it, and draw a horizontal tornado chart.

Expected output:
    A printed sensitivity table (4 rows, sorted by abs_swing descending).
    A matplotlib tornado chart displayed in the output area.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Setup — model and base parameters.
def revenue_5y(starting_units, price, growth_rate, churn_rate, years=5):
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
base_rev = revenue_5y(**base)
delta = 0.20   # ±20%

rows = []
for key in base:
    low_params  = {**base, key: base[key] * (1 - delta)}
    high_params = {**base, key: base[key] * (1 + delta)}
    low_rev  = revenue_5y(**low_params)
    high_rev = revenue_5y(**high_params)
    rows.append({"input": key, "low": low_rev, "high": high_rev})

sens = pd.DataFrame(rows)
sens["swing"]     = sens["high"] - sens["low"]
sens["abs_swing"] = sens["swing"].abs()
sens = sens.sort_values("abs_swing", ascending=False)
print(sens[["input", "low", "high", "swing"]].to_string(index=False))

fig, ax = plt.subplots(figsize=(8, 4))
bars_left  = sens["low"]  - base_rev
bars_right = sens["high"] - base_rev
y = range(len(sens))
ax.barh(list(y), bars_right, left=base_rev, color="steelblue", label="+20%")
ax.barh(list(y), bars_left,  left=base_rev, color="tomato",    label="-20%")
ax.set_yticks(list(y))
ax.set_yticklabels(sens["input"].tolist())
ax.axvline(base_rev, color="black", linewidth=1, linestyle="--")
ax.set_title("Tornado Chart — 5-Year Revenue Sensitivity")
ax.legend()
plt.tight_layout()
plt.show()
