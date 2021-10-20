from typing import List, Optional

import crud
import schemas
from db.database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Optional

router = APIRouter()


@router.get("/", response_model=List[schemas.Assignment])
def read(
    assigner: Optional[str] = None,
    assignee: Optional[str] = None,
    db: Session = Depends(get_db),
):
    return crud.assignment.read(db, assigner, assignee)


@router.post("/")
def create(assignment: schemas.AssignmentCreate, db: Session = Depends(get_db)):
    return crud.assignment.create(db, assignment)


@router.patch("/")
def update(assignment: schemas.AssignmentUpdate, db: Session = Depends(get_db)):
    return crud.assignment.update(db, assignment)


@router.delete("/", status_code=204)
def delete(assignment_name: str, db: Session = Depends(get_db)):
    return crud.assignment.delete(db, assignment_name)
