from sqlmodel import Column, Field, SQLModel, Text
from pydantic import ConfigDict
from pydantic.alias_generators import to_camel
from typing import Any

class ProductBase(SQLModel):
    title: str | None = Field(default=None, max_length=255)
    description: str | None = Field(
        default=None, 
        sa_column=Column(Text)
    )

    model_config: Any = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        from_attributes=True
    )