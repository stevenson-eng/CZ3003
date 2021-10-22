import crud
import schemas
from db.database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Optional

router = APIRouter()


@router.get("/{quest_name}", response_model=schemas.Quest)
def read(quest_name: str, db: Session = Depends(get_db)):
    return crud.quest.read(db, quest_name)

@router.get("/", response_model=List[schemas.Quest])
def read_all(db: Session = Depends(get_db)):
    return crud.quest.read_all(db)

@router.get("/category/")
def read(
    category_name: Optional[str] = None, 
    student_email: Optional[str] = None, 
    db: Session = Depends(get_db)):

    return crud.quest.read_by_category(db, category_name, student_email)

@router.get("/best_attempt/{student_email}")
def get_best_attempt(
    student_email: str, 
    category_name: str, 
    quest_name: str,
    db: Session = Depends(get_db)):
    return crud.quest.best_quest_attempt(db, student_email, category_name, quest_name)

@router.post("/")
def create(quest: schemas.QuestCreate, db: Session = Depends(get_db)):
    return crud.quest.create(db, quest)


@router.patch("/")
def update(quest: schemas.QuestUpdate, db: Session = Depends(get_db)):
    return crud.quest.update(db, quest)

