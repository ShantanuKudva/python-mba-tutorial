"""
Exercise 6 — Customer Lifetime Value and CAC ratio.

Concepts: arithmetic, conditionals, formatted output, business metrics.
Lesson: 05-mba-analytics/marketing/lessons/01-rfm.md
Difficulty: Easy
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: compute LTV, CAC, and LTV:CAC ratio for three customer segments.
A ratio >= 3 is considered healthy.

Formulas:
    LTV  = avg_revenue_per_month * gross_margin * avg_lifetime_months
    LTV:CAC = LTV / cac

Expected output:
    Segment       LTV       CAC   LTV:CAC  Verdict
    Enterprise   $18,000   $3,000    6.0x  Healthy
    Mid-Market    $7,200   $1,500    4.8x  Healthy
    SMB           $2,400     $900    2.7x  At risk
"""

# Setup — segment metrics.
segments = [
    {"name": "Enterprise", "avg_rev_per_month":  500, "gross_margin": 0.60, "lifetime_months": 60, "cac": 3_000},
    {"name": "Mid-Market", "avg_rev_per_month":  200, "gross_margin": 0.60, "lifetime_months": 60, "cac": 1_500},
    {"name": "SMB",        "avg_rev_per_month":   80, "gross_margin": 0.50, "lifetime_months": 60, "cac":   900},
]

print(f"{'Segment':<14}{'LTV':>10}{'CAC':>8}{'LTV:CAC':>10}  Verdict")

for s in segments:
    ltv     = s["avg_rev_per_month"] * s["gross_margin"] * s["lifetime_months"]
    ratio   = ltv / s["cac"]
    verdict = "Healthy" if ratio >= 3 else "At risk"
    print(f"{s['name']:<14}${ltv:>9,.0f}${s['cac']:>7,.0f}{ratio:>9.1f}x  {verdict}")
