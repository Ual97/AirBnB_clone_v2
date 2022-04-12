#!/usr/bin/python3
""" DBStorage for HBNB """


from tokenize import String
from sqlalchemy import Column, ForeignKey
from models.base_model import Base, BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import (create_engine)
from os import environ

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


class DBStorage:
    """Engine for MySQL databse"""
    __engine = None
    __session = None

    def __init__(self):
        """init for DBStorage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            environ['HBNB_MYSQL_USER'], environ['HBNB_MYSQL_PWD'], environ['HBNB_MYSQL_HOST'],
            environ['HBNB_MYSQL_DB']), pool_pre_ping=True)
        if (environ['HBNB_ENV'] == "test"):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """"""
        aux = {}
        if (cls is not None):
            objects = self.__session.query(cls).all()
            for i in objects:
                key = '{}.{}'.format(i.__class__.__name__, i.id)
                aux[key] = i
            return (aux)
        else:
            self.__session.query(
                User, State, City, Amenity, Place, Review).all()

    def new(self, obj):
        """add object to current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes on currenty databse session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes obj from current database session"""
        if (obj is not None):
            self.__session.delete(obj)

    def reload(self):
        """creates all tables in the database,
        and creates the current database session"""
        from models import Amenity, City, Place, State, User, Review
        self.__session = Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
