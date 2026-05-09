# Lesson 1 — Scenario Modeling

## A simple 5-year revenue model

```python
def revenue_5y(starting_units, price, growth_rate, churn_rate):
    units = starting_units
    total = 0
    for year in range(5):
        units = units * (1 + growth_rate) * (1 - churn_rate)
        total += units * price
    return total
```

Realistic enough for a teaching example — you'll add complexity later.

## Define scenarios as dicts

```python
base = dict(starting_units=10_000, price=240, growth_rate=0.20, churn_rate=0.10)

scenarios = {
    "best":  {**base, "growth_rate": 0.30, "churn_rate": 0.06},
    "base":  base,
    "worst": {**base, "growth_rate": 0.10, "churn_rate": 0.18},
}

for name, inputs in scenarios.items():
    print(f"{name:6} → ${revenue_5y(**inputs):,.0f}")
```

The `**inputs` syntax unpacks a dict into keyword arguments. Memorize it — it's incredibly useful.

## Output as a DataFrame for Excel

```python
import pandas as pd

rows = []
for name, inputs in scenarios.items():
    rows.append({"scenario": name, **inputs, "revenue_5y": revenue_5y(**inputs)})

df = pd.DataFrame(rows)
df.to_excel("scenarios.xlsx", index=False)
```

---

## 📚 Resources

**Official docs**
- [Investopedia — scenario analysis](https://www.investopedia.com/terms/s/scenario_analysis.asp)

**Deep dives**
- [CFI — scenario analysis](https://corporatefinanceinstitute.com/resources/financial-modeling/scenario-analysis/)

**Video tutorials**
- [YouTube — scenario analysis modeling](https://www.youtube.com/results?search_query=scenario+analysis+financial+modeling)


---

Next: [`02-sensitivity.md`](02-sensitivity.md).
