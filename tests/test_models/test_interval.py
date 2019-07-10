import pytest
from celery import schedules
from datetime import timedelta
from celerypeewee.scheduler.models import Interval


class TestInterval(object):
    def test_create_new_interval_with_all_parameters(self):
        interval = Interval.create(every=10, period="seconds")
        assert isinstance(interval, Interval)

    def test_create_new_interval_with_no_parameters(self):
        interval = Interval.create()
        assert isinstance(interval, Interval)

    def test_create_new_interval_with_invalid_parameters(self):
        with pytest.raises(TypeError):
            interval = Interval(period='abc')
            s = interval.schedule

    def test_get_interval_from_schedule(self):
        schedule = schedules.schedule(timedelta(**{"seconds": 10}))
        interval = Interval.from_schedule(schedule)
        assert isinstance(interval, Interval)
