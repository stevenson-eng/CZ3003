from typing import Optional
from uuid import UUID

from pydantic import BaseModel


# Shared properties
class NpcBase(BaseModel):
    subquest_name: str
    name: str


# Properties to receive on npc creation
class NpcCreate(NpcBase):
    pass


# Properties to receive on npc update
class NpcUpdate(BaseModel):
    """
    All update fields should be optional, as updates are done via HTTP PATCH,
    which must support partial updates
    """

    id: str
    subquest_name: Optional[str] = None
    name: Optional[str] = None


# Properties shared by models stored in DB
class NpcInDBBase(NpcBase):
    id: UUID
    subquest_name: str
    name: str

    class Config:
        orm_mode = True


# Properties to return to client
class Npc(NpcInDBBase):
    pass


# Properties properties stored in DB
class NpcInDB(NpcInDBBase):
    pass
