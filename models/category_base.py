from sqlmodel import Column, Field, SQLModel, Text

class CategoryBase(SQLModel):
    order: int | None = Field(default=0)
    title: str | None = Field(default=None, max_length=255)
    description: str | None = Field(
        default=None, 
        sa_column=Column(Text)
    )