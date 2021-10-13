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
