#!/usr/bin/python3
"""
Class FileStorage
"""


from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json

class FileStorage:
    """Serializar las instancias a json file y deserializar las instancias"""
    
#string - path to the JSON file

__file_path = "file.json"

#dictionary - empty but will store all objects by class name.id
__objects = {}

def all(self):
    """retornar el diccionario __objetos"""
    return self.__objects

def new(self):
    """En __objects el objeto con una llave obj class name.id"""
    key = obj.__class__.__name__ + "." + obj.id
    self.__objects[key] = obj

def save(self):
    """serializar __objects to the Json file path: __file_path"""
    json_objects = {}
    for key in self.__objects:
        json_objects[key] = self.__objects[key].to_dict()
    with open(self.__file_path, 'w') as f:
        json.dump(json_objects, f)
        
def reload(self):
    """deserializar el json file hacia __objects"""
    try:
        with open(self.___file_path, 'r') as f:
            json_objects = json.load(f)
        for key in json_objects:
            self-__objects[key] = BaseModel(**json_objects[key])
    except:
        pass
    
    