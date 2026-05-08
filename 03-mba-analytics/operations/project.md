# Week 8 Project — 12-Month Demand Forecast

## What you're building

A script that produces, for each SKU in `sample_demand.xlsx`:

- 12-month ETS forecast
- 95% confidence band (lower/upper)
- Recommended EOQ, safety stock, and reorder point
- A chart per SKU

Output:

- **`forecast.xlsx`** with:
  - Sheet "Forecast" — sku | month | forecast | lower | upper.
  - Sheet "Inventory" — sku | annual_demand | eoq | weekly_avg | weekly_std | safety_stock | reorder_point.
  - Sheet "History" — original input.
- **`charts/`** folder with one PNG per SKU showing history + forecast + band.

## Required structure

```python
def load(path) -> pd.DataFrame: ...
def forecast_one(series, periods=12) -> pd.DataFrame: ...
def inventory_metrics(series, lead_time_weeks=4, order_cost=75, holding_cost=3) -> dict: ...
def make_chart(history, forecast_df, sku, out_path: Path) -> None: ...
def main(): ...
```

## File to create

`03-mba-analytics/operations/forecast.py`

## Done when

- Forecast values are positive and roughly continue the historical trend.
- The confidence band widens (or stays steady) into the future, never narrows.
- Each chart shows the history and forecast clearly with shaded band.
- You committed.

🛠️ Stretch: compare ETS vs naive moving-average forecast on a held-out 6 months. Report MAE/MAPE per SKU.
