# Lesson 5 — Plotting

pandas wraps matplotlib for quick charts.

## Quick line / bar from a Series

```python
import matplotlib.pyplot as plt

monthly = df.groupby(df["date"].dt.month_name())["amount"].sum()
monthly.plot(kind="bar", title="Monthly Total")
plt.tight_layout()
plt.savefig("monthly.png", dpi=150)
plt.close()
```

`savefig` writes the chart to disk. `plt.show()` opens a window (good for exploration; not for scripts).

## A few useful kinds

| `kind=` | When |
|---|---|
| `"line"` | trend over time |
| `"bar"` | category totals |
| `"barh"` | category totals, long category names |
| `"hist"` | distribution of one numeric column |
| `"scatter"` | two numerics' relationship |

## Multiple subplots in one figure

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
df_a.plot(ax=ax1, title="A")
df_b.plot(ax=ax2, title="B")
plt.tight_layout()
plt.savefig("dashboard.png", dpi=150)
plt.close()
```

That's enough for the project.

---

Done with week 5 lessons. Move to [`exercises/`](../exercises/) and [`project.md`](../project.md).

---

## 🏋️ Practice

### Easy

Group a sales DataFrame by month and plot the monthly totals as a bar chart. Save it as `monthly_bar.png` using `savefig`. Print confirmation that the file was written.

[▶ Open exercise](#play/04-data-with-pandas/week-7/exercises/ex05_chart.py)

### Medium

Create a two-panel figure: a line chart of monthly revenue on the left and a horizontal bar chart of top-5 products by revenue on the right. Use `plt.subplots(1, 2)` and `figsize=(12, 4)`. Use `savefig("dashboard.png")` to write the file, then print a confirmation message.

[▶ Open exercise](#play/04-data-with-pandas/week-7/exercises/ex05_chart.py)

### Hard

Build a four-panel dashboard figure showing: (1) monthly revenue trend, (2) revenue by region as a bar chart, (3) a histogram of order amounts, and (4) a scatter plot of order count vs. total amount per customer. Add a title to each panel and a shared `suptitle`. Use `savefig("full_dashboard.png")` and print a confirmation message when done.

[▶ Open exercise](#play/04-data-with-pandas/week-7/exercises/ex05_chart.py)

---

## 📚 Resources

**Official docs**
- [pandas plotting](https://pandas.pydata.org/docs/user_guide/visualization.html)
- [matplotlib pyplot tutorial](https://matplotlib.org/stable/tutorials/pyplot.html)

**Deep dives**
- [Real Python — matplotlib](https://realpython.com/python-matplotlib-guide/)

**Video tutorials**
- [YouTube — Corey Schafer: matplotlib](https://www.youtube.com/results?search_query=corey+schafer+matplotlib+tutorial)

