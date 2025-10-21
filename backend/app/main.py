import os
from pathlib import Path

try:
    from dotenv import load_dotenv
    # Load .env file from backend directory
    env_path = Path(__file__).parent.parent / ".env"
    load_dotenv(dotenv_path=env_path)
except ImportError:
    print("WARNING: python-dotenv not installed. Environment variables will be loaded from system only.")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import predict, analyze, research
from app.db.database import init_db

app = FastAPI(title="LawGic AI Backend")

# Enable CORS so the frontend can communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routers
app.include_router(predict.router)
app.include_router(analyze.router)
app.include_router(research.router)

@app.get("/")
def root():
    return {"message": "Welcome to LawGic AI Backend"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.on_event("startup")
def on_startup():
    # Create database tables on startup (idempotent)
    try:
        init_db()
    except Exception as e:
        print(f"WARNING: Database initialization failed: {e}")
        print("INFO: App will run in demo mode")
