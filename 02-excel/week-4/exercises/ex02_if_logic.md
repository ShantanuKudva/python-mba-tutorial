# Exercise 02 — IF Logic 🟢

**Scenario:** The sales director wants a performance flag next to each product: `"On track"` if Q1 Total is at or above $30,000, `"Watch"` if it's between $15,000 and $30,000, and `"Underperforming"` below $15,000. She also wants a separate column showing the revenue gap to the $30k threshold — positive means surplus, negative means shortfall.

## The sheet

```sheet
src: 02-excel/datasets/sales.xlsx.json
sheet: Q1
height: 340
```

## Tasks

**Task 1 — Performance flag (column G):**  
Type the header `Status` in G1. In G2, write a nested `IF` formula:

```
=IF(F2>=30000, "On track", IF(F2>=15000, "Watch", "Underperforming"))
```

Copy this formula down to G3:G7 (click G2, then drag the fill handle down, or retype the formula for each row adjusting the row number).

**Task 2 — Gap to target (column H):**  
Type the header `Gap to $30k` in H1. In H2, write:

```
=F2 - 30000
```

Copy down to H3:H7. Positive values = products beating target. Negative = shortfall.

**Task 3 — Count underperformers:**  
In any empty cell, write `=COUNTIF(G2:G7,"Underperforming")`. How many products are underperforming?

**Task 4 — Total shortfall:**  
In any empty cell, write `=SUMIF(H2:H7,"<0",H2:H7)`. This sums only the negative gaps. What is the total shortfall for underperforming products?

## Expected results

- Licenses (row 4) and Services (row 5) should be "On track" with large surpluses.
- Cable (row 6) should be "Underperforming" with a large negative gap.
- The exact counts and totals depend on whether you computed Q1 Total correctly in column F.

## Solution

<details>
<summary>Reveal solution</summary>

G2 formula: `=IF(F2>=30000,"On track",IF(F2>=15000,"Watch","Underperforming"))`

Expected statuses:
- Widget (F2≈37,300): On track
- Gadget (F3≈26,600): Watch
- License (F4≈143,000): On track
- Service (F5≈69,500): On track
- Cable (F6≈10,500): Underperforming
- Plugin (F7≈58,500): On track

COUNTIF result: 1 (only Cable)
SUMIF shortfall: −19,500 (Cable is $19.5k below target)

</details>
