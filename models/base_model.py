#!/usr/bin/python3
from datetime import datetime as dt
from uuid import uuid4 as u

"""this file contains a class models to work with"""


class BaseModel:
    """This class containes a list of attributes"""

    def __init__(self, name='', my_number=None):
        self.id = str(u())
        self.my_number = my_number
        self.name = name
        self.created_at = dt.utcnow()
        self.updated_at = dt.utcnow()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        self.updated_at = dt.utcnow()

    def to_dict(self):
        new_dict = {}
        for keys, values in self.__dict__.items():
            if keys in ["created_at", "updated_at"]:
                new_dict[keys] = values.isoformat()
            else:
                new_dict[keys] = values
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
