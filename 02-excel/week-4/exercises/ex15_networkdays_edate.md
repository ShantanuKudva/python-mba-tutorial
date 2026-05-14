# Exercise 15 — NETWORKDAYS & EDATE: Business Deadlines 🟡

**Scenario:** Your project management team tracks orders and their business-day completion windows. They also need to automatically calculate 90-day renewal dates for each contract. You'll use NETWORKDAYS for business-day counts and EDATE for date arithmetic.

## The sheet

```sheet
src: 02-excel/datasets/dates_data.xlsx.json
sheet: Orders
height: 300
```

## Tasks

**Task 1 — Business days to complete each order (column G):**  
In G1, type `BizDays`. In G2, use NETWORKDAYS to count working days from OrderDate (C) to DueDate (D):
```
=NETWORKDAYS(C2, D2)
```
Copy to G3:G9. Compare to calendar days — which orders span a weekend?

**Task 2 — 90-day renewal date (column H):**  
In H1, type `Renewal90`. In H2, use EDATE to calculate the date exactly 3 months after the OrderDate:
```
=EDATE(C2, 3)
```
Copy to H3:H9. Format as a date.

**Task 3 — Business days from today until renewal:**  
In I1, type `BizDaysToRenewal`. In I2:
```
=NETWORKDAYS(TODAY(), H2)
```
This tells you how many business days remain until each order's 90-day renewal point. Negative values mean the renewal date is already past.

**Task 4 — Flag overdue renewals:**  
In J1, type `Status`. In J2, write an IF formula that shows "Overdue" if NETWORKDAYS(TODAY(), H2) is negative (renewal date in the past), "Due soon" if it's ≤ 30, and "On track" otherwise:
```
=IF(NETWORKDAYS(TODAY(),H2)<0,"Overdue",IF(NETWORKDAYS(TODAY(),H2)<=30,"Due soon","On track"))
```

## Expected results

- G2: 11 business days (Jan 15 to Jan 30, 2024 — crosses 2 weekends)
- H2: April 15, 2024 (3 months from Jan 15, 2024)
- I2 and J2 will vary based on today's date — as of 2026, all renewals will be "Overdue"

## Solution

<details>
<summary>Reveal solution</summary>

G2: `=NETWORKDAYS(C2,D2)` — copy to G3:G9

H2: `=EDATE(C2,3)` — format as date — copy to H3:H9

I2: `=NETWORKDAYS(TODAY(),H2)` — copy to I3:I9

J2:
```
=IF(NETWORKDAYS(TODAY(),H2)<0,"Overdue",IF(NETWORKDAYS(TODAY(),H2)<=30,"Due soon","On track"))
```
Copy to J3:J9.

Since all orders are from 2024, as of 2026 all renewal dates are long past → all show "Overdue".

</details>
