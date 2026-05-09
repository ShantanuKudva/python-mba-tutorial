"""
Exercise 2 — Score and segment RFM customers.

Concepts: pd.qcut, string concatenation, apply, segment labelling.
Lesson: 03-mba-analytics/marketing/lessons/01-rfm.md
Difficulty: Medium
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: starting from the rfm table built in ex01, add R/F/M quintile columns
(1–5), concatenate them into an "rfm_string" (e.g. "543"), map that to a
segment label ("Champion", "Loyal", "At Risk", etc.), then print:
  - segment counts
  - average spend per segment, sorted descending

Expected output (approximate):
    segment
    Champion    X
    Loyal       X
    At Risk     X
    ...
"""

import pandas as pd

# Setup — small synthetic RFM table (replaces the dataset read from disk).
rfm = pd.DataFrame({
    "customer_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "recency":     [  5, 120,  10,  90,   3, 200,  15,  60,   7,  45],  # days
    "frequency":   [  8,   1,   6,   2,  10,   1,   5,   3,   9,   4],
    "monetary":    [2400, 150, 1800, 300, 3000,  80, 1200, 500, 2700, 900],
})

# 🛠️ Step 1: add R_score (recency — lower days = higher score, so reverse=True).
#    rfm["R_score"] = pd.qcut(rfm["recency"], q=3, labels=[3, 2, 1]).astype(int)
#    (Use q=3 because our sample is small; use q=5 on a real dataset.)

# 🛠️ Step 2: add F_score and M_score (higher = better, so no reversal).
#    rfm["F_score"] = pd.qcut(rfm["frequency"], q=3, labels=[1, 2, 3]).astype(int)
#    rfm["M_score"] = pd.qcut(rfm["monetary"],  q=3, labels=[1, 2, 3]).astype(int)

# 🛠️ Step 3: build rfm_string by concatenating the three scores as strings.
#    rfm["rfm_string"] = rfm["R_score"].astype(str) + rfm["F_score"].astype(str) + rfm["M_score"].astype(str)

# 🛠️ Step 4: define a simple labeller and apply it.
#    def label(row):
#        r, f = row["R_score"], row["F_score"]
#        if r == 3 and f == 3:   return "Champion"
#        if r == 3:               return "Loyal"
#        if r == 1:               return "At Risk"
#        return "Potential"
#    rfm["segment"] = rfm.apply(label, axis=1)

# 🛠️ Step 5: print segment counts and average monetary per segment.
#    print(rfm.groupby("segment")["monetary"].agg(["count", "mean"]).sort_values("mean", ascending=False))
