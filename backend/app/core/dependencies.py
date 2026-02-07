from typing import Annotated
from uuid import UUID

from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from jwt.exceptions import InvalidTokenError

from app.core.security import decode_token
from app.repositories import user_repo
from app.db.session import get_db
from app.schemas.user import UserResponse
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token")

def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Annotated[Session, Depends(get_db)],
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode_token(token)

        if payload.get("type") != "access":
            raise credentials_exception

        user_id: str | None = payload.get("sub")   # sub is the subject of the jwt
        if user_id is None:
            raise credentials_exception
    except InvalidTokenError as e:
        raise credentials_exception

    user = user_repo.get_by_id(db, UUID(user_id))

    if user is None:
        raise credentials_exception

    return user

def get_current_active_user(user: Annotated[UserResponse, Depends(get_current_user)]) -> UserResponse:
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Account is disabled. Please contact support.",
        )
    return user


