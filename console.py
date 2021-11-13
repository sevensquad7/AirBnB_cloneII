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

class ComandAirbnb(cmd.Cmd):
	""""Class Airbnb (Hbnb)"""
	prompt = '(Hbnb)'
	file = None

	def do_quit(self, line):
		"""Exit the Program - command quit"""
		print('Thank you for using Airbnb console')
		return True
	def do_EOF(self, line):
		"""Exit the Program - command End of File"""
		print('Thank you for using Airbnb console')
		return True
	

if __name__ == '__main__' :
	ComandAirbnb().cmdloop()
