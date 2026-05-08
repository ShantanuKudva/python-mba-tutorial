# Week 7 Project — Customer Segmentation Excel

## What you're building

A script that reads the orders + customers data, computes RFM segments, and outputs a polished Excel workbook a marketing team could actually use.

## Output

`segments.xlsx` with:

- **Sheet "Customers"** — one row per customer: customer_id, name, region, R, F, M, RFM, segment, total_spend.
- **Sheet "Segments"** — segment | customer_count | total_revenue | avg_recency | avg_frequency | avg_spend.
- **Sheet "Cohorts"** — cohort retention table (monthly).
- **Sheet "Charts"** *(stretch)* — embedded chart: bar of revenue by segment.

## Required functions

```python
def load(path) -> pd.DataFrame: ...               # joined orders + customers
def rfm(orders, ref_date) -> pd.DataFrame: ...
def score(rfm_df) -> pd.DataFrame: ...
def label(row) -> str: ...
def cohort_retention(orders) -> pd.DataFrame: ...
def write_report(per_customer, per_segment, cohort, out_path) -> None: ...
```

## File to create

`03-mba-analytics/marketing/segmentation.py`

## Done when

- Champions have the highest avg_spend.
- Lost have the highest avg_recency.
- Cohort table has values that decrease (or stay flat) across periods.
- You committed.

🛠️ Stretch: produce `segments.png` — donut chart of customer count by segment.
