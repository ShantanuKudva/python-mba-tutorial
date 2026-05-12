# Lesson 5 — Charts: Bar, Line, Pie Basics

## Why this matters

A 6x3 revenue table is hard to read at a glance. A bar chart of the same data communicates the story in three seconds. This lesson covers when to use which chart type and how to think about the visual communication of data — skills that apply whether you're building a slide deck for your board or a dashboard in Tableau.

## Chart types and when to use them

| Chart type | Use when | Example |
|---|---|---|
| **Bar / Column** | Comparing discrete categories | Revenue by product, headcount by department |
| **Line** | Showing change over time | Monthly revenue trend, stock price |
| **Pie / Donut** | Showing parts of a whole (≤5 slices) | Market share, budget allocation |
| **Scatter** | Showing relationship between two numeric variables | Price vs. units sold, ad spend vs. conversion |
| **Stacked bar** | Categories that add to a total, compared across groups | Revenue by region, stacked by product |

## The preloaded sheet (Q1 Sales)

The Q1 data below has everything needed for a bar chart and a mix of chart thinking exercises.

```sheet
src: 02-excel/datasets/sales.xlsx.json
sheet: Q1
height: 340
```

## Charting with x-spreadsheet (in-browser limits)

The in-browser spreadsheet (x-spreadsheet) does not have a native chart rendering GUI — that's a limitation of the lightweight library. Instead, this lesson teaches the **chart thinking** and formula-building that feeds any chart tool (Excel desktop, Google Sheets, Tableau, or matplotlib in the next phase).

### What you would do in Excel desktop

1. Select your data range (e.g. A1:A7 and F1:F7 for product names + Q1 totals).
2. Insert → Chart → Bar/Column.
3. Choose "Clustered bar" for side-by-side comparisons.
4. Add axis labels, a title, and a data label on the highest bar.

### What to practice here

Use the embedded sheet above to prepare the chart data correctly — clean labels, a single summary metric per row, no merged cells, no blank rows inside the range. That preparation is 80% of the charting work.

---

## Chart data preparation tasks

```sheet
src: 02-excel/datasets/sales.xlsx.json
sheet: Q1
```

Good charts require clean, well-structured source data. Work in the sheet above:

1. **Product totals column (F):** Confirm F2:F7 shows Q1 Total for each product (Widget through Plugin). These will be your bar heights.

2. **Build a chart-ready summary table** starting in cell A12:

   ```
   A12: Product     B12: Q1 Total     C12: Share of Total
   A13: Widget      B13: =F2          C13: =F2/$F$8
   A14: Gadget      B14: =F3          C14: =F3/$F$8
   ... (repeat for all 6 products)
   ```

   The `$F$8` absolute reference locks to the grand total. As you copy C13 down, it stays anchored to row 8.

3. **Format the Share column:** The values in C13:C18 will be decimals (e.g. 0.23). In real Excel you'd format as Percentage. Here, wrap each in `=ROUND(F2/$F$8*100, 1)` to show e.g. `23.4` (meaning 23.4%).

4. **Sense-check:** Add `=SUM(C13:C18)` in C19. If you used the raw decimal version, it should sum to `1.0`. If you used the ×100 version, it should sum to `100`.

---

## Chart design principles

### Bar chart — ranking categories

- Sort bars **from longest to shortest** (or shortest to longest) unless there's a natural order (months, quarters).
- Keep the y-axis starting at zero. Truncated axes exaggerate differences.
- One color per series is enough. Use a different color only for a highlighted bar.
- Label the axes. Don't make readers guess what the numbers represent.

### Line chart — time series

- X-axis should always be time, evenly spaced.
- Don't connect a line over missing data — break the line or interpolate explicitly.
- More than 4–5 lines on one chart is usually too many; consider small multiples instead.

### Pie chart — use sparingly

- Works only for parts of a whole that add to 100%.
- Humans are bad at comparing angles; a bar chart is almost always clearer.
- Never use 3D pies. They distort the perception of area.

---

## Try it

Using the chart-ready table you built above (A12:C18), mentally sketch what a bar chart of Q1 Total by Product would look like. Which product is the tallest bar? Which is shortest? What percentage of total revenue does the top product represent?

Then answer: if you needed to show how revenue changed from Q1 to Q2 for the same products, which chart type would you use and why?

---

## Connecting to Python

In Phase 4 (pandas), you'll generate these charts programmatically:

```python
import matplotlib.pyplot as plt
import pandas as pd

products = ['Widget','Gadget','License','Service','Cable','Plugin']
q1 = [37300, 26600, 143000, 69500, 10500, 58500]

pd.Series(q1, index=products).sort_values(ascending=False).plot(
    kind='bar', title='Q1 Revenue by Product', ylabel='Revenue ($)'
)
plt.tight_layout()
```

The data you organized in this lesson maps directly to the DataFrame. The charting logic is identical — only the rendering layer changes.

---

Next: [Lesson 6 — When Excel Breaks](06-when-excel-breaks.md)

---

## Resources

- [Storytelling with Data — chart type selection](https://www.storytellingwithdata.com/chart-guide)
- [Financial Modeling World Cup — Excel charting best practices](https://www.fmworldcup.com/)
- [matplotlib gallery](https://matplotlib.org/stable/gallery/index.html) — preview what Python charting looks like
