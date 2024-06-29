from datetime import timedelta
from celery.schedules import crontab

BROKER_URL = 'redis://192.168.31.101:6379'  # 指定 Broker
CELERY_RESULT_BACKEND = 'redis://192.168.31.101:6379/0'  # 指定 Backend

CELERY_TIMEZONE = 'Asia/Shanghai'  # 指定时区，默认是 UTC
# CELERY_TIMEZONE='UTC'

CELERY_IMPORTS = (  # 指定导入的任务模块
    'tasks.tasks',
)

CELERTBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task':  'tasks.tasks.task1',
        'schedule': crontab(minute=1),
        'kwargs': {'a': 1, 'b': 2}
    },
    'add-every-1-minute': {
        'task': 'tasks.tasks.task1',
        'schedule': crontab(minute=2),
        'args': [13, 2]
    }
}
