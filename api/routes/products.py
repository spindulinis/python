from fastapi import APIRouter
from sqlmodel import col, func, select

from api.deps import (
    SessionDep,
)
from models.product import Product
from models.products_public import ProductsPublic


router = APIRouter(prefix="/products", tags=["products"])

@router.get("/", response_model=ProductsPublic)
def read_products(session: SessionDep, skip: int = 0, limit: int = 100):
    """
    Retrieve products.
    """

    count_statement = select(func.count()).select_from(Product)
    count = session.exec(count_statement).one()

    statement = (
        select(Product).order_by(col(Product.created_date).desc()).offset(skip).limit(limit)
    )
    products = session.exec(statement).all()

    return ProductsPublic(data=products, count=count)