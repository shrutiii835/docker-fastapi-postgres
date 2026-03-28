from fastapi import FastAPI
from app.core.config import settings
from app.db.database import Base, get_db
from app.api.todos import router as todos_router
from sqlalchemy import text
from contextlib import contextmanager

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Production-ready Dockerized FastAPI + PostgreSQL application"
)

@app.on_event("startup")
def startup_event():
    print("🚀 Starting application...")
    print("✅ FastAPI application loaded successfully")

@app.get("/")
def read_root():
    return {
        "message": "Hello from Dockerized FastAPI + PostgreSQL!",
        "project": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "docs": "/docs",
        "api": "/api/v1/todos"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy", "database": "configured with retry logic"}

# Include Todo routes
app.include_router(todos_router)

print("✅ FastAPI application initialized")
