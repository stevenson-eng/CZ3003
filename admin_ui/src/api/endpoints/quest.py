import crud
import schemas
from db.database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

router = APIRouter()


@router.get("/{id}", response_model=schemas.Quest)
def read(id: str, db: Session = Depends(get_db)):
    return crud.quest.read(db, id)

@router.get("/", response_model=List[schemas.Quest])
def read_all(db: Session = Depends(get_db)):
    return crud.quest.read_all(db)

@router.post("/")
def create(quest: schemas.QuestCreate, db: Session = Depends(get_db)):
    return crud.quest.create(db, quest)


@router.patch("/")
def update(quest: schemas.QuestUpdate, db: Session = Depends(get_db)):
    return crud.quest.update(db, quest)
