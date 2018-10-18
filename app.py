import json
import datetime
import subprocess
import test
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_time = db.Column(db.String(128))
    start_time = db.Column(db.String(128))
    exec_time = db.Column(db.String(128))
    def __repr__(self):
        return ''.format(self.id)

def to_json(data):
    return json.dumps(data) + '\n'

@app.route('/')
@app.route('/api/tasks', methods=['GET'])
def gen_tasks():
    create_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    for_json = {'create_time': create_time}
    t = Task(create_time= create_time)
    db.session.add(t)
    start_time, time_to_execute = test.main()
    for_json['start_time'] = start_time
    for_json['time_to_execute'] = '{0} sec'.format(time_to_execute)
    db.session.commit()
    return str(t.id)


if __name__ == '__main__':
    app.run(host='192.168.0.10', port=8083, debug=True)
