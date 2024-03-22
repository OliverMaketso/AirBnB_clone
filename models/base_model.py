#!/usr/bin/python3
"""
BaseModel class that defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime
import models
import json
isoform_time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    BaseModel class represents the base model for other classes in the project.

    Attributes:
        id (str): A unique identifier assigned to each instance.
        created_at (datetime): The datetime when an instance is created.
        updated_at (datetime): The datetime when an instance is created or updated.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel

        Args:
            *args: Unused arguments.
            **kwargs: Keyword arguments containing attribute name and values for the instance.
        """
        if kwargs is None or len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, isoform_time)
                elif key == "__class__":
                    pass
                elif key !=  "__class__":
                    self.__dict__[key] = value

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        Returns:
            str: Astring containing class name, id, and instance attributes
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ Public instance methods:
            updates updated_at attribute
            with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Public instance methods
            returns a dictionary containing all keys/values
            of __dict__ of the instance with self.__dict__
            we are making a copy.
            This method will be the first piece of the
            serialization/deserialization process: create a dictionary
            representation with “simple object type” of our BaseModel
        """
        dic_BaseClass = self.__dict__.copy()
        dic_BaseClass["__class__"] = self.__class__.__name__
        dic_BaseClass["created_at"] = self.created_at.isoformat()
        dic_BaseClass["updated_at"] = self.updated_at.isoformat()
        return dic_BaseClass
