# Week 5 Project — Multi-Sheet Workbook → Consolidated Dashboard

## What you're building

A script that reads a multi-sheet Excel workbook, joins the sheets, and produces:

1. A single cleaned DataFrame.
2. A summary Excel with multiple sheets (totals + pivot).
3. A PNG dashboard image with two charts.

## Input

`datasets/marketing/sample_orders.xlsx` with sheets:

- `orders` — order_id, customer_id, order_date, product_category, amount
- `customers` — customer_id, name, region, segment

## Output (next to your script)

- `dashboard.xlsx` with sheets:
  - `monthly_by_region` — pivot, rows=month, cols=region, values=sum amount.
  - `top_segments` — sorted: segment | total revenue | order count.
- `dashboard.png` — two side-by-side charts:
  - Left: bar chart of monthly revenue (overall).
  - Right: bar chart of revenue by segment.

## Required structure

```python
def load(path) -> pd.DataFrame:        # joins orders + customers
def monthly_by_region(df) -> pd.DataFrame:
def top_segments(df) -> pd.DataFrame:
def make_dashboard(df, out_png: Path) -> None:
def write_workbook(month_df, seg_df, out_xlsx: Path) -> None:
def main(): ...
```

## File to create

`02-data-with-pandas/week-5/dashboard.py`

## Done when

- `dashboard.xlsx` opens and both sheets look right.
- `dashboard.png` shows two clean, labeled charts.
- You committed.

🛠️ Stretch: also output a top-10 customers sheet by lifetime revenue.
