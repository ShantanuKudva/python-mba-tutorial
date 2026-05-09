# Week 8 Project — 12-Month Demand Forecast and Inventory Plan

## What you're building

A script that forecasts demand 12 months ahead and computes an inventory plan (EOQ, safety stock, reorder point) for each SKU.

## Required functions

```python
def forecast_one(series, periods=12) -> pd.Series:
    """Fit ETS (additive trend) and return 12-month forecast."""

def eoq(annual_demand, order_cost, holding_cost) -> float:
    """Economic Order Quantity formula."""

def inventory_metrics(series, lead_time_weeks, z) -> dict:
    """Return weekly_avg, weekly_std, safety_stock, reorder_point, eoq."""
```

## Expected output

```
=== SKU-A FORECAST ===
2027-01    1345.0
2027-02    1360.3
...

=== SKU-A INVENTORY PLAN ===
Annual demand  : 14,196
EOQ            :   845.8 units
Safety stock   :   108.4 units
Reorder point  :   637.2 units
```

## Done when

- Forecast values are positive and continue the upward trend.
- EOQ, safety stock, and reorder point are computed correctly.
- The report prints for both SKU-A and SKU-B.

**Stretch:** draw a line chart showing historical demand and the 12-month forecast for both SKUs on the same axes.

[▶ Open project playground](#play/03-mba-analytics/operations/project.py)
