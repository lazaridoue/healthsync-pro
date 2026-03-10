from fastapi import APIRouter
from app.models import HealthMetric
from app.monitoring import detect_anomaly

router = APIRouter()

health_data = []
alerts = []

@router.post("/health-data")
def ingest_health_data(data: HealthMetric):

    health_data.append(data)

    anomaly_alerts = detect_anomaly(data)

    if anomaly_alerts:
        alert = {
            "user_id": data.user_id,
            "alerts": anomaly_alerts,
            "timestamp": data.timestamp
        }

        alerts.append(alert)

        return {
            "status": "alert_triggered",
            "alerts": anomaly_alerts
        }

    return {"status": "data_received"}

@router.get("/alerts")
def get_alerts():
    return alerts