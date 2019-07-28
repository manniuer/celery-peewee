import json
from .base_model import BaseEntity
from .crontab import Crontab
from .interval import Interval
from .schedule_meta import ScheduleMeta
from peewee import DateTimeField, ForeignKeyField, CharField, TextField, BooleanField, AutoField
from celery import current_app
from datetime import datetime


class ScheduleTask(BaseEntity):
    id = AutoField(primary_key=True)
    name = CharField(unique=True)
    task = CharField()
    task_args = TextField(default='[]')
    task_kwargs = TextField(default='{}')
    queue = CharField(null=True)
    exchange = CharField(null=True)
    routing_key = CharField(null=True)
    enabled = BooleanField(default=True)
    expires_at = DateTimeField(null=True)
    created_at = DateTimeField(null=True, default=datetime.now)
    modified_at = DateTimeField(null=True)
    remarks = TextField(null=True)

    crontab = ForeignKeyField(Crontab, backref='tasks', null=True)
    interval = ForeignKeyField(Interval, backref='tasks', null=True)

    @property
    def schedule_meta(self):
        meta, _ = ScheduleMeta.get_or_create(id=self.id)
        return meta

    @property
    def args(self):
        return json.loads(self.task_args)

    @args.setter
    def args(self, data: list):
        self.task_args = json.dumps(data)

    @property
    def kwargs(self):
        return json.loads(self.task_kwargs)

    @kwargs.setter
    def kwargs(self, data: dict):
        self.task_kwargs = json.dumps(data)

    @property
    def schedule(self):
        if self.crontab:
            return self.crontab.schedule
        if self.interval:
            return self.interval.schedule

    @classmethod
    def get_available_tasks(cls):
        return (x for x in cls.select().where(cls.enabled == True) if x.task in current_app.tasks)

