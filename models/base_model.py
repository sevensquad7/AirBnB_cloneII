#!/usr/bin/python3
"""Class Base_Model"""
from datetime import datetime, time
import uuid
import models
time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """Date BaseModel"""
    def __init__(self, *args, **kwargs):
        """Iniciando la base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if hasattr(self.created_at) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            if hasattr(self.updated_at) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """clase de representacion del basemodel"""
        return"[{:s}] ({:s}) {}".format(self.__class__.__name__, self.__dict__)

    def save(self):
        """Actualizar los atributos con datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """return all content of the diccionary to keys and values"""
        new_dict = self-__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "update_at" in new_dict:
            new_dict["update_at"] = new_dict["update_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
