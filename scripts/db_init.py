from celerypeewee.scheduler.models.base_model import mysql_db as database
from celerypeewee.scheduler.models import Crontab


def table_init():
    with database:
        database.create_tables(
            [
                Crontab
            ]
        )


if __name__ == '__main__':
    table_init()
