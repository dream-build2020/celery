from config import loggin_config
from tasks.tasks import Tasks

LOGGER = loggin_config.LOGGER

if __name__ == "__main__":
    Tasks.task1.apply_async(kwargs={'a': 1, 'b': 2})
    pass
