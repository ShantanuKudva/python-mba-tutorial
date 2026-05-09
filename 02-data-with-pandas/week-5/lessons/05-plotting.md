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

## 📚 Resources

**Official docs**
- [pandas plotting](https://pandas.pydata.org/docs/user_guide/visualization.html)
- [matplotlib pyplot tutorial](https://matplotlib.org/stable/tutorials/pyplot.html)

**Deep dives**
- [Real Python — matplotlib](https://realpython.com/python-matplotlib-guide/)

**Video tutorials**
- [YouTube — Corey Schafer: matplotlib](https://www.youtube.com/results?search_query=corey+schafer+matplotlib+tutorial)

