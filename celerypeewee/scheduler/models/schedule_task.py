from .base_model import BaseEntity
from .crontab import Crontab
from .interval import Interval
from peewee import DateTimeField, ForeignKeyField, CharField, IntegerField, TextField, BooleanField


class ScheduleTask(BaseEntity):
    name = CharField(unique=True)
    task = CharField()
    task_args = TextField(default='[]')
    task_kwargs = TextField(default='{}')
    interval = ForeignKeyField(column_name="interval_id", field="id", model=Interval, null=True)
    crontab = ForeignKeyField(column_name="crontab_id", field="id", model=Crontab, null=True)
    queue = CharField(null=True)
    exchange = CharField(null=True)
    routing_key = CharField(null=True)
    enabled = BooleanField(default=1)
    expires_at = DateTimeField(null=True)
    created_at = DateTimeField(null=True)
    modified_at = DateTimeField(null=True)
    remarks = TextField(null=True)
