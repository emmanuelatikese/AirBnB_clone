#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage

"""This is the console file for the python terminal"""

class HBNBCommand(cmd.Cmd):
    """This function start"""
    prompt = "(hbnb) "

    def do_quit(self, *args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, *args):
        """This does eof stuffs"""
        print("")
        return True

    def do_create(self, args):
        """This function create a models"""
        if args == "BaseModel":
            print(BaseModel().id)
        elif args == "":
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, *args):
        if not args[0] or args[0] == " ":
            print("** class name missing **")
        elif args[0][0:9] == "BaseModel":
            if len(args[0]) == len("BaseModel"):
                print("** instance id missing **")
            else:
                ob = storage.all()
                ans = ""
                for k, x in ob.items():
                    if x.id == args[0][10:]:
                        ans = x
                if not ans:
                    print("** no instance found **")
                else:
                    print(ans)
                        
        else:
            print("** class doesn't exist **")



    def do_all(self, args):
        """This output all models"""
        if args == "BaseModel":
            l, ob = [], storage.all()
            for k, v in ob.items():
                l.append('{}'.format(v))
            print(l)
        else:
            print("** class doesn't exit **")

    def do_destroy(self, *args):

        if not args[0] or args[0] == " ":
            print("** class name missing **")
        elif args[0][0:9] == "BaseModel":
            if len(args[0]) == len("BaseModel"):
                print("** instance id missing **")
            else:
                ob = storage.all()
                ans = ""
                for k, x in ob.items():
                    if x.id == args[0][10:]:
                        ans = x
                if not ans:
                    print("** no instance found **")
                else:
                    print(ob[k])
                    ob.pop(k)
                    storage.save()
        else:
            print("** class doesn't exist **")

    def do_update(self, *args):
        l = args[0].split(" ")
        print(l)
        if not l[0] or l[0] == " ":
            print("** class name missing **")
        elif l[0] == "BaseModel":
            if len(l) == 1:
                print("** instance id missing **")
            else:
                ob = storage.all()
                ans = None
                for k, x in ob.items():
                    if x.id == l[1]:
                        ans = x
                        print("found")
                if ans != None:
                    dic = {}
                    if l[3]:
                        if l[3] == "first_name" or l[3] == "email":
                            if l[4]:
                                dic[l[3]] = l[4]
                                ans(dic)
                                storage.save()
                            else:
                                print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
