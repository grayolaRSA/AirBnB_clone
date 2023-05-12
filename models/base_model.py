#!/usr/bin/python3
""" module for base class for AirBnB clone"""
from datetime import datetime
import uuid

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    Base Model from which all other models inherit attributes from
    """

    def __init__(self, *args, **kwargs):
        """constructor for the Base Model"""
        from models.engine.file_storage import FileStorage
        storage = FileStorage()
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time)
                elif key != "__class__":
                    setattr(self, key, value)
            else:
                import models.__init__
                self.created_at = self.updated_at = datetime.now()
                storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
