from fastapi import APIRouter

from api.endpoints import mail  # TODO - import the endpoint
from api.endpoints import assignment, student, teacher

api_router = APIRouter()
api_router.include_router(student.router, prefix="/student", tags=["student"])
api_router.include_router(teacher.router, prefix="/teacher", tags=["teacher"])
api_router.include_router(assignment.router, prefix="/assignment", tags=["assignment"])
api_router.include_router(mail.router, prefix="/mail", tags=["mail"])


# TODO api_router.include_router(xxx.router, prefix="/xxx", tags=["xxx"])
