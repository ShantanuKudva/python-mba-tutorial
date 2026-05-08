# Week 9 — Strategy / Consulting

**Goal:** turn a set of input assumptions into a scenario model and a tornado chart.

## Concepts (read first)

- **KPIs** — what to measure, what to ignore. — [KPI.org basics](https://kpi.org/KPI-Basics)
- **Market sizing** — TAM, SAM, SOM. — [CFI guide](https://corporatefinanceinstitute.com/resources/management/total-addressable-market-tam/)
- **Sensitivity analysis** — vary one input, see what changes. — [CFI](https://corporatefinanceinstitute.com/resources/financial-modeling/what-is-sensitivity-analysis/)
- **Scenario analysis** — vary multiple inputs together (best/base/worst). — [CFI](https://corporatefinanceinstitute.com/resources/financial-modeling/scenario-analysis/)
- **Tornado chart** — visualize sensitivity, sorted by magnitude. — [matplotlib horizontal bar example](https://matplotlib.org/stable/gallery/lines_bars_and_markers/horizontal_barchart_distribution.html)

## What you'll build

```python
def revenue_model(price, units, churn_rate, growth_rate, years=5) -> float: ...
def scenarios(base_inputs) -> pd.DataFrame:    # rows = best/base/worst
def sensitivity(base_inputs, deltas) -> pd.DataFrame:    # for tornado
def tornado_chart(sens_df, out_path) -> None: ...
```

## Map

| File | Topic |
|---|---|
| [`lessons/01-scenarios.md`](lessons/01-scenarios.md) | Best/base/worst scenarios |
| [`lessons/02-sensitivity.md`](lessons/02-sensitivity.md) | One-at-a-time sensitivity + tornado |
| [`exercises/`](exercises/) | 3 problems |
| [`project.md`](project.md) | Scenario model + tornado |

## Dataset

`datasets/strategy/sample_inputs.xlsx` — base assumptions for a fictional SaaS business.
