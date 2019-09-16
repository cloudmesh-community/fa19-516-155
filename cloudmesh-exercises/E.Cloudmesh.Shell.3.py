# fa19-516-155 E.Cloudmesh.Shell.3
"""
Usage: E.Cloudmesh.Shell.3.py [-h]

Function to run newly created Shell command

Arguments:
   None

Options:
-h --help
"""

from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.Shell import Shell


class KetanCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_ketan(self, args, arguments):
        """
        ::

          Usage:
                ketan --file=FILE
                ketan list

          This command does some useful things.

          Arguments:
              FILE   a file name

          Options:
              -f      specify the file

        """
        arguments.FILE = arguments['--file'] or None

        VERBOSE(arguments)

        if arguments.FILE:
            print("You have used file: ", arguments.FILE)

        return ""


if __name__=="__main__":
    result = Shell.execute('cms', ['ketan', '--file', 'E.Cloudmesh.Shell.1.py'])
    print(result)
