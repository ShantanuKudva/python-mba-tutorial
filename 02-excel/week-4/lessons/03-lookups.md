# Lesson 3 — Lookups: VLOOKUP / INDEX-MATCH

## Why this matters

Your pricing team gives you a product list with list prices. Your sales team sends deal sheets with customer IDs. You need to pull the right discount rate from a customer master table into the deal sheet — for 500 rows. Doing this manually is a two-hour copy-paste nightmare that will contain errors. With `VLOOKUP` (or its more flexible replacement, `INDEX`+`MATCH`), it's one formula copied down in 20 seconds.

## The preloaded sheet (Customers + Pricing)

The `customers.xlsx` workbook has two sheets: **Customers** (the lookup table) and **Pricing** (the deal sheet that needs to pull discounts).

```sheet
src: 02-excel/datasets/customers.xlsx.json
sheet: Pricing
height: 340
```

## VLOOKUP — the classic lookup

```
=VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])
```

| Argument | What it means |
|---|---|
| `lookup_value` | The value you're searching for (e.g. a CustomerID) |
| `table_array` | The range containing the lookup table (include the key column first) |
| `col_index_num` | Which column of the table to return (1 = first column, 2 = second, …) |
| `range_lookup` | `FALSE` or `0` for an exact match (almost always what you want) |

Example — pull the discount from the Customers sheet using CustomerID in column D:

```
=VLOOKUP(D2, Customers!A:F, 6, FALSE)
```

This looks up D2 (a CustomerID) in the first column of `Customers!A:F`, then returns column 6 (Discount).

Cell E2 in the Pricing sheet already has this formula. Click E2 to verify.

### VLOOKUP limitations

1. **The key must be in the leftmost column.** You can't look up by company name and return the CustomerID — that would require the name to be first.
2. **Column index is fragile.** If someone inserts a column in the lookup table, your `6` becomes wrong and gives a silent wrong answer.
3. **No left-lookup.** You can only return columns to the right of the key.

---

## INDEX + MATCH — the professional replacement

```sheet
src: 02-excel/datasets/customers.xlsx.json
sheet: Customers
```

`INDEX` returns the value at a given row/column position in a range.  
`MATCH` finds the position of a value within a single column or row.

Together:

```
=INDEX(return_range, MATCH(lookup_value, lookup_range, 0))
```

Same example — pull the discount from the Customers sheet:

```
=INDEX(Customers!F:F, MATCH(D2, Customers!A:A, 0))
```

`MATCH(D2, Customers!A:A, 0)` finds the row number of D2 in column A.  
`INDEX(Customers!F:F, ...)` returns the value in column F at that row.

Advantages over VLOOKUP:
- Works with keys in any column (no leftmost-column restriction).
- Column reference by name, not number — inserting columns won't break it.
- Can do left-lookups.

---

## IFERROR — graceful failure

Lookups fail when the key isn't found. Wrap your formula to show a clean message instead of `#N/A`:

```
=IFERROR(VLOOKUP(D2, Customers!A:F, 6, FALSE), "Not found")
=IFERROR(INDEX(Customers!F:F, MATCH(D2, Customers!A:A, 0)), 0)
```

---

## Tasks — do these in the sheet above

```sheet
src: 02-excel/datasets/customers.xlsx.json
sheet: Pricing
```

1. **Column E (DiscountedPrice):** The formula in E2 uses `VLOOKUP`. Click E3 — does it have the same formula for row 3? If not, type `=C3*(1-VLOOKUP(D3,Customers!A:F,6,0))` in E3.

2. **Add column F (Method 2 — INDEX-MATCH):** In F1 type the header `Discount (IM)`. In F2, write the equivalent using `INDEX`+`MATCH`:  
   `=INDEX(Customers!F:F, MATCH(D2, Customers!A:A, 0))`  
   Confirm it returns the same discount as the VLOOKUP in column E.

3. **Add column G (Final Price):** In G1 type `Final Price`. In G2, write:  
   `=IFERROR(C2*(1-F2), C2)`  
   This uses the INDEX-MATCH discount, with IFERROR as a safety net.

4. **Try a missing key:** In a new row (row 6), enter product `105`, name `Widget XL`, list price `14.99`, and CustomerID `9999` (which doesn't exist). Watch what VLOOKUP returns — then compare to the IFERROR-wrapped version.

---

## Try it

Switch the sheet view to the **Customers** tab (using the sheet tab selector at the bottom of the spreadsheet above). Find CustomerID 1006 (Stark Industries). What is their discount rate? Now go back to Pricing and add a row for a new deal: `Widget` at `$9.99` for customer `1006`. Write the VLOOKUP in column E to pull their discount.

---

## Common mistakes

- **`range_lookup = TRUE`:** omitting the last argument (or using `TRUE`) does an approximate match, which can silently return the wrong row if the key column isn't sorted. Always use `FALSE` / `0`.
- **Wrong `col_index_num`:** count from the left edge of `table_array`, not from column A of the sheet.
- **Volatile lookup tables:** if the lookup table might grow or shift, use a full-column reference (`A:F`) rather than a fixed range (`A1:F100`).

---

Next: [Lesson 4 — Pivot Thinking](04-pivots-and-aggregation.md)

---

## Resources

- [Microsoft — VLOOKUP](https://support.microsoft.com/en-us/office/vlookup-function-0bbc8083-26fe-4963-8ab8-93a18ad188a1)
- [Microsoft — INDEX function](https://support.microsoft.com/en-us/office/index-function-a5dcf0dd-996d-40a4-a822-b56b061328bd)
- [Microsoft — MATCH function](https://support.microsoft.com/en-us/office/match-function-e8dffd45-c762-47d6-bf89-533f4a37673a)
- [Chandoo.org — INDEX MATCH vs VLOOKUP](https://chandoo.org/wp/index-match-vs-vlookup/)
