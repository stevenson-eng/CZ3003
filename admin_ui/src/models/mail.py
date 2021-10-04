import uuid

from db.database import Base
from sqlalchemy import Column, String, ForeignKey


class Mail(Base):
    __tablename__ = "mail"

    # TODO - ensure that foreign key constraints, if any, are enforced
    # TODO - https://docs.sqlalchemy.org/en/14/core/constraints.html
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    sender_id = Column(String, ForeignKey("teacher.id"), nullable=False)
    recipient_id = Column(String, ForeignKey("student.id"), nullable=False)
    subject = Column(String, nullable=False)
    body = Column(String, nullable=False)
