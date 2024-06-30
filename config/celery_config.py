from celery import Celery
from celery.schedules import crontab

celery_app = Celery(
    broker='redis://192.168.31.101:6379/0',
    backend='redis://192.168.31.101:6379/1',
    include=[
        'tasks.tasks.tasks1'
    ]
)

celery_app.conf.timezone = 'Asia/Shanghai'

celery_app.conf.enable_utc = False

celery_app.conf.beat_schedule = {
    'add-every-1-minute': {
        'task': 'tasks.tasks.task1',
        'schedule': crontab(minute="*/1"),
        'arg': (1, 2)
    }
}
