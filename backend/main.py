from fastapi import FastAPI
from app.core.config import settings
from app.api.router import api_router

app = FastAPI(
    title="Budget Stress Tester API",
    version="0.1.0",
)

app.include_router(api_router)

@app.get("/health")
def health_check():
    return {"status": "ok", "debug": settings.debug}
