import crud
import schemas
from db.database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Optional

router = APIRouter()


@router.get("/", response_model=List[schemas.Attempt])
def read(
    quest_name: Optional[str] = None,
    student_email: Optional[str] = None,
    db: Session = Depends(get_db),
):
    """
    Reads a list of all attempts:

    - **quest_name**: an optional quest name to filter by. If not provided, no filtering is done.
    - **student_email**: an optional student email to filter by. If not provided, no filtering is done.
    """
    return crud.attempt.read(db, quest_name, student_email)


@router.post("/")
def create(attempt: schemas.AttemptCreate, db: Session = Depends(get_db)):
    return crud.attempt.create(db, attempt)


@router.patch("/")
def update(attempt: schemas.AttemptUpdate, db: Session = Depends(get_db)):
    return crud.attempt.update(db, attempt)
