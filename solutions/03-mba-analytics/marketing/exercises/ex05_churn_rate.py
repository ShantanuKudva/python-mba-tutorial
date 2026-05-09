"""
Exercise 5 — Monthly customer churn rate.

Concepts: arithmetic, list comprehension, formatted output.
Lesson: 03-mba-analytics/marketing/lessons/01-rfm.md
Difficulty: Easy
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: given monthly start-of-month customer counts and end-of-month counts,
compute the churn rate for each month and print a summary table.

Formula:
    churn_rate = (start - end) / start   (if start > 0, else 0)

Expected output:
    Month      Start       End   Churned   Churn Rate
    Jan 2026    4,500     4,320      180        4.0%
    Feb 2026    4,320     4,180      140        3.2%
    ...
"""

# Setup — monthly customer counts.
months = ["Jan 2026", "Feb 2026", "Mar 2026", "Apr 2026", "May 2026"]
start  = [4_500,     4_320,     4_180,     4_100,     4_050]
end    = [4_320,     4_180,     4_100,     4_050,     4_010]

print(f"{'Month':<12}{'Start':>8}{'End':>8}{'Churned':>10}{'Churn Rate':>12}")

for m, s, e in zip(months, start, end):
    churned = s - e
    rate    = churned / s if s > 0 else 0
    print(f"{m:<12}{s:>8,}{e:>8,}{churned:>10,}{rate:>12.1%}")
