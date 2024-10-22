import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

from sqlalchemy import URL

BASE_DIR = Path(__file__).parent.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=os.path.join(BASE_DIR, "src", "../.env"))

    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SECRET: str
    SECRET_RESET: str

    @property
    def DATABASE_URL_asyncpg(self):
        # postgresql+asyncpg://postgres:postgres@localhost:5432/sa
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"


setting = Settings()
