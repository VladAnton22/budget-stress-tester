from typing import Annotated

from fastapi import Depends, APIRouter
from app.schemas.user import UserResponse
from app.core.dependencies import get_current_user

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me", response_model=UserResponse)
def read_me(current_user: Annotated[UserResponse, Depends(get_current_user)]):
    return current_user