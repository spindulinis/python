from sqlmodel import Field

from models.category_base import CategoryBase

class Category(CategoryBase, table=True):
    id: int | None = Field(default=None, primary_key=True)