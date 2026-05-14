"""
Exercise 11 — Summarise profitable months.

Concepts: for loop, continue, accumulator, conditional logic.
Lesson: 01-foundations/week-1/lessons/05-loops.md
Difficulty: Medium
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: given a list of monthly profits (some negative), use continue to skip
loss-making months. Count profitable months, sum their profit, and compute
average profit per profitable month.

Expected output:
    Profitable months : 4
    Total profit      : $43,700
    Average profit    : $10,925.00
"""

monthly_profit = [12_000, -3_500, 8_200, -1_100, 5_500, 18_000]

count = 0
total = 0

for profit in monthly_profit:
    if profit < 0:
        continue
    total += profit
    count += 1

average = total / count

print(f"{'Profitable months':<18}: {count}")
print(f"{'Total profit':<18}: ${total:,}")
print(f"{'Average profit':<18}: ${average:,.2f}")
