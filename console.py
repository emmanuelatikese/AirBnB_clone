#!/usr/bin/python3
"""This is all console"""
import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    '''This is all about cmd'''
    prompt = '(hbnb) '
    def do_quit(self, arg):
        '''This quits the command line'''
        return True
if __name__ == "__main__":
    HBNBCommand().cmdloop()
