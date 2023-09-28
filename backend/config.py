from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
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


@lru_cache
def get_settings() -> Settings:
    return Settings()
