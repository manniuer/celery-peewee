from .base_model import BaseEntity
from .schedule_task import ScheduleTask
from peewee import DateTimeField, IntegerField, ForeignKeyField


class ScheduleMeta(BaseEntity):
    last_run_at = DateTimeField(null=True)
    total_run_count = IntegerField(null=True, default=0)

    schedule_task = ForeignKeyField(ScheduleTask, backref='meta')
