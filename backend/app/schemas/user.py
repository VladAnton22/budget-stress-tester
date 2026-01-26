from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    currency: str
    timezone: bool

class UserCreate(UserBase):
    password: str

class USerOut(UserBase):
    id: UUID
    created_at: datetime