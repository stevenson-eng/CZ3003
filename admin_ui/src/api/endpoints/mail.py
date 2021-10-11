from typing import List

import crud
import schemas
from db.database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from mail.send_mail import send_mail_async

router = APIRouter()


@router.get("/{id}", response_model=schemas.Mail)
def read(id: str, db: Session = Depends(get_db)):
    return crud.mail.read(db, id)


@router.get("/", response_model=List[schemas.Mail])
def read_all(db: Session = Depends(get_db)):
    return crud.mail.read_all(db)


@router.post("/")
async def send_async(email: schemas.MailCreate, db: Session = Depends(get_db)):
    crud.mail.create(db, email)
    await send_mail_async(
        email.subject, email.recipients, email.body_heading, email.body_text
    )
