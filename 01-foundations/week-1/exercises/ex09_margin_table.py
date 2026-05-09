"""
Exercise 9 — Margin table with formatted output.

Concepts: nested conditionals, loops, f-string alignment, functions.
Lesson: 01-foundations/week-1/lessons/03-conditionals.md
Difficulty: Hard
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: given a list of products with revenue and cost, compute gross margin
for each product, grade it, and print a formatted table. At the end, flag
any product earning a "Loss-making" or "At risk" grade.

Grading thresholds (same as ex03):
    >= 25%   Excellent
    15–<25%  Healthy
    5–<15%   Thin
    0–<5%    At risk
    <0%      Loss-making

Expected output (approximate):
    Product       Revenue     Cost   Margin  Grade
    ----------------------------------------------------
    Widget A      $12,300   $8,000    35.0%  Excellent
    Widget B       $4,100   $1,000    75.6%  Excellent
    Widget C      $14,500  $11,200    22.8%  Healthy
    Widget D       $9,800   $9,000     8.2%  Thin
    Widget E       $3,200   $3,500    -9.4%  Loss-making ⚠️
    ----------------------------------------------------
    ⚠️ Widget E needs attention (Loss-making).
"""

# Setup — product data.
products = [
    {"name": "Widget A", "revenue": 12_300, "cost":  8_000},
    {"name": "Widget B", "revenue":  4_100, "cost":  1_000},
    {"name": "Widget C", "revenue": 14_500, "cost": 11_200},
    {"name": "Widget D", "revenue":  9_800, "cost":  9_000},
    {"name": "Widget E", "revenue":  3_200, "cost":  3_500},
]

# 🛠️ Step 1: define a grade(margin_pct) function using if/elif/else
#    that returns one of the five grade strings from the docstring.

# 🛠️ Step 2: print the table header.
#    sep = "-" * 60
#    print(f"{'Product':<14}{'Revenue':>10}{'Cost':>10}{'Margin':>9}  Grade")
#    print(sep)

# 🛠️ Step 3: loop over products, compute margin_pct, call grade(), and
#    print each row. Add " ⚠️" to the grade string if it's "Loss-making"
#    or "At risk".

# 🛠️ Step 4: after the separator, loop again to print one warning line
#    per product whose grade is "Loss-making" or "At risk".
