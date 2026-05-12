"""
Exercise 6 — Demand variance and coefficient of variation.

Concepts: statistics, pandas Series, formatted output, business interpretation.
Lesson: 05-mba-analytics/operations/lessons/01-moving-average.md
Difficulty: Medium
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: for each SKU, compute mean, standard deviation, and coefficient of
variation (CV = std/mean). Classify demand as:
    CV < 0.2  → "Stable"    (easy to forecast)
    CV < 0.5  → "Variable"  (moderate uncertainty)
    CV >= 0.5 → "Erratic"   (hard to forecast)

Expected output:
    SKU        Mean    Std Dev     CV  Classification
    SKU-A      1183       104   0.088  Stable
    SKU-B       562       284   0.505  Erratic
    SKU-C      2450       230   0.094  Stable
"""

import statistics

# Setup — 12 months of demand per SKU.
demand_data = {
    "SKU-A": [980, 1020, 1100, 1050, 1200, 1180, 1250, 1300, 1150, 1220, 1280, 1320],
    "SKU-B": [200,  800,  300, 1000,  150,  950,  400,  700,  100,  850,  600,  950],
    "SKU-C": [2200, 2300, 2400, 2350, 2500, 2450, 2600, 2550, 2450, 2400, 2600, 2650],
}

# 🛠️ Step 1: print the table header.
#    print(f"{'SKU':<10}{'Mean':>8}{'Std Dev':>10}{'CV':>8}  Classification")

# 🛠️ Step 2: loop over demand_data.items().

# 🛠️ Step 3: for each SKU, compute mean, std dev, and CV.
#    mean   = statistics.mean(values)
#    stddev = statistics.stdev(values)
#    cv     = stddev / mean

# 🛠️ Step 4: classify based on CV thresholds.

# 🛠️ Step 5: print the formatted row.
#    print(f"{sku:<10}{mean:>8.0f}{stddev:>10.0f}{cv:>8.3f}  {classification}")
