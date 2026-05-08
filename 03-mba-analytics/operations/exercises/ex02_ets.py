"""
Exercise 2 — ETS forecast.

Same SKU. Fit Holt-Winters with additive trend and seasonality (12).
Print the 12-period forecast and the residual std (for the confidence band).
"""

from pathlib import Path
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

ROOT = Path(__file__).resolve().parents[4]
df = pd.read_excel(ROOT / "datasets" / "operations" / "sample_demand.xlsx")

# 🛠️ Build the series (DatetimeIndex, monthly).
# 🛠️ Fit ExponentialSmoothing with trend='add', seasonal='add', seasonal_periods=12.
# 🛠️ Print model.forecast(12) and (demand - model.fittedvalues).std().
