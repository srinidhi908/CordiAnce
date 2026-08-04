from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="A Trustworthy Explainable Multi-Agent AI System for Early Detection of Heart Disease and Personalized Monitoring",
)


@app.get("/")
def root():
    return {
        "message": f"Welcome to {settings.APP_NAME} 🚀",
        "version": settings.APP_VERSION,
        "status": "Running Successfully"
    }