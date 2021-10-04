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
    assigner_in_db = crud.teacher.read(db, assignment.assigner)
    assignee_in_db = crud.student.read(db, assignment.assignee)
    return crud.assignment.create(
        db,
        schemas.AssignmentCreate(
            assigner=assigner_in_db.id,
            assignee=assignee_in_db.id,
        ),
    )


@router.patch("/")
def update(assignment: schemas.AssignmentUpdate, db: Session = Depends(get_db)):
    return crud.assignment.update(db, assignment)
