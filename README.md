# Task Manager DevOps Project

Minimalne API do ćwiczenia Dockera/DevOps.

## Local run
python -m venv .venv
source .venv/Scripts/activate
pip install -r app/requirements.txt
uvicorn app.main:app --reload --port 8000

## Test
curl http://localhost:8000/api/health
