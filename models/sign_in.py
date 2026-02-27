from pydantic import EmailStr, BaseModel
from sqlmodel import Field

class SignIn(BaseModel):
    email: EmailStr
    password: str = Field(
        min_length=8,
        max_length=128,
        description="Password must be between 8-128 characters"
    )