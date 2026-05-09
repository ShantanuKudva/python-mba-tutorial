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

def grade(margin_pct):
    if margin_pct >= 25:
        return "Excellent"
    elif margin_pct >= 15:
        return "Healthy"
    elif margin_pct >= 5:
        return "Thin"
    elif margin_pct >= 0:
        return "At risk"
    else:
        return "Loss-making"

sep = "-" * 60
print(f"{'Product':<14}{'Revenue':>10}{'Cost':>10}{'Margin':>9}  Grade")
print(sep)

for p in products:
    margin_pct = (p["revenue"] - p["cost"]) / p["revenue"] * 100
    g = grade(margin_pct)
    flag = " ⚠️" if g in ("Loss-making", "At risk") else ""
    print(f"{p['name']:<14}${p['revenue']:>9,}${p['cost']:>8,}{margin_pct:>8.1f}%  {g}{flag}")

print(sep)

for p in products:
    margin_pct = (p["revenue"] - p["cost"]) / p["revenue"] * 100
    g = grade(margin_pct)
    if g in ("Loss-making", "At risk"):
        print(f"⚠️ {p['name']} needs attention ({g}).")
