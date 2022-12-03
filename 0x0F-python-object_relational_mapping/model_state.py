#!/usr/bin/python3
"""using sqlalchemy to create tables from classes"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """class states which maps into table states"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
