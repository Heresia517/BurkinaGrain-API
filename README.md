🌾 BurkinaGrain API

> REST API for tracking cereal prices across Burkina Faso's regions.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-Render-blue)](https://burkinagrain-api.onrender.com/docs)
[![Tests](https://github.com/Heresia517/BurkinaGrain-API/actions/workflows/ci.yml/badge.svg)](https://github.com/Heresia517/BurkinaGrain-API/actions)

---

## 🇧🇫 Why this project matters

In Burkina Faso, cereal prices (millet, sorghum, maize) vary significantly by region and season. Farmers, traders, and consumers lack a simple, structured way to access this data programmatically. This API fills that gap by providing a production‑ready, open‑source interface to cereal price data.

**Potential impact:**
- Enable mobile apps for price transparency
- Help agricultural cooperatives make informed decisions
- Provide data for researchers and policymakers

---

## Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI |
| ORM | SQLAlchemy 2.0 + Alembic |
| Auth | JWT (python-jose + passlib) |
| Tests | Pytest — 8 tests passing |
| Deploy | Docker + docker-compose |
| DB | SQLite (dev) / PostgreSQL‑ready |

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

> **Note:** Generate a secure `SECRET_KEY` with `python -c "import secrets; print(secrets.token_hex(32))"`.

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

## Roadmap

- [ ] Add `/regions` endpoint to list available regions
- [ ] PostgreSQL support in docker-compose
- [ ] Historical price trends (time‑series data)
- [ ] Simple frontend demo (HTML/JS) consuming the API
- [ ] Role‑based access (admin, user)

---

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to report issues, suggest features, and submit pull requests.

---

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## Author

**Hezekiah TOPAN** — Python Back‑End Developer  
[LinkedIn](https://linkedin.com/in/hezekiah-topan) · [GitHub](https://github.com/Heresia517)
```
