from sqlmodel import Field, SQLModel


class ProductCategory(SQLModel, table=True):
    __tablename__ = "product_category" # type: ignore
    product_id: int = Field(foreign_key="product.id", primary_key=True)
    category_id: int = Field(foreign_key="category.id", primary_key=True)