from .base_model import BaseEntity
from peewee import DateTimeField
from datetime import datetime


class ScheduleInfo(BaseEntity):
    last_changed_at = DateTimeField(default=datetime.now)

    @classmethod
    def get_last_change_at(cls):
        instance, created = cls.get_or_create(id=1)
        return instance.last_changed_at or datetime.now()
