from sqlmodel import Field, SQLModel
from typing import Any
from pydantic import ConfigDict
from pydantic.alias_generators import to_camel

class AttributeBase(SQLModel):
    title: str | None = Field(default=None, max_length=255)
    
    model_config: Any = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        from_attributes=True
    )