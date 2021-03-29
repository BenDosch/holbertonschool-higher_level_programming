#!/usr/bin/python3
""" Script that c deletes all State objects with a name containing the
letter a from the database hbtn_0e_6_usa. Takes 3 arguments:
mysql username, mysql password and database name.
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State)
    del_states = query.filter(State.name.like('%a%'))
    for state in del_states:
        session.delete(state)
    session.commit()
    session.close
