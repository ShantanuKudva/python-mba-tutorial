"""
Exercise 4 — Safety stock and reorder point.

Concepts: descriptive statistics, safety stock formula, reorder point.
Lesson: 05-mba-analytics/operations/lessons/03-inventory.md
Difficulty: Hard
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Formulas:
    safety_stock   = z * weekly_std * sqrt(lead_time_weeks)
    reorder_point  = weekly_avg * lead_time_weeks + safety_stock

Goal: given 24 weeks of demand data, compute weekly statistics,
then calculate safety stock (z=1.65 for 95% service level) and reorder point
for a 4-week lead time. Print all four metrics.

Expected output (approximate):
    Weekly avg demand : 284.2 units
    Weekly std        :  38.7 units
    Safety stock      : 107.8 units
    Reorder point     : 1245.6 units
"""

import math
import statistics

# Setup — 24 weeks of weekly demand (units) for SKU-B.
weekly_demand = [
    260, 280, 310, 295, 275, 320, 305, 290,
    285, 300, 270, 315, 325, 280, 295, 310,
    265, 275, 290, 305, 285, 300, 320, 315,
]

z              = 1.65   # 95% service level
lead_time_weeks = 4

# 🛠️ Step 1: compute weekly_avg and weekly_std.
#    weekly_avg = statistics.mean(weekly_demand)
#    weekly_std = statistics.stdev(weekly_demand)

# 🛠️ Step 2: compute safety_stock.
#    safety_stock = z * weekly_std * math.sqrt(lead_time_weeks)

# 🛠️ Step 3: compute reorder_point.
#    reorder_point = weekly_avg * lead_time_weeks + safety_stock

# 🛠️ Step 4: print all four metrics with aligned labels.
#    print(f"{'Weekly avg demand':<22}: {weekly_avg:>6.1f} units")
#    print(f"{'Weekly std':<22}: {weekly_std:>6.1f} units")
#    print(f"{'Safety stock':<22}: {safety_stock:>6.1f} units")
#    print(f"{'Reorder point':<22}: {reorder_point:>6.1f} units")
