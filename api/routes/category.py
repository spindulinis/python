from fastapi import APIRouter, HTTPException
from sqlmodel import col, func, select

from api.deps import (
    SessionDep,
)
from crud import category as category_crud
from models.categories_public import CategoriesPublic
from models.category import Category
from models.category_create import CategoryCreate
from models.category_public import CategoryPublic
from models.category_update import CategoryUpdate
from models.products_public import ProductsPublic


router = APIRouter(prefix="/categories", tags=["categories"])

@router.get("/", response_model=CategoriesPublic)
def read_products(session: SessionDep, skip: int = 0, limit: int = 100):
    """
    Retrieve categories.
    """

    count_statement = select(func.count()).select_from(Category)
    count = session.exec(count_statement).one()

    statement = (
        select(Category).order_by(col(Category.order).desc()).offset(skip).limit(limit)
    )
    categories = session.exec(statement).all()

    return ProductsPublic(data=categories, count=count)

@router.get("/{category_id}", response_model=CategoryPublic)
def read_category_by_id(category_id: int, session: SessionDep):
    """
    Get a specific category by id.
    """
    category = session.get(Category, category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.post("/", response_model=CategoryPublic)
def create_category(*, session: SessionDep, category_in: CategoryCreate):
    """
    Create new category.
    """
    category = category_crud.create_category(session=session, category_create=category_in)
    return category

@router.patch("/{category_id}",response_model=CategoryPublic)
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