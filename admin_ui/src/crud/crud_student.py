from hashlib import sha256
from typing import List

import models
import schemas
from models.student import Student
from schemas.student import StudentCreate, StudentUpdate
from sqlalchemy.orm import Session
from sqlalchemy import desc, collate
from fastapi import HTTPException, status, Response

from crud.base import CRUDBase
from typing import List

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
    
    def read_all(self, db: Session) -> List[Student]:
        return db.query(models.Student).all()

    def update(self, db: Session, new_student: schemas.StudentUpdate):
        old_student = (
            db.query(models.Student)
            .filter(models.Student.email == new_student.email)
            .first()
        )
        return super().update(db, db_obj=old_student, obj_in=new_student)

    def getLeaderboard(self, db: Session, limit: int) -> List[Student]:
        return db.query(models.Student).order_by(
            desc(Student.points),
            collate(Student.name, 'NOCASE')
        ).limit(limit).all()

    def delete(self, db: Session, email: str):
        delete_student = db.query(models.Student).filter(models.Student.email == email).first()
        if delete_student is not None:
            print("delete", delete_student)
            db.delete(delete_student)
            db.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status_code=status.HTTP_404_NOT_FOUND)

student = CRUDStudent(Student)
