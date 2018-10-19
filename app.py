import json
import datetime
import threading
import time
import queue
import subprocess
from flask_sqlalchemy import SQLAlchemy
from flask import Flask


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_time = db.Column(db.String(128))
    start_time = db.Column(db.String(128))
    exec_time = db.Column(db.String(128))
    def __repr__(self):
        return ''.format(self.id)

db.create_all()

from app.models import Task
q = queue.Queue()

# def update_task():

def add_to_queue(arg):
    q.put(arg)
    start_time = time.time()
    db.Query(Task).filter(id = arg).update(start_time)

def to_json(data):
    return json.dumps(data) + '\n'

@app.route('/task/<id>', methods=['GET'])
def get_task_info(id):
    q = db.Query(Task).all()
    print(q)
    return str(q)


@app.route('/', methods=['GET'])
def gen_tasks():
    create_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    for_json = {'create_time': create_time}
    t = Task(create_time= create_time)
    db.session.add(t)
    subprocess.run('test.py', shell=True)
    # start_time, time_to_execute = test.main()
    # for_json['start_time'] = start_time
    # for_json['time_to_execute'] = '{0} sec'.format(time_to_execute)
    db.session.commit()
    return str(t.id)


if __name__ == '__main__':
    app.run(host='192.168.0.10', port=8083, debug=True)
