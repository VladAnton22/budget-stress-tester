from typing import Annotated

from fastapi import Depends, APIRouter
from app.schemas.user import User
from app.core.dependencies import get_current_user

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user