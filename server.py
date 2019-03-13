from bottle import route, run, view, static_file
import os
cwd = os.getcwd() + os.sep + 'views' + os.sep + 'index.tpl'
cwd_st =  os.getcwd() + os.sep + 'static' + os.sep + "<filename:path>"
class TodoItem:
    def __init__(self, description):
        self.description = description
        self.is_completed = False
    def __str__(self):
        return self.description
   
@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static')

@route ("/")
@view(cwd)
def index():
    tasks = [
        TodoItem("прочитать книгу"),
        TodoItem("учится жонглировать"),
        TodoItem("помыть посуду"),
        TodoItem("поесть"),
        ]
    return {"tasks": tasks}


if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host="localhost", port=8080, debug=True)
