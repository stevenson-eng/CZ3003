from typing import Optional
from uuid import UUID
from enum import IntEnum

from pydantic import BaseModel

class DifficultyEnum(IntEnum):
    easy = 1
    medium = 2
    hard = 3

class SdlcStageEnum(IntEnum):
    planning = 1
    designing = 2
    development = 3
    testing = 4
    deploying = 5

# Shared properties
class QuestionBase(BaseModel):
    subquest_name: str
    assignment_id: str
    difficulty: DifficultyEnum
    points: int
    sdlc_stage: SdlcStageEnum
    prompt: str
    answer: int
    choice1: str
    choice2: str
    choice3: str
    choice4: str


# Properties to receive on question creation
class QuestionCreate(QuestionBase):
    pass


# Properties to receive on question update
class QuestionUpdate(BaseModel):
    """
    All update fields should be optional, as updates are done via HTTP PATCH,
    which must support partial updates
    """

    id: str
    subquest_name: Optional[str] = None
    assignment_id: Optional[str] = None
    difficulty: Optional[DifficultyEnum] = None
    points: Optional[int] = None
    sdlc_stage: Optional[SdlcStageEnum] = None
    prompt: Optional[str] = None
    answer: Optional[int] = None
    choice1: Optional[str] = None
    choice2: Optional[str] = None
    choice3: Optional[str] = None
    choice4: Optional[str] = None


# Properties shared by models stored in DB
class QuestionInDBBase(QuestionBase):
    id: UUID
    class Config:
        orm_mode = True
        use_enum_values = True


# Properties to return to client
class Question(QuestionInDBBase):
    pass


# Properties properties stored in DB
class QuestionInDB(QuestionInDBBase):
    pass
