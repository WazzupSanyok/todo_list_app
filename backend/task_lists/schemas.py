from pydantic import BaseModel


class TaskListBaseSchema(BaseModel):
    title: str

    class Config:
        orm_mode = True


class TaskListSchema(TaskListBaseSchema):
    id: int
