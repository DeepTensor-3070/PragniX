from fastapi import FastAPI

app = FastAPI(
    title="PRAGNX Freight Intelligence API",
    version="0.1.0",
)


@app.get("/api/health")
def health():
    return {
        "status": "ok",
        "service": "pragnx-freight-intelligence",
    }
