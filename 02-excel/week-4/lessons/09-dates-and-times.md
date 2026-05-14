# Lesson 9 — Dates & Times

## Why this matters

Every business deal has a date. Orders, invoices, contracts, hire dates, renewal dates — if you can't calculate the number of days between two dates, extract the month for a pivot table, or figure out how many business days are left until a deadline, you're blind to the time dimension of your data.

Excel stores dates as serial numbers (1 = January 1, 1900) so you can do arithmetic on them. This makes date math powerful but also full of traps.

## The preloaded sheet

```sheet
src: 02-excel/datasets/dates_data.xlsx.json
sheet: Orders
height: 300
```

---

## TODAY and NOW — dynamic current date/time

```
=TODAY()     -- returns today's date (updates every time the file opens)
=NOW()       -- returns today's date AND current time
```

These are volatile — they recalculate whenever the sheet changes. Good for dashboards, bad for audit trails (use a hard-coded date for records you need to freeze).

---

## DATE — build a date from parts

```
=DATE(year, month, day)

=DATE(2024, 6, 1)     → June 1, 2024
=DATE(YEAR(A2), 1, 1) → January 1st of whatever year is in A2
```

Useful for anchoring period calculations ("first day of the current month"):
```
=DATE(YEAR(TODAY()), MONTH(TODAY()), 1)
```

---

## YEAR, MONTH, DAY — extract parts from a date

```
=YEAR("2024-06-22")    → 2024
=MONTH("2024-06-22")   → 6
=DAY("2024-06-22")     → 22
```

Try these on column C (OrderDate) in the sheet above. In a blank cell: `=YEAR(C2)` → 2024.

These are the building blocks for period pivots: `=SUMIF(YEAR(OrderDate), 2024, Amount)` style logic (though proper array formulas or pivot tables handle this better at scale).

---

## EDATE — add months

`=EDATE(start_date, months)` returns a date exactly N months from start_date — useful for contract renewal, subscription billing, and fiscal-quarter offsets.

```
=EDATE(C2, 3)    -- date 3 months after the order date
=EDATE(TODAY(), -12) -- one year ago
```

> Note: EDATE lands on the same day of the month. So EDATE("2024-01-31", 1) returns "2024-02-29" (or Feb 28 in non-leap years) — it adjusts to the last valid day.

---

## NETWORKDAYS — business days between two dates

`=NETWORKDAYS(start_date, end_date, [holidays])` counts the number of working days (Monday–Friday) between two dates, including both endpoints.

```
=NETWORKDAYS(C2, D2)           -- business days from order to due date
=NETWORKDAYS(TODAY(), D2)      -- business days remaining until due date
```

Pass an optional range of holiday dates as the third argument.

---

## DATEDIF — calculate tenure, age, or contract length

`=DATEDIF(start_date, end_date, unit)` is an undocumented but widely-used function. Excel won't autocomplete it, but it works.

| Unit | Returns |
|---|---|
| "Y"  | Complete years |
| "M"  | Complete months |
| "D"  | Total days |
| "MD" | Days ignoring months and years |
| "YM" | Months ignoring years |

```
=DATEDIF(C2, TODAY(), "Y")     -- years of tenure for an employee
=DATEDIF(C2, TODAY(), "M")     -- months since order placed
=DATEDIF(C2, TODAY(), "YM")    -- months in current (incomplete) year
```

For a human-readable tenure like "5 years, 3 months":
```
=DATEDIF(C2,TODAY(),"Y")&" yrs, "&DATEDIF(C2,TODAY(),"YM")&" mo"
```

Switch to the Employees tab to practice tenure calculations:

```sheet
src: 02-excel/datasets/dates_data.xlsx.json
sheet: Employees
height: 240
```

---

## Date formatting

Excel separates the stored value (a serial number) from how it's displayed. Right-click → Format Cells → Number → Date. Common formats:

| Format code | Example output |
|---|---|
| `DD/MM/YYYY` | 22/06/2024 |
| `MMMM DD, YYYY` | June 22, 2024 |
| `MMM-YY` | Jun-24 |
| `YYYY-MM-DD` | 2024-06-22 (ISO, preferred for sorting) |

---

## Common date pitfalls

| Problem | What's happening | Fix |
|---|---|---|
| Date arithmetic gives a huge number | Cell is formatted as General, showing the serial number | Format the cell as Date |
| "January 0, 1900" appears | A formula returned 0 | Check why the date calc returned 0; format issue or wrong reference |
| Two dates look the same but DATEDIF errors | One is stored as text, not a real date | `=DATEVALUE(A2)` to convert text-dates |
| Dates sort as text (alphabetically) | Dates were imported as text | Use `VALUE()` or `DATEVALUE()` to convert |
| NETWORKDAYS counts weekends | Wrong formula used | Use NETWORKDAYS, not just subtraction |

---

## Practice tasks

1. In the Orders sheet, add a column that calculates the number of calendar days between OrderDate and DueDate. (Simple arithmetic: `=D2-C2`.)
2. Add a column using NETWORKDAYS to count business days between OrderDate and DueDate for each order.
3. In the Employees sheet, use DATEDIF to calculate how many complete years each employee has been with the company.
4. Using TODAY, YEAR, and MONTH, write a formula that returns 1 if an order was placed in the current calendar year, 0 otherwise.
