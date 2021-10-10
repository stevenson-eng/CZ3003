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
    subquest_id: Column(String, nullable=False)
    assignment_id: Column(String, nullable=False)
    difficulty: Column(String, nullable=False)
    points: Column(Integer, nullable=False)
    sdlc_stage: Column(String, nullable=False)
    prompt: Column(String, nullable=False)
    answer: Column(String, nullable=False)
    choice1: Column(Integer, nullable=False)
    choice2: Column(Integer, nullable=False)
    choice3: Column(Integer, nullable=False)
    choice4: Column(Integer, nullable=False)
    name = Column(String, nullable=False)
