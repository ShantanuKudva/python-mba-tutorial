"""
Exercise 8 — Count occurrences of each region.

Concepts: dicts as counters, .get() with default, looping.
Lesson: lessons/02-dicts.md
Difficulty: Hard
📚 References: open the lesson above and see its 📚 Resources section at the bottom (official docs, deep dives, video tutorials). Global index in ROADMAP.md.

Goal: given a list of region tags, build a dict of {region: count}
and print each region's share, sorted from highest to lowest.

Expected output:
    North : 4 (40.0%)
    South : 3 (30.0%)
    East  : 2 (20.0%)
    West  : 1 (10.0%)
"""

regions = ["North", "South", "East", "North", "South",
           "North", "West", "East", "North", "South"]

# 🛠️ Step 1: build counts dict using a for loop.
#    Tip: counts[r] = counts.get(r, 0) + 1

# 🛠️ Step 2: total = sum(counts.values())

# 🛠️ Step 3: sort items by value (descending).
#    sorted(counts.items(), key=lambda kv: kv[1], reverse=True)

# 🛠️ Step 4: loop and print each line:
#    f"{region:<6}: {n} ({n/total:.1%})"
