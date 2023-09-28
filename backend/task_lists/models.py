from typing import TYPE_CHECKING

from tortoise import fields
from tortoise.fields import ForeignKeyRelation, ReverseRelation
from tortoise.models import Model

if TYPE_CHECKING:
    from tasks.models import Task
    from users.models import User


class TaskList(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    user: ForeignKeyRelation["User"] = fields.ForeignKeyRelation('models.User', related_name='task_lists')
    tasks: ReverseRelation["Task"]
