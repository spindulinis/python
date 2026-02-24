from typing import Any

from sqlmodel import Session

from models.category import Category
from models.category_create import CategoryCreate
from models.category_update import CategoryUpdate

def create_category(*, session: Session, category_create: CategoryCreate) -> Category:
    db_obj = Category.model_validate(category_create)
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj

def update_category(*, session: Session, db_category: Category, category_in: CategoryUpdate) -> Any:
    category_data = category_in.model_dump(exclude_unset=True)
    extra_data = {}
    db_category.sqlmodel_update(category_data, update=extra_data)
    session.add(db_category)
    session.commit()
    session.refresh(db_category)
    return db_category