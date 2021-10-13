import models
import schemas
from models.quest import Quest
from schemas.quest import QuestCreate, QuestUpdate
from sqlalchemy.orm import Session

from crud.base import CRUDBase


class CRUDQuest(CRUDBase[Quest, QuestCreate, QuestUpdate]):
    def create(self, db: Session, quest: schemas.QuestCreate):
        db_quest = models.Quest(
            quest_name=quest.quest_name,
            category_name=quest.category_name,
        )
        db.add(db_quest)
        db.commit()
        db.refresh(db_quest)
        return db_quest

    def read(self, db: Session, quest_name: str) -> Quest:
        return db.query(models.Quest).filter(models.Quest.quest_name == quest_name).first()

    def update(self, db: Session, new_quest: schemas.QuestUpdate):
        old_quest = (
            db.query(models.Quest).filter(models.Quest.quest_name == new_quest.quest_name).first()
        )
        return super().update(db, db_obj=old_quest, obj_in=new_quest)


quest = CRUDQuest(Quest)
