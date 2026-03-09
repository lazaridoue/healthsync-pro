from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="HealthSync Pro")

app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "HealthSync Pro API running"}