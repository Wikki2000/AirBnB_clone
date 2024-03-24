#!/usr/bin/python3
"""console.py - Entry point of the HBNB command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """This class defines the command interpreter"""

    prompt = "(hbnb) "

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


if __name__ == "__main__":
    HBNBCommand().cmdloop()

