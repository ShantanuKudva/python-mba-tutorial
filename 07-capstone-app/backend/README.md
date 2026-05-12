# Capstone Backend (FastAPI)

The backend is a FastAPI app that exposes four endpoints. Every endpoint is **already wired** but returns mock data. Your job over weeks 11–12 is to replace each mock with real pandas + Groq logic from earlier weeks.

## Endpoints

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/upload` | Receive `.xlsx`, return file_id |
| `POST` | `/analyze` | Run domain pipeline → metrics + chart |
| `POST` | `/summarize` | Send metrics to Groq → narrative |
| `GET`  | `/report/{file_id}` | Return generated `.xlsx` |
| `GET`  | `/health` | Liveness check |

## Folder structure

```
backend/
├── README.md                ← this file
├── main.py                  ← FastAPI app, CORS, mount routers
├── requirements.txt
├── .env.example             ← copy to .env, fill GROQ_API_KEY
├── store.py                 ← in-memory file store (NOT for prod)
├── routers/
│   ├── upload.py
│   ├── analyze.py
│   ├── summarize.py
│   └── report.py
├── pipelines/               ← domain logic (finance, marketing, ops, strategy)
│   ├── finance.py
│   ├── marketing.py
│   ├── operations.py
│   └── strategy.py
├── llm/
│   └── groq_client.py
└── reports/                 ← (generated at runtime, .gitignored)
```

## Install + run

```bash
cd 07-capstone-app/backend
python -m venv .venv
source .venv/bin/activate         # macOS/Linux
.venv\Scripts\activate            # Windows

pip install -r requirements.txt

cp .env.example .env              # then edit and add GROQ_API_KEY

uvicorn main:app --reload --port 8000
```

Visit http://localhost:8000/docs for the auto-generated Swagger UI. You can test each endpoint directly there.

## What's a "stub"?

Every router and pipeline module starts with code that returns plausible mock data, marked with `# TODO:` comments. The app runs end-to-end immediately; you replace stubs in any order.

Suggested order:

1. **`pipelines/finance.py`** — easiest. Reuse `health.py` from week 6.
2. **`routers/analyze.py`** — wire it to call `pipelines/{domain}.py`.
3. **`pipelines/marketing.py`**, **`operations.py`**, **`strategy.py`**.
4. **`llm/groq_client.py`** — port week 10 code.
5. **`routers/summarize.py`** — call the Groq client.
6. **`routers/report.py`** — write a polished xlsx using openpyxl.

## Testing as you go

```bash
curl -X POST -F "file=@datasets/finance/sample_pl.xlsx" http://localhost:8000/upload
curl -X POST -H "Content-Type: application/json" \
  -d '{"file_id":"<id>","domain":"finance"}' \
  http://localhost:8000/analyze
```

Or just use Swagger at `/docs`.
