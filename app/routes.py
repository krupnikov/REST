import json
import datetime
import time
import queue
import subprocess

from app import app
from app.database import db_session
from app.models import Task

q = queue.Queue()

# def update_task():

def add_to_queue(arg):
    q.put(arg)
    start_time = time.time()

def to_json(data):
    return json.dumps(data) + '\n'

@app.route('/task/<id>', methods=['GET'])
def get_task_info(id):
    # q = db.Query(Task).all()
    print(q)
    return str(q)


@app.route('/', methods=['GET'])
def gen_tasks():
    create_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    for_json = {'create_time': create_time}
    t = Task(create_time= create_time)
    db_session.add(t)
    subprocess.run('test.py', shell=True)
    # start_time, time_to_execute = test.main()
    # for_json['start_time'] = start_time
    # for_json['time_to_execute'] = '{0} sec'.format(time_to_execute)
    # db.session.commit()
    return str(t.id)


