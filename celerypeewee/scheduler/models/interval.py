from .base_model import BaseEntity
from peewee import IntegerField, CharField


class Interval(BaseEntity):
    every = IntegerField(null=True)
    period = CharField(null=True)
