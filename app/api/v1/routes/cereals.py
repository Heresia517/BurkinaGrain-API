from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.db.session import get_db
from app.api.v1.deps import get_current_user
from app.schemas.cereal import CerealCreate, CerealUpdate, CerealResponse
from app.models.cereal import Cereal
from app.models.user import User

router = APIRouter()

@router.get("/", response_model=List[CerealResponse])
def list_cereals(
    region: Optional[str] = Query(None),
    name: Optional[str] = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db)
):
    q = db.query(Cereal)
    if region:
        q = q.filter(Cereal.region.ilike(f"%{region}%"))
    if name:
        q = q.filter(Cereal.name.ilike(f"%{name}%"))
    return q.offset(skip).limit(limit).all()

@router.post("/", response_model=CerealResponse, status_code=201)
def create_cereal(cereal_in: CerealCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    cereal = Cereal(**cereal_in.model_dump())
    db.add(cereal)
    db.commit()
    db.refresh(cereal)
    return cereal

@router.get("/{cereal_id}", response_model=CerealResponse)
def get_cereal(cereal_id: int, db: Session = Depends(get_db)):
    cereal = db.query(Cereal).filter(Cereal.id == cereal_id).first()
    if not cereal:
        raise HTTPException(status_code=404, detail="Cereale non trouvee")
    return cereal

@router.put("/{cereal_id}", response_model=CerealResponse)
def update_cereal(cereal_id: int, cereal_in: CerealUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    cereal = db.query(Cereal).filter(Cereal.id == cereal_id).first()
    if not cereal:
        raise HTTPException(status_code=404, detail="Cereale non trouvee")
    for f, v in cereal_in.model_dump(exclude_unset=True).items():
        setattr(cereal, f, v)
    db.commit()
    db.refresh(cereal)
    return cereal

@router.delete("/{cereal_id}", status_code=204)
def delete_cereal(cereal_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    cereal = db.query(Cereal).filter(Cereal.id == cereal_id).first()
    if not cereal:
        raise HTTPException(status_code=404, detail="Cereale non trouvee")
    db.delete(cereal)
    db.commit()
