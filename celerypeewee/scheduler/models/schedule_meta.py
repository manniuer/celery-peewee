from .base_model import BaseEntity
from .schedule_task import ScheduleTask
from peewee import DateTimeField, ForeignKeyField, IntegerField


class ScheduleMeta(BaseEntity):
    parent = ForeignKeyField(column_name="id", field="id", backref='meta', model=ScheduleTask, primary_key=True)
    last_run_at = DateTimeField(null=True)
    total_run_count = IntegerField(null=True, default=0)
