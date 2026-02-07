from typing import Annotated

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app.schemas.user import UserResponse
from app.core.dependencies import get_current_user
from app.models.user import User
from app.repositories import user_repo
from app.db.session import get_db

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me", response_model=UserResponse)
def read_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user

@router.delete("/me")
def delete_account(
    current_user: Annotated[User, Depends(get_current_user)],
     db: Annotated[Session,Depends(get_db)]
):
    """
    Soft delete - disables the user's account.
    User will no longer be able to log in or use the API.
    """
    user_repo.disable_user(db, user_id=current_user.id)

    return {
        "message": "Account disabled successfully. Contact support to reactivate."
    }