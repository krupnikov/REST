import json
import datetime
import queue
import threading

from app import app
from app.database import db_session
from app.models import Task
from app.test import main

@app.teardown_appcontext
def shutdown_session(exception= None):
    db_session.remove()

q = queue.Queue()
threads = []
num_worker_threads = 2

# class Worker(threading.Thread):
#
#     def __init__(self, work_queue):
#

def worker():
    while True:
        item = q.get()
        do_work(item)
        q.task_done()

def do_work(arg):
    start_time = datetime.datetime.now()
    s = main()
    db_session.execute("UPDATE tasks SET start_time='{0}' WHERE id={1}".format(start_time, arg.id))
    db_session.commit()
    exec_time = int(s)
    db_session.execute("UPDATE tasks SET exec_time='{0}' WHERE id={1}".format(exec_time, arg.id))
    db_session.commit()

def gen_workers():
    for i in range(num_worker_threads):
        trd = threading.Thread(target=worker)
        trd.start()
        threads.append(trd)


@app.route('/task', methods=['PUT'])
def gen_tasks():
    t = Task(status='In Queue')
    q.put(t)
    db_session.add(t)
    db_session.commit()
    gen_workers()
    return str(t.id)

@app.route('/task/info/<int:id>', methods=['GET'])
def get_task_info(id):
    que = db_session.query(Task).filter(Task.id == id).first()
    out = {'status': que.status,
           'create_time': str(que.create_time),
           'start_time': str(que.start_time),
           'exec_time': str(que.exec_time)}
    return json.dumps(out, indent=4)