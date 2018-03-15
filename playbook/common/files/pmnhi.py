from bottle import route, run, template, default_app
from tasks import add 

@route('/add/<one:int>/<two:int>')
def index(one, two):
        task_id = add.delay(one, two)        
        return template('<b>Your task ID is:  {{task_id}}</b>!', task_id=task_id)

app = default_app()

