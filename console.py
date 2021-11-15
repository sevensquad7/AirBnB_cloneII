#!/usr/bin/python3
"""Class Airbnb command's"""
import cmd
import sys

from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models

classGpo = {"Amenity": Amenity,
			"BaseModel": BaseModel,
			"City": City,
			"Place": Place,
			"Review": Review,
			"State": State,
			"User": User}

class HBNBCommand(cmd.Cmd):
	""""Class Airbnb (Hbnb)"""
	prompt = '(Hbnb)'
	file = None

	def do_quit(self, line):
		"""Quit the Program - command quit"""
		return True
	def do_EOF(self, line):
		"""Exit the Program - command End of File"""
		return True
	

if __name__ == '__main__' :
	HBNBCommand().cmdloop()
