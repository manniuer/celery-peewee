from datetime import datetime
from celery import current_app as celery_app
from celery import schedules
from celery.beat import ScheduleEntry, Scheduler
from .models import Crontab, Interval, ScheduleTask, ScheduleMeta, ScheduleInfo


DEFAULT_MAX_INTERVAL = 5


class ModelEntry(ScheduleEntry):
    module_schedules = (
        (schedules.crontab, Crontab, "crontab"),
        (schedules.schedule, Interval, "interval")
    )

    def __init__(self, model, app=None):
        super().__init__(
            name=model.name,
            task=model.task,
            last_run_at=model.schedule_meta.last_run_at,
            total_run_count=model.schedule_meta.total_run_count,
            schedule=model.schedule,
            args=model.args,
            kwargs=model.kwargs,
            options={
                "queue": model.queue,
                "exchange": model.exchange,
                "routing_key": model.routing_key,
                "expires": model.expires_at
            },
            app=app or celery_app._get_current_object()
        )

        self.model = model

    def __next__(self):
        meta = self.model.schedule_meta
        meta.last_run_at = self._default_now()
        meta.total_run_count += 1
        meta.save()

        return self.__class__(model=self.model, app=self.app)

    def is_due(self):
        if not self.model.enabled:
            return False, 5.0
        return super().is_due()

    @classmethod
    def from_orig_entry(cls, name, app=None, **entry):
        task, _ = ScheduleTask.get_or_create(name=name)

        for k, v in cls._unpack_entry_fields(**entry).items():
            setattr(task, k, v)

        task.enabled = True
        task.save()

        return cls(model=task, app=app)

    @classmethod
    def to_model_schedule(cls, schedule):
        for schedule_type, model_type, model_field in cls.module_schedules:
            schedule = schedules.maybe_schedule(schedule)
            if isinstance(schedule, schedule_type):
                module_schedule = model_type.from_schedule(schedule)
                return module_schedule, model_field

        raise ValueError('Cannot convert schedule type {0!r} to model'.format(schedule))

    @classmethod
    def _unpack_entry_fields(cls, schedule, args=None, kwargs=None, relative=None, options=None, **entry):
        def _unpack_entry_options(queue=None, exchange=None, routing_key=None, **kwargs):
            return {
                'queue': queue,
                'exchange': exchange,
                'routing_key': routing_key
            }

        model_schedule, model_field = cls.to_model_schedule(schedule)
        entry.update(
            {
                model_field: model_schedule
            },
            args=args or [],
            kwargs=kwargs or {},
            **_unpack_entry_options(**options or {})
        )
        return entry


