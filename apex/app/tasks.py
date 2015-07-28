from celery import Task


class AddTheThings(Task):
    def run(self, *args):
        return sum(*args)
