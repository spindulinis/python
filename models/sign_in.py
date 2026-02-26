from pydantic import EmailStr, BaseModel

class SignIn(BaseModel):
    email: EmailStr
    password: str