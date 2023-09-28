from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from starlette.status import HTTP_201_CREATED

from users.dependencies import get_user
from users.exceptions import IncorrectUserCredentials
from users.models import User
from users.schemas import UserRegistrationSchema, UserSchema, UserLoginSchema
from users.services import create_tokens, create_user, verify_password, generate_access_token
from users.validators import UserValidator

router = APIRouter()


@router.post(
    "/register",
    status_code=HTTP_201_CREATED,
)
async def register(user_data: UserRegistrationSchema, authorize_jwt: AuthJWT = Depends()):
    user_validator = UserValidator(user_data)
    await user_validator.validate()

    user = await create_user(user_data)

    return create_tokens(user, authorize_jwt)


@router.post(
    "/login",
    status_code=HTTP_201_CREATED,
)
async def login(user_login_data: UserLoginSchema, authorize_jwt: AuthJWT = Depends()):
    user = await User.get_or_none(username=user_login_data.username)

    if not user or not verify_password(user_login_data.password, user.password):
        raise IncorrectUserCredentials()

    return create_tokens(user, authorize_jwt)


@router.post("/refresh")
async def refresh_tokens(authorize_jwt: AuthJWT = Depends()):
    authorize_jwt.jwt_refresh_token_required()

    user_id = authorize_jwt.get_jwt_subject()
    user = await User.get(id=user_id)

    return generate_access_token(user, authorize_jwt)


@router.get("/")
async def _get_user(user: User = Depends(get_user)) -> UserSchema:
    return UserSchema.from_orm(user)
