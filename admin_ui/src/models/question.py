import uuid

from db.database import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class Question(Base):
    __tablename__ = "question"

    # TODO - ensure that foreign key constraints, if any, are enforced
    # TODO - https://docs.sqlalchemy.org/en/14/core/constraints.html
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    category_name = Column(String, ForeignKey("category.category_name"), nullable=False)
    quest_name = Column(String, ForeignKey("quest.quest_name"), nullable=False)
    subquest_name = Column(String, ForeignKey("subquest.subquest_name"), nullable=False)
    assignment_id = Column(String, ForeignKey("assignment.assignment_id"), nullable=False)
    difficulty = Column(Integer, nullable=False)
    points = Column(Integer, nullable=False)
    prompt = Column(String, nullable=False)
    answer = Column(Integer, nullable=False)
    choice1 = Column(String, nullable=False)
    choice2 = Column(String, nullable=False)
    choice3 = Column(String, nullable=False)
    choice4 = Column(String, nullable=False)
