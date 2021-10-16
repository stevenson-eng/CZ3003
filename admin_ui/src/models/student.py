import uuid
import models

from db.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Student(Base):
    __tablename__ = "student"

    # TODO - ensure that foreign key constraints, if any, are enforced
    # TODO - https://docs.sqlalchemy.org/en/14/core/constraints.html
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True, index=True)
    name = Column(String)
    points = Column(Integer)
    mail = relationship(models.Mail, cascade="all,delete", backref="student")
    assignment = relationship(models.Assignment, cascade="all,delete", backref="student")
    attempt = relationship(models.Attempt, cascade="all,delete", backref="student")
