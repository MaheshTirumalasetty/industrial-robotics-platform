#!/usr/bin/env bash
set -euo pipefail

API_URL="${API_URL:-http://localhost:8000/health}"

echo "Checking API health at ${API_URL}..."

response="$(curl --silent --show-error --fail "$API_URL")"

if grep -q '"status":"healthy"' <<<"$response"; then
  echo "[PASS] Manufacturing API is healthy"
else
  echo "[FAIL] Unexpected API response: $response"
  exit 1
fi
