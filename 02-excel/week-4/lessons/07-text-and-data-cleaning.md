# Lesson 7 — Text & Data Cleaning

## Why this matters

Real data is messy. A CRM export drops customer names in ALL CAPS. An ERP system pads fields with invisible spaces. A sales rep enters "  acme corp  " while another types "Acme Corp". Before you can run a single SUMIF or VLOOKUP, you need your data to be consistent — and Excel's text functions are your first line of defence.

## The preloaded sheet

The Contacts tab below has intentionally dirty data: extra spaces, inconsistent capitalisation, and jumbled company names. Work through the functions to clean it up.

```sheet
src: 02-excel/datasets/text_data.xlsx.json
sheet: Contacts
height: 300
```

---

## TRIM — kill rogue spaces

`=TRIM(text)` removes all leading and trailing spaces, and collapses multiple internal spaces into one.

```
=TRIM("  alice JOHNSON  ")    → "alice JOHNSON"
=TRIM(B2)                     → cleans the raw name in B2
```

Try in a blank cell: `=TRIM(B2)` — the result will shed the padding around "alice JOHNSON".

---

## CLEAN — strip non-printable characters

`=CLEAN(text)` removes characters that come from database exports (carriage returns, tabs, ASCII 1–31). Use it together with TRIM when importing from ERP or CRM systems:

```
=TRIM(CLEAN(B2))
```

---

## PROPER, UPPER, LOWER — capitalisation control

| Function | Result |
|---|---|
| `=PROPER("alice johnson")` | "Alice Johnson" |
| `=UPPER("alice johnson")`  | "ALICE JOHNSON" |
| `=LOWER("ALICE JOHNSON")`  | "alice johnson" |

Use `PROPER` for names and city fields. Use `LOWER` when normalising for lookups (so "ACME" matches "acme"). Use `UPPER` sparingly — all-caps reads as shouting.

```
=PROPER(TRIM(B2))    → "Alice Johnson" from "  alice JOHNSON  "
```

---

## LEFT, RIGHT, MID — extract substrings

| Function | Syntax | Example |
|---|---|---|
| `LEFT`  | `=LEFT(text, num_chars)`         | `=LEFT("HW-WIDGET-S", 2)` → "HW" |
| `RIGHT` | `=RIGHT(text, num_chars)`         | `=RIGHT("HW-WIDGET-S", 1)` → "S" |
| `MID`   | `=MID(text, start_num, num_chars)` | `=MID("HW-WIDGET-S", 4, 6)` → "WIDGET" |

These are essential for parsing structured codes like SKUs, order IDs, and product codes.

Switch to the SKUs sheet to try them:

```sheet
src: 02-excel/datasets/text_data.xlsx.json
sheet: SKUs
height: 220
```

In column D, try `=LEFT(A2, 2)` to extract the department code from each SKU (HW, SW, SV).

---

## FIND and SEARCH — locate characters

`FIND` and `SEARCH` both return the position of a substring. The key difference: `SEARCH` is case-insensitive, `FIND` is case-sensitive.

```
=FIND("-", "HW-WIDGET-S")      → 3  (first dash)
=SEARCH("widget", "HW-WIDGET-S") → 4  (case-insensitive)
```

Use them with `MID` to extract dynamic portions:

```
-- Extract the middle segment (between the 1st and 2nd dashes):
=MID(A2, FIND("-",A2)+1, FIND("-",A2,FIND("-",A2)+1) - FIND("-",A2) - 1)
```

---

## SUBSTITUTE — find and replace inside a formula

`=SUBSTITUTE(text, old_text, new_text, [instance_num])` replaces every occurrence of `old_text` (or a specific one if you pass `instance_num`).

```
=SUBSTITUTE("globex inc", "inc", "Inc")       → "globex Inc"
=SUBSTITUTE("555-1234", "-", "")              → "5551234"  (strip dashes from phone)
=SUBSTITUTE(E2, "  ", " ")                   → collapses double-spaces (combine with TRIM)
```

---

## Combining functions: the cleaning pipeline

A realistic cleaning formula for a name column:

```
=PROPER(TRIM(CLEAN(B2)))
```

Read inside-out:
1. `CLEAN` strips non-printable chars
2. `TRIM` removes extra spaces
3. `PROPER` fixes capitalisation

For company names (which should preserve acronyms like "LLC"), PROPER is usually good enough; check manually for edge cases.

---

## Text-to-columns (conceptual workflow)

Excel's **Data → Text to Columns** wizard is the click-based tool for splitting a single column into multiple columns — for example, splitting "Alice Johnson" into FirstName | LastName, or parsing a pipe-delimited export. In formula terms you replicate this with `LEFT`, `MID`, `RIGHT`, `FIND`, and `SUBSTITUTE`.

---

## Key pitfalls

| Symptom | Likely cause | Fix |
|---|---|---|
| VLOOKUP returns `#N/A` even though the value exists | Extra spaces in lookup key | Wrap both in `TRIM()` |
| COUNTIF returns 0 for a value you can see | Case mismatch or invisible chars | `LOWER()` + `TRIM()` + `CLEAN()` |
| Numbers stored as text | CRM/ERP export | `VALUE()` or multiply by 1 |
| `PROPER` breaks acronyms | "Llc" instead of "LLC" | Post-clean with `SUBSTITUTE` |

---

## Practice tasks

1. In column G of the Contacts sheet, write a formula in G2 that produces a clean, properly-capitalised name from column B.
2. In column H, produce a clean, properly-capitalised city from column F.
3. In the SKUs sheet, extract the department code (first 2 characters) into a new column D.
4. Strip all dashes from the Phone column (column D of Contacts) using SUBSTITUTE.
