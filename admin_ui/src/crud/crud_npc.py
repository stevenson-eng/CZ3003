import models
import schemas
from models.npc import Npc
from schemas.npc import NpcCreate, NpcUpdate
from sqlalchemy.orm import Session

from crud.base import CRUDBase


class CRUDNpc(CRUDBase[Npc, NpcCreate, NpcUpdate]):
    def create(self, db: Session, npc: schemas.NpcCreate):
        db_npc = models.Npc(
            subquest_id=npc.subquest_id,
            name=npc.name,
        )
        db.add(db_npc)
        db.commit()
        db.refresh(db_npc)
        return db_npc

    def read(self, db: Session, id: str) -> Npc:
        return db.query(models.Npc).filter(models.Npc.id == id).first()

    def update(self, db: Session, new_npc: schemas.NpcUpdate):
        old_npc = db.query(models.Npc).filter(models.Npc.id == new_npc.id).first()
        return super().update(db, db_obj=old_npc, obj_in=new_npc)


npc = CRUDNpc(Npc)
