#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create an engine to interact with the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query the database for the first State object
    first_state = session.query(State).order_by(State.id).first()

    # If no states are found, print "Nothing"
    if first_state is None:
        print("Nothing")
    else:
        # Print the result
        print("{}: {}".format(first_state.id, first_state.name))

    # Close the session
    session.close()

