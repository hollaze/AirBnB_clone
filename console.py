#!/usr/bin/python3

import cmd
import sys


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    
    def __do_prompt(self, prompt):
        """Change the interactive prompt:
        (hbnb) """
        self.prompt = prompt
    
    def do_EOF(self, arg):
        """Exit the console:
        input: Ctrl+D"""
        print()
        return True

    def do_quit(self, arg):
        """Quit the console:
        write "quit" """
        return True
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()
