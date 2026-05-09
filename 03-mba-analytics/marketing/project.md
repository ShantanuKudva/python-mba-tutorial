# Week 7 Project — Customer Segmentation Report

## What you're building

A script that computes RFM segments and prints a polished summary table a marketing team could actually use.

## Required functions

```python
def rfm(orders, ref_date) -> pd.DataFrame: ...
def score(rfm_df) -> pd.DataFrame: ...
def label(row) -> str: ...
```

## Expected output

```
=== PER-CUSTOMER RFM ===
 customer_id  recency  frequency  monetary   segment
         101        6          3      3800  Champion
         102       47          2      1750    Loyal
         103       30          2      1200  Potential
         104       31          2       700  At Risk
         105       21          1       200  At Risk

=== SEGMENT SUMMARY ===
           customers  avg_spend  avg_recency
segment
Champion           1     3800.0          6.0
Loyal              1     1750.0         47.0
Potential          1     1200.0         30.0
At Risk            2      450.0         26.0
```

## Done when

- Champions have the highest average spend.
- At-Risk customers have high recency (they haven't ordered recently).
- The segment summary is sorted by avg_spend descending.

**Stretch:** add a cohort retention table using the approach from ex03.

[▶ Open project playground](#play/03-mba-analytics/marketing/project.py)
