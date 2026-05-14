"""
Exercise 10 — Sum monthly revenue with a for loop.

Concepts: for loop, range(), accumulator pattern.
Lesson: 01-foundations/week-1/lessons/05-loops.md
Difficulty: Easy
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: use a for loop to compute total revenue from a list of monthly figures,
then use range() to print each month label.

Expected output:
    Total revenue: $566,500
    Month 1
    Month 2
    Month 3
    Month 4
    Month 5
    Month 6
"""

monthly_revenue = [82_000, 91_500, 78_000, 105_000, 98_000, 112_000]

total = 0
for rev in monthly_revenue:
    total += rev

print(f"Total revenue: ${total:,}")

for month in range(1, 7):
    print(f"Month {month}")
