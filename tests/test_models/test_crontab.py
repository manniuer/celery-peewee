import pytest
from celerypeewee.scheduler.models import Crontab
from celery import schedules


class TestCrontab(object):
    def test_create_new_crontab_with_all_parameters(self):
        cron = Crontab.create(minute=12, hour=1, day_of_week=1, day_of_month=1, month_of_year=1)
        assert cron is not None

    def test_create_new_crontab_with_no_parameters(self):
        cron = Crontab.create()
        assert cron is not None

    def test_create_new_crontab_with_invalid_parameters(self):
        # TODO: minute=99???
        with pytest.raises(ValueError):
            cron = Crontab(minute=99)
            s = cron.schedule

    def test_check_schedule_attr_type(self):
        cron = Crontab(hour=1, minute=12)
        assert type(cron.schedule) == schedules.crontab

    def test_crontab_schedule_to_dict(self):
        cron = Crontab(minute=12, hour=1, day_of_week=1, day_of_month=1, month_of_year=1)
        schedule = cron.schedule
        schedule_dict = Crontab.schedule_to_dict(schedule)
        assert isinstance(schedule_dict, dict)

    def test_crontab_to_dict(self):
        cron = Crontab(minute=12, hour=1, day_of_week=1, day_of_month=1, month_of_year=1)
        cron_dict = cron.to_dict()
        assert isinstance(cron_dict, dict)

    def test_get_crontab_from_schedule(self):
        schedule = schedules.crontab(minute=12, hour=1, day_of_week=3, day_of_month=11, month_of_year=11)
        cron = Crontab.from_schedule(schedule)
        assert isinstance(cron, Crontab)

    # TODO: Add UT for Crontab.task scenarios
