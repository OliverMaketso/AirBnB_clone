#!usr/bin/python3
"""
class state that inherits from BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Defining the State class that inherits from BaseModel
    Public class attributes:
        name - string -  empty string
    """
    name = ""


