from fastapi import FastAPI
from database import init_db
from config import get_settings

app = FastAPI(
    title="TODO-List",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
)


@app.on_event("startup")
async def startup() -> None:
    settings = get_settings()

    init_db(app, settings)

    app.dependency_overrides = {
        get_settings: lambda: settings,
    }
