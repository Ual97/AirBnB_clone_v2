#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import environ
from base_model import BaseModel
from user import User
from place import Place
from state import State
from city import City
from amenity import Amenity
from review import Review

classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }

storage = None

if (environ['HBNB_TYPE_STORAGE'] == 'db'):
    from models.engine import db_storage
    storage = db_storage.DBStorage()
else:
    from models.engine import file_storage
    storage = file_storage.FileStorage()
storage.reload()
