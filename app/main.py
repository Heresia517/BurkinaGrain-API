from fastapi import FastAPI
from app.api.v1.routes import auth, cereals
from app.db.base import Base
from app.db.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="BurkinaGrain API",
    description="API REST pour les prix des cereales au Burkina Faso",
    version="1.0.0"
)

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(cereals.router, prefix="/api/v1/cereals", tags=["cereals"])

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "BurkinaGrain API"}
