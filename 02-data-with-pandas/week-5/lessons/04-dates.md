# Lesson 4 — Dates and Resampling

## Parse dates

```python
df["date"] = pd.to_datetime(df["date"])
```

This converts a column of date *strings* into real datetime objects. Now you can:

```python
df["date"].dt.year
df["date"].dt.month
df["date"].dt.quarter
df["date"].dt.day_name()
```

## Set as index for time-series ops

```python
df = df.set_index("date").sort_index()
```

## Resample (daily → monthly, monthly → quarterly, etc.)

```python
monthly = df["amount"].resample("ME").sum()      # month-end
quarterly = df["amount"].resample("QE").sum()
yearly = df["amount"].resample("YE").sum()
```

Common frequency strings: `"D"` daily, `"W"` weekly, `"ME"` month-end, `"QE"` quarter-end, `"YE"` year-end.

## Filter by date

```python
df["2026-01":"2026-03"]                 # Q1 2026 (when date is the index)
df[df["date"] >= "2026-01-01"]          # column form
```

---

Next: [`05-plotting.md`](05-plotting.md).
