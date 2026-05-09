"""
Exercise 5 — Lead-time distribution and SLA compliance.

Concepts: statistics module, list comprehensions, formatted output.
Lesson: 03-mba-analytics/operations/lessons/03-inventory.md
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

# 🛠️ Step 1: compute min, max, mean, median, and std dev.
#    lt_min    = min(lead_times)
#    lt_max    = max(lead_times)
#    lt_mean   = statistics.mean(lead_times)
#    lt_median = statistics.median(lead_times)
#    lt_std    = statistics.stdev(lead_times)

# 🛠️ Step 2: print the summary section.
#    print("Lead-time summary")
#    print(f"{'Min':<10}: {lt_min:>2} days")
#    ... (etc.)

# 🛠️ Step 3: compute SLA compliance for 7-day and 10-day thresholds.
#    within_7  = sum(1 for t in lead_times if t <= 7)  / len(lead_times)
#    within_10 = sum(1 for t in lead_times if t <= 10) / len(lead_times)

# 🛠️ Step 4: print the SLA section.
#    print("\nSLA compliance")
#    print(f"Within  7 days: {within_7:.1%}")
#    print(f"Within 10 days: {within_10:.1%}")
