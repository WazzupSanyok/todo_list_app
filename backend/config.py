from functools import lru_cache

from pydantic import BaseSettings


class DatabaseSettings(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_MODELS: list[str] = [
        "aerich.models",
        "users.models",
        "task_lists.models",
        "tasks.models"
    ]


class AuthSettings(BaseSettings):
    authjwt_secret_key: str


class Settings(DatabaseSettings, AuthSettings):
    pass


@lru_cache
def get_settings() -> Settings:
    return Settings()
