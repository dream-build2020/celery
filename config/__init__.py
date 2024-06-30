from celery import Celery

celery_app = Celery('task')  # 创建 Celery 实例
celery_app.config_from_object('config.celery_config')  # 通过 Celery 实例加载配置模块
