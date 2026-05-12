# Lesson 1 — Moving Average Forecast

The simplest forecast: "average of the last N periods, repeated."

```python
import pandas as pd

demand = pd.Series([100, 110, 105, 120, 130, 125, 140, 135, 150, 145, 160, 155],
                   index=pd.period_range("2025-01", periods=12, freq="M"))

window = 3
trailing_avg = demand.rolling(window).mean()
forecast_value = demand.tail(window).mean()

# 12 months of "flat" forecast
future_idx = pd.period_range(demand.index[-1] + 1, periods=12, freq="M")
forecast = pd.Series([forecast_value] * 12, index=future_idx)

print(forecast)
```

🧠 This is naive on purpose. It's the **baseline** to beat. Any fancier method must produce lower error than this on a held-out sample.

---

## 📚 Resources

**Official docs**
- [`DataFrame.rolling`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rolling.html)
- [Investopedia — moving average](https://www.investopedia.com/terms/m/movingaverage.asp)

**Deep dives**
- [Forecasting: Principles and Practice — moving averages](https://otexts.com/fpp3/classical-decomposition.html)

**Video tutorials**
- [YouTube — moving average forecasting](https://www.youtube.com/results?search_query=moving+average+forecasting+python+pandas)


---

Next: [`02-ets.md`](02-ets.md).

---

## 🏋️ Practice

### Easy

Given the 12-month demand series from the lesson, compute the 3-month trailing moving average for each month. Print the original demand and the moving average side by side.

[▶ Open exercise](#play/05-mba-analytics/operations/exercises/ex01_moving_avg.py)

### Medium

Compute both a 3-month and a 6-month trailing moving average. Plot both on the same line chart alongside the original demand. Use `savefig("moving_avg.png")` and print a confirmation when done. Which window smooths more aggressively?

[▶ Open exercise](#play/05-mba-analytics/operations/exercises/ex01_moving_avg.py)

### Hard

Compute the Mean Absolute Error (MAE) and Mean Absolute Percentage Error (MAPE) of the 3-month moving average against the held-out last 3 months. Then extend the forecast 6 months into the future. Print the error metrics and the forecast table.

[▶ Open exercise](#play/05-mba-analytics/operations/exercises/ex01_moving_avg.py)
