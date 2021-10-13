import uuid

from db.database import Base
from sqlalchemy import Column, String, ForeignKey, Integer


class Assignment(Base):
    __tablename__ = "assignment"

    # TODO - ensure that foreign key constraints, if any, are enforced
    # TODO - https://docs.sqlalchemy.org/en/14/core/constraints.html
    assignment_id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    assigner = Column(String, ForeignKey("teacher.email"), nullable=False)
    assignee = Column(String, ForeignKey("student.email"), nullable=False)
    description = Column(String, nullable=False)
    points_scored = Column(Integer, nullable=True)
    time_to_complete_in_seconds = Column(Integer, nullable=True)
