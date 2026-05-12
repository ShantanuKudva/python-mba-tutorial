"""
Exercise 1 — Moving-average demand forecast.

Concepts: rolling mean, list slicing, naive forecast.
Lesson: 05-mba-analytics/operations/lessons/01-moving-average.md
Difficulty: Easy
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: given 12 months of historical demand for one SKU, compute the 3-month
moving average, then use the last MA value as a constant 12-month forecast.
Print the forecast for each future period.

Expected output (approximate):
    Month 13 forecast: 1,233 units
    Month 14 forecast: 1,233 units
    ...
    Month 24 forecast: 1,233 units
"""

import pandas as pd

# Setup — 12 months of demand for SKU-A (in units).
demand = pd.Series(
    [980, 1020, 1100, 1050, 1200, 1180, 1250, 1300, 1150, 1220, 1280, 1320],
    index=range(1, 13),
    name="demand_SKU_A",
)

# 🛠️ Step 1: compute the 3-month moving average.
#    ma = demand.rolling(window=3).mean()

# 🛠️ Step 2: the naive forecast = the last MA value.
#    forecast_value = ma.iloc[-1]

# 🛠️ Step 3: print the forecast for months 13 through 24.
#    for month in range(13, 25):
#        print(f"Month {month} forecast: {forecast_value:,.0f} units")
