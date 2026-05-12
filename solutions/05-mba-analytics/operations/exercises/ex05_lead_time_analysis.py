"""
Exercise 5 — Lead-time distribution and SLA compliance.

Concepts: statistics module, list comprehensions, formatted output.
Lesson: 05-mba-analytics/operations/lessons/03-inventory.md
Difficulty: Medium
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: given 30 observed lead times (days from order to delivery), compute
summary statistics and report SLA compliance for two thresholds: 7 days and 10 days.

Expected output (approximate):
    Lead-time summary
    Min     :  3 days
    Max     : 15 days
    Mean    :  7.1 days
    Median  :  7.0 days
    Std Dev :  2.8 days

    SLA compliance
    Within  7 days: 50.0%
    Within 10 days: 86.7%
"""

import statistics

# Setup — 30 observed lead times in days.
lead_times = [
     5,  7,  8,  6,  9, 12,  4,  7,  6, 10,
     8,  3,  7,  9, 11,  5,  7,  8, 13,  6,
     7,  4, 15,  7,  8,  6,  9,  7,  5, 10,
]

lt_min    = min(lead_times)
lt_max    = max(lead_times)
lt_mean   = statistics.mean(lead_times)
lt_median = statistics.median(lead_times)
lt_std    = statistics.stdev(lead_times)

print("Lead-time summary")
print(f"{'Min':<10}: {lt_min:>2} days")
print(f"{'Max':<10}: {lt_max:>2} days")
print(f"{'Mean':<10}: {lt_mean:>4.1f} days")
print(f"{'Median':<10}: {lt_median:>4.1f} days")
print(f"{'Std Dev':<10}: {lt_std:>4.1f} days")

within_7  = sum(1 for t in lead_times if t <= 7)  / len(lead_times)
within_10 = sum(1 for t in lead_times if t <= 10) / len(lead_times)

print("\nSLA compliance")
print(f"Within  7 days: {within_7:.1%}")
print(f"Within 10 days: {within_10:.1%}")
