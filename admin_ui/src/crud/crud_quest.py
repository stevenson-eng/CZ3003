import models
import schemas
from models.quest import Quest
from schemas.quest import QuestCreate, QuestUpdate
from sqlalchemy.orm import Session

from crud.base import CRUDBase


class CRUDQuest(CRUDBase[Quest, QuestCreate, QuestUpdate]):
    def create(self, db: Session, quest: schemas.QuestCreate):
        db_quest = models.Quest(
            category_id=quest.category_id,
        )
        db.add(db_quest)
        db.commit()
        db.refresh(db_quest)
        return db_quest

    def read(self, db: Session, id: str) -> Quest:
        return db.query(models.Quest).filter(models.Quest.id == id).first()

    def update(self, db: Session, new_quest: schemas.QuestUpdate):
        old_quest = (
            db.query(models.Quest).filter(models.Quest.id == new_quest.id).first()
        )
        return super().update(db, db_obj=old_quest, obj_in=new_quest)


quest = CRUDQuest(Quest)
