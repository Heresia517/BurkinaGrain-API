# 🌾 BurkinaGrain API

> REST API for tracking cereal prices across Burkina Faso's regions.

**Real-world problem:** Cereal prices (millet, sorghum, maize) vary significantly by region and season in Burkina Faso, yet no simple, structured API exists to access this data programmatically.

This project solves that — a production-ready REST API with authentication, full CRUD, automated tests, and Docker deployment.

---

## Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI |
| ORM | SQLAlchemy 2.0 + Alembic |
| Auth | JWT (python-jose + passlib) |
| Tests | Pytest — 8 tests passing |
| Deploy | Docker + docker-compose |
| DB | SQLite (dev) / PostgreSQL-ready |

---

## Quick Start

```bash
git clone https://github.com/Heresia517/BurkinaGrain-API.git
cd BurkinaGrain-API
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Generate a secure SECRET_KEY:
# python -c "import secrets; print(secrets.token_hex(32))"
uvicorn app.main:app --reload
```

**Swagger UI:** http://localhost:8000/docs

### Or run with Docker

```bash
docker-compose up --build
```

---

## API Endpoints

| Method | Route | Auth | Description |
|---|---|---|---|
| POST | /api/v1/auth/register | ❌ | Create account |
| POST | /api/v1/auth/login | ❌ | Get JWT token |
| GET | /api/v1/cereals/ | ❌ | List prices (filter by region/name) |
| POST | /api/v1/cereals/ | ✅ | Add a price entry |
| PUT | /api/v1/cereals/{id} | ✅ | Update a price entry |
| DELETE | /api/v1/cereals/{id} | ✅ | Delete a price entry |
| GET | /health | ❌ | Health check |

---

## Example Responses

**GET /api/v1/cereals/?region=Ouagadougou**

```json
[
  {
    "id": 1,
    "name": "Millet",
    "region": "Ouagadougou",
    "price_per_kg": 285.0,
    "currency": "FCFA",
    "recorded_at": "2024-03-01T10:00:00"
  },
  {
    "id": 2,
    "name": "Sorghum",
    "region": "Ouagadougou",
    "price_per_kg": 210.0,
    "currency": "FCFA",
    "recorded_at": "2024-03-01T10:00:00"
  }
]
```

**POST /api/v1/auth/login**

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

---

## Tests

```bash
pytest tests/ -v
# 8 passed in 0.42s
```

---

## Environment Variables

| Variable | Description | Example |
|---|---|---|
| DATABASE_URL | Database connection URL | sqlite:///./burkina_grain.db |
| SECRET_KEY | JWT secret key (min 32 chars) | token_hex(32) |
| ALGORITHM | JWT algorithm | HS256 |
| ACCESS_TOKEN_EXPIRE_MINUTES | Token expiry | 30 |

---

## Project Structure

```
burkina-grain-api/
├── app/
│   ├── api/v1/routes/    # auth, cereals
│   ├── core/             # security, logging
│   ├── db/               # session, base
│   ├── models/           # User, Cereal
│   ├── schemas/          # Pydantic schemas
│   └── main.py
├── migrations/           # Alembic
├── tests/                # 8 tests
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

## Author

**Hezekiah TOPAN** — Python Back-End Developer  
[LinkedIn](https://linkedin.com/in/hezekiah-topan) · [GitHub](https://github.com/Heresia517)
