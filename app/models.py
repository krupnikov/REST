from sqlalchemy import Column, Integer, String
from app.database import Base

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    create_time = Column(String(128))
    start_time = Column(String(128))
    exec_time = Column(String(128))

    def __repr__(self):
        return "{0};{1};{2};{3}".format(self.id ,self.create_time, self.start_time, self.exec_time)