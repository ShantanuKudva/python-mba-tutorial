# Exercise 14 — Date Basics: TODAY, YEAR, MONTH 🟢

**Scenario:** You've received an order log with order dates and due dates. Your job is to extract the year and month from each date for pivot reporting, calculate calendar days to complete each order, and flag orders that were placed in Q1 (January–March).

## The sheet

```sheet
src: 02-excel/datasets/dates_data.xlsx.json
sheet: Orders
height: 300
```

Columns: A = OrderID, B = CustomerName, C = OrderDate, D = DueDate, E = Region, F = Amount.

## Tasks

**Task 1 — Extract year and month (columns G and H):**  
In G1, type `Year`. In G2: `=YEAR(C2)`. Copy to G3:G9.  
In H1, type `Month`. In H2: `=MONTH(C2)`. Copy to H3:H9.

**Task 2 — Calendar days to complete (column I):**  
In I1, type `CalendarDays`. In I2: `=D2-C2`. Copy down.

> If the cell shows a date instead of a number, format it as "Number" (right-click → Format Cells → Number).

**Task 3 — Flag Q1 orders (column J):**  
In J1, type `IsQ1`. In J2, write an IF formula that returns "Yes" if the order month (column H) is 1, 2, or 3, and "No" otherwise. Use OR or a nested IFS — or simply `=IF(MONTH(C2)<=3,"Yes","No")`.

**Task 4 — Days since order was placed:**  
In a blank cell below the data, write `=TODAY()-C2` for the first order. Format the result as a number. This tells you how many calendar days ago that order was placed.

## Expected results

| OrderID | OrderDate | Year | Month | CalendarDays | IsQ1 |
|---|---|---|---|---|---|
| 5001 | 2024-01-15 | 2024 | 1 | 15 | Yes |
| 5002 | 2024-02-03 | 2024 | 2 | 14 | Yes |
| 5003 | 2024-03-20 | 2024 | 3 | 14 | Yes |
| 5004 | 2024-04-11 | 2024 | 4 | 14 | No |

## Solution

<details>
<summary>Reveal solution</summary>

G2: `=YEAR(C2)` — copy to G3:G9

H2: `=MONTH(C2)` — copy to H3:H9

I2: `=D2-C2` — format as Number — copy to I3:I9  
(All orders here have 15-day or 14-day windows based on the data)

J2: `=IF(MONTH(C2)<=3,"Yes","No")` — copy down  
Alternative: `=IF(OR(MONTH(C2)=1,MONTH(C2)=2,MONTH(C2)=3),"Yes","No")`

Days since placed (below data): `=TODAY()-C2` → will vary depending on when you run this exercise

</details>
