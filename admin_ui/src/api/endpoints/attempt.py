import crud
import schemas
from db.database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

router = APIRouter()


@router.get("/", response_model=schemas.Attempt)
def read(quest_name: str, student_email: str, db: Session = Depends(get_db)):
    return crud.attempt.read(db, quest_name, student_email)


@router.get("/", response_model=List[schemas.Attempt])
def read_all(db: Session = Depends(get_db)):
    return crud.attempt.read_all(db)


@router.post("/")
def create(attempt: schemas.AttemptCreate, db: Session = Depends(get_db)):
    return crud.attempt.create(db, attempt)


@router.patch("/")
def update(attempt: schemas.AttemptUpdate, db: Session = Depends(get_db)):
    return crud.attempt.update(db, attempt)
