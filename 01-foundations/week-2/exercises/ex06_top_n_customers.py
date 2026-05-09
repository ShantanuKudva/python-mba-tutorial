"""
Exercise 6 — Top-N customers by revenue.

Concepts: sorting with `key=`, list slicing, tuple unpacking in loops.
Lesson: lessons/01-lists-and-loops.md, lessons/05-tuples-and-sets.md
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

# 🛠️ Step 1: sort by revenue (the second tuple item), highest first.
#    Hint: sorted(customers, key=lambda row: row[1], reverse=True)

# 🛠️ Step 2: take the first 3 with slicing [:3].

# 🛠️ Step 3: loop with `enumerate(top, start=1)` and unpack (name, rev).
#    Print:  f"{i}. {name:<10} — ${rev:>6,}"
