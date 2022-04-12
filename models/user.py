#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import Column, ForeignKey, String
from models.base_model import Base, BaseModel
from sqlalchemy.orm import relationship
from models import storage
from os import getenv
import models
from models.state import State


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
models.storagestorage.reload()