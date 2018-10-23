from sqlalchemy import Column, Integer, DateTime
from app.database import Base

# Class to describe ORM TASK in db

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    create_time = Column(DateTime)
    start_time = Column(DateTime)
    exec_time = Column(DateTime)

    def __init__(self, create_time):
        self.status = {'status': 'In Queue', 'create_time': None, 'start_time': None, 'exec_time': None}
        self.create_time = create_time

    def __repr__(self):
        return "{0};{1};{2};{3}".format(self.id, self.create_time, self.start_time, self.exec_time)