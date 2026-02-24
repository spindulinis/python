from typing import Any

from sqlmodel import Session

from models.product import Product
from models.product_create import ProductCreate
from models.product_update import ProductUpdate

def create_product(*, session: Session, product_create: ProductCreate) -> Product:
    db_obj = Product.model_validate(product_create)
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj

def update_product(*, session: Session, db_product: Product, product_in: ProductUpdate) -> Any:
    product_data = product_in.model_dump(exclude_unset=True)
    extra_data = {}
    db_product.sqlmodel_update(product_data, update=extra_data)
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product