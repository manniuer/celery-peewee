from .baseentity import BaseEntity
from peewee import *


class Crontab(BaseEntity):
    month_of_year = CharField(null=True)
    day_of_month = CharField(null=True)
    day_of_week = CharField(null=True)
    hour = CharField(null=True)
    minute = CharField(null=True)
