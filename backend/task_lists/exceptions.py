from fastapi import HTTPException
from starlette.status import HTTP_404_NOT_FOUND


class TaskListNotFound(HTTPException):
    def __init__(self):
        super().__init__(HTTP_404_NOT_FOUND, "Task list not found")
