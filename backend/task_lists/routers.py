from fastapi import APIRouter, Depends, Response
from pydantic import parse_obj_as
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT

from task_lists.exceptions import TaskListNotFound
from task_lists.models import TaskList
from task_lists.schemas import TaskListSchema, TaskListBaseSchema
from users.dependencies import get_user
from users.models import User

router = APIRouter()


@router.get("/")
async def get_tasks_lists(user: User = Depends(get_user)) -> list[TaskListSchema]:
    task_lists = await TaskList.filter(user_id=user.id).all()
    return parse_obj_as(list[TaskListSchema], task_lists)


@router.get("/{task_list_id}")
async def get_tasks_list(task_list_id: int, user: User = Depends(get_user)) -> TaskListSchema:
    task_list = await TaskList.get_or_none(id=task_list_id, user_id=user.id)

    if not task_list:
        raise TaskListNotFound()

    return TaskListSchema.from_orm(task_list)


@router.post(
    "/",
    status_code=HTTP_201_CREATED,
)
async def create_tasks_list(task_lists_data: TaskListBaseSchema, user: User = Depends(get_user)):
    task_list = await TaskList.create(
        title=task_lists_data.title,
        user_id=user.id,
    )
    return TaskListSchema.from_orm(task_list)


@router.delete(
    "/{task_list_id}",
    status_code=HTTP_204_NO_CONTENT
)
async def delete_task_list(task_list_id, user: User = Depends(get_user)) -> Response:
    task_list = await TaskList.get_or_none(id=task_list_id, user_id=user.id)

    if not task_list:
        raise TaskListNotFound()

    await TaskList.filter(id=task_list_id, user_id=user.id).delete()

    return Response(status_code=HTTP_204_NO_CONTENT)
