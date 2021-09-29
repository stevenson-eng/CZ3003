import models
import schemas
from models.category import Category
from schemas.category import CategoryCreate, CategoryUpdate
from sqlalchemy.orm import Session

from crud.base import CRUDBase


class CRUDCategory(CRUDBase[Category, CategoryCreate, CategoryUpdate]):
    def create(self, db: Session, category: schemas.CategoryCreate):
        db_category = models.Category(
            name=category.name,
        )
        db.add(db_category)
        db.commit()
        db.refresh(db_category)
        return db_category

    def read(self, db: Session, id: str) -> Category:
        return db.query(models.Category).filter(models.Category.email == id).first()

    def update(self, db: Session, new_category: schemas.CategoryUpdate):
        old_category = (
            db.query(models.Category)
            .filter(models.Category.id == new_category.id)
            .first()
        )
        return super().update(db, db_obj=old_category, obj_in=new_category)


category = CRUDCategory(Category)
