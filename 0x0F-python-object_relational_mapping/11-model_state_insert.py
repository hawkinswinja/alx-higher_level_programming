#!/usr/bin/python3
"""SQLAlchemy queries to list all data in table"""


if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import State, Base
    new = State(name = 'Louisiana')
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    session = Session(engine)
    session.add(new)
    session.commit()
    print(new.id)
    session.close()
