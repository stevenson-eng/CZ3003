from typing import Optional
from uuid import UUID

from pydantic import BaseModel


# Shared properties
class SubquestBase(BaseModel):
    quest_id: str


# Properties to receive on subquest creation
class SubquestCreate(SubquestBase):
    pass


# Properties to receive on subquest update
class SubquestUpdate(BaseModel):
    """
    All update fields should be optional, as updates are done via HTTP PATCH,
    which must support partial updates
    """

    id: str
    quest_id: Optional[str] = None


# Properties shared by models stored in DB
class SubquestInDBBase(SubquestBase):
    id: UUID
    quest_id: str

    class Config:
        orm_mode = True


# Properties to return to client
class Subquest(SubquestInDBBase):
    pass


# Properties properties stored in DB
class SubquestInDB(SubquestInDBBase):
    pass