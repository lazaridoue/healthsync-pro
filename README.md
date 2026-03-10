# HealthSync Pro

HealthSync Pro is a backend system that simulates and processes health data from wearable IoT devices such as smartwatches and fitness trackers. The system ingests health metrics, detects abnormal patterns, and exposes APIs for monitoring health stability.

This project was built to practice backend engineering, API development, system monitoring, and test-driven development using Python.

---

## Features

- FastAPI backend for high-performance API endpoints
- Simulated health IoT data ingestion
- Abnormal health detection (heart rate, sleep, activity)
- Alert monitoring system
- Interactive API documentation using Swagger
- Structured backend architecture
- Designed to support high-throughput health data simulation

---

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Pydantic
- PyTest (planned)
- React Dashboard (planned)

---

## Project Structure

```
healthsync-pro
│
├── app
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   └── monitoring.py
│
├── simulator
│   └── data_generator.py
│
├── tests
│   └── test_api.py
│
├── requirements.txt
└── README.md
```

---

## How to Run the Project

### 1. Clone the Repository

```
git clone https://github.com/lazaridoue/healthsync-pro.git
cd healthsync-pro
```

---

### 2. Install Dependencies

Make sure Python 3.9+ is installed.

Then run:

```
pip install -r requirements.txt
```

---

### 3. Start the API Server

Run the FastAPI server:

```
uvicorn app.main:app --reload
```

You should see:

```
Uvicorn running on http://127.0.0.1:8000
```

---

### 4. Open the API Documentation

Open your browser and go to:

```
http://127.0.0.1:8000/docs
```

FastAPI automatically generates interactive API documentation using Swagger UI.

---

### 5. Test Health Data Ingestion

In Swagger UI:

1. Expand the endpoint:

```
POST /health-data
```

2. Click **Try it out**

3. Use the following example request:

```
{
  "user_id": 1,
  "heart_rate": 125,
  "steps": 200,
  "sleep_hours": 3,
  "timestamp": "2026-03-09 18:00:00"
}
```

4. Click **Execute**

If abnormal values are detected, the system will return an alert.

---

### Example Alert Response

```
{
 "status": "alert_triggered",
 "alerts": [
   "High heart rate detected",
   "Low sleep detected",
   "Very low activity"
 ]
}
```

---

### 6. View System Alerts

Use the endpoint:

```
GET /alerts
```

This returns all detected abnormal health events.

---

## Example Use Case

HealthSync Pro simulates wearable devices sending real-time health metrics such as:

- Heart rate
- Daily steps
- Sleep duration

The system processes incoming data and detects abnormal health patterns to generate alerts.

---

## Future Improvements

- High-volume health data simulation (1M+ events)
- Concurrent device simulation
- Real-time health monitoring dashboard using React
- PyTest unit testing with 90%+ coverage
- System health monitoring endpoint
- Docker containerization
- CI/CD pipeline using GitHub Actions

---

## Learning Goals

This project was built to practice:

- Backend API development
- Health data ingestion systems
- Monitoring and anomaly detection
- Test-driven development
- Git and GitHub workflow
- System design for high-throughput data

---

## License

MIT License