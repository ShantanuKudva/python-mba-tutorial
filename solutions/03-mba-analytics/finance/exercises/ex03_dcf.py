"""
Exercise 3 — Mini discounted cash-flow (DCF) valuation.

Concepts: DCF, terminal value, Gordon Growth Model, numpy_financial.
Lesson: 03-mba-analytics/finance/lessons/02-time-value.md
Difficulty: Medium
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: compute enterprise value using a 5-year DCF model.

Free cash flows (FCFs): $100k, $120k, $140k, $160k, $180k.
Discount rate (WACC): 10%.
Terminal growth rate: 2.5%.

Steps:
  1. Discount each FCF to present value.
  2. Compute terminal value  TV = FCF_5 * (1 + g) / (wacc - g).
  3. Discount TV to present value.
  4. EV = sum of PV(FCFs) + PV(TV).

Expected output (approximate):
    Enterprise value: $2,014,543
"""

import numpy_financial as npf

# Setup — model parameters.
fcfs   = [100_000, 120_000, 140_000, 160_000, 180_000]
wacc   = 0.10
g      = 0.025   # terminal growth rate

pv_fcfs = [fcf / (1 + wacc) ** (t + 1) for t, fcf in enumerate(fcfs)]

tv = fcfs[-1] * (1 + g) / (wacc - g)

pv_tv = tv / (1 + wacc) ** len(fcfs)

ev = sum(pv_fcfs) + pv_tv
print(f"Enterprise value: ${ev:,.0f}")
