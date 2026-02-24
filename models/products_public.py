from sqlmodel import SQLModel
from models.product_public import ProductPublic

class ProductsPublic(SQLModel):
    data: list[ProductPublic]
    count: int