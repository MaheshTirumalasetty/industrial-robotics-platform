#!/usr/bin/env bash
set -euo pipefail

echo "Stopping the current local deployment..."
docker compose down
echo "Local deployment stopped. Redeploy a previously tagged image to complete rollback."
