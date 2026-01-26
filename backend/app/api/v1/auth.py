from typing import Annotated

from fastapi import Depends, APIRouter


router = APIRouter(prefix="/auth", tags=["auth"])
