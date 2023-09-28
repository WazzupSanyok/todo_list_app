from pydantic import BaseModel, constr


class TaskListBaseSchema(BaseModel):
    title: constr(max_length=255)

    class Config:
        orm_mode = True


class TaskListSchema(TaskListBaseSchema):
    id: int
