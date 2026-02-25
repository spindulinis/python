from sqlmodel import Field, SQLModel


class ProductAttribute(SQLModel, table=True):
    __tablename__ = "product_attribute" # type: ignore
    product_id: int | None = Field(default=None, foreign_key="product.id", primary_key=True)
    attribute_id: int | None = Field(default=None, foreign_key="attribute.id", primary_key=True)