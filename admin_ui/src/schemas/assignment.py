from typing import Optional
from uuid import UUID

from pydantic import BaseModel


# Shared properties
class AssignmentBase(BaseModel):
    assigner: str
    assignee: str


# Properties to receive on assignment creation
class AssignmentCreate(AssignmentBase):
    pass


# Properties to receive on assignment update
class AssignmentUpdate(BaseModel):
    """
    All update fields should be optional, as updates are done via HTTP PATCH,
    which must support partial updates
    """

    id: str
    assigner: Optional[str] = None
    assignee: Optional[str] = None


# Properties shared by models stored in DB
class AssignmentInDBBase(AssignmentBase):
    id: UUID
    assigner: str
    assignee: str

    class Config:
        orm_mode = True


# Properties to return to client
class Assignment(AssignmentInDBBase):
    pass


# Properties properties stored in DB
class AssignmentInDB(AssignmentInDBBase):
    pass
