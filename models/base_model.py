#!/usr/bin/python3
"""
contains class base models
"""
import uuid
from datetime import datetime
import models

class BaseModel:
    """initialize base model instance"""
    def __init__(self, *args, **kwargs):
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "update_at":
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)

        models.storage.new(self)
        
    def save(self):
        """updates the attribute 'updated_at' with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns dict containing all values """
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__

        if isinstance(inst_dict["created_at"], datetime):
            inst_dict["created_at"] = inst_dict["created_at"].isoformat()
        if isinstance(inst_dict["updated_at"], datetime):
            inst_dict["updated_at"] = inst_dict["updated_at"].isoformat()

        return inst_dict

    def __str__(self):
        """returns the string representation of BaseModel instance"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
