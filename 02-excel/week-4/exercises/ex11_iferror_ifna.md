# Exercise 11 — IFERROR & IFNA: Defensive Formulas 🟢

**Scenario:** You have a Q1 sales sheet and a customer lookup table. Some lookups will fail because not every product or customer ID exists in the reference list. Without error-handling, `#N/A` and `#DIV/0!` errors break aggregations and look unprofessional in reports. Your job is to wrap formulas so they degrade gracefully.

## The sheet

```sheet
src: 02-excel/datasets/sales.xlsx.json
sheet: Q1
height: 340
```

## Tasks

**Task 1 — Safe average (avoid #DIV/0!):**  
In a blank cell, type `=C2/0`. You'll see `#DIV/0!`. Wrap this in IFERROR so it returns `0` instead:
```
=IFERROR(C2/0, 0)
```

Now try dividing by a blank cell: `=IFERROR(C2/G2, "no data")` — it should show "no data".

**Task 2 — Safe VLOOKUP with IFNA:**  
Write a VLOOKUP that looks for a product called "Fridge" (which doesn't exist in column B):
```
=VLOOKUP("Fridge", B2:F7, 5, 0)
```
It returns `#N/A`. Wrap it with IFNA to show a dash instead:
```
=IFNA(VLOOKUP("Fridge", B2:F7, 5, 0), "—")
```

**Task 3 — Chain IFERROR with a fallback formula:**  
A common pattern: try the precise lookup first; if it fails, try a broader one; if that also fails, show a message. In a blank cell:
```
=IFERROR(VLOOKUP("Widget", B2:F7, 2, 0), IFERROR(VLOOKUP("widget", B2:F7, 2, 0), "Not found"))
```
The first lookup succeeds and returns January revenue for Widget.

**Task 4 — Distinguish IFERROR from IFNA:**  
In a blank cell, write `=IFERROR(1/0, "caught")`. It shows "caught" because IFERROR catches all errors including `#DIV/0!`.  
Now write `=IFNA(1/0, "caught")`. It still shows `#DIV/0!` — because IFNA only catches `#N/A`.

Understand the difference: use IFNA when you want `#DIV/0!` to remain visible as a debugging signal.

## Expected results

- `=IFERROR(C2/0, 0)` → 0
- `=IFNA(VLOOKUP("Fridge", B2:F7, 5, 0), "—")` → "—"
- `=IFERROR(VLOOKUP("Widget", B2:F7, 2, 0), ...)` → 8500 (Feb revenue for Widget)
- `=IFNA(1/0, "caught")` → `#DIV/0!` (NOT caught)

## Solution

<details>
<summary>Reveal solution</summary>

Task 1: `=IFERROR(C2/0, 0)` → 0

Task 2: `=IFNA(VLOOKUP("Fridge",B2:F7,5,0),"—")` → "—"

Task 3: `=IFERROR(VLOOKUP("Widget",B2:F7,2,0), IFERROR(VLOOKUP("widget",B2:F7,2,0),"Not found"))` → 8500

Task 4:
- `=IFERROR(1/0,"caught")` → "caught"
- `=IFNA(1/0,"caught")` → #DIV/0! (IFNA only catches #N/A)

</details>
