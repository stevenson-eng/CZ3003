import crud
import schemas
from db.database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

router = APIRouter()


@router.get("/{email}", response_model=schemas.Student)
def read(email: str, db: Session = Depends(get_db)):
    return crud.student.read(db, email)

@router.get("/", response_model=List[schemas.Student])
def read_all(db: Session = Depends(get_db)):
    return crud.student.read_all(db)

@router.post("/")
def create(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.student.create(db, student)

@router.patch("/")
def update(student: schemas.StudentUpdate, db: Session = Depends(get_db)):
    return crud.student.update(db, student)

@router.delete("/")
def delete(email: str, db: Session = Depends(get_db)):
    return crud.student.delete(db, email)
