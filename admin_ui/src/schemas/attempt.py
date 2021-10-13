# from datetime import datetime
# from typing import Optional
# from uuid import UUID

# from pydantic import BaseModel
# from sqlalchemy.sql.sqltypes import DATETIME


# # Shared properties
# class AttemptBase(BaseModel):
#     quest_id: str
#     student_email: str
#     points_scored: int
#     time_to_complete_in_seconds: int
#     completion_datetime: DATETIME


# # Properties to receive on attempt creation
# class AttemptCreate(AttemptBase):
#     pass


# # Properties to receive on attempt update
# class AttemptUpdate(BaseModel):
#     """
#     All update fields should be optional, as updates are done via HTTP PATCH,
#     which must support partial updates
#     """

#     id: str
#     quest_id: Optional[str] = None
#     student_email: Optional[str] = None
#     points_scored: Optional[int] = None
#     time_to_complete_in_seconds: Optional[int] = None
#     completion_datetime: Optional[DATETIME] = None


# # Properties shared by models stored in DB
# class AttemptInDBBase(AttemptBase):
#     id: UUID
#     quest_id: str
#     student_email: str
#     points_scored: int
#     time_to_complete_in_seconds: int
#     completion_datetime: DATETIME

#     class Config:
#         orm_mode = True
#         arbitrary_types_allowed = True


# # Properties to return to client
# class Attempt(AttemptInDBBase):
#     pass


# # Properties properties stored in DB
# class AttemptInDB(AttemptInDBBase):
#     pass
