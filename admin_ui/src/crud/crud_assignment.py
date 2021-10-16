from typing import List

import models
import schemas
from models.assignment import Assignment
from schemas.assignment import AssignmentCreate, AssignmentUpdate
from sqlalchemy.orm import Session

from crud.base import CRUDBase


class CRUDAssignment(CRUDBase[Assignment, AssignmentCreate, AssignmentUpdate]):
    def create(self, db: Session, assignment: schemas.AssignmentCreate):
        db_assignment = models.Assignment(
            assignment_name = assignment.assignment_name,
            assigner=assignment.assigner,
            assignee=assignment.assignee,
            description=assignment.description,
            points_scored=assignment.points_scored,
            time_to_complete_in_seconds=assignment.time_to_complete_in_seconds,
        )
        db.add(db_assignment)
        db.commit()
        db.refresh(db_assignment)
        return db_assignment

    def read(self, db: Session, assigner: str, assignee: str) -> List[Assignment]:
        results = db.query(models.Assignment)

        if assigner is not None:
            results = results.filter(models.Assignment.assigner == assigner)

        if assignee is not None:
            results = results.filter(models.Assignment.assignee == assignee)

        return results.all()

    def update(self, db: Session, new_assignment: schemas.AssignmentUpdate):
        old_assignment = (
            db.query(models.Assignment)
            .filter(
                models.Assignment.assigner == new_assignment.assigner,
                models.Assignment.assignee == new_assignment.assignee,
            )
            .first()
        )
        return super().update(db, db_obj=old_assignment, obj_in=new_assignment)


assignment = CRUDAssignment(Assignment)