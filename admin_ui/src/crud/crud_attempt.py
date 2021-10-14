from typing import List

import models
import schemas
from models.attempt import Attempt
from schemas.attempt import AttemptCreate, AttemptUpdate
from sqlalchemy.orm import Session

from crud.base import CRUDBase


class CRUDAttempt(CRUDBase[Attempt, AttemptCreate, AttemptUpdate]):
    def create(self, db: Session, attempt: schemas.AttemptCreate):
        db_attempt = models.Attempt(
            quest_name=attempt.quest_name,
            student_email=attempt.student_email,
            points_scored=attempt.points_scored,
            time_to_complete_in_seconds=attempt.time_to_complete_in_seconds,
            completion_datetime=attempt.completion_datetime,
        )
        db.add(db_attempt)
        db.commit()
        db.refresh(db_attempt)
        return db_attempt

    def read(self, db: Session, quest_name: str, student_email: str) -> Attempt:
        return (
            db.query(models.Attempt)
            .filter(
                models.Attempt.quest_name == quest_name,
                models.Attempt.student_email == student_email,
            )
            .first()
        )

    def read_all(self, db: Session) -> List[Attempt]:
        return db.query(models.Attempt).all()

    def update(self, db: Session, new_attempt: schemas.AttemptUpdate):
        old_attempt = (
            db.query(models.Attempt)
            .filter(
                models.Attempt.quest_name == new_attempt.quest_name,
                models.Attempt.student_email == new_attempt.student_email,
            )
            .first()
        )
        return super().update(db, db_obj=old_attempt, obj_in=new_attempt)


attempt = CRUDAttempt(Attempt)
