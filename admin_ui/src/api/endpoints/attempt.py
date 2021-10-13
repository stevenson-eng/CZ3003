import crud
import schemas
from db.database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/{id}", response_model=schemas.Attempt)
def read(id: str, db: Session = Depends(get_db)):
    return crud.attempt.read(db, id)


@router.post("/")
def create(attempt: schemas.AttemptCreate, db: Session = Depends(get_db)):
    return crud.attempt.create(db, attempt)


@router.patch("/")
def update(attempt: schemas.AttemptUpdate, db: Session = Depends(get_db)):
    return crud.attempt.update(db, attempt)
