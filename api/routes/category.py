from fastapi import APIRouter, HTTPException
from sqlmodel import col, func, select

from api.deps import (
    SessionDep,
)
from crud import category as category_crud
from models.categories_public import CategoriesPublic
from models.category import Category
from models.category_public import CategoryPublic
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