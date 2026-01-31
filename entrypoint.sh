#!/bin/sh

echo "Rodando migrations..."
poetry run alembic upgrade head

echo "Iniciando aplicação..."
exec poetry run uvicorn fastapi_zero.app:app --host 0.0.0.0 --port 8000
