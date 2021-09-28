from fastapi import APIRouter

from api.endpoints import student, teacher

api_router = APIRouter()
api_router.include_router(student.router, prefix="/student", tags=["student"])
api_router.include_router(teacher.router, prefix="/teacher", tags=["teacher"])

# TODO api_router.include_router(xxx.router, prefix="/xxx", tags=["xxx"])
