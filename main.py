#!/usr/bin/env python3
"""Shell module which uses the cmd shell to generate the shell environment for
handling the user activity passed with default commands like fetch, get, and
others"""

import cmd
from datetime import datetime
from helpers import push_event, create_event
import urllib3
import sys


class Terminal(cmd.Cmd):
    """Handles the method for controlling the shell environment"""
    intro: str = """Welcome to github-activity-shell
    Type 'help' for more information.
    """
    prompt = 'git-shell$ '
    # url: str = 'https://api.github.com/users/{}/events'

    def do_help(self, arg: str) -> bool | None:
        return super().do_help(arg)

    def do_greet(self, line: str) -> None:
        if line == "":
            print("Hello, stranger!")
        else:
            print(f"Hello, {line.title()}!")

    def do_find(self, line: str) -> bool:
        """Finds users git account based on the name passed on the command
        line"""
        if not line:
            print('ERROR: find : Must include <github username>')
        else:
            re = urllib3.request(
                'GET',
                'https://api.github.com/users/{}/events'.format(line))
            if re.status == 200:
                user_data: list = re.json()
                if user_data != []:
                    print('{} have made {} new commits today'.format(
                        push_event(line, user_data)))
                    print('{} have created {} new repos'.format(
                        create_event(line, user_data)))
                else:
                    print('No recent activity')
            else:
                print('{}: User not found'.format(line))

    def do_exit(self, line) -> bool:
        """when called deactivate the shell environment"""
        return True


if __name__ == '__main__':
    try:
        Terminal().cmdloop()
    except KeyboardInterrupt:
        sys.exit('^Bye')
