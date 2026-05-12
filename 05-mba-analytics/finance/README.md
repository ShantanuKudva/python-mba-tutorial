# Week 8 — Finance

**Goal:** read a P&L + balance sheet, compute the standard set of financial ratios, and produce a one-page health report.

## Concepts (read first)

- **Liquidity ratios** — current ratio, quick ratio. Can the company pay short-term bills? — [CFI guide](https://corporatefinanceinstitute.com/resources/accounting/liquidity-ratio/)
- **Leverage ratios** — debt-to-equity, debt-to-assets. How much is borrowed money? — [CFI guide](https://corporatefinanceinstitute.com/resources/accounting/leverage-ratios/)
- **Profitability ratios** — gross margin, operating margin, net margin, ROE, ROA. — [CFI guide](https://corporatefinanceinstitute.com/resources/accounting/profitability-ratios/)
- **NPV / IRR** — time value of money for cash-flow projects. — [`numpy_financial`](https://numpy.org/numpy-financial/)
- **DCF** — value a company by its discounted future cash flows. — [CFI free guide](https://corporatefinanceinstitute.com/resources/financial-modeling/dcf-model-training-free-guide/)

## What you'll build

Functions you'll keep reusing:

```python
def current_ratio(balance_sheet) -> float: ...
def quick_ratio(balance_sheet) -> float: ...
def debt_to_equity(balance_sheet) -> float: ...
def gross_margin(pl) -> float: ...
def net_margin(pl) -> float: ...
def npv(rate, cashflows) -> float: ...
def irr(cashflows) -> float: ...
```

## Map

| File | Topic |
|---|---|
| [`lessons/01-ratios.md`](lessons/01-ratios.md) | Computing the ratio set |
| [`lessons/02-time-value.md`](lessons/02-time-value.md) | NPV, IRR, DCF |
| [`exercises/`](exercises/) | 4 problems |
| [`project.md`](project.md) | 1-page health report |

## Dataset

`datasets/finance/sample_pl.xlsx` and `datasets/finance/sample_balance_sheet.xlsx`. Generate via [`datasets/generate_samples.py`](../../datasets/generate_samples.py).

## Done when

- All ratio functions in `health.py` produce correct numbers on the sample data.
- `health_report.xlsx` opens with a formatted summary sheet.
- You committed.
