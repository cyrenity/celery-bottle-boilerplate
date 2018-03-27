from bottle import route, run, template, default_app
from tasks import add 

@route('/')
def root():
    welcome_msg = "<h3>App Framework is successfully installed </h3>"
    welcome_msg += '<p>Point your browser to <a href=\'/add/1/2\'>/add/1/2<a/> to execute your first task</p>'
    return welcome_msg

@route('/add/<one:int>/<two:int>')
def index(one, two):
        task_id = add.delay(one, two)        
        return template('<b>Your task ID is:  {{task_id}}</b>!, <p>Point your browser to <a href="/flower">/flower</a> to check task progress</p>', task_id=task_id)

app = default_app()

