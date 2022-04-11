#!/usr/bin/python3
""" State Module for HBNB project """
from os import stat_result
from tokenize import String

from sqlalchemy import Column
from models.base_model import BaseModel
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """
    name = ""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan")
    
