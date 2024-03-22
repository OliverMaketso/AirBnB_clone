#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """
    Class that define the command interpreter:
    """

    prompt = 'hbnb '

    def do_quit(self, arg):
        """
        Quit command to exit the programme with Ctrl+D
        """
        return True

    def do_EOF(self, arg):
        """
        Handle EOF signal (Ctrl+D) to exit the program.
        """
        return True

    def emptyline(self):
        """
        Do nothing on empty line.
        if the line is empty, emptyline() is called.
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

