from celery import Celery

celery_app = Celery('tasks',
                    broker='redis://localhost:6379/0',
                    include=["tasks.tasks"]
                    )

