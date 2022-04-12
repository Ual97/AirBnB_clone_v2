#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, ForeignKey, String
from models.base_model import Base, BaseModel
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.state import State

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    
    if (getenv("HBNB_TYPE_STORAGE") == "db"):
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        state = relationship("State")
    else:
        state_id = ""
        name = ""