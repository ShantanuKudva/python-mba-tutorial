"""
Exercise 1 — Total revenue from two parallel lists.

Concepts: zip, sum, loop.
Lesson: lessons/01-lists-and-loops.md
Difficulty: Easy
📚 References: see the 📚 Resources block at the bottom of the related lesson(s) in `lessons/` for official docs, deep dives, and video tutorials. Global resource index lives in ROADMAP.md.

Goal: given two parallel lists (units and prices), compute total revenue.

Expected output:
    Total revenue: $32,475.00
"""

units = [120, 80, 200, 45]
prices = [49.99, 99.50, 25.00, 199.00]

total = sum(u * p for u, p in zip(units, prices))

print(f"Total revenue: ${total:,.2f}")
