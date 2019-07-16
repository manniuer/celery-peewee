import pytest
from celerypeewee.scheduler.models import ScheduleMeta, ScheduleTask
from peewee import InternalError


class TestScheduleMeta(object):
    def test_create_meta_without_params(self):
        with pytest.raises(InternalError):
            ScheduleMeta.create()

    def test_create_meta_with_schedule_task_id(self):
        task, created = ScheduleTask.get_or_create(name="test_create_meta_with_schedule_task_id", task="abc.abc",
                                                   enabled=False)
        meta, created = ScheduleMeta.get_or_create(schedule_task_id=task.id)
        assert isinstance(meta, ScheduleMeta)

    def test_get_meta_by_task_id(self):
        task, created = ScheduleTask.get_or_create(name="test_get_meta_by_task_id", task="abc.abc", enabled=False)
        meta, created = ScheduleMeta.get_or_create(schedule_task_id=task.id)

        task_metas = [meta for meta in task.meta]
        for _meta in task_metas:
            assert _meta.id == meta.id
