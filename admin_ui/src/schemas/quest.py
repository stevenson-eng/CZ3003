from typing import Optional
from uuid import UUID

from pydantic import BaseModel


# Shared properties
class QuestBase(BaseModel):
    quest_name: str
    category_name: str


# Properties to receive on quest creation
class QuestCreate(QuestBase):
    pass


# Properties to receive on quest update
class QuestUpdate(BaseModel):
    """
    All update fields should be optional, as updates are done via HTTP PATCH,
    which must support partial updates
    """
    quest_name: Optional[str] = None
    category_name: Optional[str] = None


# Properties shared by models stored in DB
class QuestInDBBase(QuestBase):
    quest_name: str
    category_name: str

    class Config:
        orm_mode = True


# Properties to return to client
class Quest(QuestInDBBase):
    pass


# Properties properties stored in DB
class QuestInDB(QuestInDBBase):
    pass
