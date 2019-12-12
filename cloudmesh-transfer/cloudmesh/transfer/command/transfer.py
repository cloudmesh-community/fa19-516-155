from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
#from cloudmesh.transfer.api.manager import Manager
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from cloudmesh.common.debug import VERBOSE
from cloudmesh.shell.command import command, map_parameters
from cloudmesh.transfer.Provider import Provider
from cloudmesh.common.util import banner
import sys


class TransferCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_transfer(self, args, arguments):
        """
        ::

          Usage:
            transfer copy --source=awss3:source_obj --target=azure:target_obj
            transfer list --target=awss3:target_obj
            transfer delete --target=awss3:target_obj

          This command is part of Cloudmesh's multi-cloud storage service.
          Command allows users to transfer files/directories from storage of
          one Cloud Service Provider (CSP) to storage of other CSP.
          Current implementation is to transfer data between Azure blob
          storage and AWS S3 bucket.
          AWS S3/ Azure Blob storage credentials and container details will
          be fetched from storage section of "~\.cloudmesh\cloudmesh.yaml"


          Arguments:
            awss3:source_obj  Combination of cloud name and the source object
                              name
            source_obj        Source object. Can be file or a directory.
            azure:target_obj  Combination of cloud name and the target object
                              name
            target_obj        Target object. Can be file or a directory.
            transfer_id       A unique id/name assigned by cloudmesh to each
                              transfer instance.


          Options:
            -h                          Help function.
            --source=awss3:source_obj   Specify source cloud and source object.
            --target=azure:target_obj   Specify target cloud and target object.
            -r                          Recursive transfer for folders.


          Description:
            transfer copy --source=<awss3:source_obj>
            .             --target=<azure:target_obj> [-r]
                Copy file/folder from source to target. Source/target CSPs
                and name of the source/target objects to be provided.
                Optional argument "-r" indicates recursive copy.

            transfer list --target=awss3:target_obj
                Enlists available files on target CSP at target object

            transfer delete --target=awss3:target_obj
                Deletes target object from the target CSP.


          Examples:
            transfer copy --source=awss3:sampleFileS3.txt
            .             --target=azure:sampleFileBlob.txt
        """

        print("EXECUTING: ")

        map_parameters(arguments,
                       "source",
                       "target")

        VERBOSE(arguments)

        # Following code is added to include transfer command location in
        # PYTHONPATH. It is required so that PyCharm can import transfer
        # providers with cloudmesh coding standards.

        # pprint(sys.path)
        try:
            sys.path.insert(0,
            r"c:\study\iumsds\fall2019\cloudcomputing\fa19-516-155\cloudmesh-transfer")
        except Exception as e:
            print("PYTHONPATH not updated.")

        # Extract source and target details from the arguments
        if arguments.source:
            source_CSP, source_obj = arguments.source.split(':')
        else:
            source_CSP, source_obj = None, None
        if arguments.target:
            # print("************** ", arguments.target)
            target_CSP, target_obj = arguments.target.split(':')
            # print("************** ", target_CSP, target_obj )
        else:
            target_CSP, target_obj = None, None

        banner(f'''Working on: source CSP = {source_CSP}
         source object = {source_obj}
            target CSP = {target_CSP}
         target object = {target_obj}''')

        # return

        if arguments.FILE:
            print("option a")

        elif arguments.list:
            banner(f"Executing List command for {target_CSP} provider on "
                   f"{target_obj}.")

            provider = Provider(source=None,       source_obj=None,
                                target=target_CSP, target_obj=target_obj)

            provider.list(source=None,       source_obj=None,
                          target=target_CSP, target_obj=target_obj,
                          recursive=True)

        elif arguments.delete:
            banner(f"Executing Delete command for {target_CSP} provider on "
                   f"{target_obj}")

            provider = Provider(source=None,       source_obj=None,
                                target=target_CSP, target_obj=target_obj)

            provider.delete(source=None,       source_obj=None,
                            target=target_CSP, target_obj=target_obj,
                            recursive=True)
        elif arguments.copy:
            # This flow is designed in such a way that copy command is run
            # in target CSP's provider

            banner(f"Executing Copy command from {source_CSP} to {target_CSP} "
                   f"providers for {source_obj}")

            provider = Provider(source=source_CSP, source_obj=source_obj,
                                target=target_CSP, target_obj=target_obj)

            provider.copy(source=source_CSP, source_obj=source_obj,
                          target=target_CSP, target_obj=target_obj,
                          recursive=True)
        else:
            Console.error("Invalid argument provided.")
            return ""


# if __name__ == "__main__":
#     try:
#         inst = TransferCommand()
#         inst.do_transfer('list --target=local:a')
#     except Exception as e:
#         print(e)
