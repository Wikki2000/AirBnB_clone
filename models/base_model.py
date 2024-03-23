#!/usr/bin/python3
"""This module models a base class of the AirBnb clone project"""
from datetime import datetime
from uuid import uuid4
from models import storage


class BaseModel:
    """This is the base class for the AIRBNB-Console project."""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance
        Args:
            id (str): Unique identifier of an object.
                    If not provided, a new UUID will be generated.
            created_at (str): Time when the instance is created in ISO format.
                    If not provided, current time will be used.
            updated_at (str): Time when the instance is last updated in
                    ISO format.If not provided, current time will be used.
        """
        if not kwargs:
            self.id = str(uuid4())
            self.updated_at = datetime.now()
            self.created_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)

    def __str__(self):
        """This method return a string representation of the object."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """This method update time were the instance of the object is save"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """This method returns dict containing all keys/values of __dict__"""
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__

        # Change the format of <created_at> & <updated_at> to iso str format
        my_dict['updated_at'] = my_dict['updated_at'].isoformat()
        my_dict['created_at'] = my_dict['created_at'].isoformat()
        return my_dict
