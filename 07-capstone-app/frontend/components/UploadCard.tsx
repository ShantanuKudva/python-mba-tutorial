"use client";

import * as React from "react";
import { FileSpreadsheet, Upload, X } from "lucide-react";
import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";

interface Props {
  file: File | null;
  onChange: (file: File | null) => void;
  disabled?: boolean;
}

export function UploadCard({ file, onChange, disabled }: Props) {
  const inputRef = React.useRef<HTMLInputElement>(null);
  const [dragOver, setDragOver] = React.useState(false);

  const onDrop = (e: React.DragEvent) => {
    e.preventDefault();
    setDragOver(false);
    if (disabled) return;
    const f = e.dataTransfer.files[0];
    if (f) onChange(f);
  };

  return (
    <div
      onDragOver={(e) => {
        e.preventDefault();
        setDragOver(true);
      }}
      onDragLeave={() => setDragOver(false)}
      onDrop={onDrop}
      className={cn(
        "relative flex flex-col items-center justify-center gap-3 rounded-xl border-2 border-dashed p-10 text-center transition-colors",
        dragOver
          ? "border-primary bg-primary/5"
          : "border-muted-foreground/30 hover:border-muted-foreground/50",
        disabled && "opacity-60"
      )}
    >
      <input
        ref={inputRef}
        type="file"
        accept=".xlsx,.xls"
        className="hidden"
        onChange={(e) => onChange(e.target.files?.[0] ?? null)}
      />

      {file ? (
        <div className="flex items-center gap-3">
          <FileSpreadsheet className="h-6 w-6 text-primary" />
          <div className="text-sm">
            <div className="font-medium">{file.name}</div>
            <div className="text-muted-foreground">
              {(file.size / 1024).toFixed(1)} KB
            </div>
          </div>
          <Button
            variant="ghost"
            size="icon"
            disabled={disabled}
            onClick={() => onChange(null)}
            aria-label="Remove file"
          >
            <X className="h-4 w-4" />
          </Button>
        </div>
      ) : (
        <>
          <Upload className="h-8 w-8 text-muted-foreground" />
          <div className="text-sm">
            <div className="font-medium">Drag an .xlsx here</div>
            <div className="text-muted-foreground">or click to browse</div>
          </div>
          <Button
            type="button"
            variant="outline"
            disabled={disabled}
            onClick={() => inputRef.current?.click()}
          >
            Choose file
          </Button>
        </>
      )}
    </div>
  );
}
