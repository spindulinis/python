from sqlmodel import SQLModel
from models.product_public import ProductPublic

class ProductsPublic(SQLModel):
    items: list[ProductPublic]
    total: int
    limit: int
    offset: int