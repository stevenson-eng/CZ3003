import schemas
from fastapi import APIRouter

from mail.send_mail import send_mail_async

router = APIRouter()


@router.post("/")
async def send_async(email: schemas.MailCreate):
    await send_mail_async(email.subject, email.recipients, email.body)
