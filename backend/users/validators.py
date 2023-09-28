from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from users.models import User
from users.schemas import UserRegistrationSchema


class UserValidator:
    def __init__(self, user_data: UserRegistrationSchema):
        self.user_data = user_data
        self.__errors: list[str] = []

    async def validate(self) -> None:
        await self._validate_email_uniqueness()
        await self._validate_username_uniqueness()
        self._validate_passwords()

        if self.__errors:
            raise HTTPException(HTTP_400_BAD_REQUEST, self.__errors)

    async def _validate_email_uniqueness(self) -> None:
        user = await User.get_or_none(email=self.user_data.email)
        if user:
            self.__errors.append("The user's email address already exists")

    async def _validate_username_uniqueness(self) -> None:
        user = await User.get_or_none(username=self.user_data.username)
        if user:
            self.__errors.append("This username is taken by another user")

    def _validate_passwords(self) -> None:
        if self.user_data.password != self.user_data.repeated_password:
            self.__errors.append("The entered passwords do not match")
