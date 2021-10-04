import crud
import schemas
from db.database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/{id}", response_model=schemas.Subquest)
def read(id: str, db: Session = Depends(get_db)):
    return crud.subquest.read(db, id)


@router.post("/")
def create(subquest: schemas.SubquestCreate, db: Session = Depends(get_db)):
    return crud.subquest.create(db, subquest)


@router.patch("/")
def update(subquest: schemas.SubquestUpdate, db: Session = Depends(get_db)):
    return crud.subquest.update(db, subquest)