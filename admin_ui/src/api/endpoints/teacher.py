import crud
import schemas
from db.database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/{email}", response_model=schemas.Teacher)
def read(email: str, db: Session = Depends(get_db)):
    return crud.teacher.read(db, email)


@router.post("/")
def create(teacher: schemas.TeacherCreate, db: Session = Depends(get_db)):
    return crud.teacher.create(db, teacher)


@router.patch("/")
def update(teacher: schemas.TeacherUpdate, db: Session = Depends(get_db)):
    return crud.teacher.update(db, teacher)
