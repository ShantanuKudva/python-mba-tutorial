"""
Exercise 1 — Read a text file (in-memory).

Concepts: string slicing, .splitlines(), iterating over lines.
Lesson: 01-foundations/week-3/lessons/01-files.md
Difficulty: Easy
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: given the CSV data below as a string, print the first 3 lines,
simulating what you would see when opening a real file.

# (Browser note: this uses an in-memory string instead of a real file.)

Expected output (first 3 lines):
    date,category,description,amount
    2026-01-03,Travel,Flight to client,452.10
    2026-01-05,Meals,Team lunch,86.50
"""

# Setup — the CSV data lives in memory (no real file needed in the browser).
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

first_three = lines[:3]

for line in first_three:
    print(line)
