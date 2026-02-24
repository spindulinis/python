from sqlmodel import Column, Field, SQLModel, Text

class ProductBase(SQLModel):
    title: str | None = Field(default=None, max_length=255)
    description: str | None = Field(
        default=None, 
        sa_column=Column(Text)
    )