from sqlalchemy import Column, Integer, String
from app.database import Base

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    create_time = Column(String(128))
    start_time = Column(String(128))
    exec_time = Column(String(128))

    def __repr__(self):
        return ''.format(self.id)