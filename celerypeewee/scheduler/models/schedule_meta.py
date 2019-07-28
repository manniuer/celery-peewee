from .base_model import BaseEntity
from peewee import DateTimeField, IntegerField


class ScheduleMeta(BaseEntity):
    last_run_at = DateTimeField(null=True)
    total_run_count = IntegerField(null=True, default=0)
