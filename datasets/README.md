# Datasets

Sample workbooks used by exercises and projects in weeks 4–10.

## Generate

The datasets are produced by [`generate_samples.py`](generate_samples.py) so they're reproducible and don't pollute git history with binaries.

From the repo root:

```bash
python datasets/generate_samples.py
```

This creates:

```
datasets/
├── finance/
│   ├── sample_pl.xlsx               (week 4 + 6)
│   └── sample_balance_sheet.xlsx    (week 6)
├── marketing/
│   └── sample_orders.xlsx           (week 5 + 7) — sheets: orders, customers
├── operations/
│   └── sample_demand.xlsx           (week 8) — 24 months of monthly units per SKU
└── strategy/
    └── sample_inputs.xlsx           (week 9) — base assumptions for SaaS scenarios
```

## Re-run safely

Re-running the script overwrites existing files. The data has a fixed random seed, so the same inputs produce the same outputs every time — your exercises stay reproducible.

## Content notes

- `sample_pl.xlsx` intentionally has a few "N/A" strings, blank cells, and trailing whitespace — that's the cleaning practice for week 4.
- `sample_orders.xlsx` covers ~2 years of activity across 4 regions and 4 product categories.
- `sample_demand.xlsx` has clear seasonality + trend so ETS can shine in week 8.

## Replace with your own data

For projects, you can swap in your own `.xlsx` — just keep the column names the same as the sample, or update the project code to match yours.
