"""
Week 10 Project — 12-Month Demand Forecast and Inventory Plan.

Concepts: ETS (Holt-Winters), EOQ, safety stock, reorder point, formatted output.
Lesson: 05-mba-analytics/operations/project.md
Difficulty: Hard

Goal: for each SKU, fit an ETS model, produce a 12-month forecast, compute
inventory metrics (EOQ, safety stock, reorder point), and print a combined report.

Expected output:
    === SKU-A FORECAST ===
    (12 rows: month, forecast)

    === SKU-A INVENTORY PLAN ===
    Annual demand  : 14,904
    EOQ            :   864.5 units
    Safety stock   :   112.3 units
    Reorder point  :   659.3 units
    ...
"""

import math
import statistics
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Setup — historical demand for two SKUs.
demand_data = {
    "SKU-A": pd.Series(
        [980, 1020, 1100, 1050, 1200, 1180, 1250, 1300, 1150, 1220, 1280, 1320],
        index=pd.date_range("2026-01", periods=12, freq="MS"),
    ),
    "SKU-B": pd.Series(
        [200, 280, 250, 310, 270, 300, 290, 320, 280, 305, 315, 330],
        index=pd.date_range("2026-01", periods=12, freq="MS"),
    ),
}

order_cost      = 75.0    # $ per order
holding_cost    = 3.0     # $ per unit per year
lead_time_weeks = 4
z               = 1.65    # 95% service level

# 🛠️ Step 1: define forecast_one(series, periods=12) → pd.Series.
#    Fit ETS with trend="add", seasonal=None.
#    Return fitted.forecast(periods).

# 🛠️ Step 2: define eoq(annual_demand, order_cost, holding_cost) → float.
#    Return math.sqrt(2 * annual_demand * order_cost / holding_cost).

# 🛠️ Step 3: define inventory_metrics(series, lead_time_weeks, z) → dict.
#    weekly_series = series / 4.33  (approximate weekly from monthly)
#    Compute weekly_avg, weekly_std, safety_stock, reorder_point.
#    Also compute annual_demand = series.sum() and eoq.

# 🛠️ Step 4: for each SKU, call forecast_one and inventory_metrics, then print.
#    Print the 12-month forecast table and the inventory plan.
