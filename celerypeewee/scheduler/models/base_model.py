from peewee import Model, MySQLDatabase
from playhouse.shortcuts import model_to_dict

# TODO: Put the db info to a configure file.
mysql_db = MySQLDatabase("test-celery-peewee",
                         user='root', password='peolinux',
                         host='192.168.101.115')


class BaseEntity(Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = mysql_db
        legacy_table_names = False

    def to_dict(self):
        return model_to_dict(self)
