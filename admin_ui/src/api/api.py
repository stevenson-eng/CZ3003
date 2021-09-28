from fastapi import APIRouter

from api.endpoints import assignment, student, teacher  # TODO - import the endpoint

api_router = APIRouter()
api_router.include_router(student.router, prefix="/student", tags=["student"])
api_router.include_router(teacher.router, prefix="/teacher", tags=["teacher"])
api_router.include_router(assignment.router, prefix="/assignment", tags=["assignment"])


# TODO api_router.include_router(xxx.router, prefix="/xxx", tags=["xxx"])
