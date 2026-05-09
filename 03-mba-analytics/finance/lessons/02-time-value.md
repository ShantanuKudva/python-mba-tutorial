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

---

## 🏋️ Practice

### Easy

Given a list of cash flows `[-1000, 300, 300, 300, 300, 300]` and a discount rate of 10%, compute and print the NPV and IRR using `numpy_financial`. Interpret: is this a good investment?

[▶ Open exercise](#play/03-mba-analytics/finance/exercises/ex02_npv.py)

### Medium

Build a 5-year DCF model from scratch using a pandas DataFrame of projected free cash flows. Use a 10% discount rate and a 2.5% terminal growth rate. Compute the enterprise value and print a year-by-year table showing FCF, discount factor, and present value.

[▶ Open exercise](#play/03-mba-analytics/finance/exercises/ex03_dcf.py)

### Hard

Create a DCF sensitivity table that varies the discount rate (8%, 10%, 12%) and terminal growth rate (1.5%, 2.5%, 3.5%) in a 3×3 grid. Each cell should show the resulting enterprise value. Print the table with rows as discount rates and columns as terminal growth rates. Highlight the base-case cell.

[▶ Open exercise](#play/03-mba-analytics/finance/exercises/ex03_dcf.py)

---

## 📚 Resources

**Official docs**
- [`numpy_financial` docs](https://numpy.org/numpy-financial/latest/)
- [Investopedia — time value of money](https://www.investopedia.com/terms/t/timevalueofmoney.asp)
- [Investopedia — NPV](https://www.investopedia.com/terms/n/npv.asp)

**Deep dives**
- [CFI — NPV vs IRR](https://corporatefinanceinstitute.com/resources/financial-modeling/npv-vs-irr/)

**Video tutorials**
- [YouTube — NPV & IRR explained](https://www.youtube.com/results?search_query=npv+irr+time+value+of+money+explained)

