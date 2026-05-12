"""
Exercise 2 — Three-scenario comparison.

Concepts: dicts, **kwargs unpacking, formatted output, percent change.
Lesson: 05-mba-analytics/strategy/lessons/01-scenarios.md
Difficulty: Medium
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: define base/best/worst scenario dicts and compare the 5-year totals.
Then print a ranked table showing each scenario and its % difference vs base.

Expected output (approximate):
    best   → $17,890,000  (+41% vs base)
    base   → $12,675,000
    worst  →  $7,902,000  (-38% vs base)
"""

# Setup — the revenue model function.
def revenue_5y(starting_units, price, growth_rate, churn_rate, years=5):
    total = 0.0
    units = starting_units
    for _ in range(years):
        units = units * (1 + growth_rate - churn_rate)
        total += units * price
    return total

# Base-case parameters.
base = {
    "starting_units": 1_000,
    "price":          2_400,
    "growth_rate":    0.12,
    "churn_rate":     0.05,
}

# 🛠️ Step 1: define `scenarios` as a dict of dicts:
#    scenarios = {
#        "best":  {**base, "growth_rate": 0.20, "churn_rate": 0.03},
#        "base":  base,
#        "worst": {**base, "growth_rate": 0.06, "churn_rate": 0.10},
#    }

# 🛠️ Step 2: compute the base revenue once.
#    base_rev = revenue_5y(**base)

# 🛠️ Step 3: loop over scenarios (in order: best, base, worst).
#    For each, compute revenue_5y(**params) and the % vs base.

# 🛠️ Step 4: print a formatted table line for each scenario.
#    For best/worst, show the % difference with a sign:
#        f"{name:<6} → ${rev:>12,.0f}  ({pct:+.0%} vs base)"
#    For base, omit the percentage column.
