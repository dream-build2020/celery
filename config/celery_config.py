from celery import Celery

celery_app = Celery(
    broker='redis://192.168.31.101:6379/0',
    backend='redis://192.168.31.101:6379/1',
    include=[
        'tasks.tasks.tasks1'
    ]
)

celery_app.conf.timezone = 'Asia/Shanghai'

celery_app.conf.enable_utc = False
