from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel


# Shared properties
class StudentBase(BaseModel):
    # Password should never be exposed by default, hashed or not
    id: UUID = uuid4()
    email: str
    name: str
    points: int = 0


# Properties to receive on student creation
class StudentCreate(StudentBase):
    password: str


# Properties to receive on student update
class StudentUpdate(BaseModel):
    """
    All update fields should be optional, as updates are done via HTTP PATCH,
    which must support partial updates
    """

    id: str
    email: Optional[str] = None
    name: Optional[str] = None
    points: Optional[int] = None
    password: Optional[str] = None


# Properties shared by models stored in DB
class StudentInDBBase(StudentBase):
    id: UUID
    email: str
    hashed_password: str
    name: str
    points: int

    class Config:
        orm_mode = True


# Properties to return to client
class Student(StudentInDBBase):
    pass


# Properties properties stored in DB
class StudentInDB(StudentInDBBase):
    pass
