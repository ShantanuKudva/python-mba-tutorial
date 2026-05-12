"""
Exercise 4 — Composite financial health score.

Concepts: ratio analysis, weighted scoring, conditionals, formatted output.
Lesson: 05-mba-analytics/finance/lessons/01-ratios.md
Difficulty: Hard
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: take the six ratios computed in ex01 and produce a single 0–100 health
score using the heuristic below, then print the score and a verdict.

Scoring heuristic:
  +20 if current_ratio  >= 1.5  else +20 * (current_ratio  / 1.5)
  +20 if quick_ratio    >= 1.0  else +20 * (quick_ratio    / 1.0)
  +20 if de_ratio       <= 1.0  else max(0, 20 - 20 * (de_ratio - 1.0))
  +15 if gross_margin   >= 0.30 else +15 * (gross_margin   / 0.30)
  +15 if op_margin      >= 0.10 else +15 * (op_margin      / 0.10)
  +10 if net_margin     >= 0.05 else +10 * (net_margin     / 0.05)

Verdict: score >= 70 → "Healthy", 40–70 → "Stable", < 40 → "Distressed"

Expected output (approximate):
    Health score: 78 / 100 — Healthy
"""

# Setup — ratios from ex01 (computed inline here for self-containment).
pl = {
    "Revenue":          5_400,
    "Gross Profit":     2_160,
    "Operating Income": 1_000,
    "Net Income":         605,
}
bs = {
    "Current Assets":      3_200,
    "Inventory":           1_200,
    "Current Liabilities": 1_700,
    "Total Debt":          2_100,
    "Shareholders Equity": 2_900,
}

current_ratio = bs["Current Assets"] / bs["Current Liabilities"]
quick_ratio   = (bs["Current Assets"] - bs["Inventory"]) / bs["Current Liabilities"]
de_ratio      = bs["Total Debt"] / bs["Shareholders Equity"]
gross_margin  = pl["Gross Profit"]     / pl["Revenue"]
op_margin     = pl["Operating Income"] / pl["Revenue"]
net_margin    = pl["Net Income"]       / pl["Revenue"]

s_current = min(20, 20 * (current_ratio / 1.5))
s_quick   = min(20, 20 * (quick_ratio   / 1.0))
s_de      = max(0,  20 - 20 * max(0, de_ratio - 1.0))
s_gross   = min(15, 15 * (gross_margin  / 0.30))
s_op      = min(15, 15 * (op_margin     / 0.10))
s_net     = min(10, 10 * (net_margin    / 0.05))

score = round(s_current + s_quick + s_de + s_gross + s_op + s_net)

if score >= 70:
    verdict = "Healthy"
elif score >= 40:
    verdict = "Stable"
else:
    verdict = "Distressed"

print(f"Health score: {score} / 100 — {verdict}")
