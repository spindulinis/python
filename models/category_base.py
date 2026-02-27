from typing import Optional, Any

from pydantic import ConfigDict
from pydantic.alias_generators import to_camel
from sqlmodel import Column, Field, SQLModel, Text

class CategoryBase(SQLModel):
    order: int | None = Field(default=0)
    title: str | None = Field(default=None, max_length=255)
    description: str | None = Field(
        default=None, 
        sa_column=Column(Text)
    )
    parent_id: Optional[int] = Field(default=None, foreign_key="category.id")

    model_config: Any = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        from_attributes=True
    )