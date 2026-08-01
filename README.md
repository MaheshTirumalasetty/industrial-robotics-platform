# Industrial Robotics Platform

A production-like platform engineering project built to simulate an industrial robotic manufacturing cell.

## Employer Context

This project is framed as an internal engineering platform developed at Entity IT Tek Inc. for advanced manufacturing use cases. It does not claim direct access to any customer's production systems, credentials, or proprietary infrastructure.

## Business Objective

The platform simulates a robotic manufacturing cell where sensor data is published through ROS 2, processed by a controller service, exposed through a REST API, deployed using containers and Kubernetes, and monitored through Prometheus and Grafana.

## Initial Scope

- ROS 2 sensor publisher
- ROS 2 robot controller subscriber
- FastAPI manufacturing API
- Docker and Docker Compose
- Unit tests
- CI/CD starter workflows
- Kubernetes manifests
- Platform bring-up and health-check scripts
- Documentation and runbooks

## Repository Layout

```text
industrial-robotics-platform/
├── api/
├── docs/
├── docker/
├── kubernetes/
├── monitoring/
├── ros2_ws/
├── scripts/
├── tests/
├── .github/workflows/
├── .gitlab-ci.yml
├── docker-compose.yml
└── README.md
```

## Local Quick Start

### API

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r api/manufacturing_api/requirements.txt
uvicorn api.manufacturing_api.app.main:app --host 0.0.0.0 --port 8000
```

Open:

- `http://localhost:8000/health`
- `http://localhost:8000/status`
- `http://localhost:8000/metrics`

### Tests

```bash
pytest -q
```

### Docker Compose

```bash
docker compose up --build
```

### Platform Validation

```bash
bash scripts/platform_bringup.sh
bash scripts/health_check.sh
```

## Interview Summary

This project demonstrates platform bring-up, Linux troubleshooting, ROS 2 integration, Python, Bash, Docker, Kubernetes, CI/CD, REST, JSON, monitoring, networking, release validation, and production-style troubleshooting.
