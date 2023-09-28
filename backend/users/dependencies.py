from fastapi import Depends
from fastapi_jwt_auth import AuthJWT

from users.models import User


async def get_user(authorize_jwt: AuthJWT = Depends()):
    authorize_jwt.jwt_required()

    user_id = authorize_jwt.get_jwt_subject()
    return await User.get(id=user_id)
