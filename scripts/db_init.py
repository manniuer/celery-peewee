from celerypeewee.scheduler.models.base_model import mysql_db as database
from celerypeewee.scheduler.models import Crontab, Interval, ScheduleMeta, ScheduleTask, ScheduleInfo


def table_init():
    with database:
        database.create_tables(
            [
                Crontab,
                Interval,
                ScheduleInfo,
                ScheduleTask,
                ScheduleMeta
            ]
        )


if __name__ == '__main__':
    table_init()
