"""
Exercise 5 — Pricing function with bulk discount.

Concepts: function with default args, conditionals.

Write `price_for(units, unit_price, bulk_threshold=100, bulk_rate=0.15)`:
- If units >= bulk_threshold, apply `bulk_rate` discount.
- Otherwise, full price.
- Return the total.

Test with:
    price_for(50, 10)            → 500.0
    price_for(150, 10)           → 1275.0   (15% off)
    price_for(200, 10, 200, 0.2) → 1600.0   (20% off, threshold 200)

📚 References: see the 📚 Resources block at the bottom of the related lesson(s) in `lessons/` for official docs, deep dives, and video tutorials. Global resource index lives in ROADMAP.md.
"""

# 🛠️ def price_for(units, unit_price, bulk_threshold=100, bulk_rate=0.15):
#         ...

# 🛠️ Print the three test calls.
