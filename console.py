#!/usr/bin/python3

"""This is the console base for the unit """

import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter"""

    prompt = "(hbnb)"
    valid_classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def emptylibe(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_quit(self, arg):
        """Close program and saves safely data """
        return True

    def help_quit(self, arg):
        """gets help"""
        print("Quit command to exit")
        
    def do_EOF(self, arg):
        """End Of File command to exit the program."""
        print()
        return True

    def do_create(self, arg):
        """create a new instance of BaseModel and saves it to JSON file"""
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f"{commands[0]}()")
            storage.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """deletes an instance based on class name and id"""
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects =storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """prints a string representation of all instances"""
        objects = storage.all()
        commands = shlex.split(arg)
        if len(commands) == 0:
            for key, value in objects.items():
                print(str(value))
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == commands[0]:
                    print(str(value))

    def default(self, arg):
        """default of cmd module for invalid syntax"""
        arg_list = arg.split('.') #User.all() output: ['User', 'all()']
        incoming_class_name = arg_list[0]
        command = arg_list[1].split('(')

        incoming_method = command[0]

        method_dict = {
            'all': self.do_all,
            'show': self.do_show,
            'destroy': self.do_destroy,
            'update': self.do_update,
            'count': self.do_count
        }

        if incoming_method in method_dict.keys():
            return method_dict[incoming_method]("{} {}".format(incoming_class_name, ''))
        print("*** Unknown syntax: {}".format(arg))
        return False
    
    def do_count(self, arg):
        """counts and retrives the number of instances of a class: <class name>.count()"""
        objects = storage.all()
        commands = shlex.split(arg)
        if arg:
            incoming_class_name = commands[0]

        count = 0
        if commands:
            if incoming_class_name in self.valid_classes:
                for obj in objects.values():
                    if obj.__class__.__name__ == incoming_class_name:
                        count += 1
                print(count)
            else:
                print("** class name doesn't exist **")
        else:
            print("** class name missing **")
        

    def do_update(self, arg):
        """updates an instance by adding or updating an attribute"""
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn'y exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key not in objects:
                print("** no instance found **")
            elif len(commands) < 3:
                print("** attribute name missing **")
            elif len(commands) < 4:
                print("** value missing **")
            else:
                obj = objects[key]
                attr_name = commands[2]
                attr_value = commands[3]

                try:
                    attr_value = eval(attr_value)
                except Exception:
                    pass
                setattr(obj, attr_name, attr_value)
                obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
