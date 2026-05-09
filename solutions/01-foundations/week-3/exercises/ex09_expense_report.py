"""
Exercise 9 — Expense report: categorise, total, and flag anomalies.

Concepts: csv.DictReader, io.StringIO, dicts-as-accumulators, error handling,
          formatted output.
Lesson: 01-foundations/week-3/lessons/02-csv.md
Difficulty: Hard
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: parse the expense CSV, total spend per category, and flag any single
transaction that exceeds the per-category limit below.

Limits: Travel $500 | Meals $200 | Software $100 | Office $75

Expected output (approximate):
    EXPENSE REPORT
    ==============
    Travel      : $762.10  (2 transactions)
    Meals       : $254.70  (2 transactions)
    Software    :  $84.00  (2 transactions)
    Office      :  $75.75  (2 transactions)
    --------------
    TOTAL       : $1,176.55  (8 valid transactions, 1 skipped)

    ⚠️ ANOMALIES
    None
"""

import csv
from io import StringIO

# Setup — the CSV data lives in memory.
# (Browser note: this uses io.StringIO instead of a real file.)
csv_data = """id,date,category,description,amount
INV-001,2026-01-03,Travel,Flight to client,452.10
INV-002,2026-01-05,Meals,Team lunch,86.50
INV-003,2026-01-09,Software,SaaS subscription,29.00
INV-004,2026-01-12,Travel,Hotel,310.00
INV-005,2026-01-15,Office,Stationery,42.75
INV-006,2026-01-18,Meals,Client dinner,168.20
INV-007,2026-01-22,Software,Cloud hosting,55.00
INV-008,2026-01-25,Travel,Taxi,bad-value
INV-009,2026-01-28,Office,,33.00"""

limits = {
    "Travel":   500.0,
    "Meals":    200.0,
    "Software": 100.0,
    "Office":    75.0,
}

totals = {}
skipped = 0
anomalies = []
reader = csv.DictReader(StringIO(csv_data))

for row in reader:
    try:
        amount = float(row["amount"])
    except (ValueError, KeyError):
        skipped += 1
        continue
    cat = row.get("category", "Unknown")
    if cat not in totals:
        totals[cat] = {"sum": 0.0, "count": 0}
    totals[cat]["sum"]   += amount
    totals[cat]["count"] += 1
    if cat in limits and amount > limits[cat]:
        anomalies.append(dict(row, amount=amount))

print("EXPENSE REPORT")
print("==============")

for cat, info in totals.items():
    print(f"{cat:<12}: ${info['sum']:>7.2f}  ({info['count']} transactions)")

print("-" * 14)

valid_count = sum(v["count"] for v in totals.values())
grand_total = sum(v["sum"] for v in totals.values())
print(f"TOTAL       : ${grand_total:,.2f}  ({valid_count} valid transactions, {skipped} skipped)")

print()
print("⚠️ ANOMALIES")
if anomalies:
    for a in anomalies:
        print(f"{a['id']}  {a['category']}  ${a['amount']:.2f}  — over limit")
else:
    print("None")
