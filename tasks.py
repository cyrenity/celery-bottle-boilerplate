from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def add(params):
        try:
            x  = int(params['one'])
            y  = int(params['two'])
        except KeyError as err:
            raise Exception("missing param(s): %s" % err.message)

        return x + y
