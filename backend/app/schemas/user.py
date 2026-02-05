from pydantic import BaseModel, EmailStr
from uuid import UUID

class UserBase(BaseModel):
    username: str
    email: EmailStr | None = None
    disabled: bool | None = None

class UserResponse(BaseModel):
    id: UUID
    username: str
    email: EmailStr
    disabled: bool

    class Config:
        from_attribute = True