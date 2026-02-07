from pydantic import BaseModel, EmailStr, ConfigDict
from uuid import UUID


class UserResponse(BaseModel):
    id: UUID
    username: str
    email: EmailStr
    disabled: bool

    model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    email: EmailStr | None = None

    model_config = ConfigDict(from_attributes=True)