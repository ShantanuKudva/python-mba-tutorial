# Week 4 Project — Sales Dashboard from Raw Transactions

**Time estimate:** 45–60 minutes.

## The scenario

You're the analytics lead at a mid-size SaaS company. The head of sales sends you the Q1 and Q2 raw revenue data (by product and region) and asks for a one-page executive dashboard that answers three questions:

1. Which products are growing from Q1 to Q2?
2. Which region has the highest total revenue across both quarters?
3. Which products are at risk (Q2 lower than Q1)?

You have everything you need in the two workbooks below.

---

## Step 1 — Explore the Q1 data

```sheet
src: 02-excel/datasets/sales.xlsx.json
sheet: Q1
height: 300
```

Take 2 minutes to understand the structure: products in rows A2:A7, regions in B2:B7, monthly data in C:E, Q1 totals in F.

---

## Step 2 — Explore Q2 and compare

Use the sheet tab selector to switch to Q2. The structure is identical, covering April, May, June.

Note the Q2 totals in column F. Mentally compare Widget (row 2): did it grow or shrink vs Q1?

---

## Step 3 — Build the dashboard

In the empty area of the Q1 sheet (starting around row 12), build a comparison table using the following columns:

| Column | Label | Formula |
|---|---|---|
| A | Product | (copy from A2:A7) |
| B | Q1 Total | `=F2` … `=F7` |
| C | Q2 Total | Type the Q2 values directly (see Q2 tab) or reference another sheet if supported |
| D | Growth $ | `=C2-B2` |
| E | Growth % | `=D2/B2` (round to 2 decimal places) |
| F | Trend | `=IF(D2>0,"Growing","Declining")` |

> Note: cross-sheet references like `=Q2!F2` may not be supported in the in-browser spreadsheet. In that case, type the Q2 totals manually in column C. The formula logic in D:F is the same.

**Q2 reference values (from the Q2 tab):**

| Product | Q2 Total |
|---|---|
| Widget | =SUM(Apr+May+Jun) ≈ 45,700 |
| Gadget | ≈ 31,500 |
| License | ≈ 166,000 |
| Service | ≈ 79,000 |
| Cable | ≈ 13,400 |
| Plugin | ≈ 70,500 |

---

## Step 4 — Regional summary

Below the product comparison table (around row 22), build a regional summary using `SUMIF`:

| | A | B | C | D |
|---|---|---|---|---|
| Row 22 | Region | Q1 Total | Q2 Total | Growth % |
| Row 23 | North | `=SUMIF(B2:B7,"North",F2:F7)` | (type Q2 North total) | `=(C23-B23)/B23` |
| Row 24 | East | … | … | … |
| Row 25 | West | … | … | … |

Q2 regional totals (from Q2 tab):
- North (Widget + Gadget): ~77,200
- East (License + Service): ~245,000
- West (Cable + Plugin): ~83,900

---

## Step 5 — Key metrics block

In cells H2:I6, build a KPI block:

| | H | I |
|---|---|---|
| Row 2 | Total Q1 Revenue | `=SUM(B13:B18)` (or your range) |
| Row 3 | Total Q2 Revenue | `=SUM(C13:C18)` |
| Row 4 | Overall Growth % | `=(I3-I2)/I2` |
| Row 5 | Growing Products | `=COUNTIF(F13:F18,"Growing")` |
| Row 6 | Declining Products | `=COUNTIF(F13:F18,"Declining")` |

---

## Deliverable

A spreadsheet with:

1. A product-level Q1 vs Q2 comparison with growth calculations and trend flags.
2. A regional breakdown showing which geography is growing fastest.
3. A KPI summary block with totals, overall growth %, and product counts.

Use the **Download** button (top of the sheet widget) to export your completed dashboard as an `.xlsx` file.

---

## What you practiced

- SUM, SUMIF, COUNTIF aggregation
- Growth calculations (absolute and percentage)
- IF-based categorical flags
- Structuring data for an executive audience
- Cross-referencing multiple data sources

---

## Extension (optional)

If you finish early, add a "risk score" column: `=IF(E2<-0.05,"HIGH",IF(E2<0,"MEDIUM","LOW"))` — a three-level flag based on the growth percentage. Which products are HIGH risk?
