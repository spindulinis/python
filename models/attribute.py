from sqlmodel import Field
from models.attribute_base import AttributeBase

class Attribute(AttributeBase, table=True):
    id: int | None = Field(default=None, primary_key=True)