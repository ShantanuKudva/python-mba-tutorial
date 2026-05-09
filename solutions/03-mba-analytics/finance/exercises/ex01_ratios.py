"""
Exercise 1 — Compute standard financial ratios.

Concepts: arithmetic, dicts, formatted output.
Lesson: 03-mba-analytics/finance/lessons/01-ratios.md
Difficulty: Easy
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: given the P&L and balance-sheet lookup dicts below, compute six key ratios
and print each one with the correct unit (x for multiples, % for margins).

Expected output (approximate):
    Current ratio     : 1.88x
    Quick ratio       : 1.25x
    D/E ratio         : 0.72x
    Gross margin      : 40.0%
    Operating margin  : 18.5%
    Net margin        : 11.2%
"""

# Setup — simplified P&L and balance-sheet figures (all in $000s).
pl = {
    "Revenue":           5_400,
    "COGS":              3_240,
    "Gross Profit":      2_160,
    "Operating Income":  1_000,
    "Net Income":          605,
}

bs = {
    "Current Assets":    3_200,
    "Inventory":         1_200,
    "Current Liabilities": 1_700,
    "Total Debt":        2_100,
    "Shareholders Equity": 2_900,
}

current_ratio = bs["Current Assets"] / bs["Current Liabilities"]
quick_ratio   = (bs["Current Assets"] - bs["Inventory"]) / bs["Current Liabilities"]
de_ratio      = bs["Total Debt"] / bs["Shareholders Equity"]

gross_margin  = pl["Gross Profit"]     / pl["Revenue"]
op_margin     = pl["Operating Income"] / pl["Revenue"]
net_margin    = pl["Net Income"]       / pl["Revenue"]

print(f"{'Current ratio':<20}: {current_ratio:.2f}x")
print(f"{'Quick ratio':<20}: {quick_ratio:.2f}x")
print(f"{'D/E ratio':<20}: {de_ratio:.2f}x")
print(f"{'Gross margin':<20}: {gross_margin:.1%}")
print(f"{'Operating margin':<20}: {op_margin:.1%}")
print(f"{'Net margin':<20}: {net_margin:.1%}")
