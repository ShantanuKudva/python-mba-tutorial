# Week 9 Project — Scenario Model with Tornado

## What you're building

A script that takes base assumptions (read from `sample_inputs.xlsx`) and produces:

1. A scenario table (best/base/worst).
2. A sensitivity table.
3. A tornado chart.
4. A formatted Excel report combining all three.

## Output

- **`strategy_report.xlsx`** with:
  - Sheet "Inputs" — the base assumptions (annotated).
  - Sheet "Scenarios" — best/base/worst with their input values + 5-yr revenue.
  - Sheet "Sensitivity" — input | low | high | swing | abs_swing, sorted.
- **`tornado.png`** — saved alongside.

## Required structure

```python
def revenue_model(starting_units, price, growth_rate, churn_rate, years=5) -> float: ...
def scenarios_table(base) -> pd.DataFrame: ...
def sensitivity_table(base, model, delta=0.20) -> pd.DataFrame: ...
def tornado_chart(sens_df, base_value, out_path) -> None: ...
def write_report(base, scenarios_df, sens_df, out_path) -> None: ...
```

## File to create

`03-mba-analytics/strategy/scenarios.py`

## Done when

- All three sheets present and populated.
- Tornado is sorted (largest swing at top).
- The ranking of inputs by impact is sensible (price and growth almost always dominate).
- You committed.

🛠️ Stretch: 2-way sensitivity — for the top-2 inputs, build a heatmap of revenue across a grid of values.
