def detect_anomaly(metric):
    alerts = []

    if metric.heart_rate > 110:
        alerts.append("High heart rate detected")

    if metric.sleep_hours < 4:
        alerts.append("Low sleep detected")

    if metric.steps < 500:
        alerts.append("Very low activity")

    return alerts