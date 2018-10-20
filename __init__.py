from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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

def create_app():
    app

if __name__ == '__main__':
    app.run(host='192.168.0.10', port=8083, debug=True)