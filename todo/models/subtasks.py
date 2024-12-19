from backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime, Time
from sqlalchemy.orm import relationship
from datetime import datetime
from models.tasks import Task

class Subtask(Base):
    __tablename__ = "subtasks"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    # due_date = Column(DateTime)
    # lead_time = Column(Time)
    # check_mark = Column(Boolean, default=False)
    task_id = Column(Integer, ForeignKey('tasks.id'))
    slug = Column(String, unique=True, index=True)
    task = relationship('Task', back_populates='subtasks')

# from sqlalchemy.schema import CreateTable
# print(CreateTable(Subtask.__table__))