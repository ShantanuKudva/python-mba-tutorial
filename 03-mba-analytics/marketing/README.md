# Week 7 — Marketing/Sales

**Goal:** segment customers by behavior and quantify which segments matter most.

## Concepts (read first)

- **Cohort analysis** — group customers by signup month, track behavior over time. — [Mode tutorial](https://mode.com/blog/cohort-analysis-tutorial)
- **Funnel conversion** — measure drop-off between stages. — [Amplitude guide](https://amplitude.com/explore/analytics/funnel-analysis-guide)
- **RFM segmentation** — Recency, Frequency, Monetary. The classic CRM segmentation. — [Optimove primer](https://www.optimove.com/resources/learning-center/rfm-segmentation), [Kaggle walkthrough](https://www.kaggle.com/code/regivm/rfm-analysis-tutorial)
- **A/B testing** — t-test for "is variant B actually better?" — [`scipy.stats.ttest_ind`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html), [StatQuest video](https://www.youtube.com/watch?v=pTmLQvMM-1M)

## What you'll build

```python
def rfm(orders, ref_date) -> pd.DataFrame: ...
def rfm_score(rfm_df, bins=5) -> pd.DataFrame: ...
def segment_label(score_row) -> str:    # Champions / Loyal / At Risk / Lost / etc.
def cohort_retention(orders) -> pd.DataFrame: ...
def ab_test(group_a, group_b) -> dict:  # mean_a, mean_b, p_value, significant
```

## Map

| File | Topic |
|---|---|
| [`lessons/01-rfm.md`](lessons/01-rfm.md) | Building RFM scores |
| [`lessons/02-cohorts.md`](lessons/02-cohorts.md) | Monthly cohort retention table |
| [`lessons/03-ab-test.md`](lessons/03-ab-test.md) | t-test for conversion lift |
| [`exercises/`](exercises/) | 4 problems |
| [`project.md`](project.md) | Customer-segmentation Excel |

## Dataset

`datasets/marketing/sample_orders.xlsx` (sheets: `orders`, `customers`).

## Done when

- `segments.xlsx` exists with one row per customer including their segment.
- Counts per segment match what you'd expect by inspection (e.g., Champions are top spenders).
- You committed.
