"""
Exercise 15 — Shipping cost calculator.

Concepts: //, %, math.ceil, **, augmented assignment, comparison.
Lesson: 01-foundations/week-1/lessons/06-operators-and-math.md
Difficulty: Hard
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: given total_units and pallet_capacity, compute full pallets and loose
units using // and %. Full pallets cost $120 each. Loose units fill a partial
pallet; charge 120 * ceil(loose / pallet_capacity). Apply a 5% surcharge if
the order value exceeds $5,000. Print a full cost breakdown.

Expected output (for values below):
    Units ordered      :    500
    Full pallets       :     10
    Loose units        :     20
    Full pallet cost   :  $1,200.00
    Partial pallet cost:    $120.00
    Subtotal           :  $1,320.00
    Surcharge (5%)     :      $0.00
    Total shipping     :  $1,320.00
"""

import math

total_units     = 500
pallet_capacity = 48
pallet_rate     = 120.0    # $ per pallet
order_value     = 4_800    # $ value of the goods being shipped
surcharge_rate  = 0.05
surcharge_threshold = 5_000

# 🛠️ Step 1: compute full_pallets = total_units // pallet_capacity
#    and loose = total_units % pallet_capacity.

# 🛠️ Step 2: compute full_cost = full_pallets * pallet_rate.
#    Use math.ceil to compute partial_cost:
#    partial_cost = pallet_rate * math.ceil(loose / pallet_capacity) if loose > 0 else 0.

# 🛠️ Step 3: subtotal = full_cost + partial_cost.
#    surcharge = subtotal * surcharge_rate if order_value > surcharge_threshold else 0.
#    total = subtotal + surcharge.

# 🛠️ Step 4: print the breakdown table shown in the expected output above.
#    Labels :<25, numbers :>10 (with $ for currency, :,.2f for amounts).
