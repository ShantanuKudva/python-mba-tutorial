/**
 * Domain-specific stat extraction. Pure, testable. Returns a small set of
 * highlight stats for the StatsRow at the top of the results section.
 */

import type { Domain } from "@/lib/api";
import type { Stat } from "@/components/StatsRow";

function pct(v: unknown): string {
  if (typeof v !== "number") return "—";
  return `${(v * 100).toFixed(1)}%`;
}

function multX(v: unknown): string {
  if (typeof v !== "number") return "—";
  return `${v.toFixed(2)}x`;
}

function money(v: unknown): string {
  if (typeof v !== "number") return "—";
  if (Math.abs(v) >= 1_000_000) return `$${(v / 1_000_000).toFixed(2)}M`;
  if (Math.abs(v) >= 1_000) return `$${(v / 1_000).toFixed(1)}K`;
  return `$${v.toFixed(0)}`;
}

function num(v: unknown): string {
  if (typeof v !== "number") return "—";
  return v.toLocaleString();
}

function get(obj: Record<string, unknown>, key: string): unknown {
  return obj[key];
}

export function deriveStats(
  domain: Domain,
  metrics: Record<string, unknown>
): Stat[] {
  switch (domain) {
    case "finance": {
      const score = get(metrics, "score");
      const tone =
        typeof score === "number"
          ? score >= 70
            ? "good"
            : score >= 50
            ? "warn"
            : "bad"
          : "default";
      return [
        { label: "Health score", value: typeof score === "number" ? score.toFixed(0) : "—", tone },
        { label: "Verdict", value: String(get(metrics, "verdict") ?? "—") },
        { label: "Net margin", value: pct(get(metrics, "net_margin")) },
        { label: "Debt / Equity", value: multX(get(metrics, "debt_to_equity")) },
      ];
    }
    case "marketing": {
      const segments = (get(metrics, "segments") as Array<Record<string, unknown>>) ?? [];
      const top = segments[0];
      return [
        { label: "Total revenue", value: money(get(metrics, "total_revenue")) },
        { label: "Customers", value: num(get(metrics, "customer_count")) },
        { label: "Top segment", value: String(top?.name ?? "—") },
        {
          label: "M1 retention",
          value: typeof get(metrics, "top_cohort_retention_pct_m1") === "number"
            ? `${(get(metrics, "top_cohort_retention_pct_m1") as number).toFixed(1)}%`
            : "—",
        },
      ];
    }
    case "operations": {
      const skus = (get(metrics, "skus") as Array<Record<string, unknown>>) ?? [];
      return [
        { label: "SKUs covered", value: String(skus.length) },
        { label: "12-mo total units", value: num(get(metrics, "total_forecast_units")) },
        {
          label: "Avg reorder point",
          value: skus.length
            ? Math.round(
                skus.reduce((s, x) => s + ((x.reorder_point as number) ?? 0), 0) /
                  skus.length
              ).toString()
            : "—",
        },
        {
          label: "Avg EOQ",
          value: skus.length
            ? Math.round(
                skus.reduce((s, x) => s + ((x.eoq as number) ?? 0), 0) / skus.length
              ).toString()
            : "—",
        },
      ];
    }
    case "strategy": {
      const scenarios = (get(metrics, "scenarios") as Array<Record<string, unknown>>) ?? [];
      const find = (n: string) =>
        scenarios.find((s) => s.name === n)?.revenue_5y as number | undefined;
      const sens = (get(metrics, "sensitivity") as Array<Record<string, unknown>>) ?? [];
      return [
        { label: "Best case", value: money(find("best")), tone: "good" },
        { label: "Base case", value: money(find("base")) },
        { label: "Worst case", value: money(find("worst")), tone: "bad" },
        { label: "Top driver", value: String(sens[0]?.input ?? "—") },
      ];
    }
  }
}
