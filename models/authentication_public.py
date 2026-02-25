from sqlmodel import Field, SQLModel

from models.user_public import UserPublic

class AuthenticationPublic(SQLModel):
    user: UserPublic
    accessToken: str = Field(serialization_alias="accessToken")