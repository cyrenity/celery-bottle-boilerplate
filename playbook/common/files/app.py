from bottle import route, run, template, default_app, request, response, _parse_qsl
from itertools import chain
from celery.task.control import  inspect
from json import dumps
import socket
import tasks

@route('/')
def root():
    ip_address = socket.gethostbyname(socket.gethostname())
    i = inspect()
    tasks = i.registered_tasks().values()
    set_of_tasks = set(chain.from_iterable( i.registered_tasks().values() ))

    list_of_tasks = '<ol>'
    for task in set_of_tasks: 
        list_of_tasks += '<li>%s</li>' % task
    list_of_tasks += '</ol>'
    

    welcome_msg =  "<HTML><HEAD><STYLE>p { font-size: 12px; }</STYLE></HEAD>"
    welcome_msg += "<h3>App Framework is successfully installed </h3>"
    welcome_msg += "<p><strong>List of registered tasks:</strong> %s </p>" % list_of_tasks
    welcome_msg += '<p>Point your brower to http://%s/<strong>task-runner/[task name]?arg1=value1&arg2=value2&arg3=value3</strong> to run a task/job</p>' % ip_address
    welcome_msg += '<p>Add output=pretty in args list to output human readable response</p>'
    welcome_msg += '<p>Add output=empty in args list to omit output and send an empty response to client</p>'
    welcome_msg += '<p>Add output=json (default) in args list to output a json response</p>'
    welcome_msg += '<p>Click here to publish your first task <a href=\'/task-runner/tasks.add?one=2&two=4&output=pretty\'>/task-runner/tasks.add?one=2&two=4&output=pretty<a/></p>' 

    return welcome_msg

@route('/task-runner/<task_name>')
def index(task_name):
        params_qs = request.query_string
        param_pairs = _parse_qsl(params_qs)
        final_params = {}

        for key, value in param_pairs:
            final_params[key] = value

        output = final_params.pop('output', 'json')
        my_task = tasks.app.signature(task_name)
        try:
            task_id = my_task.delay(final_params)
            if output == 'pretty':
                return template('<b>Your task ID is:  {{task_id}}</b><p>Point your browser to <a href="/flower/tasks">/flower</a> to check task progress</p>', task_id=task_id)
            elif output == 'empty':
                return
            elif output == 'json':
                response.content_type = 'application/json'
                return dumps({'task_id': str(task_id)})
        except TypeError as err:
            return template('<b>Task Error:  {{error}}</b> <p>Args: {{args}}</p>', error=err, args=request.query_string )

app = default_app()

