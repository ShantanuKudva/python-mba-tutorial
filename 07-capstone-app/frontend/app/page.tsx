"use client";

import * as React from "react";
import {
  AnalyzeResponse,
  Domain,
  SummarizeResponse,
  UploadResponse,
  analyze,
  reportUrl,
  summarize,
  uploadFile,
} from "@/lib/api";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Skeleton } from "@/components/ui/skeleton";
import { Badge } from "@/components/ui/badge";
import {
  AlertTriangle,
  BarChart3,
  Download,
  Github,
  Loader2,
  RotateCcw,
  Sparkles,
  Wand2,
} from "lucide-react";
import { UploadCard } from "@/components/UploadCard";
import { DomainPicker } from "@/components/DomainPicker";
import { MetricsPanel } from "@/components/MetricsPanel";
import { SummaryPanel } from "@/components/SummaryPanel";
import { Stepper, type StepState } from "@/components/Stepper";
import { StatsRow } from "@/components/StatsRow";
import { ThemeToggle } from "@/components/ThemeToggle";
import { EmptyState } from "@/components/EmptyState";
import { UseCases } from "@/components/UseCases";
import { deriveStats } from "@/lib/derive";

type Phase = "idle" | "uploading" | "analyzing" | "summarizing" | "done" | "error";

