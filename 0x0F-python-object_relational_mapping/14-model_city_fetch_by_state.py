#!/usr/bin/python3
"""querying ORM model relationships"""


if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    session = Session(engine)
    cities = session.query(City).join(State, City.state_id == State.id).order_by(City.id).all()
    for city in cities:
        print('{}: ({}) {}'.format(city.state.name, city.id, city.name))
    session.close()
