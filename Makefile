.PHONY: install lint test run docker-up docker-down validate

install:
	python3 -m pip install -r requirements-dev.txt

lint:
	ruff check api tests

test:
	pytest -q

run:
	uvicorn api.manufacturing_api.app.main:app --host 0.0.0.0 --port 8000

docker-up:
	docker compose up --build -d

docker-down:
	docker compose down

validate:
	bash scripts/platform_bringup.sh
