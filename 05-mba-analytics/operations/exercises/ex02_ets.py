"""
Exercise 2 — ETS (Holt-Winters) forecast.

Concepts: ExponentialSmoothing, Holt-Winters, forecast, residual std.
Lesson: 05-mba-analytics/operations/lessons/02-ets.md
Difficulty: Medium
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: fit a Holt-Winters ETS model (additive trend, no seasonality — our
history is only 12 months which is too short for seasonal decomposition)
on the same SKU-A demand series from ex01. Print the 12-month forecast
and the residual standard deviation.

Expected output (approximate):
    Forecast:
    2027-01    1234
    2027-02    1256
    ...
    Residual std: 48.3 units
"""

import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Setup — 12 months of demand for SKU-A with a DatetimeIndex.
demand = pd.Series(
    [980, 1020, 1100, 1050, 1200, 1180, 1250, 1300, 1150, 1220, 1280, 1320],
    index=pd.date_range("2026-01", periods=12, freq="MS"),
    name="demand_SKU_A",
)

# 🛠️ Step 1: fit the ETS model (additive trend, no seasonality).
#    model = ExponentialSmoothing(demand, trend="add", seasonal=None)
#    fitted = model.fit(optimized=True)

# 🛠️ Step 2: produce a 12-month forecast.
#    forecast = fitted.forecast(12)
#    print("Forecast:")
#    print(forecast.round(0).to_string())

# 🛠️ Step 3: compute and print residual standard deviation.
#    residuals = demand - fitted.fittedvalues
#    print(f"\nResidual std: {residuals.std():.1f} units")
