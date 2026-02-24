from fastapi import APIRouter, HTTPException
from sqlmodel import col, func, select

from api.deps import (
    SessionDep,
)
import crud
from models.product import Product
from models.product_create import ProductCreate
from models.product_public import ProductPublic
from models.product_update import ProductUpdate
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

@router.get("/{product_id}", response_model=ProductPublic)
def read_product_by_id(product_id: int, session: SessionDep):
    """
    Get a specific product by id.
    """
    product = session.get(Product, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/", response_model=ProductPublic)
def create_product(*, session: SessionDep, product_in: ProductCreate):
    """
    Create new product.
    """
    product = crud.create_product(session=session, product_create=product_in)
    return product

@router.patch("/{product_id}",response_model=ProductPublic)
def update_user(*, session: SessionDep, product_id: int, product_in: ProductUpdate):
    """
    Update a product.
    """

    db_product = session.get(Product, product_id)
    if not db_product:
        raise HTTPException(
            status_code=404,
            detail="The product with this id does not exist in the system",
        )
    db_product = crud.update_product(session=session, db_product=db_product, product_in=product_in)
    return db_product