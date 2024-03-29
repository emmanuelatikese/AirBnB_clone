#!/usr/bin/python3
from datetime import datetime as dt
from uuid import uuid4 as u

"""this file contains a class models to work with"""


class BaseModel:
    """This class containes a list of attributes"""

    def __init__(self, *args, **kwargs):
        dt_fmt = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at":
                    self.created_at = dt.strptime(v, dt_fmt)
                elif k == "updated_at":
                    self.updated_at = dt.strptime(v, dt_fmt)
                elif k == "__class__":
                    pass
                else:
                    setattr(self, k, v)
        else:
            from models import storage
            self.id = str(u())
            self.created_at = dt.utcnow()
            self.updated_at = dt.utcnow()
            storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        self.updated_at = dt.utcnow()
        from models import storage
        storage.save()

    def to_dict(self):
        new_dict = {}
        for keys, values in self.__dict__.items():
            if keys in ["created_at", "updated_at"]:
                new_dict[keys] = values.isoformat()
            else:
                new_dict[keys] = values
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
