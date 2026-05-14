# Exercise 09 — LEFT, MID & RIGHT: Parse SKU Codes 🟡

**Scenario:** Your inventory system uses structured SKU codes in the format `DEPT-PRODUCT-SIZE` (e.g. `HW-WIDGET-S`). You need to split each SKU into three separate columns so the data can be used in pivot tables and reports.

## The sheet

```sheet
src: 02-excel/datasets/text_data.xlsx.json
sheet: SKUs
height: 240
```

## Tasks

**Task 1 — Extract the department code (column D):**  
In D1, type `DeptCode`. In D2, write a formula that extracts the first 2 characters from the SKU in column A (e.g. "HW", "SW", "SV"). Copy down to D7.

**Task 2 — Extract the product name segment (column E):**  
In E1, type `ProductCode`. In E2, write a formula using MID that extracts the middle segment of the SKU (between the two dashes). For "HW-WIDGET-S" the result should be "WIDGET".

Hint: Use FIND to locate the positions of the dashes dynamically rather than hardcoding character positions.

**Task 3 — Extract the size/variant (column F):**  
In F1, type `Variant`. The last segment is always after the second dash. Use RIGHT and FIND (or LEN) to extract "S", "ENT", "M", "PRO", "USB", "API" from each SKU.

**Task 4 — Verify the round-trip:**  
In G2, reconstruct the SKU from your three extracted columns using `&`:
`=D2&"-"&E2&"-"&F2`
It should exactly match A2.

## Expected results

| SKU | DeptCode | ProductCode | Variant | Reconstructed |
|---|---|---|---|---|
| HW-WIDGET-S | HW | WIDGET | S | HW-WIDGET-S |
| SW-LICENSE-ENT | SW | LICENSE | ENT | SW-LICENSE-ENT |
| HW-GADGET-M | HW | GADGET | M | HW-GADGET-M |
| SV-SUPPORT-PRO | SV | SUPPORT | PRO | SV-SUPPORT-PRO |

## Solution

<details>
<summary>Reveal solution</summary>

D2 (DeptCode): `=LEFT(A2,2)` — copy down

E2 (ProductCode):
```
=MID(A2, FIND("-",A2)+1, FIND("-",A2,FIND("-",A2)+1) - FIND("-",A2) - 1)
```
Breakdown: start after the 1st dash; length = position of 2nd dash minus position of 1st dash minus 1.

F2 (Variant):
```
=RIGHT(A2, LEN(A2) - FIND("-",A2,FIND("-",A2)+1))
```
Alternatively: `=MID(A2, FIND("-",A2,FIND("-",A2)+1)+1, 100)` — MID returns to end of string when num_chars exceeds remaining length.

G2 (Reconstruct): `=D2&"-"&E2&"-"&F2`

</details>
