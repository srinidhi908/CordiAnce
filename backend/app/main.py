from fastapi import FastAPI

from app.modules.auth.router import router as auth_router

app = FastAPI(
    title="CordiAnce API",
    version="1.0.0",
)

app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to CordiAnce API"
    }