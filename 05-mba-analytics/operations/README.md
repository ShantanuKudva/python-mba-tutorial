# Week 10 — Operations

**Goal:** forecast next 12 months of demand and recommend reorder quantities.

## Concepts (read first)

- **EOQ** — Economic Order Quantity. Optimal batch size minimizing order + holding cost. — [CFI](https://corporatefinanceinstitute.com/resources/management/economic-order-quantity-eoq/)
- **Safety stock** — buffer for demand variability + lead-time uncertainty. — [Investopedia](https://www.investopedia.com/terms/s/safety-stock.asp)
- **Reorder point** — the stock level that triggers a new order. — [CFI](https://corporatefinanceinstitute.com/resources/management/reorder-point/)
- **Moving average** — `Series.rolling(window).mean()`. — [pandas window guide](https://pandas.pydata.org/docs/user_guide/window.html)
- **Exponential smoothing (ETS)** — weighted-toward-recent forecast. — [statsmodels example](https://www.statsmodels.org/stable/examples/notebooks/generated/exponential_smoothing.html)
- Free deep-dive book: [Forecasting: Principles and Practice (Hyndman)](https://otexts.com/fpp3/) — chapters 1–8 cover everything you need.

## What you'll build

```python
def moving_avg_forecast(series, window=3, periods=12) -> pd.Series: ...
def ets_forecast(series, periods=12) -> pd.DataFrame:   # forecast + lower/upper
def eoq(annual_demand, order_cost, holding_cost) -> float: ...
def safety_stock(demand_std, lead_time_weeks, z=1.65) -> float: ...
def reorder_point(weekly_demand_avg, lead_time_weeks, safety_stock_units) -> float: ...
```

## Map

| File | Topic |
|---|---|
| [`lessons/01-moving-average.md`](lessons/01-moving-average.md) | Naive forecast |
| [`lessons/02-ets.md`](lessons/02-ets.md) | Exponential smoothing with statsmodels |
| [`lessons/03-inventory.md`](lessons/03-inventory.md) | EOQ, safety stock, reorder point |
| [`exercises/`](exercises/) | 4 problems |
| [`project.md`](project.md) | 12-month forecast workbook |

## Dataset

`datasets/operations/sample_demand.xlsx` (24 months of historical units sold per SKU).
