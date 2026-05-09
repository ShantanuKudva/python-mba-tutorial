"""
Exercise 3 — Economic Order Quantity (EOQ).

Concepts: math.sqrt, function definition, formatted output.
Lesson: 03-mba-analytics/operations/lessons/03-inventory.md
Difficulty: Easy
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Formula: EOQ = sqrt(2 * annual_demand * order_cost / holding_cost_per_unit)

Goal: implement the EOQ function and test it with the two cases below.

Expected output:
    EOQ (12000, 50, 2)  →  774.6 units
    EOQ (50000, 100, 4) → 1581.1 units
"""

import math

def eoq(annual_demand, order_cost, holding_cost):
    return math.sqrt(2 * annual_demand * order_cost / holding_cost)

print(f"EOQ (12000, 50, 2)  → {eoq(12_000, 50, 2):>7.1f} units")
print(f"EOQ (50000, 100, 4) → {eoq(50_000, 100, 4):>7.1f} units")
