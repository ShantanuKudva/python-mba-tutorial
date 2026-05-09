"""
Exercise 8 — Filter invoices by date range and compute days outstanding.

Concepts: datetime, strptime, timedelta math.
Lesson: lessons/06-datetime.md
Difficulty: Hard
📚 References: open the lesson above and see its 📚 Resources section at the bottom (official docs, deep dives, video tutorials). Global index in ROADMAP.md.

Goal: given a list of invoices, print every invoice that was issued
on or after 2026-02-01, along with how many days old it is today.

Use:    today = date(2026, 5, 9)   # pretend today, for stable output

Expected output:
    INV-002 issued 2026-02-15 — 83 days old
    INV-003 issued 2026-03-15 — 55 days old
    INV-004 issued 2026-04-02 — 37 days old
"""

from datetime import date, datetime

today = date(2026, 5, 9)
cutoff = date(2026, 2, 1)

invoices = [
    {"id": "INV-001", "issued": "2026-01-12"},
    {"id": "INV-002", "issued": "2026-02-15"},
    {"id": "INV-003", "issued": "2026-03-15"},
    {"id": "INV-004", "issued": "2026-04-02"},
]

# 🛠️ Step 1: loop over invoices.
# 🛠️ Step 2: parse "issued" using datetime.strptime(..., "%Y-%m-%d").date()
# 🛠️ Step 3: skip the row if issued < cutoff.
# 🛠️ Step 4: days_old = (today - issued_date).days
# 🛠️ Step 5: print  f"{id} issued {issued} — {days_old} days old"
