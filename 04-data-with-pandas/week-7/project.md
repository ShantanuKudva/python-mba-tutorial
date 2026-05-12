# Week 7 Project — Multi-Sheet Dashboard

## What you're building

A script that joins two tables, produces a pivot table and a top-segments summary, then draws a two-panel dashboard chart.

## Input

Two in-memory DataFrames:

- `orders` — order_id, customer_id, amount, order_date
- `customers` — customer_id, name, region, segment

## Expected output

```
=== MONTHLY × REGION PIVOT ===
region     East  North  South  West
month
2026-01    2300   4200   8100     0
...

=== TOP SEGMENTS ===
             revenue  orders
segment
Enterprise     30700       7
SMB            10400       5

(A 1×2 matplotlib chart in the output area)
```

## Required structure

```python
def load(orders_df, customers_df) -> pd.DataFrame:
    """Merge on customer_id, add month column."""

def monthly_by_region(df) -> pd.DataFrame:
    """pivot_table(index=month, columns=region, values=amount, aggfunc=sum)."""

def top_segments(df) -> pd.DataFrame:
    """groupby(segment).agg(revenue, orders).sort_values(revenue desc)."""

def make_dashboard(df) -> None:
    """Draw 1×2 subplot: bar by segment + cumulative revenue line."""
```

## Done when

- The pivot table has months as rows and regions as columns.
- The top-segments table is sorted by revenue descending.
- The chart displays two panels with labelled axes and titles.

**Stretch:** add a third panel to the chart showing revenue by customer name (top 5 only).

[▶ Open project playground](#play/04-data-with-pandas/week-7/project.py)
