"""
Exercise 5 — Pricing function with bulk discount.

Concepts: function definition, default parameters, conditionals.
Lesson: 01-foundations/week-2/lessons/04-functions.md
Difficulty: Easy
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: write `price_for(units, unit_price, bulk_threshold=100, bulk_rate=0.15)`.
- If units >= bulk_threshold, apply the bulk_rate discount.
- Otherwise, charge the full unit price.
- Return the total.

Expected output:
    price_for(50, 10)            → 500.0
    price_for(150, 10)           → 1275.0
    price_for(200, 10, 200, 0.2) → 1600.0
"""

# 🛠️ Step 1: define the function.
#    def price_for(units, unit_price, bulk_threshold=100, bulk_rate=0.15):
#        if units >= bulk_threshold:
#            return units * unit_price * (1 - bulk_rate)
#        return units * unit_price

# 🛠️ Step 2: call the function three times and print the results.
#    print(price_for(50, 10))
#    print(price_for(150, 10))
#    print(price_for(200, 10, 200, 0.2))
