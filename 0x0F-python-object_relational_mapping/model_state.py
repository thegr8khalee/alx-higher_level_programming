#!/usr/bin/python3
"""contains the class definition of a State and an instance Base = declarative_base()"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymd = MetaData()
Base = declarative_base(metadata=mymd)


class State(Base):
    """inherits from Base"""

    __tablename__ = "states"
    id = id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
