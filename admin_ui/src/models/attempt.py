# import uuid

# from sqlalchemy.sql.sqltypes import DateTime
# from db.database import Base
# from sqlalchemy import Column, String, ForeignKey, Integer, DATETIME


# class Attempt(Base):
#     __tablename__ = "attempt"

#     # TODO - ensure that foreign key constraints, if any, are enforced
#     # TODO - https://docs.sqlalchemy.org/en/14/core/constraints.html
#     id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
#     quest_id = Column(String, ForeignKey("quest.id"), nullable=False)
#     student_email = Column(String, ForeignKey("student.email"), nullable=False)
#     points_scored = Column(Integer, nullable=False)
#     time_to_complete_in_seconds = Column(Integer, nullable=False)
#     completion_datetime = Column(DATETIME)


