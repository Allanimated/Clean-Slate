from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, desc
from sqlalchemy import (CheckConstraint, UniqueConstraint,
                        Column, DateTime, Integer, String, ForeignKey)
from sqlalchemy.orm import relationship, backref


engine = create_engine('sqlite:///clean_slate.db')

Base = declarative_base()

# models


class Cleaner(Base):

    __tablename__ = 'cleaners'

    # Table columns
    cleaner_id = Column(Integer(), primary_key=True)
    full_name = Column(String(25))
    contact_number = Column(Integer())
    experience_level = Column(String())
    # Table relations
    cleaning_tasks = relationship('CleaningTask', backref='cleaner')

    def __repr__(self):
        return f"Cleaner {self.cleaner_id}: " \
            + f"{self.full_name}, " \
            + f"Experience Level {self.experience_level}"


class Client(Base):
    __tablename__ = "clients"
    __table_args__ = (
        UniqueConstraint('email', name='unique_email'),
    )
    client_id = Column(Integer(), primary_key=True)
    client_name = Column(String(25))
    email = Column(String())
    password = Column(String())
    contact_number = Column(Integer())

    # Table relations
    cleaning_tasks = relationship('ClientTask', back_populates='client')

    def __repr__(self):
        return f"Client {self.client_id}: " \
            + f"{self.client_name}"


class CleaningTask(Base):
    __tablename__ = 'cleaning_tasks'

    task_id = Column(Integer(), primary_key=True)
    task_description = Column(String())
    price = Column(Integer())
    cleaner_id = Column(Integer(), ForeignKey('cleaners.cleaner_id'))

    # Table relations
    clients = relationship('ClientTask', back_populates='task')

    def __repr__(self):
        return f"Task {self.task_id} " \
            + f"{self.task_description}, " \
            + f"Price {self.price}"


class ClientTask(Base):
    __tablename__ = 'client_tasks'
    # Table columns
    client_task_id = Column(Integer(), primary_key=True)
    client_id = Column(Integer(), ForeignKey('clients.client_id'))
    task_id = Column(Integer(), ForeignKey('cleaning_tasks.task_id'))

    client = relationship('Client', back_populates='cleaning_tasks')
    task = relationship('CleaningTask', back_populates='clients')

    def __repr__(self):
        return f'ClientTask(client_id={self.client_id}, ' + \
            f'task_id={self.task_id})'
