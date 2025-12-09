# backend-90days

Small FastAPI app for my 90-day backend upgrade.

## Endpoints
- `GET /health` -> `{ "status": "ok" }`
- `GET /hello?name=Asif` -> `{"message": "Hello, Asif!"}`
- `GET /time` -> server time

## Quick start
```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000