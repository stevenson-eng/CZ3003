from uuid import UUID, uuid4

from pydantic import BaseModel


# Shared properties
class StudentBase(BaseModel):
    # Password should never be exposed by default, hashed or not
    id: UUID
    email: str
    name: str
    points: int


# Properties to receive on student creation
class StudentCreate(StudentBase):
    password: str


# Properties to receive on student update
class StudentUpdate(StudentBase):
    password: str

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
