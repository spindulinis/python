from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import col, func, select

from api.deps import (
    SessionDep,
    get_current_admin_user,
)
from crud import category as category_crud
from models.base import Message
from models.categories_public import CategoriesPublic
from models.category import Category
from models.category_create import CategoryCreate
from models.category_public import CategoryPublic
from models.category_update import CategoryUpdate


router = APIRouter(prefix="/category", tags=["category"])

@router.get("/", response_model=CategoriesPublic, dependencies=[Depends(get_current_admin_user)])
def read_categories(session: SessionDep, skip: int = 0, limit: int = 100):
    """
    Retrieve categories.
    """

    count_statement = select(func.count()).select_from(Category)
    count = session.exec(count_statement).one()

    statement = (
        select(Category).order_by(col(Category.order).desc()).offset(skip).limit(limit)
    )
    categories = session.exec(statement).all()

    return CategoriesPublic(data=categories, count=count)

@router.get("/{category_id}", response_model=CategoryPublic, dependencies=[Depends(get_current_admin_user)])
def read_category_by_id(category_id: int, session: SessionDep):
    """
    Get a specific category by id.
    """
    category = session.get(Category, category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.post("/", response_model=CategoryPublic, dependencies=[Depends(get_current_admin_user)])
def create_category(*, session: SessionDep, category_in: CategoryCreate):
    """
    Create new category.
    """
    category = category_crud.create_category(session=session, category_create=category_in)
    return category

@router.patch("/{category_id}",response_model=CategoryPublic, dependencies=[Depends(get_current_admin_user)])
def update_category(*, session: SessionDep, category_id: int, category_in: CategoryUpdate):
    """
    Update a category.
    """

    db_category = session.get(Category, category_id)
    if not db_category:
        raise HTTPException(
            status_code=404,
            detail="The category with this id does not exist in the system",
        )
    db_category = category_crud.update_category(session=session, db_category=db_category, category_in=category_in)
    return db_category

@router.delete("/{category_id}")
def delete_category(session: SessionDep, category_id: int, dependencies=[Depends(get_current_admin_user)]):
    """
    Delete a category.
    """
    category = session.get(Category, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    session.delete(category)
    session.commit()
    return Message(message="Category deleted successfully")