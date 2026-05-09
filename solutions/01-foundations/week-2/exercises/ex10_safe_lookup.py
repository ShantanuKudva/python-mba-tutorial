"""
Exercise 10 — Safe lookup with negative indexing and IndexError.

Concepts: negative indexing, len(), try/except IndexError.
Lesson: lessons/01-lists-and-loops.md
Difficulty: Medium
📚 References: open the lesson above and see its 📚 Resources section at the bottom (official docs, deep dives, video tutorials). Global index in ROADMAP.md.

Goal: given a list of monthly revenue, report:
   - latest month   (last element via negative index)
   - prior month    (second-to-last via negative index)
   - month #N       (1-indexed, asked by the user) — but never crash.

Expected output for the data below:
    Latest month : $14,500
    Prior month  : $13,200
    Month 3      : $11,000
    Month 99     : (out of range — only 6 months on file)
"""

revenue = [9_800, 10_500, 11_000, 12_400, 13_200, 14_500]

requested_months = [3, 99]   # user asks for these (1-indexed)

print(f"Latest month : ${revenue[-1]:,}")
print(f"Prior month  : ${revenue[-2]:,}")

for n in requested_months:
    try:
        print(f"Month {n}      : ${revenue[n - 1]:,}")
    except IndexError:
        print(f"Month {n}      : (out of range — only {len(revenue)} months on file)")

# revenue[len(revenue)] raises IndexError because valid indices are 0..len-1;
# revenue[-1] does not because Python wraps negative indices from the end.
