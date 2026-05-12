# Exercises — Week 9 · Marketing Analytics

> Practice problems for the lessons in this module. Each exercise opens directly in the browser playground — fill in the steps and click ▶ Run.

## 📚 Read first

Skim these before attempting the harder exercises:
- [Lesson 01 — RFM Analysis](../lessons/01-rfm.md)
- [Lesson 02 — Cohort Analysis](../lessons/02-cohorts.md)
- [Lesson 03 — A/B Testing](../lessons/03-ab-test.md)
- [Klaviyo — RFM Guide](https://www.klaviyo.com/blog/rfm-analysis)
- [scipy.stats docs](https://docs.scipy.org/doc/scipy/reference/stats.html)

## 🟢 Easy

- [ex01 — Compute raw RFM metrics](#play/05-mba-analytics/marketing/exercises/ex01_rfm_compute.py) — groupby, agg, recency / frequency / monetary.
- [ex05 — Monthly churn rate](#play/05-mba-analytics/marketing/exercises/ex05_churn_rate.py) — churn formula, formatted table.
- [ex06 — LTV and CAC ratio](#play/05-mba-analytics/marketing/exercises/ex06_ltv_cac.py) — LTV formula, LTV:CAC classification.

## 🟡 Medium

- [ex02 — RFM scoring and segments](#play/05-mba-analytics/marketing/exercises/ex02_rfm_score.py) — `pd.qcut`, segment labelling, groupby summary.
- [ex04 — A/B test (t-test)](#play/05-mba-analytics/marketing/exercises/ex04_ab_test.py) — `scipy.stats.ttest_ind`, p-value, significance verdict.

## 🔴 Hard

- [ex03 — Monthly cohort retention](#play/05-mba-analytics/marketing/exercises/ex03_cohort.py) — cohort acquisition period, period_index, retention matrix, `unstack`, `div`.
