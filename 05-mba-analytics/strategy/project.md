# Week 11 Project — Scenario Model with Tornado Chart

## What you're building

A script that takes base assumptions and produces: a scenario table, a sensitivity table, and a tornado chart.

## Required functions

```python
def revenue_model(starting_units, price, growth_rate, churn_rate, years=5) -> float: ...
def scenarios_table(base) -> pd.DataFrame: ...
def sensitivity_table(base, delta=0.20) -> pd.DataFrame: ...
```

Plus code that draws a horizontal tornado chart.

## Expected output

```
=== SCENARIO TABLE ===
best   → $17,890,000  (+41% vs base)
base   → $12,675,000
worst  →  $7,902,000  (-38% vs base)

=== SENSITIVITY TABLE ===
         input         low        high       swing   abs_swing
           price   7,200,000  18,900,000  11,700,000  11,700,000
    growth_rate    8,100,000  17,000,000   8,900,000   8,900,000
     churn_rate   10,100,000  15,300,000   5,200,000   5,200,000
  starting_units  10,200,000  15,200,000   5,000,000   5,000,000

(A horizontal tornado chart in the output area)
```

## Done when

- The scenario table is sorted best → base → worst.
- The sensitivity table is sorted by abs_swing descending.
- The tornado chart is horizontal (barh) with the largest-swing input at the top.
- The ranking (price > growth_rate > churn_rate) is sensible.

**Stretch:** build a 2-way sensitivity heatmap for the top-2 inputs using a grid of values.

[▶ Open project playground](#play/05-mba-analytics/strategy/project.py)
