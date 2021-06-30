#!/usr/bin/python3
"""
Console module
"""
from models.base_model import BaseModel
from models.place import Place
from models.city import City
from models.user import User
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
import models
import cmd


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
            return
        else:
            all_objs = models.storage.all()
            for obj in all_objs.values():
                if len(args) > 0 and args_list[0] == obj.__class__.__name__:
                    obj_list.append(obj.__str__())
                elif len(args_list) == 0:
                    obj_list.append(obj.__str__())
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

    def do_User(self, args):
        """
        Usage:
                User.all() - displays all objects of class User
                User.count() - displays number of objects of class User
                User.show("id") - displays object of class User with id
                User.destroy("id") - deletes object of class User with id
        """
        self._execute('User', args)

    def do_BaseModel(self, args):
        """
        Usage:
                BaseModel.all() - displays all objects of class BaseMod
                BaseModel.count() - displays number of objects of class BaseMod
                BaseModel.show("id") - displays object of class BaseMod with id
                BaseModel.destroy("id") - deletes object of class BaseM with id
        """
        self._execute('BaseModel', args)

    def do_State(self, args):
        """
        Usage:
                State.all() - displays all objects of class State
                State.count() - displays number of objects of class State
                State.show("id") - displays object of class State with id
                State.destroy("id") - deletes object of class BaseModel with id
        """
        self._execute('State', args)

    def do_City(self, args):
        """
        Usage:
                City.all() - displays all objects of class City
                City.count() - displays number of objects of class City
                City.show("id") - displays object of class City with id
                City.destroy("id") - deletes object of class City with id
        """
        self._execute('City', args)

    def do_Amenity(self, args):
        """
        Usage:
                Amenity.all() - displays all objects of class Amenity
                Amenity.count() - displays number of objects of class Amenity
                Amenity.show("id") - displays object of class Amenity with id
                Amenity.destroy("id") - deletes object of class Amenity with id
        """
        self._execute('Amenity', args)

    def do_Place(self, args):
        """
        Usage:
                Place.all() - displays all objects of class Place
                Place.count() - displays number of objects of class Place
                Place.show("id") - displays object of class Place with id
                Place.destroy("id") - deletes object of class Place with id
        """
        self._execute('Place', args)

    def do_Review(self, args):
        """
        Usage:
                Review.all() - displays all objects of class Review
                Review.count() - displays number of objects of class Review
                Review.show("id") - displays object of class Review with id
                Review.destroy("id") - deletes object of class Review with id
        """
        self._execute('Review', args)

    def _execute(self, class_name, args):
        """
        Wrapper function for <class name>.action():

            <class name>.all() - displays all objects of <class name>
            <class name>.count() - displays number of objects of <class name>
            <class name>.show("id") - displays object of <class name> with id
            <class name>.destroy("id") - deletes object of <class name> with id
        """
        if args[:6] == '.all()':
            self.do_all(class_name)
        elif args[:6] == '.show(':
            print(class_name)
            print(args[7:-2])
            self.do_show(class_name + ' ' + args[7:-2])
        elif args[:8] == ".count()":
            all_objs = {k: v for (k, v) in models.storage.all().items()
                        if type(v) == eval(class_name)}
            print(len(all_objs))
        elif args[:9] == '.destroy(':
            self.do_destroy(class_name + ' ' + args[10:-2])
        else:
            print("Not a valid command")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
