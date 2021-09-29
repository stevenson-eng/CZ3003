import uuid

from db.database import Base
from sqlalchemy import Column, String, ForeignKey


class Category(Base):
    __tablename__ = "category"

    # TODO - ensure that foreign key constraints, if any, are enforced
    # TODO - https://docs.sqlalchemy.org/en/14/core/constraints.html
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
