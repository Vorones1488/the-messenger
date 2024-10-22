from typing import Optional

from fastapi_users import schemas
from pydantic import EmailStr


class UserRead(schemas.BaseUser[int]):
    id: int
    name: str
    email: EmailStr
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = True


class UserCreate(schemas.BaseUserCreate):
    name: str
    email: EmailStr
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = True
