from fastapi import APIRouter

router = APIRouter()


@router.get("/{student_id}")
def read_student(student_id: int):
    return {"student_id": student_id}
