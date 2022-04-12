#!/usr/bin/python3
"""This module defines a class User"""
from ast import For
from email.policy import default
from sqlalchemy import Column, Float, Integer, String, ForeignKey
from models.base_model import Base, BaseModel
from sqlalchemy.orm import relationship
import models


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    reviews = relationship("Review", backref="user", cascade="all, delete, delete-orphan")

    @property
    def reviews(self):
        """getter for reviews"""
        aux = []
        import models
        for review in models.storage.all("Review").values():
            if (review.place_id == self.id):
                aux.append(review)
        return (aux)
