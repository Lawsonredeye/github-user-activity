#!/usr/bin/env python3
"""Shell module which uses the cmd shell to generate the shell environment for
handling the user activity passed with default commands like fetch, get, and
others"""

import cmd
import requests
import sys


class Terminal(cmd.Cmd):
    """Handles the method for controlling the shell environment"""
    intro: str = "Welcome to GitShell"
    prompt = 'git-shell$ '
    url: str = f'https://api.github.com/users/'

    def do_help(self, arg: str) -> bool | None:
        return super().do_help(arg)
    
    def do_greet(self, line: str) -> None:
        if line == "":
            print("Hello, stranger!")
        else:
            print(f"Hello, {line.title()}!")
    
    def do_fetch(self, line: str) -> None:
        if line:
            print('a request had been made with:', line)
        else:
            print('Invalid name')
        pass
    
    def do_find(self, line: str) -> bool:
        """Finds users git account based on the name passed on the"""
        if not line:
            return 'Must include name'
        re = requests.get(self.url + line)
        if re.status_code == 200:
            user_data: dict = re.json()
            print('You have {} followers and following {}'.format(
                user_data['followers'], user_data['following']))
    
    def do_exit(self, line) -> bool:
        """when called deactivate the shell environment"""
        return True

if __name__ == '__main__':
    try:
        Terminal().cmdloop()
    except KeyboardInterrupt:
        sys.exit('^Bye')
