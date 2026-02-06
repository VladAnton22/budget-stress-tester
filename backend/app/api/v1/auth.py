from typing import Annotated
from uuid import UUID

from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.schemas.auth import RegisterRequest, TokenResponse, RefreshTokenRequest
from app.schemas.user import UserResponse
from app.core.security import verify_password, create_access_token, create_refresh_token, verify_token, get_password_hash
from app.repositories import user_repo
from app.db.session import get_db

router = APIRouter(prefix="/auth", tags=["auth"])

oauth2_refresh_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/refresh")


@router.post("/token", response_model=TokenResponse)
def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        db: Session = Depends(get_db),
):
    user = user_repo.get_by_username(db, username=form_data.username)
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(subject=str(user.id))
    refresh_token = create_refresh_token(subject=str(user.id))

    return TokenResponse(
        access_token=access_token,
        refresh_token=refresh_token,
        token_type="bearer"
    )


@router.post("/register", response_model=UserResponse, status_code=201)
def register_user(
        payload: RegisterRequest,
        db: Annotated[Session, Depends(get_db)]
):
    if user_repo.exists_by_username(db, username=payload.username):
        raise HTTPException(
            status_code=400,
            detail="Username already taken",
        )

    if user_repo.exists_by_email(db, email=payload.email):
        raise HTTPException(
            status_code=400,
            detail="Email already registered",
        )

    user = user_repo.create_user(
        db,
        username=payload.username,
        email=payload.email,
        password_hash=get_password_hash(payload.password),
    )

    return user


@router.post("/refresh", response_model=TokenResponse)
def refresh_access_token(
        request: RefreshTokenRequest,
        db: Session = Depends(get_db)
):
    payload = verify_token(request.refresh_token, token_type="refresh")

    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload.",
        )

    user = user_repo.get_by_id(db, user_id=UUID(user_id))
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found."
        )

    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is disabled.",
        )

    new_access_token = create_access_token(subject=user_id)
    new_refresh_token = create_refresh_token(subject=user_id)

    return TokenResponse(
        access_token=new_access_token,
        refresh_token=new_refresh_token,
    )
