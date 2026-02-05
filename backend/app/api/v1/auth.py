from typing import Annotated

from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta

from app.schemas.auth import Token, RegisterRequest
from app.schemas.user import UserResponse
from app.core.security import verify_password, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES, get_password_hash
from app.repositories import user_repo
from app.db.session import get_db

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/token", response_model=Token)
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
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    )
    return {"access_token": access_token, "token_type": "bearer"}


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
