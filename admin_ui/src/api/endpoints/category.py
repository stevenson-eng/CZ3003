from enum import IntEnum
from schemas.question import DifficultyEnum
import crud
import schemas
from db.database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

router = APIRouter()


@router.get("/{id}", response_model=schemas.Category)
def read(id: str, db: Session = Depends(get_db)):
    return crud.category.read(db, id)

@router.get("/", response_model=List[schemas.Category])
def read_all(db: Session = Depends(get_db)):
    return crud.category.read_all(db)

@router.post("/")
def create(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.category.create(db, category)


@router.patch("/")
def update(category: schemas.CategoryUpdate, db: Session = Depends(get_db)):
    return crud.category.update(db, category)


@router.get("/{id}/{_difficulty}")
def get_questions(id: str, difficulty: DifficultyEnum, number:int , db: Session = Depends(get_db)):
    # if difficulty == DifficultyEnum.easy:
    #     difficulty_in_json = {
    #         "difficulty": 1
    #     }
    #     return crud.category.get_questions_by_quest(db, id, difficulty_in_json, number)
    # if difficulty == DifficultyEnum.medium:
    #     difficulty_in_json = {
    #         "difficulty": 2
    #     }
    #     return crud.category.get_questions_by_quest(db, id, difficulty_in_json, number)
    # if difficulty == DifficultyEnum.hard:
    #     difficulty_in_json = {
    #         "difficulty": 3
    #     }
    return crud.category.get_questions_by_quest(db, id, difficulty, number)