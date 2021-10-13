from hashlib import sha256

import models
import schemas
from models.student import Student
from schemas.student import StudentCreate, StudentUpdate
from sqlalchemy.orm import Session

from crud.base import CRUDBase


class CRUDStudent(CRUDBase[Student, StudentCreate, StudentUpdate]):
    def create(self, db: Session, student: schemas.StudentCreate):
        db_student = models.Student(
            email=student.email,
            name=student.name,
            points=student.points,
        )
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return db_student

    def read(self, db: Session, email: str) -> Student:
        return db.query(models.Student).filter(models.Student.email == email).first()

    def update(self, db: Session, new_student: schemas.StudentUpdate):
        old_student = (
            db.query(models.Student)
            .filter(models.Student.email == new_student.email)
            .first()
        )
        return super().update(db, db_obj=old_student, obj_in=new_student)


student = CRUDStudent(Student)
