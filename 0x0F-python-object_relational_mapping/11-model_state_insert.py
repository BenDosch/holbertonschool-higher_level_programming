#!/usr/bin/python3
""" Script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa. Takes 3 arguments:
mysql username, mysql password and database name.
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    Louisiana = State(name='Louisiana')
    session.add(Louisiana)
    session.commit()
    state = session.query(State).\
        order_by(State.id.asc()).\
        filter(State.name == 'Louisiana').first()
    print(state.id)
    session.close
