#!/usr/bin/python3
"""
Class Airbnb command's
"""
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

classGpo = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City, "Place": Place, "Review": Review, "State": State, "User": User}

class HBNBCommand(cmd.Cmd):
	""""
	Class Airbnb (Hbnb)
	"""
	prompt = '(Hbnb)'
	file = None

	def do_quit(self, line):
		"""Quit the Program - command quit"""
		return True
	def do_EOF(self, line):
		"""Exit the Program - command End of File"""
		return True
	def emptyline(self):
		return False
	def do_create(self, arg):
     	#reacion de nuevas instancias de la clase
     	args = arg.split()
     	if len(args) == 0:
         	print("**Nombre de la clase perdido")
         	return False
     	if args[0] in classes:
         	instance = eval(args[0])()
    	else:
        	print("**La clase no existe")
        	return False
    	print(instance.id)
    		instance.save()
     def do_show(self,arg):
#Imprimir las instacias en base cadennna en la clase y ID
		args = arg.split()
		if len(args) == 0:
			print("** nombre de la clase perdido")
			return False
		if args[0] in classes:
			if len(args) > 1:
				key = arg[0] + "." + args[1]
				if key in models.storage.all():
					print(models.storage.all()[key])
				else:
					print("** No funciona la instancia**")
			else:
				print("** Instancia perdida **")
		else:
			print("** Clase no existe**")
    
def help_quit(self, line):
		print("""Quit the Program - command quit""")
		
	def help_EOF(self, line):
		print("""Exit the Program - command End of File""")
if __name__ == '__main__' :
	HBNBCommand().cmdloop()
