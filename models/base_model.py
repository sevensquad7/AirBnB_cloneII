#!/usr/bin/python3
"""Class Base_Model"""
from datetime import datetime, time
import uuid

class BaseModel:
    """Date BaseModel"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
    def __str__(self):
        """clase de representacion del basemodel"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.__dict__)
    def save(self):
        """Actualizar los atributos con datetime"""
        self.updated_at = datetime.now()
    def to_dict(self):
        """devuelve todo el contenido del diccionario con las llabes y valores"""
        time = "%Y-%m-%dT%H:%S.%f"
        new_dict = self-__dict__.copy()
        new_dict["created_at"] = new_dict["created_at"].strftime(time)
        new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        return new_dict