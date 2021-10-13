import models
import schemas
from models.question import Question
from schemas.question import QuestionCreate, QuestionUpdate
from sqlalchemy.orm import Session

from crud.base import CRUDBase


class CRUDQuestion(CRUDBase[Question, QuestionCreate, QuestionUpdate]):
    def create(self, db: Session, question: schemas.QuestionCreate):
        db_question = models.Question(
            subquest_name=question.subquest_name,
            assignment_id=question.assignment_id,
            difficulty=question.difficulty,
            points=question.points,
            sdlc_stage=question.sdlc_stage,
            prompt=question.prompt,
            answer=question.answer,
            choice1=question.choice1,
            choice2=question.choice2,
            choice3=question.choice3,
            choice4=question.choice4,
        )
        db.add(db_question)
        db.commit()
        db.refresh(db_question)
        return db_question

    def read(self, db: Session, id: str) -> Question:
        return db.query(models.Question).filter(models.Question.id == id).first()

    def update(self, db: Session, new_question: schemas.QuestionUpdate):
        old_question = (
            db.query(models.Question)
            .filter(models.Question.id == new_question.id)
            .first()
        )
        return super().update(db, db_obj=old_question, obj_in=new_question)


question = CRUDQuestion(Question)
