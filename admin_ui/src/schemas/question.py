from typing import Optional
from uuid import UUID
from enum import Enum

from pydantic import BaseModel

class DifficultyEnum(int, Enum):
    easy = 1
    medium = 2
    hard = 3

class SdlcStageEnum(int, Enum):
    planning = 1
    designing = 2
    development = 3
    testing = 4
    deploying = 5

# Shared properties
class QuestionBase(BaseModel):
    subquest_id: str
    assignment_id: str
    difficulty: DifficultyEnum
    points: int
    sdlc_stage: SdlcStageEnum
    prompt: str
    answer: str
    choice1: int
    choice2: int
    choice3: int
    choice4: int
    name: str


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
    subquest_id: Optional[str] = None
    assignment_id: Optional[str] = None
    difficulty: Optional[DifficultyEnum] = None
    points: Optional[int] = None
    sdlc_stage: Optional[SdlcStageEnum] = None
    prompt: Optional[str] = None
    answer: Optional[str] = None
    choice1: Optional[int] = None
    choice2: Optional[int] = None
    choice3: Optional[int] = None
    choice4: Optional[int] = None
    name: Optional[str] = None


# Properties shared by models stored in DB
class QuestionInDBBase(QuestionBase):
    id: UUID
    subquest_id: str
    assignment_id: str
    difficulty: DifficultyEnum
    points: int
    sdlc_stage: SdlcStageEnum
    prompt: str
    answer: str
    choice1: int
    choice2: int
    choice3: int
    choice4: int
    name: str

    class Config:
        orm_mode = True


# Properties to return to client
class Question(QuestionInDBBase):
    pass


# Properties properties stored in DB
class QuestionInDB(QuestionInDBBase):
    pass
