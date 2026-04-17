# Nielsen RMS Intelligence — Demo Edition

Zero-config, single-service demo for showcasing the Nielsen RMS Intelligence Platform to stakeholders.

**What this is:** A fully working demonstrator with 5 dashboards + AI chatbot, using synthetic SLMG data. No database setup, no local installation. Deploys to Railway in ~3 minutes.

**What this isn't:** The production system. For the real version (Excel ingestion, DuckDB persistence, anomaly engine on live data, local Ollama option), see the main project.

---

## Deploy to Railway — 3 steps

### 1. Push this folder to GitHub

- Create a new repo on GitHub (e.g. `nielsen-demo`)
- Upload all files using GitHub Desktop or:

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USER/nielsen-demo.git
git push -u origin main
```

### 2. Deploy on Railway

- Go to [railway.app](https://railway.app) → **New Project** → **Deploy from GitHub repo**
- Select your repository
- Railway auto-detects the Dockerfile and builds. Wait ~2 minutes.

### 3. Set the Anthropic API key

- In Railway → your service → **Variables** tab
- Add: `ANTHROPIC_API_KEY` = your key from [console.anthropic.com](https://console.anthropic.com)
- The service will auto-redeploy

### 4. Generate a public URL

- Railway → your service → **Settings** → **Networking** → **Generate Domain**
- Copy the URL (e.g. `https://nielsen-demo-abc.railway.app`) — that's your live app

Done. Share the URL.

---

## Architecture

```
Single Railway service
┌─────────────────────────────────┐
│  FastAPI (port 8000)            │
│                                 │
│  /api/*         → JSON API      │
│  /              → React SPA     │
│                                 │
│  Synthetic SLMG data baked in   │
│  (demo_data.py)                 │
│                                 │
│  Chatbot → Anthropic API        │
└─────────────────────────────────┘
```

No database. No separate frontend build. Everything runs from one container.

---

## What's in the demo

- **Portfolio view** — TCCC KPIs, brand-owner share, live anomaly strip
- **Brand Dive** — select any brand × zone, see 4-period MS / WD / SPPD / RR trends
- **Geography** — zone scorecard with automatic status flags
- **Anomalies** — 6 pre-configured anomalies (Leaky Bucket, Competitor Surge, Hidden Gem, etc.) with recommended actions
- **AI Analyst** — live chatbot connected to Anthropic Claude, with the full SLMG context embedded

---

## Local run (optional)

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...
cd app && uvicorn main:app --reload
# → http://localhost:8000
```

---

## Files

```
nielsen-demo/
├── Dockerfile              Single-container build
├── railway.toml            Railway deployment config
├── Procfile                Fallback start command
├── requirements.txt        5 Python dependencies (fastapi, uvicorn, requests, pydantic, multipart)
├── .gitignore
├── README.md
└── app/
    ├── main.py             FastAPI app — API + static SPA serving
    ├── demo_data.py        Synthetic SLMG dataset
    ├── prompts.py          AI Analyst system prompt (full SLMG context)
    └── static/
        └── index.html      Single-file React app (CDN React + Recharts, no build)
```

---

## Going from demo to production

When you're ready to use real data:

1. Replace `demo_data.py` with a real ingestion pipeline (see the main project's `backend/ingest.py`)
2. Swap in DuckDB + ChromaDB for persistence
3. Add the `/api/ingest` endpoint for monthly Excel uploads
4. Deploy with a Railway volume for data persistence
5. Optionally swap Anthropic for a local Ollama instance for full offline operation

The API contract stays identical — the frontend needs no changes.
