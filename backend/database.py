from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

from config import get_settings, Settings

TORTOISE_ORM = {
    "connections": {"default": f"postgres://{get_settings().POSTGRES_USER}:{get_settings().POSTGRES_PASSWORD}"
                               f"@{get_settings().POSTGRES_HOST}:{get_settings().POSTGRES_PORT}"
                               f"/{get_settings().POSTGRES_DB}"},
    "apps": {
        "models": {
            "models": get_settings().POSTGRES_MODELS,
            "default_connection": "default",
        },
    },
}


def init_db(app: FastAPI, settings: Settings) -> None:
    register_tortoise(
        app,
        db_url=f"postgres://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}"
               f"@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}",
        modules={"models": settings.POSTGRES_MODELS},
        generate_schemas=False,
        add_exception_handlers=True,
    )
    Tortoise.init_models(get_settings().POSTGRES_MODELS, "models")
