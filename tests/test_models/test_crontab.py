from celerypeewee.scheduler.models import Crontab


def test_create_new_crontab():
    cron = Crontab.create(hour=1, minute=12)
    assert cron is not None



# if __name__ == '__main__':
#     new_cron1 = Crontab.create(hour=1, minute=12)
#     schedule = new_cron1.schedule
#     schedule._orig_day_of_month = 12
#     new_cron2 = Crontab.from_schedule(schedule)
#     print(repr(new_cron2))
#     print(new_cron2.to_dict())
#
#     pass
