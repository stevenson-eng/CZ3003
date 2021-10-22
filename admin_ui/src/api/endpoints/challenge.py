from typing import List, Optional

import crud
import schemas
from db.database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[schemas.Challenge])
def read(
    challenger_email: Optional[str] = None,
    challengee_email: Optional[str] = None,
    quest_name: Optional[str] = None,
    category_name: Optional[str] = None,
    db: Session = Depends(get_db),
):
    return crud.challenge.read(
        db, challenger_email, challengee_email, quest_name, category_name
    )


@router.post("/")
def create(challenge: schemas.ChallengeCreate, db: Session = Depends(get_db)):
    return crud.challenge.create(db, challenge)


@router.patch("/")
def update(challenge: schemas.ChallengeUpdate, db: Session = Depends(get_db)):
    return crud.challenge.update(db, challenge)


@router.delete("/", status_code=204)
def delete(challenger_email: str, challengee_email: str, db: Session = Depends(get_db)):
    return crud.challenge.delete(db, challenger_email, challengee_email)
