#!/usr/bin/python3
"""console.py - Entry point of the HBNB command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """This class defines the command interpreter"""

    intro = "Welcome to the HBNB command interpreter. Type 'help' to list commands."
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Exit the program when EOF is reached (Ctrl+D)"""
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()