export default function Home() {
  const [file, setFile] = React.useState<File | null>(null);
  const [domain, setDomain] = React.useState<Domain>("finance");

  const [phase, setPhase] = React.useState<Phase>("idle");
  const [error, setError] = React.useState<string | null>(null);

  const [uploaded, setUploaded] = React.useState<UploadResponse | null>(null);
  const [analysis, setAnalysis] = React.useState<AnalyzeResponse | null>(null);
  const [summary, setSummary] = React.useState<SummarizeResponse | null>(null);

  const busy = phase === "uploading" || phase === "analyzing" || phase === "summarizing";

  function reset(hard = false) {
    setUploaded(null);
    setAnalysis(null);
    setSummary(null);
    setError(null);
    setPhase("idle");
    if (hard) setFile(null);
  }

  async function run() {
    if (!file) return;
    reset();
    try {
      setPhase("uploading");
      const u = await uploadFile(file);
      setUploaded(u);

      setPhase("analyzing");
      const a = await analyze(u.file_id, domain);
      setAnalysis(a);

      setPhase("summarizing");
      const s = await summarize(u.file_id);
      setSummary(s);

      setPhase("done");
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e));
      setPhase("error");
    }
  }

  const stepState = (n: 1 | 2 | 3): StepState => {
    if (phase === "error") return n === 1 ? "active" : "pending";
    if (phase === "uploading") return n === 1 ? "active" : "pending";
    if (phase === "analyzing")
      return n < 2 ? "done" : n === 2 ? "active" : "pending";
    if (phase === "summarizing") return n < 3 ? "done" : "active";
    if (phase === "done") return "done";
    return "pending";
  };

  return (
    <div className="relative min-h-screen">
      {/* Decorative background */}
      <div className="pointer-events-none absolute inset-x-0 top-0 -z-10 h-[420px] bg-gradient-to-b from-primary/10 via-primary/[0.04] to-transparent" />

      {/* Top nav */}
      <header className="border-b bg-background/70 backdrop-blur supports-[backdrop-filter]:bg-background/50">
        <div className="container flex h-14 max-w-6xl items-center justify-between">
          <div className="flex items-center gap-2">
            <div className="flex h-7 w-7 items-center justify-center rounded-md bg-primary text-primary-foreground">
              <BarChart3 className="h-4 w-4" />
            </div>
            <span className="font-semibold tracking-tight">Excel Insights</span>
            <Badge variant="outline" className="ml-2 hidden sm:inline-flex">
              Capstone · weeks 11–12
            </Badge>
          </div>
          <div className="flex items-center gap-2">
            <Button
              asChild
              variant="ghost"
              size="sm"
              className="hidden sm:inline-flex"
            >
              <a
                href="https://github.com/"
                target="_blank"
                rel="noreferrer"
                aria-label="Source"
              >
                <Github className="h-4 w-4" />
                Source
              </a>
            </Button>
            <ThemeToggle />
          </div>
        </div>
      </header>

      <main className="container max-w-6xl py-10">
        {/* Hero */}
        <section className="mb-10 text-center md:text-left">
          <Badge className="mb-3" variant="secondary">
            <Sparkles className="mr-1 h-3 w-3" /> Powered by Groq
          </Badge>
          <h1 className="text-3xl font-semibold tracking-tight md:text-4xl">
            Turn any Excel file into{" "}
            <span className="bg-gradient-to-r from-primary to-foreground bg-clip-text text-transparent">
              executive insight
            </span>
            .
          </h1>
          <p className="mt-3 max-w-2xl text-muted-foreground md:text-lg">
            Upload a workbook, pick a domain, get computed metrics, an
            AI-written summary, and a polished report — in seconds.
          </p>
        </section>

        {/* Stepper */}
        <div className="mb-6">
          <Stepper
            steps={[
              { label: "Upload", state: stepState(1) },
              { label: "Analyze", state: stepState(2) },
              { label: "Summarize", state: stepState(3) },
            ]}
          />
        </div>

        {/* Inputs */}
        <Card className="mb-8 overflow-hidden">
          <CardHeader>
            <CardTitle>Configure your run</CardTitle>
          </CardHeader>
          <CardContent className="space-y-6">
            <div className="grid grid-cols-1 gap-6 lg:grid-cols-[1fr_320px]">
              <UploadCard file={file} onChange={setFile} disabled={busy} />
              <div className="space-y-6">
                <DomainPicker
                  value={domain}
                  onChange={setDomain}
                  disabled={busy}
                />
                <div className="flex flex-wrap items-center gap-3">
                  <Button
                    onClick={run}
                    disabled={!file || busy}
                    size="lg"
                    className="min-w-[180px]"
                  >
                    {busy ? (
                      <>
                        <Loader2 className="h-4 w-4 animate-spin" />
                        {phase === "uploading"
                          ? "Uploading…"
                          : phase === "analyzing"
                          ? "Analyzing…"
                          : "Summarizing…"}
                      </>
                    ) : (
                      <>
                        <Wand2 className="h-4 w-4" />
                        Run analysis
                      </>
                    )}
                  </Button>
                  {(analysis || error) && (
                    <Button
                      onClick={() => reset(true)}
                      variant="outline"
                      size="lg"
                      disabled={busy}
                    >
                      <RotateCcw className="h-4 w-4" />
                      Reset
                    </Button>
                  )}
                  {uploaded && (
                    <span className="font-mono text-xs text-muted-foreground">
                      file_id: {uploaded.file_id}
                    </span>
                  )}
                </div>
              </div>
            </div>
          </CardContent>
        </Card>

        {error && (
          <Alert variant="destructive" className="mb-8">
            <AlertTriangle className="h-4 w-4" />
            <AlertTitle>Something went wrong</AlertTitle>
            <AlertDescription className="break-words">{error}</AlertDescription>
          </Alert>
        )}

        {!analysis && !busy && !error && <EmptyState />}

        {busy && !analysis && (
          <div className="space-y-4">
            <div className="grid grid-cols-2 gap-3 md:grid-cols-4">
              {Array.from({ length: 4 }).map((_, i) => (
                <Skeleton key={i} className="h-[88px]" />
              ))}
            </div>
            <Skeleton className="h-[260px]" />
          </div>
        )}

        {analysis && (
          <section className="space-y-6">
            <div className="flex flex-wrap items-end justify-between gap-3">
              <div>
                <div className="text-xs uppercase tracking-wide text-muted-foreground">
                  Headline
                </div>
                <p className="text-lg font-medium">{analysis.headline}</p>
              </div>
              <Badge className="capitalize">{analysis.domain}</Badge>
            </div>

            <StatsRow stats={deriveStats(analysis.domain, analysis.metrics)} />

            <Tabs defaultValue="summary" className="w-full">
              <TabsList>
                <TabsTrigger value="summary">
                  <Sparkles className="h-3.5 w-3.5" /> Summary
                </TabsTrigger>
                <TabsTrigger value="metrics">
                  <BarChart3 className="h-3.5 w-3.5" /> Metrics
                </TabsTrigger>
                <TabsTrigger value="download">
                  <Download className="h-3.5 w-3.5" /> Download
                </TabsTrigger>
              </TabsList>

              <TabsContent value="summary">
                {summary ? (
                  <SummaryPanel
                    summary={summary.summary}
                    model={summary.model}
                  />
                ) : (
                  <Skeleton className="h-[260px]" />
                )}
              </TabsContent>

              <TabsContent value="metrics">
                <MetricsPanel metrics={analysis.metrics} />
              </TabsContent>

              <TabsContent value="download">
                <Card>
                  <CardContent className="flex flex-col items-start gap-3 pt-6">
                    <div>
                      <div className="font-semibold">Polished xlsx report</div>
                      <p className="text-sm text-muted-foreground">
                        Multi-sheet workbook with the metrics, AI summary, and
                        original data preserved for traceability.
                      </p>
                    </div>
                    <Button asChild size="lg" disabled={!uploaded}>
                      <a
                        href={uploaded ? reportUrl(uploaded.file_id) : "#"}
                        download
                      >
                        <Download className="h-4 w-4" />
                        Download .xlsx
                      </a>
                    </Button>
                  </CardContent>
                </Card>
              </TabsContent>
            </Tabs>
          </section>
        )}

        <UseCases />
      </main>

      <footer className="mt-16 border-t">
        <div className="container flex max-w-6xl flex-col items-center justify-between gap-2 py-6 text-xs text-muted-foreground sm:flex-row">
          <span>
            Packaged by{" "}
            <span className="font-medium text-foreground">Shantanu</span>.
          </span>
          <span>Next.js · shadcn/ui · FastAPI · Groq</span>
        </div>
      </footer>
    </div>
  );
}
