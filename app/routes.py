import json
import datetime
import time
import queue
import subprocess
from . import test

from app import app
from app.database import db_session
from app.models import Task

q = queue.Queue()

# def update_task():

def add_to_queue(arg):
    q.put(arg)
    start_time = time.time()


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
    for_json = {'create_time': create_time}
    t = Task(create_time=create_time)
    db_session.add(t)
    subprocess.run('test.py', shell=True)
    # start_time, time_to_execute = test.main()
    # for_json['start_time'] = start_time
    # for_json['time_to_execute'] = '{0} sec'.format(time_to_execute)
    db_session.commit()
    return str(t.id)


