#!/usr/bin/env bash
set -euo pipefail

docker compose up --build -d
sleep 5
bash scripts/health_check.sh
docker compose ps
