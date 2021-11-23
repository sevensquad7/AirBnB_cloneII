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

classGpo = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
            "Place": Place, "Review": Review, "State": State, "User": User}


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
    
    def _key_value_parser(self, args):
        """creates a dictionary from a list of strings"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except:
                        try:
                            value = float(value)
                        except:
                            continue
                new_dict[key] = value
        return new_dict

    def do_create(self, arg):
        """reacion de nuevas instancias de la clase"""
        args = arg.split()
        if len(args) == 0:
            print("**Nombre de la clase perdido")
            return False

        if args[0] in classes:
            new_dict = self._key_value_parser(args[1:])
            instance = classes[args[0]](**new_dict)
        else:
            print("**La clase no existe")
            return False
        print(instance.id)
        instance.save()

        print(instance.id)
        instance.save()

    def do_show(self, arg):
        """Imprimir las instacias en base cadennna en la clase y ID"""
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
            
    def do_destroy(self, arg):
        """Deletes an instance based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** instancia no funciona**")
            else:
                print("** se perdio la instancia **")
        else:
            print("** clase no existe **")
            
    def do_all(self, arg):
        """Prints string representations of instances"""
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            obj_dict = models.storage.all()
        elif args[0] in classes:
            obj_dict = models.storage.all(classes[args[0]])
        else:
            print("** class doesn't exist **")
            return False
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
        print("[", end="")
        print(", ".join(obj_list), end="")
        print("]")
        
    def do_update(self, arg):
        """Actualización del nombre de la clase id, atributos & valores"""
        args = shlex.split(arg)
        integers = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]
        floats = ["latitude", "longitude"]
        if len(args) == 0:
            print("** clase perdida **")
        elif args[0] in classes:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Place":
                                if args[2] in integers:
                                    try:
                                        args[3] = int(args[3])
                                    except:
                                        args[3] = 0
                                elif args[2] in floats:
                                    try:
                                        args[3] = float(args[3])
                                    except:
                                        args[3] = 0.0
                            setattr(models.storage.all()[k], args[2], args[3])
                            models.storage.all()[k].save()
                        else:
                            print("** valor perdido **")
                    else:
                        print("** nombre de atributo perdido **")
                else:
                    print("** instancia no funciona **")
            else:
                print("** instancia perdida **")
        else:
            print("** clase no existe **")
            
def help_quit(self, line):
    print("""Quit the Program - command quit""")


def help_EOF(self, line):
    print("""Exit the Program - command End of File""")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
