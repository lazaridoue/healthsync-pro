from fastapi import APIRouter
from app.models import HealthMetric

router = APIRouter()

health_data = []

@router.post("/health-data")
def ingest_health_data(data: HealthMetric):
    health_data.append(data)
    return {"status": "data received", "user": data.user_id}

@router.get("/health-data")
def get_health_data():
    return health_data