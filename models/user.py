#!/usr/bin/python3
"""
class user that inherits from BaseModel
"""
from models.base_model import BaseModel

class User(BaseModel):
    """
    Defining the user class that inherits from BaseModel
    Public class attributes:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
