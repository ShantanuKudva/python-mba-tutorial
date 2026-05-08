"use client";

import { Check, Loader2 } from "lucide-react";
import { cn } from "@/lib/utils";

export type StepState = "pending" | "active" | "done";

interface Step {
  label: string;
  state: StepState;
}

interface Props {
  steps: Step[];
}

export function Stepper({ steps }: Props) {
  return (
    <ol className="flex flex-wrap items-center gap-2">
      {steps.map((step, i) => {
        const isLast = i === steps.length - 1;
        return (
          <li key={step.label} className="flex items-center gap-2">
            <div
              className={cn(
                "flex h-7 w-7 items-center justify-center rounded-full border text-xs font-semibold transition-colors",
                step.state === "done" &&
                  "border-primary bg-primary text-primary-foreground",
                step.state === "active" &&
                  "border-primary bg-background text-primary",
                step.state === "pending" &&
                  "border-muted-foreground/30 bg-background text-muted-foreground"
              )}
            >
              {step.state === "done" ? (
                <Check className="h-3.5 w-3.5" />
              ) : step.state === "active" ? (
                <Loader2 className="h-3.5 w-3.5 animate-spin" />
              ) : (
                i + 1
              )}
            </div>
            <span
              className={cn(
                "text-sm",
                step.state === "pending"
                  ? "text-muted-foreground"
                  : "font-medium text-foreground"
              )}
            >
              {step.label}
            </span>
            {!isLast && (
              <div
                className={cn(
                  "mx-1 h-px w-8 transition-colors",
                  step.state === "done" ? "bg-primary" : "bg-border"
                )}
              />
            )}
          </li>
        );
      })}
    </ol>
  );
}
