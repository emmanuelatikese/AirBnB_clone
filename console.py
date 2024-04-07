#!/usr/bin/python3
"""This is all console"""
import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    '''This is all about cmd'''
    prompt = '(hbnb) '

    def do_quit(self, *arg):
        '''This quits the command line'''
        return True

    def do_EOF(self, *arg):
        '''This ends everything'''
        return True

    def emptyline(self):
        ''' this literally does nothing'''
        pass

    def do_create(self, *arg):
        '''This create'''
        _str = "BaseModel"
        if arg and '' not in arg:
            print("** class doesn't exist **") if arg[0] != _str else\
                   print(BaseModel().id)
        else:
            print("** class name missing **")

    def do_show(self, *arg):
        '''This is show class'''
        _str = "BaseModel"
        arg = arg[0].split(" ")
        if arg and '' not in arg:
            print("** class doesn't exist **") if arg[0] != _str else\
                   ''
            if len(arg) == 1:
                print("** instance id missing **")
            else:
                from models import storage
                all_dict = storage.all()
                k = "BaseModel." + arg[1]
                print("** no instance found **") if not all_dict.get(k) else\
                    print(all_dict.get(k))

        else:
            print("** class name missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
