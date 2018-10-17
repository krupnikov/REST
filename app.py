import json
import datetime
import subprocess
import test
from flask import Flask



app = Flask(__name__)

def to_json(data):
    return json.dumps(data) + '\n'

@app.route('/')
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    create_time = datetime.datetime.now().isoformat()
    for_json = {'start_time': create_time}
    print(str(for_json))
    time_to_execute = test.main()
    for_json['time_to_execute'] = time_to_execute
    print(for_json)
    return str(for_json)


if __name__ == '__main__':
    app.run(host='localhost', port=4445)
