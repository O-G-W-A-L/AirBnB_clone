#!/usr/bin/python3
"""Contains the FileStorage class"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime

class FileStorage:
    """serializes instances to a JSON file & deserializes back to instances"""
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        obj_name = obj.__class__.__name__
        key = "{}.{}".format(obj_name, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        all_objs = FileStorage.__objects
        obj_dict = {}
        all_objs = FileStorage.__objects
        obj_dict = {}
        for obj_key, obj in all_objs.items():
            obj_dict[obj_key] = obj.to_dict()
            for key, value in obj_dict[obj_key].items():
                if isinstance(value, datetime):
                    obj_dict[obj_key][key] = value.isoformat()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)
            
    def reload(self):
        """Reloads the stored objects"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r",encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)
                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')
                        cls = eval(class_name)
                        instance = cls(**value)
                        FileStorage.__objects[key] = instance
                except Exception:
                    pass
