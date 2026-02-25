from sqlmodel import Field, SQLModel

class AttributeBase(SQLModel):
    title: str | None = Field(default=None, max_length=255)