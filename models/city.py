#!/usr/bin/python3
""" City Module for HBNB project """
from tokenize import String
from sqlalchemy import Column, ForeignKey
from models.base_model import Base, BaseModel
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(ForeignKey('states.id'), String(60), nullable=False)
    state = relationship("State")