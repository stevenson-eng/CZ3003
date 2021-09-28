import crud
import schemas
from db.database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/{id}", response_model=schemas.Assignment)
def read(id: str, db: Session = Depends(get_db)):
    return crud.assignment.read(db, id)


@router.post("/")
def create(assignment: schemas.AssignmentCreate, db: Session = Depends(get_db)):
    return crud.assignment.create(db, assignment)


@router.patch("/")
def update(assignment: schemas.AssignmentUpdate, db: Session = Depends(get_db)):
    return crud.assignment.update(db, assignment)
