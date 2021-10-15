import crud
import schemas
from db.database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Optional

router = APIRouter()


@router.get("/{id}", response_model=schemas.Question)
def read(id: str, db: Session = Depends(get_db)):
    return crud.question.read(db, id)

@router.get("/")
def read(
    category_name: Optional[str] = None, 
    quest_name: Optional[str] = None, 
    subquest_name: Optional[str] = None, 
    difficulty: Optional[int]= None, 
    limit: Optional[int] = None, 
    db: Session = Depends(get_db)):

    # If no parameters are provided
    if not any([category_name, quest_name, subquest_name, difficulty]):
        return crud.question.read_all(db)
    
    # If there is at least 1 filter provided
    return crud.question.read_by_parameters(
        db, category_name, quest_name, subquest_name, difficulty, limit)

@router.post("/")
def create(question: schemas.QuestionCreate, db: Session = Depends(get_db)):
    return crud.question.create(db, question)


@router.patch("/")
def update(question: schemas.QuestionUpdate, db: Session = Depends(get_db)):
    return crud.question.update(db, question)
    