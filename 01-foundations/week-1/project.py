"""
Week 1 Project — Break-even Calculator.

Concepts: variables, arithmetic, conditionals, f-strings, input().
Lesson: 01-foundations/week-1/project.md
Difficulty: Hard

Goal: build a break-even calculator that asks for three numbers, computes
the break-even point, and tells you whether the business is viable.

Formula:
    contribution_margin = price_per_unit - variable_cost_per_unit
    break_even_units    = fixed_costs / contribution_margin   (round up)
    break_even_revenue  = break_even_units * price_per_unit

Expected output (for fixed=50000, price=25, variable=15):
    Contribution margin per unit: $10.00
    Break-even units: 5,000
    Break-even revenue: $125,000.00
    Verdict: Viable — each unit contributes $10.00 toward fixed costs.

If contribution margin <= 0:
    Verdict: NOT VIABLE — variable cost is at or above price.
"""

import math

# 🛠️ Step 1: ask the user for three inputs using input() and convert to float.
#    fixed_costs       = float(input("Fixed costs ($): "))
#    price_per_unit    = float(input("Price per unit ($): "))
#    variable_cost     = float(input("Variable cost per unit ($): "))
#
#    Tip: build with hard-coded values first, then replace with input() calls.
#    fixed_costs    = 50_000
#    price_per_unit = 25.0
#    variable_cost  = 15.0

# 🛠️ Step 2: compute contribution margin.
#    cm = price_per_unit - variable_cost

# 🛠️ Step 3: if cm <= 0, print the NOT VIABLE verdict and stop.
#    Otherwise compute break-even units (use math.ceil) and revenue.

# 🛠️ Step 4: print contribution margin, break-even units, revenue, and verdict.
#    print(f"Contribution margin per unit: ${cm:.2f}")
#    print(f"Break-even units: {beu:,}")
#    print(f"Break-even revenue: ${ber:,.2f}")
#    print(f"Verdict: Viable — each unit contributes ${cm:.2f} toward fixed costs.")

# 🛠️ Stretch: wrap the input() calls in try/except ValueError so a
#    non-numeric entry prints a friendly error message instead of crashing.
