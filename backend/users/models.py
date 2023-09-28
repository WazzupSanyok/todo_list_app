from typing import TYPE_CHECKING

from tortoise import fields
from tortoise.fields import ReverseRelation
from tortoise.models import Model

if TYPE_CHECKING:
    from task_lists.models import TaskList


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=63)
    mail = fields.CharField(max_length=255)
    password = fields.CharField(max_length=63)
    task_lists: ReverseRelation["TaskList"]
