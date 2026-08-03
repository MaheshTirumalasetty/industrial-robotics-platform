import os
import time
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel

app = FastAPI(
    title="Industrial Robotics Manufacturing API",
    version="0.1.0",
    description="Health, status, and metrics API for the simulated manufacturing platform.",
)

START_TIME = time.time()
SERVICE_NAME = os.getenv("SERVICE_NAME", "manufacturing-api")
ENVIRONMENT = os.getenv("ENVIRONMENT", "local")


class PlatformStatus(BaseModel):
    service: str
    environment: str
    manufacturing_cell: str
    robot_controller: str
    sensor_pipeline: str


@app.get("/health")
def health() -> dict:
    return {
        "status": "healthy",
        "service": SERVICE_NAME,
        "environment": ENVIRONMENT,
    }

@app.get("/cpu-load")
def cpu_load() -> dict:
    start = time.time()

    while time.time() - start < 10:
        pass

    return {
        "status": "completed",
        "duration_seconds": 10,
        "message": "CPU load generated",
    }

@app.get("/status", response_model=PlatformStatus)
def status() -> PlatformStatus:
    return PlatformStatus(
        service=SERVICE_NAME,
        environment=ENVIRONMENT,
        manufacturing_cell="operational",
        robot_controller="ready",
        sensor_pipeline="active",
    )


@app.get("/metrics", response_class=PlainTextResponse)
def metrics() -> str:
    uptime_seconds = max(0, int(time.time() - START_TIME))
    return "\n".join(
        [
            "# HELP manufacturing_api_up API health status.",
            "# TYPE manufacturing_api_up gauge",
            "manufacturing_api_up 1",
            "# HELP manufacturing_api_uptime_seconds API uptime in seconds.",
            "# TYPE manufacturing_api_uptime_seconds counter",
            f"manufacturing_api_uptime_seconds {uptime_seconds}",
            "",
        ]
    )
