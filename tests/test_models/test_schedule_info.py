from celerypeewee.scheduler.models.schedule_info import ScheduleInfo
from datetime import datetime


class TestScheduleInfo(object):
    def test_create_default_schedule_info(self):
        schedule_info = ScheduleInfo.create()
        assert isinstance(schedule_info, ScheduleInfo)

    def test_get_last_changed_at(self):
        last_changed_at = ScheduleInfo.get_last_change_at()
        print(last_changed_at)
        assert isinstance(last_changed_at, datetime)
