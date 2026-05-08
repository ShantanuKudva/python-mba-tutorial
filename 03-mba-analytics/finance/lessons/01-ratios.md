# Lesson 1 — Financial Ratios in pandas

## The shape of the data

A P&L workbook usually has rows like:

| line_item | amount |
|---|---|
| Revenue | 5,000,000 |
| COGS | 3,000,000 |
| Gross Profit | 2,000,000 |
| Operating Expenses | 1,200,000 |
| Operating Income | 800,000 |
| Interest Expense | 50,000 |
| Tax | 200,000 |
| Net Income | 550,000 |

A balance sheet:

| line_item | amount |
|---|---|
| Cash | 400,000 |
| Receivables | 600,000 |
| Inventory | 500,000 |
| Total Current Assets | 1,500,000 |
| Total Assets | 5,000,000 |
| Current Liabilities | 800,000 |
| Total Liabilities | 2,500,000 |
| Total Equity | 2,500,000 |

## Read into a dict for easy lookup

```python
import pandas as pd

def to_lookup(df: pd.DataFrame) -> dict:
    return dict(zip(df["line_item"].str.strip(), df["amount"]))

pl = to_lookup(pd.read_excel("datasets/finance/sample_pl.xlsx"))
bs = to_lookup(pd.read_excel("datasets/finance/sample_balance_sheet.xlsx"))

print(pl["Revenue"])             # 5000000
print(bs["Total Assets"])        # 5000000
```

## Liquidity

```python
def current_ratio(bs):
    return bs["Total Current Assets"] / bs["Current Liabilities"]

def quick_ratio(bs):
    quick_assets = bs["Cash"] + bs["Receivables"]
    return quick_assets / bs["Current Liabilities"]
```

Healthy current ratio is typically 1.5–3.0 depending on industry.

## Leverage

```python
def debt_to_equity(bs):
    return bs["Total Liabilities"] / bs["Total Equity"]

def debt_to_assets(bs):
    return bs["Total Liabilities"] / bs["Total Assets"]
```

## Profitability

```python
def gross_margin(pl):
    return (pl["Revenue"] - pl["COGS"]) / pl["Revenue"]

def operating_margin(pl):
    return pl["Operating Income"] / pl["Revenue"]

def net_margin(pl):
    return pl["Net Income"] / pl["Revenue"]
```

## Display nicely

```python
def pct(x): return f"{x*100:.1f}%"
def x(v):   return f"{v:.2f}x"

print(f"Current ratio:    {x(current_ratio(bs))}")
print(f"Debt/Equity:      {x(debt_to_equity(bs))}")
print(f"Gross margin:     {pct(gross_margin(pl))}")
print(f"Net margin:       {pct(net_margin(pl))}")
```

---

Next: [`02-time-value.md`](02-time-value.md).
