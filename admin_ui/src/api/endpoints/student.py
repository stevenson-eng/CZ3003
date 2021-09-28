import crud
import schemas
from db.database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/{email}", response_model=schemas.Student)
def read(email: str, db: Session = Depends(get_db)):
    return crud.student.read(db, email)


@router.post("/")
def create(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.student.create(db, student)


@router.patch("/")
def update(student: schemas.StudentUpdate, db: Session = Depends(get_db)):
    return crud.student.update(db, student)
