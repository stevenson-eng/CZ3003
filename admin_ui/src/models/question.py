import uuid

from sqlalchemy.sql.sqltypes import Integer

from db.database import Base
from sqlalchemy import Column, String, ForeignKey


class Question(Base):
    __tablename__ = "question"

    # TODO - ensure that foreign key constraints, if any, are enforced
    # TODO - https://docs.sqlalchemy.org/en/14/core/constraints.html
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    subquest_id = Column(String, ForeignKey("subquest.id"), nullable=False)
    assignment_id = Column(String, ForeignKey("assignment.id"), nullable=False)
    difficulty: Column(Integer, nullable=False)
    points: Column(Integer, nullable=False)
    sdlc_stage: Column(Integer, nullable=False)
    prompt: Column(String, nullable=False)
    answer: Column(Integer, nullable=False)
    choice1: Column(String, nullable=False)
    choice2: Column(String, nullable=False)
    choice3: Column(String, nullable=False)
    choice4: Column(String, nullable=False)
    name = Column(String, nullable=False)
