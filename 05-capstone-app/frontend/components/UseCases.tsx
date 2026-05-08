"use client";

import {
  Briefcase,
  FileSearch,
  Mail,
  Newspaper,
  ScanLine,
  Store,
} from "lucide-react";
import { Card, CardContent } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";

const USE_CASES = [
  {
    icon: FileSearch,
    title: "Financial red-flag screener",
    pitch:
      "Upload P&L + balance sheet for 50 Nifty 500 firms. Surface receivables-vs-revenue spikes, hidden leverage, profit-without-cash anomalies.",
    tags: ["Finance", "Equity research"],
    difficulty: "Beginner",
  },
  {
    icon: Briefcase,
    title: "Consulting intern automator",
    pitch:
      "Market-size any sector (\"EV chargers in India\") with structured TAM/SAM/SOM, assumptions table, and a McKinsey-style one-pager.",
    tags: ["Strategy", "Consulting"],
    difficulty: "Intermediate",
  },
  {
    icon: ScanLine,
    title: "Resume screener for HR",
    pitch:
      "Upload JD criteria + resume text. AI scores, ranks, explains — pitch this to your placement cell as a real portfolio piece.",
    tags: ["HR", "AI"],
    difficulty: "Beginner",
  },
  {
    icon: Store,
    title: "SME cash-flow tracker",
    pitch:
      "Most kirana / cloud-kitchen / boutique owners have zero cash visibility. Daily entries → weekly projections → simple risk flags.",
    tags: ["SME", "Finance"],
    difficulty: "Beginner",
  },
  {
    icon: Newspaper,
    title: "Equity research agent",
    pitch:
      "Ticker → fetched financials + news → ratios + sentiment → structured research note. Compare to a real analyst report.",
    tags: ["Finance", "AI agent"],
    difficulty: "Advanced",
  },
  {
    icon: Mail,
    title: "MIS report automator",
    pitch:
      "Take ERP data dumps. Auto-clean, auto-pivot, auto-chart. Reuse the polished xlsx output flow you already built.",
    tags: ["Operations", "Reporting"],
    difficulty: "Intermediate",
  },
];

const diffTone: Record<string, string> = {
  Beginner:
    "bg-emerald-50 text-emerald-700 dark:bg-emerald-500/10 dark:text-emerald-400",
  Intermediate:
    "bg-amber-50 text-amber-700 dark:bg-amber-500/10 dark:text-amber-400",
  Advanced:
    "bg-rose-50 text-rose-700 dark:bg-rose-500/10 dark:text-rose-400",
};

export function UseCases() {
  return (
    <section className="mt-16">
      <div className="mb-6 flex items-end justify-between">
        <div>
          <div className="text-xs uppercase tracking-wide text-muted-foreground">
            Extend this app
          </div>
          <h2 className="mt-1 text-2xl font-semibold tracking-tight">
            Build something real for your MBA portfolio
          </h2>
          <p className="mt-1 max-w-2xl text-sm text-muted-foreground">
            Each idea below reuses the same backend pattern — drop in a new
            pipeline module, point the frontend at it, ship.
          </p>
        </div>
      </div>

      <div className="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
        {USE_CASES.map(({ icon: Icon, title, pitch, tags, difficulty }) => (
          <Card key={title} className="flex flex-col">
            <CardContent className="flex flex-1 flex-col gap-3 pt-6">
              <div className="flex items-center gap-2">
                <div className="flex h-8 w-8 items-center justify-center rounded-md bg-primary/10 text-primary">
                  <Icon className="h-4 w-4" />
                </div>
                <span
                  className={`rounded-full px-2 py-0.5 text-[10px] font-semibold uppercase tracking-wide ${diffTone[difficulty]}`}
                >
                  {difficulty}
                </span>
              </div>
              <div>
                <h3 className="font-semibold">{title}</h3>
                <p className="mt-1 text-sm text-muted-foreground">{pitch}</p>
              </div>
              <div className="mt-auto flex flex-wrap gap-1.5 pt-2">
                {tags.map((t) => (
                  <Badge key={t} variant="outline" className="font-normal">
                    {t}
                  </Badge>
                ))}
              </div>
            </CardContent>
          </Card>
        ))}
      </div>
    </section>
  );
}
