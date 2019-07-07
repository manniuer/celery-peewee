from .base_model import BaseEntity
from .schedule_task import ScheduleTask
from peewee import DateTimeField, ForeignKeyField, IntegerField


class ScheduleMeta(BaseEntity):
    last_run_at = DateTimeField(null=True)
    parent = ForeignKeyField(column_name="schedule_task_id", field="id", model=ScheduleTask, primary_key=True)
    total_run_count = IntegerField(null=True)
