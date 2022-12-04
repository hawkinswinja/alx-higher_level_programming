#!/usr/bin/python3
"""SQLAlchemy queries to list all data in table"""


if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import State, Base
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    session.query(State).filter(State.name.contains('a')).delete(synchronize_session=False)
    session.commit()
    session.close()
