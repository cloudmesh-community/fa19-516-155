from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.transfer.api.manager import Manager
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE

class TransferCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_transfer(self, args, arguments):
        """
        ::

          Usage:
                transfer config [--file=ip_file]
                transfer --id=<transfer_id> --data=<file_name> [--copy=True|False]
                transfer status --id=<transfer_id>
                transfer statistic

          This command is part of CloudMesh's multicloud storage service. Command allows users to transfer
          files/directories from storage of one Cloud Service Provider (CSP) to storage of other CSP.
          Current implementation is to transfer data between Azure blob storage and AWS S3 bucket.

          Arguments:
              transfer_id   A unique id/name assigned by user to each transfer instance
              file_name     Name of the file/directory to be transferred
              Boolean       True/False argument for --copy option. When False, data will be removed from source location
              ip_file       Input file used to configure 'transfer' command

          Options:
              --id=transfer_id        Specify a unique i/name to the transfer instance
              --data=file_name        Specify the file/directory name to be transferred
              --copy=True|False       Specify is the data should be kept in source location after the transfer
              --file=ip_file          Specify the file to be used for configuration of the transfer instance
              -h                      Help function

          Description:
              transfer config [options..]
                    Configures source/destination and authentication details to be used by transfer command

              transfer [options..]
                    Transfers file/directory from storage of one CSP to storage of another CSP

              transfer status [options..]
                    Returns status of given transfer instance

              transfer statistic
                    Returns statistics of all transfer processes

          Examples:
              transfer --id="Dummy transfer" --data=dummy_file.txt --copy=True
        """
        arguments.FILE = arguments['--file'] or None

        VERBOSE(arguments)

        m = Manager()

        if arguments.FILE:
            print("option a")
            m.list(path_expand(arguments.FILE))

        elif arguments.list:
            print("option b")
            m.list("just calling list without parameter")

        Console.error("This is just a sample")
        return ""
