from typing import List

import models
import schemas
from models.assignmentQuestion import AssignmentQuestion
from schemas.assignmentQuestion import AssignmentQuestionCreate, AssignmentQuestionUpdate
from sqlalchemy.orm import Session

from crud.base import CRUDBase


class CRUDAssignmentQuestion(CRUDBase[AssignmentQuestion, AssignmentQuestionCreate, AssignmentQuestionUpdate]):
    def create(self, db: Session, assignmentQuestion: schemas.AssignmentQuestionCreate):
        db_assignmentQuestion = models.AssignmentQuestion(
            assignment_id=assignmentQuestion.assignment_id,
            difficulty=assignmentQuestion.difficulty,
            points=assignmentQuestion.points,
            prompt=assignmentQuestion.prompt,
            answer=assignmentQuestion.answer,
            choice1=assignmentQuestion.choice1,
            choice2=assignmentQuestion.choice2,
            choice3=assignmentQuestion.choice3,
            choice4=assignmentQuestion.choice4,
        )
        db.add(db_assignmentQuestion)
        db.commit()
        db.refresh(db_assignmentQuestion)
        return db_assignmentQuestion

    def read(self, db: Session, id: str) -> AssignmentQuestion:
        return db.query(models.AssignmentQuestion).filter(models.AssignmentQuestion.id == id).first()

    def read_all(self, db: Session) -> List[AssignmentQuestion]:
        return db.query(models.AssignmentQuestion).all()

    def update(self, db: Session, new_assignmentQuestion: schemas.AssignmentQuestionUpdate):
        old_assignmentQuestion = (
            db.query(models.AssignmentQuestion)
            .filter(models.AssignmentQuestion.id == new_assignmentQuestion.id)
            .first()
        )
        return super().update(db, db_obj=old_assignmentQuestion, obj_in=new_assignmentQuestion)


assignmentQuestion = CRUDAssignmentQuestion(AssignmentQuestion)
