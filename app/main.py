from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.database import engine, Base
from app.api.v1.router import api_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url="/api/v1/openapi.json",
    description="SupportPulse AI Platform - AI Ticket Ingestion & Vector RAG Intelligence API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/health", tags=["Health"])
def health():
    return {
        "status": "ok",
        "service": settings.PROJECT_NAME,
        "llm_provider": settings.LLM_PROVIDER
    }
