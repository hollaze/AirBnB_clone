#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
import sys
import models
import models.engine


class HBNBCommand(cmd.Cmd):
    class_list = ['BaseModel', 'User']
    prompt = "(hbnb) "
    
    
    def __do_prompt(self, prompt):
        """Change the interactive prompt:
        (hbnb) """
        self.prompt = prompt
    
    def do_EOF(self, arg):
        """Exit the console:
        input: Ctrl+D"""
        print()
        return True

    def do_quit(self, arg):
        """Quit the console:
        write "quit" """
        return True

    def do_create(self, args):
        """ Create a new instance and saves
            it to a JSON file
        """
        if len(args) == 0:
            print('** class name missing **')
        elif args not in self.class_list:
            print("** class doesn't exist **")
        else:
            new_inst = eval(args)()
            new_inst.save()
            print(new_inst.id)
                      
    def do_show(self, args):
        """
            Prints the string representation of an instance
            based on a class name 
        """
        args_list = args.split()
        objs_dict = models.storage.all()
        if len(args_list) == 0:
            print('** class name missing **')
        elif args_list[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(args_list) == 1:
            print('** instance id missing **')
        elif "{}.{}".format(args_list[0], args_list[1]) in objs_dict.keys():
            print(objs_dict["{}.{}".format(args_list[0], args_list[1])])
        else:
            print('** no instance found **')

if __name__ == '__main__':
    HBNBCommand().cmdloop()
