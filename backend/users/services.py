from fastapi_jwt_auth import AuthJWT
from passlib.context import CryptContext

from users.models import User
from users.schemas import AuthTokens, UserRegistrationSchema, AccessToken


async def create_user(user_data: UserRegistrationSchema) -> User:
    crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    user = await User.create(
        username=user_data.username,
        email=user_data.email,
        password=crypt_context.hash(user_data.password)
    )
    return user


def verify_password(password: str, password_hash: str) -> bool:
    crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return crypt_context.verify(password, password_hash)


def create_tokens(user: User, authorize_jwt: AuthJWT) -> AuthTokens:
    access_token = authorize_jwt.create_access_token(user.id)
    refresh_token = authorize_jwt.create_refresh_token(user.id)
    return AuthTokens(
        access_token=access_token,
        refresh_token=refresh_token,
    )


def generate_access_token(user: User, authorize_jwt: AuthJWT) -> AccessToken:
    access_token = authorize_jwt.create_access_token(user.id)
    return AccessToken(
        access_token=access_token,
    )
