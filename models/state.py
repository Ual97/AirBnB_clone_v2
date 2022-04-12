#!/usr/bin/python3
""" State Module for HBNB project """
from os import stat_result, getenv
from tokenize import String

from sqlalchemy import Column
from models.base_model import BaseModel
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """
    if (getenv("HBNB_TYPE_STORAGE") == "db"):
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete, delete-orphan")
    else:
        name = ""
    
