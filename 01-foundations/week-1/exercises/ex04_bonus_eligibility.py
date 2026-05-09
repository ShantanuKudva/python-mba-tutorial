"""
Exercise 4 — Bonus eligibility.

Concepts: and / or / not, booleans.
Lesson: lessons/03-conditionals.md
📚 References: open the lesson above and see its 📚 Resources section at the bottom (official docs, deep dives, video tutorials). Global index in ROADMAP.md.

Rules:
- Eligible for full bonus if: revenue >= target AND no compliance violations.
- Eligible for partial bonus if: revenue >= 0.9 * target AND no compliance violations.
- Otherwise: no bonus.

Test all three branches.
"""

revenue = 95_000
target = 100_000
has_violation = False

# 🛠️ Compute eligibility and print one of:
#     "Full bonus"
#     "Partial bonus"
#     "No bonus"
