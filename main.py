from config import loggin_config
from tasks import tasks

LOGGER = loggin_config.LOGGER

if __name__ == "__main__":
    tasks.task1.apply_async(kwargs={'a': 1, 'b': 2})
    pass
