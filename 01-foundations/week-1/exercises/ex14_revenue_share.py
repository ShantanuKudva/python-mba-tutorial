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

# 🛠️ Step 1: compute revenue for each product (units * price) and store in a
#    list called revenues. Use a for loop or do it manually.

# 🛠️ Step 2: accumulate the grand total using += in a loop.

# 🛠️ Step 3: print the header and separator (see expected output above).

# 🛠️ Step 4: loop over products with enumerate, compute share = revenue / total,
#    and print each row. Product name :<18, revenue :>9, share :.1%.

# 🛠️ Step 5: print the separator and the Total row.
