# Exercise 12 — IFS & SWITCH: Multi-Tier Categorisation 🟡

**Scenario:** Your CFO wants every product tiered based on Q1 revenue: Flagship (>$100k), Growth ($30k–$100k), or Niche (below $30k). She also wants each product's category label mapped to a plain-English department name. IFS handles the tiering; SWITCH handles the mapping.

## The sheet

```sheet
src: 02-excel/datasets/sales.xlsx.json
sheet: Q1
height: 340
```

Columns: B = Product, C = Jan, D = Feb, E = Mar, F = Q1 Total.

## Tasks

**Task 1 — Tier each product with IFS (column G):**  
In G1, type `Tier`. In G2, write an IFS formula that:
- Returns "Flagship" if F2 > 100000
- Returns "Growth" if F2 > 30000
- Returns "Niche" for anything else (use `TRUE` as the final condition)

Copy down to G7. Which products land in each tier?

**Task 2 — Compare with nested IF:**  
In H2, write the equivalent nested IF and confirm both columns match:
```
=IF(F2>100000,"Flagship",IF(F2>30000,"Growth","Niche"))
```

**Task 3 — Map product to department with SWITCH (column I):**  
In I1, type `Department`. Products in the Q1 sheet belong to departments. Use SWITCH on column B:
- "Widget" → "Hardware"
- "Gadget" → "Hardware"
- "Cable" → "Hardware"
- "License" → "Software"
- "Plugin" → "Software"
- "Service" → "Professional Services"
- Default → "Other"

In I2: `=SWITCH(B2, "Widget","Hardware", "Gadget","Hardware", "Cable","Hardware", "License","Software", "Plugin","Software", "Service","Professional Services", "Other")`

Copy to I3:I7.

**Task 4 — Count by tier:**  
Below the data, use three COUNTIF formulas to count how many products fall in each tier column G:
- Count of Flagship: `=COUNTIF(G2:G7,"Flagship")`
- Count of Growth: `=COUNTIF(G2:G7,"Growth")`
- Count of Niche: `=COUNTIF(G2:G7,"Niche")`

## Expected results

| Product | Q1 Total (F) | Tier (G) | Department (I) |
|---|---|---|---|
| Widget | ~$32k | Growth | Hardware |
| Gadget | ~$47k | Growth | Hardware |
| License | ~$143k | Flagship | Software |
| Service | ~$82k | Growth | Professional Services |
| Cable | ~$10k | Niche | Hardware |
| Plugin | ~$31k | Growth | Software |

(Exact totals depend on the dataset. One product should be Flagship, one Niche.)

## Solution

<details>
<summary>Reveal solution</summary>

G2 (IFS): `=IFS(F2>100000,"Flagship",F2>30000,"Growth",TRUE,"Niche")` — copy to G3:G7

H2 (nested IF): `=IF(F2>100000,"Flagship",IF(F2>30000,"Growth","Niche"))` — should match G column

I2 (SWITCH):
```
=SWITCH(B2,"Widget","Hardware","Gadget","Hardware","Cable","Hardware","License","Software","Plugin","Software","Service","Professional Services","Other")
```
Copy to I3:I7.

Tier counts:
- `=COUNTIF(G2:G7,"Flagship")` → 1
- `=COUNTIF(G2:G7,"Growth")` → 4
- `=COUNTIF(G2:G7,"Niche")` → 1

</details>
