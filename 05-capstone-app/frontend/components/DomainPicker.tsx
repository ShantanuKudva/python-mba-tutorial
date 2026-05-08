"use client";

import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Label } from "@/components/ui/label";
import type { Domain } from "@/lib/api";

interface Props {
  value: Domain;
  onChange: (d: Domain) => void;
  disabled?: boolean;
}

const OPTIONS: { value: Domain; label: string; hint: string }[] = [
  {
    value: "finance",
    label: "Finance — Red-flag screener",
    hint: "Ratios, leverage, margin compression, health score",
  },
  {
    value: "marketing",
    label: "Marketing — Customer concentration",
    hint: "RFM segments, cohort retention, top-segment risk",
  },
  {
    value: "operations",
    label: "Operations — Demand forecast",
    hint: "12-month forecast, EOQ, reorder point",
  },
  {
    value: "strategy",
    label: "Strategy — Market sizing & sensitivity",
    hint: "Best/base/worst, tornado, top driver",
  },
];

export function DomainPicker({ value, onChange, disabled }: Props) {
  return (
    <div className="space-y-2">
      <Label htmlFor="domain">Analysis domain</Label>
      <Select
        value={value}
        onValueChange={(v) => onChange(v as Domain)}
        disabled={disabled}
      >
        <SelectTrigger id="domain">
          <SelectValue />
        </SelectTrigger>
        <SelectContent>
          {OPTIONS.map((opt) => (
            <SelectItem key={opt.value} value={opt.value}>
              <div className="flex flex-col">
                <span>{opt.label}</span>
                <span className="text-xs text-muted-foreground">
                  {opt.hint}
                </span>
              </div>
            </SelectItem>
          ))}
        </SelectContent>
      </Select>
    </div>
  );
}
