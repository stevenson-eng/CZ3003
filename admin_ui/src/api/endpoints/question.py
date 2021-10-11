import crud
import schemas
from db.database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/{id}", response_model=schemas.Question)
def read(id: str, db: Session = Depends(get_db)):
    return crud.question.read(db, id)


@router.post("/")
def create(question: schemas.QuestionCreate, db: Session = Depends(get_db)):
    return crud.question.create(db, question)


@router.patch("/")
def update(question: schemas.QuestionUpdate, db: Session = Depends(get_db)):
    return crud.question.update(db, question)