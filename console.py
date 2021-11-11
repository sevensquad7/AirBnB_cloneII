#!/usr/bin/python3

import cmd
import sys


class ComandAirbnb(cmd.Cmd):
  """"started console Airbnb"""
  prompt = '(Hbnb)'
  file = None

  def do_quit(self, line):
        """Exit the Program - comand quit"""
        print('Thank you for using Airbnb console')
        return True
  
if __name__ == '__main__' :
  ComandAirbnb().cmdloop()
