import uuid

from db.database import Base
from sqlalchemy import Column, String, ForeignKey


class Quest(Base):
    __tablename__ = "quest"

    # TODO - ensure that foreign key constraints, if any, are enforced
    # TODO - https://docs.sqlalchemy.org/en/14/core/constraints.html
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    category_id = Column(String, ForeignKey("category.id"), nullable=False)
