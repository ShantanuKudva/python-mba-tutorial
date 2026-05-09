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

## 📚 Resources

**Official docs**
- [Time series / date functionality](https://pandas.pydata.org/docs/user_guide/timeseries.html)
- [`pandas.to_datetime`](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html)

**Deep dives**
- [Real Python — pandas time series](https://realpython.com/pandas-time-series/)

**Video tutorials**
- [YouTube — pandas datetime](https://www.youtube.com/results?search_query=pandas+datetime+time+series+tutorial)


---

Next: [`05-plotting.md`](05-plotting.md).
