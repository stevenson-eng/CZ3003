from typing import Optional

from pydantic import BaseModel


# Shared properties
class StudentBase(BaseModel):
    email: str
    name: str
    points: int = 0


# Properties to receive on student creation
class StudentCreate(StudentBase):
    pass


# Properties to receive on student update
class StudentUpdate(BaseModel):
    """
    All update fields should be optional, as updates are done via HTTP PATCH,
    which must support partial updates
    """

    email: Optional[str] = None
    name: Optional[str] = None
    points: Optional[int] = None


# Properties shared by models stored in DB
class StudentInDBBase(StudentBase):
    class Config:
        orm_mode = True


# Properties to return to client
class Student(StudentInDBBase):
    pass


# Properties properties stored in DB
class StudentInDB(StudentInDBBase):
    pass
