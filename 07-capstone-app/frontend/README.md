# Capstone Frontend (Next.js + shadcn/ui)

This is the **fully-built** part of the capstone. It already:

- Lets you upload an `.xlsx`.
- Lets you pick a domain (Finance / Marketing / Operations / Strategy).
- Calls the backend's `/upload`, `/analyze`, `/summarize`, `/report` endpoints.
- Renders metrics, AI summary, and a download button.

You **shouldn't need to edit anything here** to ship the capstone. Optional polish only.

## Stack

- **Next.js 14** (App Router) — React framework.
- **Tailwind CSS** — utility-first styling.
- **shadcn/ui** — accessible component primitives. Sources are in [`components/ui/`](components/ui/).
- **TypeScript** — typed everywhere.

## Run locally

```bash
cd 07-capstone-app/frontend
npm install
npm run dev
```

Open http://localhost:3000.

The frontend expects the backend at `http://localhost:8000` by default. Override via `.env.local`:

```
NEXT_PUBLIC_API_BASE=http://localhost:8000
```

## Folder structure

```
frontend/
├── app/
│   ├── layout.tsx
│   ├── page.tsx          ← the whole app — single page, top to bottom
│   └── globals.css
├── components/
│   ├── ui/               ← shadcn primitives (button, card, select, …)
│   ├── UploadCard.tsx
│   ├── DomainPicker.tsx
│   ├── MetricsPanel.tsx
│   └── SummaryPanel.tsx
├── lib/
│   ├── api.ts            ← typed wrapper around the backend
│   └── utils.ts          ← `cn` helper used by shadcn
├── package.json
├── tailwind.config.ts
├── tsconfig.json
└── next.config.mjs
```

## Build for production

```bash
npm run build
npm start
```

## Deploy to Vercel

```bash
npx vercel
```

Set `NEXT_PUBLIC_API_BASE` in the Vercel project settings to your deployed backend URL.

## What you might tweak

- Theme colors in [`app/globals.css`](app/globals.css).
- Brand name in [`app/layout.tsx`](app/layout.tsx) `metadata`.
- Charting: the basic implementation uses `<svg>` directly. Add `recharts` if you want fancier visuals.

That's it — focus on the backend.
