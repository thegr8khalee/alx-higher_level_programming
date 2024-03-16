#!/usr/bin/python3
"""
_summary_
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    keys = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()
    for key in keys:
        print(key.id, key.name, sep=": ")
