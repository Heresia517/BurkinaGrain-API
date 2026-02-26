# 🌾 BurkinaGrain API

> API REST pour le suivi des prix des céréales au Burkina Faso

Problème réel : les prix des céréales varient fortement selon la région et la saison au Burkina Faso, mais aucune API simple n'existe pour accéder à ces données.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111-green)
![Tests](https://img.shields.io/badge/Tests-8%20passing-brightgreen)
![Docker](https://img.shields.io/badge/Docker-ready-blue)

## Stack

- **Framework** : FastAPI
- **ORM** : SQLAlchemy 2.0 + Alembic
- **Auth** : JWT (python-jose + passlib)
- **Tests** : Pytest (8 tests)
- **Deploy** : Docker + docker-compose

## Installation

```bash
git clone https://github.com/Heresia517/BurkinaGrain-API.git
cd BurkinaGrain-API
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edite .env et remplace SECRET_KEY par une vraie clé :
# python -c "import secrets; print(secrets.token_hex(32))"
uvicorn app.main:app --reload
```

Swagger UI : http://localhost:8000/docs

## Endpoints

| Method | Route                 | Auth | Description                         |
| ------ | --------------------- | ---- | ----------------------------------- |
| POST   | /api/v1/auth/register | ❌   | Créer un compte                     |
| POST   | /api/v1/auth/login    | ❌   | Obtenir un token JWT                |
| GET    | /api/v1/cereals/      | ❌   | Lister les prix (filtre région/nom) |
| POST   | /api/v1/cereals/      | ✅   | Ajouter un prix                     |
| PUT    | /api/v1/cereals/{id}  | ✅   | Modifier un prix                    |
| DELETE | /api/v1/cereals/{id}  | ✅   | Supprimer un prix                   |
| GET    | /health               | ❌   | Health check                        |

## Tests

```bash
pytest tests/ -v
# 8 passed
```

## Variables d'environnement

| Variable                    | Description                    | Exemple                      |
| --------------------------- | ------------------------------ | ---------------------------- |
| DATABASE_URL                | URL de la base de données      | sqlite:///./burkina_grain.db |
| SECRET_KEY                  | Clé secrète JWT (min 32 chars) | token_hex(32)                |
| ALGORITHM                   | Algorithme JWT                 | HS256                        |
| ACCESS_TOKEN_EXPIRE_MINUTES | Durée du token                 | 30                           |

## Structure

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
└── docker-compose.yml
```
