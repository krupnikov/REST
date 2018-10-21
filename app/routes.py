import json
import datetime
import queue
import threading

from app import app
from app.database import db_session
from app.models import Task
from app.test import main

q = queue.Queue()
threads = []
num_worker_threads = 2

def worker():
    while True:
        item = q.get()
        if item is None:
            break
        do_work(item)
        q.task_done()

def do_work(arg):
    s = main()
    start_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    db_session.execute("UPDATE tasks SET start_time='{0}' WHERE id={1}".format(start_time, arg.id))
    db_session.commit()
    exec_time = s
    db_session.execute("UPDATE tasks SET exec_time='{0}' WHERE id={1}".format(exec_time, arg.id))
    db_session.commit()

def gen_workers():
    for i in range(num_worker_threads):
        t = threading.Thread(target=worker)
        t.start()
        threads.append(t)

def add_to_queue(arg):
    q.put(arg)

def to_json(data):
    l = data.split(sep=';')
    dic = {'status': 'In Queue', 'create_time': None, 'start_time': None, 'exec_time': None}
    dic['create_time'] = l[0]
    dic['start_time'] = l[1]
    dic['exec_time'] = l[2]
    if (dic['start_time'] != 'None') and (dic['exec_time'] == 'None'):
        dic['status'] = 'Run'
    elif (dic['start_time'] !='None') and (dic['exec_time'] != 'None'):
        dic['status'] = 'Completed'
    return json.dumps(dic, indent=4)

@app.route('/task/<int:id>', methods=['GET'])
def get_task_info(id):
    q = str(Task.query.filter(Task.id == id).first())
    return to_json(q)


@app.route('/', methods=['GET'])
def gen_tasks():
    create_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    t = Task(create_time=create_time)
    db_session.add(t)
    db_session.commit()
    add_to_queue(t)
    gen_workers()
    return str(t.id)