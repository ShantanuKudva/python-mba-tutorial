# Exercise 10 — SUBSTITUTE: Normalise Company Names 🟡

**Scenario:** Your contacts dataset has company names entered inconsistently — "globex inc", "INITECH LLC", "stark industries". You need to normalise them so VLOOKUP and COUNTIF work reliably, and then strip dashes from phone numbers to get bare digits.

## The sheet

```sheet
src: 02-excel/datasets/text_data.xlsx.json
sheet: Contacts
height: 300
```

## Tasks

**Task 1 — Strip phone dashes (column G):**  
In G1, type `PhoneDigits`. In G2, write a SUBSTITUTE formula that removes all dashes from the phone number in column D, leaving only digits (e.g. "555-1234" → "5551234"). Copy down to G9.

**Task 2 — Normalise company names (column H):**  
In H1, type `Company_Clean`. In H2, write a formula that:
1. Applies PROPER capitalisation to the company name in column E
2. Then substitutes " Inc" with ", Inc" and " Llc" with ", LLC" (PROPER will capitalise the first letter of "inc" and "llc")

For row 2, the result should be "Globex, Inc" (or just "Globex Inc" if you skip the comma — either is fine as long as it's consistent).

**Task 3 — Lower-case lookup key (column I):**  
In I1, type `LookupKey`. In I2, write `=LOWER(TRIM(E2))` to create a normalised lookup key. This lets COUNTIF and VLOOKUP match regardless of whether the source data is upper, lower, or title case.

**Task 4 — Count Globex entries:**  
In a blank cell below the data, write a COUNTIF that counts how many rows have "globex inc" in their company column (E), using the LOWER lookup key column (I) you just built:
`=COUNTIF(I2:I9, "globex inc")`

## Expected results

- G2: `5551234`
- H3 (Bob Smith's company): something like "Globex, Inc" or "Globex Inc"
- The COUNTIF for "globex inc" should return 2 (rows 3 and 8 are both Globex contacts)

## Solution

<details>
<summary>Reveal solution</summary>

G2 (strip dashes): `=SUBSTITUTE(D2,"-","")` — copy down

H2 (normalise company):
```
=SUBSTITUTE(SUBSTITUTE(PROPER(TRIM(E2))," Inc",", Inc")," Llc",", LLC")
```
Note: PROPER converts "inc" → "Inc" and "llc" → "Llc" so we substitute those exact patterns.

I2 (lookup key): `=LOWER(TRIM(E2))` — copy down

COUNTIF: `=COUNTIF(I2:I9,"globex inc")` → 2

</details>
