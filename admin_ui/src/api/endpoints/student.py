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
    """
    Create a student with all the information:

    - **email**: required
    - **name**: required
    - **points**: optional, default value = 0
    - **status**: optional, default value = 2, which is "offline"
    - **rank**: do not input, default value = None, rank will be calculated from points
    - **position**: do not input, default value = None, position will be calculated based on number of current students
    """
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
