#!/usr/bin/python3
"""module that serializes and deserializes json instances"""
import json
import os.path


class FileStorage:
    """
    class that is used to serialize
    and deserialize Base Model instances
    """
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets value of key in dictionary pair of instance"""
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """serialise object into json file"""
        with open(self.__file_path, 'w') as f:
            return json.dump(self.__objects, f)

    def reload(self):
        """deserialises json file into object"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                try:
                    objs = json.load(f)
                except json.decoder.JSONDecodeError:
                    return
                for key, value in objs.items():
                    cls_name, obj_id = key.split(".")
                    cls = eval(cls_name)
                    obj = cls(**value)
                    self.__objects[key] = obj
