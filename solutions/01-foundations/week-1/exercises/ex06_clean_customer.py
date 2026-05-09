"""
Exercise 6 — Clean a messy customer name.

Concepts: string methods (.strip, .title, .replace).
Lesson: lessons/04-strings.md
Difficulty: Easy
📚 References: open the lesson above and see its 📚 Resources section at the bottom (official docs, deep dives, video tutorials). Global index in ROADMAP.md.

Goal: take a raw customer name like "  ACME industries, LLC.  " and
produce a clean, presentable version.

Expected output for raw = "  ACME industries, LLC.  ":
    Acme Industries, Llc

Expected output for raw = "globex CORP. ":
    Globex Corp
"""

raw = "  ACME industries, LLC.  "

clean = raw.strip()
clean = clean.replace(".", "")
clean = clean.title()

print(clean)
