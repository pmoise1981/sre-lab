from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from prometheus_client import Counter, generate_latest

app = FastAPI()
REQUESTS = Counter("http_requests_total", "Total HTTP requests", ["path"])

@app.get("/healthz")
def health():
    REQUESTS.labels(path="/healthz").inc()
    return {"status": "ok"}

@app.get("/metrics", response_class=PlainTextResponse)
def metrics():
    return generate_latest().decode("utf-8")
