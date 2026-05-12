"""
Exercise 5 — Break-even analysis.

Concepts: contribution margin, break-even point, formatted output.
Lesson: 05-mba-analytics/finance/lessons/01-ratios.md
Difficulty: Medium
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: implement a break-even calculator and run it for three product scenarios.
Report contribution margin, break-even units, and break-even revenue for each.

Formula:
    contribution_margin_per_unit = price - variable_cost
    break_even_units = fixed_costs / contribution_margin_per_unit
    break_even_revenue = break_even_units * price

Expected output (approximate):
    Product A:  CM/unit $15.00, break-even 3,333 units, revenue $99,990.00
    Product B:  CM/unit $30.00, break-even 1,667 units, revenue $116,690.00
    Product C:  NOT VIABLE — contribution margin is zero or negative.
"""

import math

# Setup — three product scenarios.
products = [
    {"name": "Product A", "price": 25.00,  "variable_cost": 10.00, "fixed_costs":  50_000},
    {"name": "Product B", "price": 80.00,  "variable_cost": 50.00, "fixed_costs":  50_000},
    {"name": "Product C", "price": 15.00,  "variable_cost": 15.00, "fixed_costs":  40_000},
]

# 🛠️ Step 1: loop over products.

# 🛠️ Step 2: for each product, compute contribution_margin_per_unit.
#    cm = p["price"] - p["variable_cost"]

# 🛠️ Step 3: if cm <= 0, print the NOT VIABLE message and skip.
#    Otherwise compute break_even_units (use math.ceil) and break_even_revenue.

# 🛠️ Step 4: print a formatted summary line for each product.
#    print(f"{p['name']}: CM/unit ${cm:.2f}, break-even {beu:,} units, revenue ${ber:,.2f}")
