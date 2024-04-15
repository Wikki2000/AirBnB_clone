#!/usr/bin/python3
"""console.py - Entry point of the HBNB command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage


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
    def invalid_instance():
        """ print no instance found """
        print("** no instance found **")

    @staticmethod
    def missing_id():
        """ print instance id is missing message """
        print("** instance id missing **")

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Exit the program when EOF is reached (Ctrl+D)"""
        print("")  # Print a newline before exiting
        return True

    def do_create(self, arg):
        """Create an instance of BaseModel """
        obj_dict = {
                "BaseModel": BaseModel,
                }
        if len(arg) == 0: # Alternatively: arg == ""
            self.missing_name()
        elif arg not in obj_dict:
            self.wrong_class()
        else:
            obj = obj_dict[arg]()
            obj.save()
            print(obj.id)

    def do_show(self, args):
        """show an instance of a class"""
        obj_dict = {
                "BaseModel": BaseModel,
                }
        obj_storage = storage.all()
        args_list = args.split()
        if len(args_list) == 0:
            self.missing_name()
        elif args_list[0] not in obj_dict:
            self.wrong_class()

if __name__ == "__main__":
    HBNBCommand().cmdloop()

