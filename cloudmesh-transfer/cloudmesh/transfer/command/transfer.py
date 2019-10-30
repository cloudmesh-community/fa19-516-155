from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.transfer.api.manager import Manager
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE
from cloudmesh.shell.command import command, map_parameters

class TransferCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_transfer(self, args, arguments):
        """
        ::

          Usage:
            transfer copy --source=aws:sourceObj --target=azure:targetObj [-r]
            transfer list --target=aws:targetObj
            transfer delete --target=aws:targetObj
            transfer status --id=transfer_id
            transfer statistic

          This command is part of Cloudmesh's multi-cloud storage service.
          Command allows users to transfer files/directories from storage of
          one Cloud Service Provider (CSP) to storage of other CSP.
          Current implementation is to transfer data between Azure blob
          storage and AWS S3 bucket.
          AWS S3/ Azure Blob storage credentials and container details will
          be fetched from storage section of "~\.cloudmesh\cloudmesh.yaml"


          Arguments:
            aws:sourceObj   Combination of cloud name and the source object name
            sourceObj       Source object. Can be file or a directory.
            azure:targetObj Combination of cloud name and the target object name
            targetObj       Target object. Can be file or a directory.
            transfer_id     A unique id/name assigned by cloudmesh to each
                            transfer instance.


          Options:
            --id=transfer_id            Unique id/name of the transfer instance.
            -h                          Help function.
            --source=aws:sourceObj      Specify source cloud and source object.
            --target=azure:targetObj    Specify target cloud and target object.
            -r                          Recursive transfer for folders.


          Description:
            transfer copy --source=<aws:sourceObj> --target=<azure:targetObj> [-r]
                Copy file/folder from source to target. Source/target CSPs
                and name of the source/target objects to be provided.
                Optional argument "-r" indicates recursive copy.

            transfer list --target=aws:targetObj
                Enlists available files on target CSP at target object

            transfer delete --target=aws:targetObj
                Deletes target object from the target CSP.

            transfer status --id=<transfer_id>
                Returns status of given transfer instance

            transfer statistic
                Returns statistics of all transfer processes


          Examples:
            transfer copy --source=aws:sampleFileS3.txt
            .             --target=azure:sampleFileBlob.txt
        """
        print("EXECUTING: ")
        map_parameters(arguments,
                       "source",
                       "target")

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
