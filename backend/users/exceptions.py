from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST


class IncorrectUserCredentials(HTTPException):
    def __init__(self):
        super().__init__(HTTP_400_BAD_REQUEST, "Incorrect user credentials")
