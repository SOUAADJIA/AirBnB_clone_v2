#!/usr/bin/python3
"""Module Docs"""
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """Class Docs"""

    __engine = None
    __session = None

    def __init__(self):
        """Function Docs"""
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env_name = getenv("HBNB_ENV")

        self.__engine = create_engine(
                f"mysql+mysqldb://{user}:{pwd}@{host}/{db}",
                pool_pre_ping=True,
                )

        if env_name == "test":
            Base.metadata.drop_all(self.__engine)

    def reload(self):
        """ reload method """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False)
        )
        self.__session = Session

    def all(self, cls=None):
        """
        query all classes or specific one"""
        allClasses = [User, Place, State, City, Amenity, Review]
        result = {}
        if cls is not None:
            for obj in self.__session.query(cls).all():
                ClassName = obj.__class__.__name__
                keyName = ClassName + "." + obj.id
                result[keyName] = obj
        else:
            for clss in allClasses:
                for obj in self.__session.query(clss).all():
                    ClassName = obj.__class__.__name__
                    keyName = ClassName + "." + obj.id
                    result[keyName] = obj
        return result

    def new(self, obj):
        """add new obj"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit all changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def close(self):
        """
        Function docs
        """
        self.__session.remove()  # Or you can also use self.__session.close()
