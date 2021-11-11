#!/usr/bin/python3
"""Class Airbnb command's"""
import cmd
import sys


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
