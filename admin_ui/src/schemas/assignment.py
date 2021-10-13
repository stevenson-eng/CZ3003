from typing import Optional
from uuid import UUID

from pydantic import BaseModel


# Shared properties
class AssignmentBase(BaseModel):
    assigner: str
    assignee: str
    points_scored: Optional[int] = None
    time_to_complete_in_seconds: Optional[int] = None
    description: Optional[str] = None

# Properties to receive on assignment creation
class AssignmentCreate(AssignmentBase):
    pass


# Properties to receive on assignment update
class AssignmentUpdate(BaseModel):
    """
    All update fields should be optional, as updates are done via HTTP PATCH,
    which must support partial updates
    """

    assigner: Optional[str] = None
    assignee: Optional[str] = None
    points_scored: Optional[int] = None
    time_to_complete_in_seconds: Optional[int] = None
    description: Optional[str] = None

# Properties shared by models stored in DB
class AssignmentInDBBase(AssignmentBase):
    id: UUID

    class Config:
        orm_mode = True


# Properties to return to client
class Assignment(AssignmentInDBBase):
    pass


# Properties properties stored in DB
class AssignmentInDB(AssignmentInDBBase):
    pass
