import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Excel Insights",
  description:
    "Upload an Excel workbook. Get metrics, AI-written executive summary, and a polished report.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className="min-h-screen antialiased">{children}</body>
    </html>
  );
}
