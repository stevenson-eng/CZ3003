from typing import List, Optional

import crud
import models
import schemas
from models.mail import Mail
from schemas.mail import MailCreate, MailUpdate
from sqlalchemy.orm import Session

from crud.base import CRUDBase


class CRUDMail(CRUDBase[Mail, MailCreate, MailUpdate]):
    def create(self, db: Session, mail: schemas.MailCreate):
        sender_in_db = crud.teacher.read(db, mail.sender)

        for recipient in mail.recipients:
            recipient_in_db = crud.student.read(db, recipient)
            db_mail = models.Mail(
                sender_id=sender_in_db.id,
                recipient_id=recipient_in_db.id,
                subject=mail.subject,
                body=mail.subject,
            )
            db.add(db_mail)

        db.commit()
        db.refresh(db_mail)
        return db_mail

    def read(self, db: Session, id: str) -> Optional[Mail]:
        return db.query(models.Mail).filter(models.Mail.id == id).first()

    def read_all(self, db: Session) -> List[Mail]:
        return db.query(models.Mail).all()


mail = CRUDMail(Mail)
