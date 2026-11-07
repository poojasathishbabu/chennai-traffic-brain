setup:
	pip install -e .
test:
	pytest -q
run-api:
	uvicorn src-api-main:app --reload --port 8000
