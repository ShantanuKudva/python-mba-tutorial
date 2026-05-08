"use client";

import { FileSpreadsheet, Sparkles, Download } from "lucide-react";
import { Card, CardContent } from "@/components/ui/card";

const ITEMS = [
  {
    icon: FileSpreadsheet,
    title: "Drop in any .xlsx",
    body: "Finance ratios, customer orders, demand history, scenario inputs.",
  },
  {
    icon: Sparkles,
    title: "AI-written summary",
    body: "Groq turns your numbers into 5 bullet executive insight.",
  },
  {
    icon: Download,
    title: "Polished report",
    body: "Download a multi-sheet xlsx ready to share with stakeholders.",
  },
];

export function EmptyState() {
  return (
    <div className="grid grid-cols-1 gap-4 md:grid-cols-3">
      {ITEMS.map(({ icon: Icon, title, body }) => (
        <Card key={title} className="border-dashed">
          <CardContent className="pt-6">
            <Icon className="h-5 w-5 text-primary" />
            <h3 className="mt-3 font-semibold">{title}</h3>
            <p className="mt-1 text-sm text-muted-foreground">{body}</p>
          </CardContent>
        </Card>
      ))}
    </div>
  );
}
