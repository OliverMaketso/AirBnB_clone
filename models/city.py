#!usr/bin/python3
"""
class city that inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Defining class city that inherits from Basemodel
    Public instane Attributes:
        state_id: string - empty string: it will be the State.id
        name: string - empty string
    """
    state_id = ""
    name = ""
