import pytest
import operator
from celerypeewee.scheduler.models import *
from peewee import InternalError, IntegrityError
from celery import schedules


class TestScheduleTask(object):
    def test_delete_all(self):
        assert ScheduleTask.delete().execute()

    def test_create_new_one_with_no_params(self):
        with pytest.raises(InternalError):
            ScheduleTask.create()

    def test_create_new_one_with_task_name(self):
        task = ScheduleTask.create(name="Test_Task", task="abc.abc", enabled=False)
        assert isinstance(task, ScheduleTask)

    def test_create_tasks_with_duplicated_name(self):
        with pytest.raises(IntegrityError):
            ScheduleTask.create(name="Task1", task="a.a")
            ScheduleTask.create(name="Task1", task="a.a")

    def test_create_task_with_crontab(self):
        cron = Crontab.create()
        task = ScheduleTask.create(name="test_create_task_with_crontab",
                                   task="a.a",
                                   crontab=cron)
        assert isinstance(task, ScheduleTask)

    def test_create_task_with_interval(self):
        itval = Interval.create(every=10, period="seconds")
        task = ScheduleTask.create(name="test_create_task_with_interval",
                                   task="a.a",
                                   interval=itval)
        assert isinstance(task, ScheduleTask)

    def test_get_args_attr(self):
        task = ScheduleTask.create(name="test_args_attr", task="a.a")
        args = task.args
        assert isinstance(args, list)

    def test_set_args_attr(self):
        org_args = [1, 2, 3]
        task = ScheduleTask(name="test_set_args_attr", task="a.a")
        task.args = org_args
        task.save()

        retrieved_task = ScheduleTask.get(task.id)
        assert operator.eq(org_args, retrieved_task.args)

    def test_get_kwargs_attr(self):
        task = ScheduleTask.create(name="test_get_kwargs_attr", task="a.a")
        args = task.kwargs
        assert isinstance(args, dict)

    def test_set_kwargs_attr(self):
        org_kwargs = {"a": "b", "b": "b"}
        task = ScheduleTask(name="test_set_kwargs_attr", task="a.a")
        task.kwargs = org_kwargs
        task.save()

        retrieved_task = ScheduleTask.get(task.id)
        assert operator.eq(org_kwargs, retrieved_task.kwargs)

    def test_get_crontab_schedule(self):
        cron = Crontab.create()
        task = ScheduleTask.create(name="test_get_crontab_schedule",
                                   task="a.a",
                                   crontab=cron)
        assert isinstance(task.schedule, schedules.crontab)

    def test_get_interval_schedule(self):
        interval = Interval.create(every=18, period="seconds")
        task = ScheduleTask.create(name="test_get_interval_schedule",
                                   task="a.a",
                                   interval=interval)
        assert isinstance(task.schedule, schedules.schedule)

    def test_get_available_tasks(self):
        tasks = ScheduleTask.get_available_tasks()
        assert all([x.enabled is True for x in tasks])

