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
            self.__dict__ = kwargs
            if "created_at" in kwargs:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            if "updated_at" in kwargs:
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
        new_dict["created_at"] = new_dict["created_at"].strftime(time)
        new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
