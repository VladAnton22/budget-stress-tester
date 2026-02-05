from typing import Annotated

from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from jwt.exceptions import InvalidTokenError

from app.core.security import decode_token
from app.repositories.user_repo import get_by_username
from app.db.session import get_db
from app.schemas.user import UserBase

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token")

def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Annotated[Session, Depends(get_db)],
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode_token(token)
        username: str | None = payload.get("sub")   # sub is the subject of the jwt
        if username is None:
            raise credentials_exception
    except InvalidTokenError:
        raise credentials_exception

    user = get_by_username(db, username)
    if user is None:
        raise credentials_exception

    return user

def get_current_active_user(user: Annotated[UserBase, Depends(get_current_user)]):
    if user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return user


