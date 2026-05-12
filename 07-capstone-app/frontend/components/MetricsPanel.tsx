"use client";

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";

interface Props {
  metrics: Record<string, unknown>;
}

function formatValue(v: unknown): string {
  if (typeof v === "number") {
    if (Number.isInteger(v) && Math.abs(v) < 1000) return v.toString();
    if (Math.abs(v) >= 1000) return v.toLocaleString();
    return v.toFixed(3);
  }
  if (Array.isArray(v)) return `${v.length} items`;
  if (typeof v === "object" && v !== null) return "{...}";
  return String(v);
}

function flatten(
  obj: Record<string, unknown>,
  prefix = ""
): { key: string; value: unknown }[] {
  const out: { key: string; value: unknown }[] = [];
  for (const [k, v] of Object.entries(obj)) {
    const full = prefix ? `${prefix}.${k}` : k;
    if (Array.isArray(v) && v.every((x) => typeof x === "object")) {
      out.push({ key: full, value: v });
    } else if (typeof v === "object" && v !== null && !Array.isArray(v)) {
      out.push(...flatten(v as Record<string, unknown>, full));
    } else {
      out.push({ key: full, value: v });
    }
  }
  return out;
}

export function MetricsPanel({ metrics }: Props) {
  const rows = flatten(metrics);

  return (
    <Card>
      <CardHeader className="flex flex-row items-center justify-between gap-4">
        <CardTitle className="text-base">All metrics</CardTitle>
        <Badge variant="outline">{rows.length} fields</Badge>
      </CardHeader>
      <CardContent>
        <div className="grid grid-cols-1 gap-2 sm:grid-cols-2">
          {rows.map((row) => (
            <div
              key={row.key}
              className="group flex items-baseline justify-between rounded-md border bg-muted/30 px-3 py-2 transition-colors hover:bg-muted/60"
            >
              <span className="truncate text-xs font-mono text-muted-foreground">
                {row.key}
              </span>
              <span className="ml-2 font-mono text-sm tabular-nums">
                {formatValue(row.value)}
              </span>
            </div>
          ))}
        </div>
      </CardContent>
    </Card>
  );
}
