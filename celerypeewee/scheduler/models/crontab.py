from .base_model import BaseEntity
from peewee import CharField
from celery import schedules


class Crontab(BaseEntity):
    month_of_year = CharField(default="*")
    day_of_month = CharField(default="*")
    day_of_week = CharField(default="*")
    hour = CharField(default="*")
    minute = CharField(default="*")

    @property
    def schedule(self):
        return schedules.crontab(
            minute=self.minute,
            hour=self.hour,
            day_of_week=self.day_of_week,
            day_of_month=self.day_of_month,
            month_of_year=self.month_of_year
        )

    @classmethod
    def schedule_to_dict(cls, schedule: schedules.crontab):
        return dict(
            [
                (x, getattr(schedule, f"_orig_{x}"))
                for x in ('minute', 'hour', 'day_of_week', 'day_of_month', 'month_of_year')
            ]
        )

    @classmethod
    def from_schedule(cls, schedule: schedules.crontab):
        data = cls.schedule_to_dict(schedule)
        instance, created = cls.get_or_create(**data)
        return instance

    def __repr__(self):
        return self.schedule.__repr__()
