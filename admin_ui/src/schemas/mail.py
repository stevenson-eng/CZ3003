from typing import List

from pydantic import BaseModel


class BodyBase(BaseModel):
    heading: str
    text: str


class Body(BodyBase):
    pass


class MailBase(BaseModel):
    subject: str
    body: Body
    recipients: List[str]


class Mail(MailBase):
    pass


class MailCreate(MailBase):
    pass
