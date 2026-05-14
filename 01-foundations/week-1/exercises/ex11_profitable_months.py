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

# 🛠️ Step 1: initialise count = 0 and total = 0.

# 🛠️ Step 2: loop over monthly_profit. If a value is negative, use continue
#    to skip it. Otherwise add to total and increment count.

# 🛠️ Step 3: compute average = total / count.

# 🛠️ Step 4: print the three-line summary shown in the docstring above.
#    Use label width of 18 chars (left-align with :<18) and right-align numbers.
