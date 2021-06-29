#!/usr/bin/python3
"""
Console module
"""
import ast
import cmd
from models.base_model import BaseModel
from models.place import Place
from models.city import City
from models.user import User
from models.state import State
from models.review import Review
from models.amenity import Amenity
import models
import models.engine


class HBNBCommand(cmd.Cmd):
    """
    Command line interpreter
    
    Attributes:
    -----------
    class_list: list[str]
        A list of classes, to usefull for using commands
    prompt: str
        Prompt of the new console

    Methods:
    --------
    __do_prompt(prompt):
        Gives prompt of the new console
    emptyline():
        Do nothing upon receiving an empty line
    do_create(args):
        Create a new instance of a class, saves
        it to a JSON file and prints the id
    do_show(args):
        Prints the string representation of an instance
        based on a class name and id
    do_destroy(args):
        Deletes an instance based on the class name and id
        Saves the change into the JSON file
    do_all(args):
        Prints all string representation of all instances
    do_updates(args):
        Updates an instance based on the class name and id
        by adding or updating attribute, saves the change into
        the JSON file
    """
    
    class_list = ['BaseModel', 'User', 'State',
                  'City', 'Amenity', 'Place', 'Review']
    prompt = "(hbnb) "

    def __do_prompt(self, prompt):
        """
        Change the interactive prompt:
            (hbnb)
        """
        self.prompt = prompt

    def emptyline(self):
        """
        Do nothing upon receiving an empty line
        """
        pass

    def do_EOF(self, arg):
        """
        Exit the console

        Usage:
            EOF
        """
        print()
        return True

    def do_quit(self, arg):
        """
        Quit command to exit the console

        Usage:
            quit
        """
        return True
    def do_create(self, args):
        """
        Create a new instance of a class, saves
        it to a JSON file and prints the id

        Usage:
            create <class name>
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
        based on a class name and id

        Usage:
            show <class name> <id>
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

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        Saves the change into the JSON file

        Usage:
            destroy <class name> <id>
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
            del objs_dict["{}.{}".format(args_list[0], args_list[1])]
            models.storage.save()
        else:
            print('** no instance found **')

    def do_all(self, args):
        """
        Prints all string representation of all instances

        Usage:
            all
            all <classname>
        """
        args_list = args.split()
        obj_list = []
        if args not in self.class_list and len(args_list) > 0:
            print("** class doesn't exist **")
        else:
            all_objs = models.storage.all()
            for key in all_objs.keys():
                key_name_id = key.split('.')
                if key_name_id[0] in self.class_list:
                    obj_list.append(str(all_objs[key]))
                elif len(args_list) == 0:
                    obj_list.append(str(all_objs[key]))
            print(obj_list)

    def do_update(self, args):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute, saves the change into
        the JSON file

        Usage:
            update <class name> <id> <attributate name> <"attribute value">
        """
        args_list = args.split()
        objs_dict = models.storage.all()
        if len(args_list) == 0:
            print('** class name missing **')
        elif args_list[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(args_list) == 1:
            print('** instance id missing **')
        elif "{}.{}".format(args_list[0],
                            args_list[1]) not in objs_dict.keys():
            print('** no instance found **')
        elif len(args_list) == 2:
            print('** attribute name missing **')
        elif len(args_list) == 3:
            print('** value missing **')
        else:
            key = args_list[0] + '.' + args_list[1]
            u = objs_dict[key]
            u.__dict__[args_list[2]] = eval(args_list[3])
            u.save()

   # def do_count(self, arg):
    #    """
     #   """

    #def default(self, line):
     #   """
      #  Change the default behavior to <class>.cmds()
       # """



if __name__ == '__main__':
    HBNBCommand().cmdloop()
