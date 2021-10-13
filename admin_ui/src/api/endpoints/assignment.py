import crud
import schemas
from db.database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Optional

router = APIRouter()


@router.get("/{id}", response_model=schemas.Assignment)
def read(id: str, db: Session = Depends(get_db)):
    return crud.assignment.read(db, id)


@router.get("/", response_model=List[schemas.Assignment])
def read_all(
    assigner: Optional[str] = None,
    assignee: Optional[str] = None,
    db: Session = Depends(get_db),
):
    return crud.assignment.read_all(db, assigner, assignee)


@router.post("/")
def create(assignment: schemas.AssignmentCreate, db: Session = Depends(get_db)):
    assigner_in_db = crud.teacher.read(db, assignment.assigner)
    assignee_in_db = crud.student.read(db, assignment.assignee)
    return crud.assignment.create(
        db,
        schemas.AssignmentCreate(
            assigner=assigner_in_db.email,
            assignee=assignee_in_db.email,
            points_scored=assignment.points_scored,
            time_to_complete_in_seconds=assignment.time_to_complete_in_seconds,
            description=assignment.description,
        ),
    )


@router.patch("/")
def update(assignment: schemas.AssignmentUpdate, db: Session = Depends(get_db)):
    return crud.assignment.update(db, assignment)
