from config import celery_app


class Tasks:
    @staticmethod
    @celery_app.tasks
    def task1(a, b):
        restart = a + b
        return restart
