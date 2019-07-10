from .base_model import BaseEntity
from peewee import IntegerField, CharField
from celery import schedules
from datetime import timedelta


class Interval(BaseEntity):
    every = IntegerField(null=True)
    period = CharField(null=True)

    @property
    def schedule(self):
        return schedules.schedule(timedelta(**(self.to_dict())))

    @classmethod
    def from_schedule(cls, schedule):
        every = max(schedule.run_every.total_seconds(), 0)
        instance, created = cls.get_or_create(every=every, period='seconds')
        return instance

    def __repr__(self):
        return self.schedule.__repr__()
