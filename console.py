#!/usr/bin/python3
"""console.py - Entry point of the HBNB command interpreter"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """This class defines the command interpreter"""

    prompt = "(hbnb) "

    @staticmethod
    def wrong_class():
        """Print  "** class doesn't exist **", if class does not exist"""
        print("** class doesn't exist **")

    @staticmethod
    def missing_name():
        """Print "**class name missing **", if class name is not given"""
        print("** class name missing **")

    @staticmethod
    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Exit the program when EOF is reached (Ctrl+D)"""
        print("")  # Print a newline before exiting
        return True

    def emptyline(self):
        """Do nothing on empty line (pressing ENTER)"""
        pass

    def do_create(self, class_name):
        """Create instance of a class"""
        class_list = [BaseModel, User]
        if class_list == "":
            self.missing_name()
        elif class_name not in class_list:
            self.wrong_class()
        else:
            # Retrieve the index number of given class in class_list
            # Using this index to get the class so as to create an instance
            class_index = class_list.index(class_name)
            obj_instance = class_name[class_index]()
            obj_instance.save()
            print(obj_instance.id)

if __name__ == "__main__":
    HBNBCommand().cmdloop()

