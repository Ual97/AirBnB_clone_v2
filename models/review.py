#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, ForeignKey, String
from models.base_model import Base, BaseModel
from sqlalchemy.orm import relationship

class Review(BaseModel):
    """ Review classto store review information """
    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey('places.id', nullable=False))
    user_id = Column(String(60), ForeignKey('users.id', nullable=False))
    text = Column(String(1024), nullable=False)
