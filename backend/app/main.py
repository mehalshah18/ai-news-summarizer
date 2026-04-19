from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import news
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="AI News Summarizer API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(news.router)

@app.on_event("startup")
async def startup_event():
    from app.services.scheduler import start_scheduler
    start_scheduler()

@app.get("/health")
async def health():
    return {"status": "ok"}
