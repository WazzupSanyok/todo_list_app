from fastapi import FastAPI, Request
from fastapi_jwt_auth.exceptions import AuthJWTException
from starlette.responses import JSONResponse

from config import get_settings
from database import init_db
from users.routers import router as users_router

from fastapi_jwt_auth import AuthJWT

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
    AuthJWT.load_config(lambda: settings)
    app.dependency_overrides = {
        get_settings: lambda: settings,
    }


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )


app.include_router(users_router, tags=["Users"], prefix="/api/users")
