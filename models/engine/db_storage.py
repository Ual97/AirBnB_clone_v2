#!/usr/bin/python3
""" DBStorage for HBNB """


from tokenize import String
from sqlalchemy import Column, ForeignKey
from models.base_model import Base, BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import (create_engine)
from os import getenv
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }

class DBStorage:
    """Engine for MySQL databse"""
    __engine = None
    __session = None

    def __init__(self):
        """init for DBStorage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'), getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')), pool_pre_ping=True)
        """if (environ['HBNB_ENV'] == "test"):
            Base.metadata.drop_all(self.__engine)"""

    def all(self, cls=None):
        """"""
        aux = {}
        if (cls is not None):
            objects = self.__session.query(classes[cls]).all()
            for i in objects:
                dic = '{}.{}'.format(i.__class__.__name__, i.id)
                aux[dic] = i
            return (aux)
        else:
            for dic, value in classes.items():
                if dic != "BaseModel":
                    objs = []
                    try:
                        objs = self.__session.query(value).all()
                    except Exception:
                        pass
                    if len(objs) > 0:
                        for i in objs:
                            dic = "{}.{}".format(i.__class__.__name__, i.id)
                            aux[dic] = i
            return (aux)


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
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.state import State
        from models.user import User
        from models.review import Review
        from models.base_model import BaseModel
        self.__session = Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
