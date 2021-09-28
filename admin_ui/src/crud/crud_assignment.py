import models
import schemas
from models.assignment import Assignment
from schemas.assignment import AssignmentCreate, AssignmentUpdate
from sqlalchemy.orm import Session

from crud.base import CRUDBase


class CRUDAssignment(CRUDBase[Assignment, AssignmentCreate, AssignmentUpdate]):
    def create(self, db: Session, assignment: schemas.AssignmentCreate):
        db_assignment = models.Assignment(
            assigner=assignment.assigner,
            assignee=assignment.assignee,
        )
        db.add(db_assignment)
        db.commit()
        db.refresh(db_assignment)
        return db_assignment

    def read(self, db: Session, id: str) -> Assignment:
        return db.query(models.Assignment).filter(models.Assignment.email == id).first()

    def update(self, db: Session, new_assignment: schemas.AssignmentUpdate):
        old_assignment = (
            db.query(models.Assignment)
            .filter(models.Assignment.id == new_assignment.id)
            .first()
        )
        return super().update(db, db_obj=old_assignment, obj_in=new_assignment)


assignment = CRUDAssignment(Assignment)
