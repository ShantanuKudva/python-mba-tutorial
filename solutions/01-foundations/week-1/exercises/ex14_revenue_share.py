"""
Exercise 14 — Revenue share per product.

Concepts: *, +=, /, comparison operators, f-string formatting.
Lesson: 01-foundations/week-1/lessons/06-operators-and-math.md
Difficulty: Medium
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: compute per-product revenue using *, accumulate the total with +=,
then compute each product's share of total using /. Print a formatted table.

Expected output (approximate — exact spacing depends on your formatting choices):
    Product            Revenue   Share
    ----------------------------------
    Laptop Bag        $ 18,400   49.7%
    Wireless Keyboard $  9,200   24.8%
    Monitor Stand     $  6,750   18.2%
    Webcam            $  2,700    7.3%
    ----------------------------------
    Total             $ 37,050  100.0%
"""

products     = ["Laptop Bag", "Wireless Keyboard", "Monitor Stand", "Webcam"]
units_sold   = [184, 230, 135, 108]
unit_prices  = [100.0, 40.0, 50.0, 25.0]

revenues = []
for units, price in zip(units_sold, unit_prices):
    revenues.append(units * price)

total = 0
for rev in revenues:
    total += rev

sep = "-" * 34
print(f"{'Product':<18}{'Revenue':>8}{'Share':>8}")
print(sep)

for name, rev in zip(products, revenues):
    share = rev / total
    print(f"{name:<18}${int(rev):>7,}{share:>8.1%}")

print(sep)
print(f"{'Total':<18}${int(total):>7,}{'100.0%':>8}")
