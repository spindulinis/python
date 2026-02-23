from models.base import UserBase
from datetime import datetime

class UserPublic(UserBase):
    id: int
    created_date: datetime | None = None