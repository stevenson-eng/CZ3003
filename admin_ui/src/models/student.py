from db.base_class import Base
from sqlalchemy import Column, Integer, String


class Student(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    hashed_password = Column(String)
    name = Column(String)
    points = Column(Integer)
    # name = Column(Integer, ForeignKey("user.id"))
    # points = relationship("User", back_populates="items")
