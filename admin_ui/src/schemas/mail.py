from typing import List
from uuid import UUID

from pydantic import BaseModel


class BodyBase(BaseModel):
    heading: str
    text: str


class Body(BodyBase):
    pass


class MailBase(BaseModel):
    subject: str
    body: Body
    sender: str
    recipients: List[str]


class MailCreate(MailBase):
    pass


class MailUpdate(MailBase):
    pass


class MailInDBBase(BaseModel):
    id: UUID
    sender_id: str
    recipient_id: str
    subject: str
    body: str

    class Config:
        orm_mode = True


# Properties to return to client
class Mail(MailInDBBase):
    pass


# Properties properties stored in DB
class MailInDB(MailInDBBase):
    pass
