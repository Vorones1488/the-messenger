from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from src.auth.auth import auth_backend
from src.auth.manage import get_user_manager
from src.model.user import User
from src.schemas.auth_schemas import UserCreate, UserRead

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
app = FastAPI()

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
