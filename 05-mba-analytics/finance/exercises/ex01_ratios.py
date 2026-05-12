"""
Exercise 1 — Compute standard financial ratios.

Concepts: arithmetic, dicts, formatted output.
Lesson: 05-mba-analytics/finance/lessons/01-ratios.md
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

# 🛠️ Step 1: compute the three liquidity / leverage ratios.
#    current_ratio = bs["Current Assets"] / bs["Current Liabilities"]
#    quick_ratio   = (bs["Current Assets"] - bs["Inventory"]) / bs["Current Liabilities"]
#    de_ratio      = bs["Total Debt"] / bs["Shareholders Equity"]

# 🛠️ Step 2: compute the three margin ratios (as decimals, e.g. 0.40 for 40%).
#    gross_margin  = pl["Gross Profit"]     / pl["Revenue"]
#    op_margin     = pl["Operating Income"] / pl["Revenue"]
#    net_margin    = pl["Net Income"]       / pl["Revenue"]

# 🛠️ Step 3: print all six ratios with aligned labels.
#    Use   f"{'Current ratio':<20}: {current_ratio:.2f}x"
#    Use   f"{'Gross margin':<20}: {gross_margin:.1%}"
