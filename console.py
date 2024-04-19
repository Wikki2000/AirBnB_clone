#!/usr/bin/python3
"""console.py - Entry point of the HBNB command interpreter"""
import cmd
from models.base_model import BaseModel
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """This class defines the command interpreter"""
    __obj_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
        }
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
        
    @staticmethod
    def class_name(args):
        """Retrieve class name"""
        args_list = args.split()
        class_name = args_list[0]  # Get the class name from args_list
        obj_class = HBNBCommand.__obj_dict[class_name]  # Get the class from obj_dict using the class name
        return obj_class
        
        

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Exit the program when EOF is reached (Ctrl+D)"""
        print("")  # Print a newline before exiting
        return True

    def do_create(self, arg):
        """Create an instance of BaseModel """
        if len(arg) == 0: # Alternatively: arg == ""
            self.missing_name()
        elif arg not in HBNBCommand.__obj_dict:
            self.wrong_class()
        else:
            obj = HBNBCommand.__obj_dict[arg]() # Create an instance of a class
            obj.save()
            print(obj.id)

    def do_show(self, args):
        """Prints the string representation of an instance based on the class name and id"""
        obj_storage = storage.all()
        args_list = args.split()
        if len(args_list) == 0:
            self.missing_name()
        elif args_list[0] not in HBNBCommand.__obj_dict:
            self.wrong_class()
        elif args_list[0] in HBNBCommand.__obj_dict and len(args_list) != 2:
            self.missing_id()
        else:
            instance_id = args_list[1]  # Get the instance ID from args_list
            obj_class = self.class_name(args)
            
            for key, obj in obj_storage.items():
                if isinstance(obj, obj_class) and obj.id == instance_id:
                    print(obj)
                    break
                else:
                    self.invalid_instance()
    
    def do_destroy(self, args):
        """Deletes an instance based on the class name and id (save the change into the JSON file)"""
        obj_storage = storage.all()
        args_list = args.split()
        if len(args_list) == 0:
            self.missing_name()
        elif args_list[0] not in HBNBCommand.__obj_dict:
            self.wrong_class()
        elif args_list[0] in HBNBCommand.__obj_dict and len(args_list) != 2:
            self.missing_id()
        else:
            obj_class = self.class_name(args)
            instance_id = args_list[1]
            for key, obj in obj_storage.copy().items():
                if isinstance(obj, obj_class) and obj.id == instance_id:
                    del obj_storage[key]
                    storage.save()
                    break
                else:
                    self.invalid_instance()
    
    def do_all(self, args):
        obj_storage = storage.all()
        """Print a list of all string rep. of all instances based or not on class name"""
        obj_list = []
        args_list = args.split()
        if len(args_list) == 1:
            if args_list[0] not in HBNBCommand.__obj_dict:
                self.wrong_class()
            else:
                obj_class = self.class_name(args)
                for key, obj in obj_storage.items():
                    if isinstance(obj, obj_class):
                        obj_list.append(str(obj))
                print(obj_list)
        elif len(args_list) == 0:
            for key, obj in obj_storage.items():
                obj_list.append(str(obj))
            print(obj_list)
    
    def do_update(self, args):
        """Update an attribute of a class"""
        obj_storage = storage.all()
        args_list = args.split()
        if len(args_list) == 0:
            self.missing_name()
        elif args_list[0] not in HBNBCommand.__obj_dict:
            self.wrong_class()
        elif args_list[0] in HBNBCommand.__obj_dict:
            if len(args_list) == 1:
                self.missing_id()
            elif len(args_list) == 2:
                    print("** attribute name missing **")
            elif len(args_list) == 3:
                print("** value missing **")
            elif len(args_list) == 4:
                
                # Check for invalid object id
                obj_class = self.class_name(args)
                instance_id = args_list[1]
                for key, obj in obj_storage.items():
                    if isinstance(obj, obj_class) and obj.id == instance_id:
                        setattr(obj, args_list[2], args_list[3])
                        break
                else:
                    self.invalid_instance()
            else:
                print("** number of arguments exceeded **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
