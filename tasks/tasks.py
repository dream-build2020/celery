from config import celery_app


@celery_app.task
def task1(a, b):
    restart = a + b
    return restart
