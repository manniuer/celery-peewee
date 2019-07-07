from .baseentity import BaseEntity
from peewee import DateTimeField


class ScheduleInfo(BaseEntity):
    last_changed_at = DateTimeField(null=True)
