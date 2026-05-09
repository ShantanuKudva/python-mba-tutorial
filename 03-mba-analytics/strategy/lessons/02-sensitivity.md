# Lesson 2 — Sensitivity Analysis + Tornado Chart

## One-at-a-time sensitivity

For each input, vary it by ±20% from base, recompute the output, and record the change.

```python
def sensitivity(base, model, delta=0.20):
    base_value = model(**base)
    rows = []
    for key, value in base.items():
        low = {**base, key: value * (1 - delta)}
        high = {**base, key: value * (1 + delta)}
        rows.append({
            "input":   key,
            "low":     model(**low),
            "high":    model(**high),
            "swing":   model(**high) - model(**low),
        })
    sens = pd.DataFrame(rows)
    sens["abs_swing"] = sens["swing"].abs()
    return sens.sort_values("abs_swing", ascending=False).reset_index(drop=True)
```

The bigger the `swing`, the more your output depends on that input.

## Tornado chart

```python
import matplotlib.pyplot as plt

def tornado_chart(sens, base_value, out_path):
    fig, ax = plt.subplots(figsize=(8, 4))
    inputs = sens["input"]
    ax.barh(inputs, sens["high"] - base_value, left=base_value, color="#0969da")
    ax.barh(inputs, sens["low"]  - base_value, left=base_value, color="#cf222e")
    ax.axvline(base_value, color="black", linewidth=1)
    ax.invert_yaxis()    # largest swing on top
    ax.set_xlabel("5-year revenue ($)")
    ax.set_title("Sensitivity tornado")
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.close()
```

🧠 Reading a tornado: the longest bar at the top is the input that swings the answer most. That's where to focus management attention. Inputs at the bottom barely matter.

---

Done with strategy lessons. Move to [`exercises/`](../exercises/) and [`project.md`](../project.md).

---

## 📚 Resources

**Official docs**
- [Investopedia — sensitivity analysis](https://www.investopedia.com/terms/s/sensitivityanalysis.asp)
- [matplotlib — barh (tornado)](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.barh.html)

**Deep dives**
- [CFI — sensitivity analysis & tornado charts](https://corporatefinanceinstitute.com/resources/financial-modeling/sensitivity-analysis/)

**Video tutorials**
- [YouTube — tornado chart tutorial](https://www.youtube.com/results?search_query=tornado+chart+sensitivity+analysis+tutorial)

