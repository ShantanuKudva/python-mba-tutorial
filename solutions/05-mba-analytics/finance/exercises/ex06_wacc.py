"""
Exercise 6 — Weighted Average Cost of Capital (WACC).

Concepts: weighted average, percentage formatting, capital structure.
Lesson: 05-mba-analytics/finance/lessons/02-time-value.md
Difficulty: Medium
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: compute the WACC for a company using its capital structure below.

Formula:
    WACC = (E/V) * Re + (D/V) * Rd * (1 - tax_rate)
    where:
        E   = market value of equity
        D   = market value of debt
        V   = E + D
        Re  = cost of equity
        Rd  = pre-tax cost of debt
        tax_rate = corporate tax rate

Expected output:
    Equity weight  : 60.0%
    Debt weight    : 40.0%
    WACC           : 10.20%
"""

# Setup — capital structure inputs.
equity_value  = 600_000_000   # $600M market cap
debt_value    = 400_000_000   # $400M total debt
cost_of_equity = 0.14         # 14% required return on equity (CAPM or similar)
cost_of_debt   = 0.06         # 6% pre-tax cost of debt
tax_rate       = 0.25         # 25% corporate tax

V   = equity_value + debt_value
w_e = equity_value / V
w_d = debt_value   / V

wacc = w_e * cost_of_equity + w_d * cost_of_debt * (1 - tax_rate)

print(f"{'Equity weight':<16}: {w_e:.1%}")
print(f"{'Debt weight':<16}: {w_d:.1%}")
print(f"{'WACC':<16}: {wacc:.2%}")
