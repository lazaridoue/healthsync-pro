import requests
import random
import time

API_URL = "http://127.0.0.1:8000/health-data"

def generate_data():
    return {
        "user_id": random.randint(1, 1000),
        "heart_rate": random.randint(60, 120),
        "steps": random.randint(0, 10000),
        "sleep_hours": round(random.uniform(4, 9), 2),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

while True:
    data = generate_data()
    requests.post(API_URL, json=data)
    print("Sent:", data)
    time.sleep(1)