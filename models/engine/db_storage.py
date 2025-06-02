#!/usr/bin/python3
"""Defines the DBStorage engine."""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.city import City
from models.state import State
import os


class DBStorage:
    """Manages storage of models in a MySQL database."""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage."""
        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV")

        self.__engine = create_engine(
            f"mysql+mysqldb://{user}:{password}@{host}/{db}",
            pool_pre_ping=True
        )

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session."""
        objects = {}
        if cls:
            if isinstance(cls, str):
                cls = eval(cls)
            for obj in self.__session.query(cls).all():
                key = f"{obj.__class__.__name__}.{obj.id}"
                objects[key] = obj
        else:
            for cls_type in [State, City]:
                for obj in self.__session.query(cls_type).all():
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    objects[key] = obj
