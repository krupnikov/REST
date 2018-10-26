from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base
from datetime import datetime

# Class to describe ORM TASK in db

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    create_time = Column(DateTime, default=datetime.now())
    start_time = Column(DateTime)
    exec_time = Column(Integer)
    status = Column(String(10))

    def __init__(self, create_time=None, start_time=None, exec_time=None, status=None):
        self.create_time = create_time
        self.start_time = start_time
        self.exec_time = exec_time
        self.status = status

    def __repr__(self):
        return '{0}'.format(self.id)