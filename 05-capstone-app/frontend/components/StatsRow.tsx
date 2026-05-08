"use client";

import { Card } from "@/components/ui/card";
import { cn } from "@/lib/utils";

interface Stat {
  label: string;
  value: string;
  hint?: string;
  tone?: "default" | "good" | "warn" | "bad";
}

interface Props {
  stats: Stat[];
}

const toneClass: Record<NonNullable<Stat["tone"]>, string> = {
  default: "text-foreground",
  good: "text-emerald-600 dark:text-emerald-400",
  warn: "text-amber-600 dark:text-amber-400",
  bad: "text-rose-600 dark:text-rose-400",
};

export function StatsRow({ stats }: Props) {
  if (stats.length === 0) return null;
  return (
    <div className="grid grid-cols-2 gap-3 md:grid-cols-4">
      {stats.map((s) => (
        <Card key={s.label} className="p-4">
          <div className="text-xs uppercase tracking-wide text-muted-foreground">
            {s.label}
          </div>
          <div
            className={cn(
              "mt-1 text-2xl font-semibold tabular-nums",
              toneClass[s.tone ?? "default"]
            )}
          >
            {s.value}
          </div>
          {s.hint && (
            <div className="mt-1 text-xs text-muted-foreground">{s.hint}</div>
          )}
        </Card>
      ))}
    </div>
  );
}

export type { Stat };
