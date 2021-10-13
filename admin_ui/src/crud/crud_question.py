from typing import List
import models
import schemas
from models.question import Question
from schemas.question import QuestionCreate, QuestionUpdate
from sqlalchemy.orm import Session
from crud.base import CRUDBase


class CRUDQuestion(CRUDBase[Question, QuestionCreate, QuestionUpdate]):
    def create(self, db: Session, question: schemas.QuestionCreate):
        db_question = models.Question(
            category_name=question.category_name,
            quest_name=question.quest_name,
            subquest_name=question.subquest_name,
            assignment_id=question.assignment_id,
            difficulty=question.difficulty,
            points=question.points,
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

    def read_all(self, db: Session) -> List[Question]:
        return db.query(models.Question).all()

    def read_by_parameters(self, db: Session, category_name: str, quest_name:str, \
        subquest_name: str, difficulty: int, limit: int) -> List[Question]:
        questions_by_parameters=db.query(Question).filter(
            Question.category_name == category_name,
            Question.quest_name == quest_name,
            Question.subquest_name == subquest_name
        )
        # if category_name is not None:
        #     questions_by_parameters = questions_by_parameters.filter(
        #         Question.category_name == category_name)

        # if quest_name is not None:
        #     questions_by_parameters = questions_by_parameters.filter(
        #         Question.quest_name == quest_name)

        # if subquest_name is not None:
        #     questions_by_parameters = questions_by_parameters.filter(
        #         Question.subquest_name == subquest_name)

        if difficulty is not None:
            questions_by_parameters = questions_by_parameters.filter(
                Question.difficulty == difficulty
            )

        return questions_by_parameters.limit(limit).all()


    def update(self, db: Session, new_question: schemas.QuestionUpdate):
        old_question = (
            db.query(models.Question)
            .filter(models.Question.id == new_question.id)
            .first()
        )
        return super().update(db, db_obj=old_question, obj_in=new_question)

question = CRUDQuestion(Question)
