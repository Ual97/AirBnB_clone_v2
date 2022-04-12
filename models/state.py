#!/usr/bin/python3
""" State Module for HBNB project """
from os import stat_result, getenv

from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship



class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states", cascade="all, delete, delete-orphan")
    
    @property
    def cities(self):
        """"""
        aux = []
        for city in models.storage.all("City").values():
            if (city.state_id == self.id):
                aux.append(city)
        return (aux)
