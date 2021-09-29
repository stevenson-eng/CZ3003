import crud
import schemas
from db.database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/{id}", response_model=schemas.Quest)
def read(id: str, db: Session = Depends(get_db)):
    return crud.quest.read(db, id)


@router.post("/")
def create(quest: schemas.QuestCreate, db: Session = Depends(get_db)):
    return crud.quest.create(db, quest)


@router.patch("/")
def update(quest: schemas.QuestUpdate, db: Session = Depends(get_db)):
    return crud.quest.update(db, quest)
