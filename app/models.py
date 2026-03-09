from pydantic import BaseModel

class HealthMetric(BaseModel):
    user_id: int
    heart_rate: int
    steps: int
    sleep_hours: float
    timestamp: str