from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class CerealBase(BaseModel):
    name: str
    region: str
    price_per_kg: float
    unit: str = "kg"
    source: Optional[str] = None

class CerealCreate(CerealBase):
    pass

class CerealUpdate(BaseModel):
    price_per_kg: Optional[float] = None
    source: Optional[str] = None

class CerealResponse(CerealBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime