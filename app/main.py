"""
Nielsen RMS Intelligence — Demo Version
Single FastAPI service that serves both the API and the React frontend.
Uses synthetic SLMG data. Chatbot uses Anthropic Claude API.
Zero setup, zero database, zero local installation.
"""

import os, json
from pathlib import Path
from typing import AsyncGenerator

import requests
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

import demo_data as D
from prompts import SYSTEM_PROMPT

ANTHROPIC_KEY = os.getenv("ANTHROPIC_API_KEY", "")
STATIC_DIR    = Path(__file__).parent / "static"

app = FastAPI(title="Nielsen RMS Intelligence — Demo", version="1.0.0")

# CORS — permissive in demo since everything comes from the same origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=False,
    allow_methods=["*"], allow_headers=["*"],
)

# ── META ──────────────────────────────────────────────────────────────────────

@app.get("/api/meta/periods")
def get_periods():
    return [{"period_label": p, "period_end_date": None} for p in D.PERIODS]

@app.get("/api/meta/brands")
def get_brands(tccc_only: bool = Query(False)):
    return D.TCCC_BRANDS if tccc_only else D.ALL_BRANDS

@app.get("/api/meta/zones")
def get_zones():
    return D.ZONES

# ── DASHBOARD ─────────────────────────────────────────────────────────────────

@app.get("/api/dashboard/portfolio")
def portfolio_summary(period: str = Query(...), zone: str = Query("SLMG Total"),
                      category_group: str | None = Query(None)):
    data = D.PORTFOLIO.get((period, zone))
    if not data:
        # Return SLMG Total as fallback
        data = D.PORTFOLIO.get((period, "SLMG Total"), {})
    return {"period": period, "zone": zone, **data}

@app.get("/api/dashboard/brand")
def brand_metrics(brand: str = Query(...), periods: str = Query(...),
                  zone: str = Query("SLMG Total")):
    brand_data = D.BRAND_METRICS.get(brand, {})
    zone_data  = brand_data.get(zone, brand_data.get("SLMG Total", []))
    period_list = [p.strip() for p in periods.split(",")]
    return [
        {"brand": brand, "zone": zone, **row}
        for row in zone_data if row["period"] in period_list
    ]

@app.get("/api/dashboard/brand-owners")
def brand_owner_share(period: str = Query(...), zone: str = Query("SLMG Total")):
    return D.BRAND_OWNER_SHARE.get((period, zone),
                                    D.BRAND_OWNER_SHARE.get(("Mar 26", "SLMG Total"), []))

@app.get("/api/dashboard/geo")
def geo_scorecard(period: str = Query(...)):
    return D.GEO_SCORECARD.get(period, D.GEO_SCORECARD["Mar 26"])

@app.get("/api/dashboard/anomalies")
def get_anomalies(current_period: str = Query(...),
                  prior_period: str | None = Query(None),
                  ly_period: str | None = Query(None)):
    return D.ANOMALIES

# ── CHATBOT (Anthropic API) ───────────────────────────────────────────────────

class ChatRequest(BaseModel):
    question: str
    history: list[dict] = []

def _anthropic_headers() -> dict:
    h = {"Content-Type": "application/json", "anthropic-version": "2023-06-01"}
    if ANTHROPIC_KEY:
        h["x-api-key"] = ANTHROPIC_KEY
    return h

@app.post("/api/chat")
def chat(req: ChatRequest):
    if not ANTHROPIC_KEY:
        return {"answer": "⚠ Anthropic API key not configured. Set the ANTHROPIC_API_KEY environment variable in Railway."}
    try:
        history = req.history or []
        # Strip any extra fields the client might send
        msgs = [{"role": m["role"], "content": m["content"]} for m in history]
        msgs.append({"role": "user", "content": req.question})

        r = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers=_anthropic_headers(),
            json={
                "model": "claude-sonnet-4-6",
                "max_tokens": 1500,
                "system": SYSTEM_PROMPT,
                "messages": msgs,
            },
            timeout=60,
        )
        r.raise_for_status()
        return {"answer": r.json()["content"][0]["text"]}
    except requests.HTTPError as e:
        return {"answer": f"API error: {e.response.status_code}. Check your ANTHROPIC_API_KEY."}
    except Exception as e:
        return {"answer": f"Error: {e}"}

@app.post("/api/chat/stream")
async def chat_stream(req: ChatRequest):
    async def generator() -> AsyncGenerator[str, None]:
        if not ANTHROPIC_KEY:
            yield f"data: ⚠ Anthropic API key not configured.\n\n"
            yield "data: [DONE]\n\n"
            return
        try:
            history = req.history or []
            msgs = [{"role": m["role"], "content": m["content"]} for m in history]
            msgs.append({"role": "user", "content": req.question})
            with requests.post(
                "https://api.anthropic.com/v1/messages",
                headers=_anthropic_headers(),
                json={
                    "model": "claude-sonnet-4-6",
                    "max_tokens": 1500,
                    "stream": True,
                    "system": SYSTEM_PROMPT,
                    "messages": msgs,
                },
                stream=True, timeout=60,
            ) as r:
                for line in r.iter_lines():
                    if line and line.startswith(b"data: "):
                        try:
                            data = json.loads(line[6:])
                            if data.get("type") == "content_block_delta":
                                token = data["delta"].get("text", "")
                                if token:
                                    yield f"data: {token}\n\n"
                        except json.JSONDecodeError:
                            pass
            yield "data: [DONE]\n\n"
        except Exception as e:
            yield f"data: [ERROR] {e}\n\n"
    return StreamingResponse(generator(), media_type="text/event-stream")

# ── HEALTH ────────────────────────────────────────────────────────────────────

@app.get("/api/health")
def health():
    return {
        "status": "ok",
        "mode": "demo",
        "has_api_key": bool(ANTHROPIC_KEY),
        "environment": os.getenv("RAILWAY_ENVIRONMENT", "local"),
    }

# ── SERVE REACT FRONTEND ──────────────────────────────────────────────────────
# Everything after this point catches anything that's NOT /api/* and serves the SPA

if STATIC_DIR.exists():
    # Mount built React assets (JS, CSS, images)
    # app.mount("/assets", StaticFiles(directory=STATIC_DIR / "assets"), name="assets")

    @app.get("/")
    @app.get("/{full_path:path}")
    def serve_spa(full_path: str = ""):
        """Serve index.html for any non-API route (SPA routing)"""
        if full_path.startswith("api/"):
            raise HTTPException(404, "Not found")
        index = STATIC_DIR / "index.html"
        if index.exists():
            return FileResponse(index)
        raise HTTPException(404, "Frontend not built")
else:
    @app.get("/")
    def root():
        return {"message": "API running. Frontend not built yet. See /docs for API."}

# ── LAUNCH ────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
