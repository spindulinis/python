from fastapi import APIRouter, HTTPException
from sqlmodel import col, func, select

from api.deps import (
    SessionDep,
)
from models.product import Product
from models.product_public import ProductPublic
from models.products_public import ProductsPublic


router = APIRouter(prefix="/public-products", tags=["public-products"])

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

@router.get("/{product_id}", response_model=ProductPublic)
def read_product_by_id(product_id: int, session: SessionDep):
    """
    Get a specific product by id.
    """
    product = session.get(Product, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product