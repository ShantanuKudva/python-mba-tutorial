"""
Exercise 2 — Count non-empty lines.

Concepts: .splitlines(), string methods, counting with a loop.
Lesson: 01-foundations/week-3/lessons/01-files.md
Difficulty: Easy
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: count the total number of non-empty lines in the CSV data below.
A line is "empty" if it contains only whitespace after calling .strip().

# (Browser note: this uses an in-memory string instead of a real file.)

Expected output:
    Non-empty lines: 9
"""

# Setup — the CSV data lives in memory.
csv_data = """date,category,description,amount
2026-01-03,Travel,Flight to client,452.10
2026-01-05,Meals,Team lunch,86.50
2026-01-09,Software,SaaS subscription,29.00
2026-01-12,Travel,Hotel,310.00
2026-01-15,Office,Stationery,42.75
2026-01-18,Meals,Client dinner,168.20
2026-01-22,Software,Cloud hosting,55.00
2026-01-25,Travel,Taxi,bad-value
2026-01-28,Office,,33.00"""

lines = csv_data.strip().splitlines()

# 🛠️ Step 1: initialise a counter variable called `count` to 0.

# 🛠️ Step 2: loop over `lines` and add 1 to `count` whenever
#    line.strip() != ""

# 🛠️ Step 3: print the result.
#    print(f"Non-empty lines: {count}")
