import uuid

from db.database import Base
from sqlalchemy import Column, Integer, String


class Student(Base):
    __tablename__ = "student"

    # TODO - ensure that foreign key constraints, if any, are enforced
    # TODO - https://docs.sqlalchemy.org/en/14/core/constraints.html
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True, index=True)
    name = Column(String)
    points = Column(Integer)
