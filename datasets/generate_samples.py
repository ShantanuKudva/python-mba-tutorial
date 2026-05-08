"""
Generate sample Excel workbooks for the course.

Run from repo root:
    python datasets/generate_samples.py

Idempotent — re-running overwrites with the same content (fixed seed).
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


SEED = 42
ROOT = Path(__file__).parent


# ---------------------------------------------------------------------------
# Finance
# ---------------------------------------------------------------------------

def write_finance() -> None:
    out_dir = ROOT / "finance"
    out_dir.mkdir(exist_ok=True)

    # Messy P&L for week 4 cleaning + week 6 ratios.
    pl = pd.DataFrame({
        "line_item": [
            "Revenue", "COGS", "Gross Profit",
            "Operating Expenses ", "  Operating Income",
            "Interest Expense", "Tax", "Net Income",
            "Other Income", "Restructuring",
        ],
        "amount": [
            5_000_000, 3_000_000, 2_000_000,
            1_200_000, 800_000,
            50_000, 200_000, 550_000,
            None, "N/A",
        ],
        "category": [
            "revenue", "cogs", "subtotal",
            "opex", "subtotal",
            "non-op", "tax", "net",
            None, "non-op",
        ],
    })
    pl.to_excel(out_dir / "sample_pl.xlsx", index=False)

    bs = pd.DataFrame({
        "line_item": [
            "Cash", "Receivables", "Inventory",
            "Total Current Assets", "Total Assets",
            "Current Liabilities", "Total Liabilities",
            "Total Equity",
        ],
        "amount": [
            400_000, 600_000, 500_000,
            1_500_000, 5_000_000,
            800_000, 2_500_000,
            2_500_000,
        ],
    })
    bs.to_excel(out_dir / "sample_balance_sheet.xlsx", index=False)

    print("  ✓ finance/")


# ---------------------------------------------------------------------------
# Marketing
# ---------------------------------------------------------------------------

def write_marketing() -> None:
    out_dir = ROOT / "marketing"
    out_dir.mkdir(exist_ok=True)

    rng = np.random.default_rng(SEED)

    n_customers = 250
    customers = pd.DataFrame({
        "customer_id":  [f"C-{i:04d}" for i in range(1, n_customers + 1)],
        "name":         [f"Customer {i}" for i in range(1, n_customers + 1)],
        "region":       rng.choice(["NA", "EMEA", "APAC", "LATAM"], n_customers, p=[0.45, 0.3, 0.18, 0.07]),
        "segment":      rng.choice(["SMB", "Mid-Market", "Enterprise"], n_customers, p=[0.6, 0.3, 0.1]),
        "signup_date":  pd.to_datetime("2024-01-01") + pd.to_timedelta(rng.integers(0, 730, n_customers), unit="D"),
    })

    # Each customer has 1–25 orders, biased by segment.
    orders = []
    order_id = 1
    for _, c in customers.iterrows():
        seg_mult = {"SMB": 1, "Mid-Market": 3, "Enterprise": 8}[c["segment"]]
        n_orders = max(1, int(rng.normal(loc=4 * seg_mult, scale=2 * seg_mult)))
        for _ in range(n_orders):
            order_dt = c["signup_date"] + pd.to_timedelta(int(rng.uniform(0, 720)), unit="D")
            if order_dt > pd.Timestamp("2026-04-30"):
                continue
            amount = float(np.round(rng.lognormal(mean=4 + 0.5 * np.log(seg_mult), sigma=0.7), 2))
            orders.append({
                "order_id":         f"O-{order_id:06d}",
                "customer_id":      c["customer_id"],
                "order_date":       order_dt.date(),
                "product_category": rng.choice(["Widgets", "Gadgets", "Services", "Add-ons"], p=[0.45, 0.25, 0.2, 0.10]),
                "amount":           amount,
            })
            order_id += 1

    orders_df = pd.DataFrame(orders)
    orders_df["order_date"] = pd.to_datetime(orders_df["order_date"])

    # Add region to orders (denormalized) so single-sheet exercises also work.
    orders_df = orders_df.merge(customers[["customer_id", "region"]], on="customer_id", how="left")

    with pd.ExcelWriter(out_dir / "sample_orders.xlsx") as w:
        orders_df.to_excel(w, sheet_name="orders", index=False)
        customers.to_excel(w, sheet_name="customers", index=False)

    print(f"  ✓ marketing/  ({len(orders_df):,} orders, {n_customers} customers)")


# ---------------------------------------------------------------------------
# Operations
# ---------------------------------------------------------------------------

def write_operations() -> None:
    out_dir = ROOT / "operations"
    out_dir.mkdir(exist_ok=True)

    rng = np.random.default_rng(SEED)
    months = pd.period_range("2024-01", periods=24, freq="M").to_timestamp()

    skus = ["W-001", "W-002", "W-003"]
    rows = []
    for sku in skus:
        base = {"W-001": 200, "W-002": 80, "W-003": 350}[sku]
        trend = {"W-001": 4.0, "W-002": 1.5, "W-003": 2.0}[sku]
        season_amp = {"W-001": 25, "W-002": 10, "W-003": 40}[sku]
        for i, m in enumerate(months):
            seasonal = season_amp * np.sin(2 * np.pi * (m.month - 1) / 12)
            noise = rng.normal(0, base * 0.05)
            units = max(0, int(round(base + trend * i + seasonal + noise)))
            rows.append({"sku": sku, "month": m, "units": units})

    pd.DataFrame(rows).to_excel(out_dir / "sample_demand.xlsx", index=False)
    print(f"  ✓ operations/  ({len(skus)} SKUs × {len(months)} months)")


# ---------------------------------------------------------------------------
# Strategy
# ---------------------------------------------------------------------------

def write_strategy() -> None:
    out_dir = ROOT / "strategy"
    out_dir.mkdir(exist_ok=True)

    inputs = pd.DataFrame([
        {"input": "starting_units",  "value": 10_000, "unit": "users",     "note": "Active subscribers at year 0"},
        {"input": "price",           "value": 240,    "unit": "$/yr",      "note": "Annual subscription price"},
        {"input": "growth_rate",     "value": 0.20,   "unit": "ratio",     "note": "Annual user growth"},
        {"input": "churn_rate",      "value": 0.10,   "unit": "ratio",     "note": "Annual churn"},
        {"input": "wacc",            "value": 0.10,   "unit": "ratio",     "note": "Cost of capital for DCF"},
    ])
    inputs.to_excel(out_dir / "sample_inputs.xlsx", index=False)
    print("  ✓ strategy/")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    print("Generating sample datasets...")
    write_finance()
    write_marketing()
    write_operations()
    write_strategy()
    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
