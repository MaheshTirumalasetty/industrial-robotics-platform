#!/usr/bin/env bash
set -euo pipefail

required_commands=(git python3 docker)

echo "Starting platform bring-up validation..."

for command in "${required_commands[@]}"; do
  if command -v "$command" >/dev/null 2>&1; then
    echo "[PASS] $command is installed"
  else
    echo "[FAIL] $command is not installed"
    exit 1
  fi
done

if docker info >/dev/null 2>&1; then
  echo "[PASS] Docker daemon is running"
else
  echo "[FAIL] Docker daemon is unavailable"
  exit 1
fi

if [[ -f "docker-compose.yml" ]]; then
  echo "[PASS] Docker Compose definition exists"
else
  echo "[FAIL] docker-compose.yml is missing"
  exit 1
fi

if [[ -d "kubernetes" ]]; then
  echo "[PASS] Kubernetes manifests exist"
else
  echo "[FAIL] Kubernetes manifests are missing"
  exit 1
fi

echo "Platform bring-up validation completed successfully."
