from typing import List

import crud
import schemas
from db.database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/{id}", response_model=schemas.AssignmentQuestion)
def read(id: str, db: Session = Depends(get_db)):
    return crud.assignmentQuestion.read(db, id)


@router.get("/", response_model=List[schemas.AssignmentQuestion])
def read_all(db: Session = Depends(get_db)):
    return crud.assignmentQuestion.read_all(db)


@router.post("/")
def create(
    assignmentQuestion: schemas.AssignmentQuestionCreate, db: Session = Depends(get_db)
):
    return crud.assignmentQuestion.create(db, assignmentQuestion)


@router.patch("/")
def update(
    assignmentQuestion: schemas.AssignmentQuestionUpdate, db: Session = Depends(get_db)
):
    return crud.assignmentQuestion.update(db, assignmentQuestion)


@router.delete("/", status_code=204)
def delete(id: str, db: Session = Depends(get_db)):
    return crud.assignmentQuestion.delete(db, id)
