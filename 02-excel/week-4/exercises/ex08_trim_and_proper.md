# Exercise 08 — TRIM & PROPER: Fix the Contact List 🟢

**Scenario:** Your sales ops team just exported 8 contacts from the CRM. The names came out with random capitalisation and extra spaces — classic CRM export mess. Before you can use this list for mail-merge or a pivot table, you need to clean columns B and F.

## The sheet

```sheet
src: 02-excel/datasets/text_data.xlsx.json
sheet: Contacts
height: 300
```

## Tasks

**Task 1 — Clean the name (column G):**  
In G1, type the header `CleanName`. In G2, write a formula that removes extra spaces AND applies proper capitalisation to column B. Copy the formula down to G9.

**Task 2 — Clean the city (column H):**  
In H1, type `CleanCity`. In H2, write a formula that trims the city in column F and applies PROPER capitalisation. Copy down to H9.

**Task 3 — Spot-check your results:**  
After running your formulas, verify:
- G2 should read "Alice Johnson" (not "  alice JOHNSON  ")
- H2 should read "New York" (not "  new york  ")
- G7 should read "Grace Tan"

**Task 4 — Build a full name + city label (column I):**  
In I1, type `Label`. In I2, concatenate the clean name and clean city with a comma and space between them:
`"Alice Johnson, New York"`

Use the `&` operator or `TEXTJOIN`.

## Expected results

| Row | CleanName (G) | CleanCity (H) | Label (I) |
|---|---|---|---|
| 2 | Alice Johnson | New York | Alice Johnson, New York |
| 3 | Bob Smith | Chicago | Bob Smith, Chicago |
| 4 | Carol Lee | San Francisco | Carol Lee, San Francisco |
| 8 | Henry Park | Chicago | Henry Park, Chicago |

## Solution

<details>
<summary>Reveal solution</summary>

G2: `=PROPER(TRIM(B2))` — copy to G3:G9

H2: `=PROPER(TRIM(F2))` — copy to H3:H9

I2: `=G2&", "&H2` — copy to I3:I9

Alternative for I2 using TEXTJOIN: `=TEXTJOIN(", ",TRUE,G2,H2)`

</details>
