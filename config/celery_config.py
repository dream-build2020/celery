from celery.schedules import crontab

BROKER_URL = 'redis://192.168.31.101:6379/0'  # 指定 Broker
CELERY_RESULT_BACKEND = 'redis://192.168.31.101:6379/1'  # 指定 Backend

CELERY_TIMEZONE = 'Asia/Shanghai'  # 指定时区，默认是 UTC
# CELERY_TIMEZONE='UTC'

CELERY_ENABLE_UTC = False

CELERY_IMPORTS = (  # 指定导入的任务模块
    'tasks.tasks'
)

# 定时任务
CELERYBEAT_SCHEDULE = {
    'add-every-1-minute': {
        'task': 'tasks.tasks.task1',
        'schedule': crontab(minute="*/1"),
        'args': (1, 3)
    }
}
