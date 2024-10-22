from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import String, Boolean
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.model.base import Base

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.model.chat import Chat
from src.model.message import Messege


class User(SQLAlchemyBaseUserTable[int], Base):
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    email: Mapped[str] = mapped_column(
        String(length=320), unique=True, index=True, nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    message_to_chat: Mapped[list["Messege"]] = relationship(
        back_populates="created_by_user"
    )
    chats_user: Mapped[list["Chat"]] = relationship(
        back_populates="users_chat", secondary="chat_users"
    )


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
