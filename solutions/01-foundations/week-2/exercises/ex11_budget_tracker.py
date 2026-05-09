"""
Exercise 11 — Department budget tracker.

Concepts: dicts of dicts, nested loops, arithmetic, formatted table output.
Lesson: 01-foundations/week-2/lessons/02-dicts.md
Difficulty: Hard
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: given a budget dict and a spending dict (both keyed by department),
compute each department's variance (budget − spent), print a formatted table,
and summarise how many departments are over-budget.

Expected output:
    Department     Budget       Spent    Variance  Status
    ----------------------------------------------------------
    Sales         $120,000    $118,500     $1,500  OK
    Marketing      $80,000     $84,200    -$4,200  OVER
    Engineering   $200,000    $198,750     $1,250  OK
    HR             $45,000     $46,100    -$1,100  OVER
    Operations     $95,000     $92,300     $2,700  OK
    ----------------------------------------------------------
    Summary: 2 of 5 departments are over-budget.
"""

# Setup — annual budgets and actual spend (in $).
budget = {
    "Sales":       120_000,
    "Marketing":    80_000,
    "Engineering": 200_000,
    "HR":           45_000,
    "Operations":   95_000,
}

spent = {
    "Sales":       118_500,
    "Marketing":    84_200,
    "Engineering": 198_750,
    "HR":           46_100,
    "Operations":   92_300,
}

sep = "-" * 62
print(f"{'Department':<16}{'Budget':>12}{'Spent':>12}{'Variance':>12}  Status")
print(sep)

for dept, bud in budget.items():
    s = spent[dept]
    variance = bud - s
    status = "OK" if variance >= 0 else "OVER"
    var_str = f"${variance:,}" if variance >= 0 else f"-${abs(variance):,}"
    print(f"{dept:<16}${bud:>11,}${s:>11,}{var_str:>12}  {status}")

print(sep)

over_count = sum(1 for d in budget if budget[d] < spent[d])
print(f"\nSummary: {over_count} of {len(budget)} departments are over-budget.")
