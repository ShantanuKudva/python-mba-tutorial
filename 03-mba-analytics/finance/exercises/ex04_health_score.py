"""
Exercise 4 — Composite health score.

Take the 6 ratios from ex01 and turn them into a single 0–100 health score.

Suggested heuristic (tweak as you like, but document your choice):

  +20 if current ratio >= 1.5      else proportional
  +20 if quick ratio   >= 1.0      else proportional
  +20 if D/E           <= 1.0      (lower is better; cap at 0)
  +15 if gross margin  >= 30%      else proportional
  +15 if operating margin >= 10%   else proportional
  +10 if net margin    >= 5%       else proportional

Print the final score and a one-line verdict
(Strong / Stable / Watch / At Risk).
"""

# 🛠️ Implement scoring + verdict.
