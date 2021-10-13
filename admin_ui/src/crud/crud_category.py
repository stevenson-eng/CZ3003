from os import name
from typing import List

import models
import schemas
from models.category import Category
from models.subquest import Subquest
from models.quest import Quest
from models.question import Question
from fastapi.encoders import jsonable_encoder
from schemas.category import CategoryCreate, CategoryUpdate
from sqlalchemy.orm import Session

from crud.base import CRUDBase


class CRUDCategory(CRUDBase[Category, CategoryCreate, CategoryUpdate]):
    def create(self, db: Session, category: schemas.CategoryCreate):
        db_category = models.Category(
            category_name=category.category_name,
        )
        db.add(db_category)
        db.commit()
        db.refresh(db_category)
        return db_category

    def read(self, db: Session, category_name: str) -> Category:
        return db.query(models.Category).filter(models.Category.category_name == category_name).first()

    def read_all(self, db: Session) -> List[Category]:
        return db.query(models.Category).all()

    def update(self, db: Session, new_category: schemas.CategoryUpdate):
        old_category = (
            db.query(models.Category)
            .filter(models.Category.category_name == new_category.category_name)
            .first()
        )
        return super().update(db, db_obj=old_category, obj_in=new_category)

    def get_questions_by_quest(self, db: Session, id: str, difficulty: int, number: int):
        json_compatible_difficulty = jsonable_encoder(difficulty)
        json_compatible_number=jsonable_encoder(number)

        import pdb
        pdb.set_trace()
        # join_table = db.query(models.Question).join(models.Subquest).join(models.Quest).join(models.Category).\
        #     filter(models.Category.id == id).all()
        join_table=db.query(Question).join(Question.subquest_id == Subquest.id, \
            Subquest.quest_id == Quest.id, Quest.category_id==Category.id)
        print(join_table)
        import pdb
        pdb.set_trace()
        questions_by_quest_query = join_table.\
            filter(models.Category.id == id).filter(models.Question.difficulty == difficulty).limit(number)
        
        # questions_by_quest_query = db.query(Question).join(Question.subquest_id == Subquest.id, \
        #     Subquest.quest_id == Quest.id, Quest.category_id==Category.id).\
        #         filter(Category.id == id).filter(models.Question.difficulty == difficulty).limit(number)

        # for result in questions_by_quest_query:
        #     print(result)

        return questions_by_quest_query


category = CRUDCategory(Category)
