"use client";

import { Badge } from "@/components/ui/badge";
import { Sparkles } from "lucide-react";

interface Props {
  summary: string;
  model: string;
}

export function SummaryPanel({ summary, model }: Props) {
  return (
    <div className="rounded-xl border bg-gradient-to-br from-primary/5 via-background to-background p-6">
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-2">
          <Sparkles className="h-4 w-4 text-primary" />
          <h3 className="font-semibold">AI Executive Summary</h3>
        </div>
        <Badge variant="secondary" className="font-mono text-[10px]">
          {model}
        </Badge>
      </div>
      <pre className="mt-4 whitespace-pre-wrap font-sans text-sm leading-relaxed text-foreground">
        {summary}
      </pre>
    </div>
  );
}
