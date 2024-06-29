from config import celery_app


class Tasks:
    @staticmethod
    @celery_app.tasks
    def task1(a: int, b: int) -> int:
        restart = a + b
        return restart
