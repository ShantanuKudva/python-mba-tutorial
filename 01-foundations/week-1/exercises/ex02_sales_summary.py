"""
Exercise 2 — Sales summary line.

Concepts: f-strings, number formatting.
Lesson: lessons/02-variables-and-types.md
📚 References: open the lesson above and see its 📚 Resources section at the bottom (official docs, deep dives, video tutorials). Global index in ROADMAP.md.

Given units sold and price per unit, print:
    Q3 sales: 1,200 units × $49.99 = $59,988.00

Number formatting cheat sheet:
    f"{n:,}"      → 1,234,567
    f"{n:.2f}"    → 1234.57
    f"{n:,.2f}"   → 1,234.57
"""

quarter = "Q3"
units = 1200
price = 49.99

# 🛠️ Step 1: compute revenue.
# revenue = ...

# 🛠️ Step 2: print the formatted line.
# Use {units:,} and {revenue:,.2f}.
