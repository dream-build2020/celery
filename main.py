from tasks import tasks

if __name__ == "__main__":
    tasks.task1.apply_async(kwargs={'a': 1, 'b': 2})
    pass
