#!/usr/bin/python3
""" DBStorage for HBNB """


from tokenize import String
from sqlalchemy import Column, ForeignKey
from models.base_model import Base, BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import (create_engine)
from os import environ
from models import Amenity, City, Place, State, User, Review


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
        if (cls is not None):
            self.__session.query(cls).all()
        else:
            self.__session.query(User, State, City, Amenity, Place, Review).all()
        ##falta retornar un dictionary con key(class.id : object)

