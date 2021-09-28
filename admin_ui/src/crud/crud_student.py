from hashlib import sha256

import models
import schemas
from models.student import Student
from schemas.student import StudentCreate, StudentUpdate
from sqlalchemy.orm import Session

from crud.base import CRUDBase


class CRUDStudent(CRUDBase[Student, StudentCreate, StudentUpdate]):
    def create(self, db: Session, student: schemas.StudentCreate):
        hashed_password = sha256(student.password.encode("utf-8")).hexdigest()
        db_student = models.Student(
            email=student.email,
            hashed_password=hashed_password,
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
            db.query(models.Student).filter(models.Student.id == new_student.id).first()
        )
        return super().update(db, db_obj=old_student, obj_in=new_student)


student = CRUDStudent(Student)
