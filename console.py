#!/usr/bin/python3

import cmd
import models
import datetime

  class comandosAirbnb (cmd.Cmd):
        prompt = '(HNBN)'
        
        def do_EOF(self, arg): 
            """salir de la consola"""
            return True
        