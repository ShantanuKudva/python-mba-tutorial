"""
Exercise 6 — Top-N customers by revenue.

Concepts: sorting with `key=`, list slicing, tuple unpacking in loops.
Lesson: lessons/01-lists-and-loops.md, lessons/05-tuples-and-sets.md
Difficulty: Medium
📚 References: open the lesson above and see its 📚 Resources section at the bottom (official docs, deep dives, video tutorials). Global index in ROADMAP.md.

Goal: given a list of (name, revenue) tuples, print the TOP 3 by revenue,
ranked.

Expected output for the data below:
    1. globex     — $14,500
    2. acme       — $12,300
    3. umbrella   —  $9,800
"""

customers = [
    ("acme",      12_300),
    ("initech",    4_100),
    ("globex",    14_500),
    ("umbrella",   9_800),
    ("stark",      3_400),
]

sorted_customers = sorted(customers, key=lambda row: row[1], reverse=True)
top3 = sorted_customers[:3]

for i, (name, rev) in enumerate(top3, start=1):
    print(f"{i}. {name:<10} — ${rev:>6,}")
