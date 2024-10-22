from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from src.config import setting

engine = create_async_engine(
    setting.DATABASE_URL_asyncpg, poolclass=NullPool, echo=True
)
async_session_factory = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session():
    async with async_session_factory() as session:
        yield session
