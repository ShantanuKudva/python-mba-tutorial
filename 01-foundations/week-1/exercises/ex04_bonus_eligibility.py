"""
Exercise 4 — Bonus eligibility.

Concepts: and / or / not, boolean logic.
Lesson: 01-foundations/week-1/lessons/03-conditionals.md
Difficulty: Easy
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Rules:
- Full bonus if: revenue >= target AND no compliance violations.
- Partial bonus if: revenue >= 0.9 * target AND no compliance violations.
- Otherwise: no bonus.

Expected output for the values below:
    Partial bonus

Try changing `revenue` to 100_000 (full bonus) and 70_000 (no bonus).
"""

revenue = 95_000
target = 100_000
has_violation = False

# 🛠️ Step 1: write the if / elif / else ladder using `and`/`not` on the
#    rules above. Store the result in `verdict`.

# 🛠️ Step 2: print(verdict)
