#!/usr/bin/python3
""""<HBNBCommand> module: Models the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """This is a subclass for command interpreter"""
    prompt = '(hbnb)'

    def do_quit(self, args):
        """This method use to quit program"""
        return True

    def do_EOF(self, args):
        """This method use to quit program"""
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
