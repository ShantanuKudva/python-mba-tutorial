# Lesson 2 — Exponential Smoothing (ETS)

Weighted-toward-recent forecast. Handles trend and seasonality. statsmodels does the heavy lifting.

```python
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

demand = pd.Series(
    [100, 110, 105, 120, 130, 125, 140, 135, 150, 145, 160, 155,
     170, 165, 180, 175, 190, 185, 200, 195, 210, 205, 220, 215],
    index=pd.period_range("2024-01", periods=24, freq="M").to_timestamp(),
)

model = ExponentialSmoothing(
    demand,
    trend="add",
    seasonal="add",
    seasonal_periods=12,
).fit()

forecast = model.forecast(12)
print(forecast)
```

Parameters:

- `trend="add"` for additive trend (e.g., +10 units/month). Use `"mul"` if trend is proportional.
- `seasonal="add"` for additive seasonality. `seasonal_periods=12` for monthly.

## Confidence band (rough)

```python
import numpy as np

resid_std = (demand - model.fittedvalues).std()
z = 1.96
band = pd.DataFrame({
    "forecast": forecast,
    "lower": forecast - z * resid_std,
    "upper": forecast + z * resid_std,
})
```

🧠 This is a back-of-envelope band, not a proper prediction interval. Good enough for a one-page report. For real work read fpp3 chapter 8.

---

## 📚 Resources

**Official docs**
- [statsmodels — exponential smoothing](https://www.statsmodels.org/stable/tsa.html#exponential-smoothing)
- [`ExponentialSmoothing`](https://www.statsmodels.org/stable/generated/statsmodels.tsa.holtwinters.ExponentialSmoothing.html)

**Deep dives**
- [FPP3 — exponential smoothing chapter](https://otexts.com/fpp3/expsmooth.html)

**Video tutorials**
- [YouTube — Holt-Winters in Python](https://www.youtube.com/results?search_query=holt+winters+exponential+smoothing+python+tutorial)


---

Next: [`03-inventory.md`](03-inventory.md).
