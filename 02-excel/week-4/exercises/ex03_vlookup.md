# Exercise 03 — VLOOKUP 🟡

**Scenario:** Your pricing team has a customer master list with discount tiers. The sales ops team has a deal sheet with customer IDs and list prices. Your job: pull the right discount from the master list into the deal sheet — for every row — using a single formula that can be copied down.

## The sheet (Pricing tab)

```sheet
src: 02-excel/datasets/customers.xlsx.json
sheet: Pricing
height: 280
```

## Tasks

**Task 1 — Verify the existing VLOOKUP (cell E2):**  
Click on E2. The formula bar should show something like `=C2*(1-VLOOKUP(D2,Customers!A:F,6,0))`. Confirm it returns a number less than the list price in C2 (it should — the customer has a positive discount).

**Task 2 — Write E3 from scratch:**  
Click E3. Type the following formula yourself (don't copy from E2):

```
=C3*(1-VLOOKUP(D3,Customers!A:F,6,0))
```

What discount was applied to Globex (CustomerID 1002)?

**Task 3 — Add a "Discount %" column (F):**  
In F1, type the header `Discount %`. In F2, write a VLOOKUP that returns just the discount rate (not the final price):

```
=VLOOKUP(D2,Customers!A:F,6,0)
```

Copy down to F3:F5. Do the discounts match what you'd expect from an Enterprise vs. SMB vs. Mid-Market customer?

**Task 4 — Replace with INDEX-MATCH (column G):**  
In G1, type `Discount (IM)`. In G2, write the INDEX-MATCH equivalent:

```
=INDEX(Customers!F:F, MATCH(D2, Customers!A:A, 0))
```

Copy down to G3:G5. Columns F and G should match exactly.

**Task 5 — Add a safety net:**  
Wrap your G2 formula in `IFERROR(...)` so that if the CustomerID isn't found, it shows `"Unknown customer"` instead of `#N/A`.

## Expected results

- Stark Industries (CustomerID 1006, Enterprise) has the highest discount: 20%.
- Globex (CustomerID 1002, Mid-Market) has 10%.
- The VLOOKUP and INDEX-MATCH columns should be identical.

## Solution

<details>
<summary>Reveal solution</summary>

E2 final price formula: `=C2*(1-VLOOKUP(D2,Customers!A:F,6,0))`

F2 discount lookup: `=VLOOKUP(D2,Customers!A:F,6,0)`

G2 INDEX-MATCH: `=INDEX(Customers!F:F,MATCH(D2,Customers!A:A,0))`

G2 with IFERROR: `=IFERROR(INDEX(Customers!F:F,MATCH(D2,Customers!A:A,0)),"Unknown customer")`

</details>
