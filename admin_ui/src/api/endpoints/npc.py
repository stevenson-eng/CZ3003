import crud
import schemas
from db.database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

router = APIRouter()


@router.get("/{id}", response_model=schemas.Npc)
def read(id: str, db: Session = Depends(get_db)):
    return crud.npc.read(db, id)

@router.get("/", response_model=List[schemas.Npc])
def read_all(db: Session = Depends(get_db)):
    return crud.npc.read_all(db)

@router.post("/")
def create(npc: schemas.NpcCreate, db: Session = Depends(get_db)):
    return crud.npc.create(db, npc)


@router.patch("/")
def update(npc: schemas.NpcUpdate, db: Session = Depends(get_db)):
    return crud.npc.update(db, npc)
