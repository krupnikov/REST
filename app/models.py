class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_time = db.Column(db.String(128))
    start_time = db.Column(db.String(128))
    exec_time = db.Column(db.String(128))
    def __repr__(self):
        return ''.format(self.id)