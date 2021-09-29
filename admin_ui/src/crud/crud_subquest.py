import models
import schemas
from models.subquest import Subquest
from schemas.subquest import SubquestCreate, SubquestUpdate
from sqlalchemy.orm import Session

from crud.base import CRUDBase


class CRUDSubquest(CRUDBase[Subquest, SubquestCreate, SubquestUpdate]):
    def create(self, db: Session, subquest: schemas.SubquestCreate):
        db_subquest = models.Subquest(
            quest_id=subquest.quest_id,
        )
        db.add(db_subquest)
        db.commit()
        db.refresh(db_subquest)
        return db_subquest

    def read(self, db: Session, id: str) -> Subquest:
        return db.query(models.Subquest).filter(models.Subquest.email == id).first()

    def update(self, db: Session, new_subquest: schemas.SubquestUpdate):
        old_subquest = (
            db.query(models.Subquest)
            .filter(models.Subquest.id == new_subquest.id)
            .first()
        )
        return super().update(db, db_obj=old_subquest, obj_in=new_subquest)


subquest = CRUDSubquest(Subquest)
