/**
 * Typed wrapper around the FastAPI backend.
 * Override the base URL with NEXT_PUBLIC_API_BASE.
 */

export const API_BASE =
  process.env.NEXT_PUBLIC_API_BASE || "http://localhost:8000";

export type Domain = "finance" | "marketing" | "operations" | "strategy";

export interface UploadResponse {
  file_id: string;
  original_name: string;
  size_bytes: number;
}

export interface AnalyzeResponse {
  file_id: string;
  domain: Domain;
  metrics: Record<string, unknown>;
  headline: string;
}

export interface SummarizeResponse {
  file_id: string;
  summary: string;
  model: string;
}

async function asJson<T>(res: Response): Promise<T> {
  if (!res.ok) {
    const text = await res.text();
    throw new Error(`${res.status} ${res.statusText} — ${text}`);
  }
  return res.json() as Promise<T>;
}

export async function uploadFile(file: File): Promise<UploadResponse> {
  const form = new FormData();
  form.append("file", file);
  const res = await fetch(`${API_BASE}/upload`, {
    method: "POST",
    body: form,
  });
  return asJson<UploadResponse>(res);
}

export async function analyze(
  file_id: string,
  domain: Domain
): Promise<AnalyzeResponse> {
  const res = await fetch(`${API_BASE}/analyze`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ file_id, domain }),
  });
  return asJson<AnalyzeResponse>(res);
}

export async function summarize(
  file_id: string,
  focus?: string
): Promise<SummarizeResponse> {
  const res = await fetch(`${API_BASE}/summarize`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ file_id, focus }),
  });
  return asJson<SummarizeResponse>(res);
}

export function reportUrl(file_id: string): string {
  return `${API_BASE}/report/${file_id}`;
}
