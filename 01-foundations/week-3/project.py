"""
Week 3 Project — Expense Categoriser.

Concepts: csv.DictReader, io.StringIO, dicts-as-accumulators, functions,
          error handling, formatted output.
Lesson: 01-foundations/week-3/project.md
Difficulty: Hard

Goal: parse the expense CSV, total spend per category, and write a plain-text
summary to the output area.

Expected output:
    EXPENSE SUMMARY
    ===============
    Travel       $762.10  (2 transactions)
    Meals        $254.70  (2 transactions)
    Software      $84.00  (2 transactions)
    Office        $75.75  (2 transactions)
    ---
    TOTAL      $1,176.55  (8 transactions)
    Skipped 1 bad row.
"""

import csv
from io import StringIO

# Setup — expense CSV data in memory.
# (Browser note: this uses io.StringIO instead of a real file on disk.)
CSV_DATA = """date,category,description,amount
2026-01-03,Travel,Flight to client,452.10
2026-01-05,Meals,Team lunch,86.50
2026-01-09,Software,SaaS subscription,29.00
2026-01-12,Travel,Hotel,310.00
2026-01-15,Office,Stationery,42.75
2026-01-18,Meals,Client dinner,168.20
2026-01-22,Software,Cloud hosting,55.00
2026-01-25,Travel,Taxi,bad-value
2026-01-28,Office,,33.00"""

# 🛠️ Step 1: define load_expenses(csv_text) → (rows, skipped_count).
#    Parse CSV_DATA with csv.DictReader(StringIO(csv_text)).
#    Convert amount to float; skip rows that raise ValueError.
#    Return a list of clean row dicts and the count of skipped rows.

# 🛠️ Step 2: define summarise(rows) → dict {category: {"total": float, "count": int}}.
#    Loop over rows and accumulate total and count per category.

# 🛠️ Step 3: call both functions.
#    rows, skipped = load_expenses(CSV_DATA)
#    summary = summarise(rows)

# 🛠️ Step 4: print the expense report.
#    - Header: "EXPENSE SUMMARY" + "=" * 15
#    - One line per category, sorted by total descending:
#        f"{cat:<12} ${total:>7,.2f}  ({count} transaction{'s' if count != 1 else ''})"
#    - Separator "---"
#    - Total line and skipped count.

# 🛠️ Stretch: sort by total descending instead of alphabetically.
#    categories_sorted = sorted(summary.items(), key=lambda kv: kv[1]["total"], reverse=True)
