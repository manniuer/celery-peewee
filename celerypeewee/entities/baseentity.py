from peewee import Model, MySQLDatabase

# TODO: add right mysql configuration.
mysql_db = MySQLDatabase("my_database")


class BaseEntity(Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = mysql_db
        legacy_table_names = False
