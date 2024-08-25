import cmd
import requests
import sys


class Terminal(cmd.Cmd):
    intro: str = "Welcome to GitShell"
    prompt = 'git-shell$ '
    url: str = f'https://api.github.com/users/'

    def do_help(self, arg: str) -> bool | None:
        return super().do_help(arg)
    
    def do_greet(self, line: str) -> str:
        if line == "":
            print("Hello, stranger!")
        else:
            print(f"Hello, {line.title()}!")
    
    def do_fetch(self, line: str):
        if line:
            print('a request had been made with:', line)
        else:
            print('Invalid name')
        pass
    
    def do_find(self, line) -> bool:
        re = requests.get(self.url + line)
        if re.status_code == 200:
            user_data: dict = re.json()
            print('You have {} followers and following {}'.format(
                user_data['followers'], user_data['following']))
    
    def do_exit(self, line):
        return True

if __name__ == '__main__':
    try:
        Terminal().cmdloop()
    except KeyboardInterrupt:
        sys.exit('^Bye')
