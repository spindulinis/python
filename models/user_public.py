from datetime import datetime
from models.user_base import UserBase

class UserPublic(UserBase):
    id: int
    created_date: datetime | None = None