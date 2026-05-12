"""
Exercise 2 — NPV and IRR decision.

Concepts: numpy_financial, npv, irr, investment accept/reject rule.
Lesson: 05-mba-analytics/finance/lessons/02-time-value.md
Difficulty: Easy
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: evaluate a capital project using NPV and IRR.
Project: invest $500 000 upfront, receive $130 000/yr for 5 years, discount rate 8%.

Accept if NPV > 0 (or equivalently IRR > discount rate).

Expected output:
    NPV     : $19,477.01
    IRR     : 9.43%
    Verdict : Accept
"""

import numpy_financial as npf

# Setup — cash-flow assumptions.
initial_investment = 500_000
annual_inflow      = 130_000
years              = 5
discount_rate      = 0.08

# 🛠️ Step 1: build the cash-flows list (negative first, then positives).
#    cashflows = [-initial_investment] + [annual_inflow] * years

# 🛠️ Step 2: compute NPV and IRR.
#    npv_value = npf.npv(discount_rate, cashflows)
#    irr_value = npf.irr(cashflows)

# 🛠️ Step 3: determine verdict.
#    verdict = "Accept" if npv_value > 0 else "Reject"

# 🛠️ Step 4: print the three lines.
#    print(f"NPV     : ${npv_value:,.2f}")
#    print(f"IRR     : {irr_value:.2%}")
#    print(f"Verdict : {verdict}")
