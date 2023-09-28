from typing import TYPE_CHECKING

from tortoise import fields
from tortoise.fields import ForeignKeyRelation
from tortoise.models import Model

if TYPE_CHECKING:
    from task_lists.models import TaskList


class Task(Model):
    id = fields.IntField(pk=True)
    task_list: ForeignKeyRelation["TaskList"] = fields.ForeignKeyField('models.TaskList', related_name='tasks')
    name = fields.CharField(max_length=255)
    description = fields.TextField(max_length=1023)
    complete = fields.BooleanField
