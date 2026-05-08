# Lesson 2 — NPV, IRR, and DCF

## Why time value matters

A dollar today ≠ a dollar in five years. Discount future cash flows back to today's dollars to compare them fairly.

## NPV with `numpy-financial`

```python
import numpy_financial as npf

# Year 0 outflow (-1000), then 5 years of $300 cash flow
cashflows = [-1000, 300, 300, 300, 300, 300]
discount_rate = 0.10

print(npf.npv(discount_rate, cashflows))
```

⚠️ `npf.npv` treats the **first** cash flow as occurring at year 0 (no discount applied). Make sure the initial investment is the first element.

## IRR

```python
print(npf.irr(cashflows))   # 0.1524...  → 15.24%
```

If `npf.irr` returns `nan`, your cash flows don't cross zero (e.g., all positive) — IRR is undefined.

## DCF in pandas (mini example)

```python
import pandas as pd
import numpy_financial as npf

projections = pd.DataFrame({
    "year": [1, 2, 3, 4, 5],
    "fcf":  [120_000, 140_000, 160_000, 180_000, 200_000],
})

terminal_growth = 0.025
discount_rate = 0.10

# Terminal value at year 5 (Gordon growth)
last_fcf = projections["fcf"].iloc[-1]
terminal_value = last_fcf * (1 + terminal_growth) / (discount_rate - terminal_growth)

# Cash flow in final year includes terminal value
cashflows = projections["fcf"].tolist()
cashflows[-1] += terminal_value

# Present value (initial investment = 0 here, so prepend 0)
enterprise_value = npf.npv(discount_rate, [0] + cashflows)
print(f"Enterprise value: ${enterprise_value:,.0f}")
```

🧠 In a real DCF, the discount rate is the **WACC**, terminal growth is conservative (~GDP rate), and you sanity-check by varying both. Sensitivity is week 9's job.

---

Done with finance lessons. On to [`exercises/`](../exercises/) and [`project.md`](../project.md).
