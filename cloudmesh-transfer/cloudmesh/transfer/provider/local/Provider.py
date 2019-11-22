# import boto3
# from botocore.exceptions import ClientError
from cloudmesh.storage.StorageNewABC import StorageABC
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.console import Console
from cloudmesh.common.util import banner
from cloudmesh.configuration.Config import Config
from cloudmesh.common.console import Console
from cloudmesh.storage.provider.local.Provider import Provider as \
    StorageLocalProvider

# from cloudmesh.storage.Provider import Provider as StorageProvider

from pathlib import Path
from glob import glob
import os, shutil, queue
from pprint import pprint

# from azure.storage.blob import BlockBlobService


class Provider(StorageABC):
    """
    Provider class for local storage.
    This class allows transfer of objects from local storage location to a AWS
    S3 bucket or Azure blob storage container.

    Default parameters are read from ~/.cloudmesh/cloudmesh.yaml :

    storage:
        local:
          cm:
            s3active: true
            blobactive: true
            heading: local_to_CSP
            host: localhost
            kind: local
            label: local_storage
            version: 0.1
            service: storage
          default:
            directory: ~\cmStorage
          credentials:
            userid: None
            password: None
    """

    def __init__(self, source=None, source_obj=None, target=None,
                 target_obj=None, config="~/.cloudmesh/cloudmesh.yaml"):

        # super().__init__(service=source, config=config)

        banner(f"""In LOCAL provider
        source csp = {source}, source object = {source_obj}
        target csp = {target}, target object = {target_obj}""")

        # if source
        # source_provider = init source storage provider
        # same for target_provider

        # TODO: initialize storage local provider for list delete
        # initialize storage aws/azure for copy to/from local

    # TODO - check pass recursive argument from master provider & transfer.py

    def list(self, source=None, source_obj=None,
                   target=None, target_obj=None,
                   recursive=True):
        """
        To enlist content of "target object"
        :param source:
        :param source_object:
        :param target:
        :param target_object:
        :param recursive:
        :return:
        """
        print("CALLING LOCAL PROVIDER'S LIST METHOD")
        # Storage local provider expects a path relative to the default
        # directory read from .yaml. Hence:
        target_path = Path(target_obj)
        relative_target = target_path.relative_to(*target_path.parts[:2])

        # TODO: Move this init to init class

        storage_provider = StorageLocalProvider(service=target)
        result = storage_provider.list(source=relative_target)

        # TODO : Print a table using printer utility of cm
        pprint(result)

    def delete(self, source=None, source_obj=None,
                     target=None, target_obj=None,
                     recursive=True):
        """
        To delete content of "target object"
        :param source:
        :param source_object:
        :param target:
        :param target_object:
        :param recursive:
        :return:
        """
        print("CALLING LOCAL PROVIDER'S LIST METHOD")
        # Storage local provider expects a path relative to the default
        # directory read from .yaml. Hence:
        target_path = Path(target_obj)
        relative_target = target_path.relative_to(*target_path.parts[:2])

        print("IN TRANSFER LOCAL PROCIDER FOR DELETE.")
        print(target_path, "\n", relative_target)
        # TODO: Move this init to init class

        storage_provider = StorageLocalProvider(service=target)
        result = storage_provider.delete(source=relative_target)

        # TODO : Print a table using printer utility of cm
        # TODO : NOTE - delete doesn't return the directory name (source)
        Console.ok(f"Deleted following objects from provided object "
                   f"{target_obj}") 
        pprint(result)


if __name__ == "__main__":
    p = Provider(source=None, source_obj=None,
                 target="local", target_obj="~\cmStorage")
    # p.list(source=None, source_obj=None,
    #        target="local", target_obj="~\cmStorage")

    p.delete(source=None, source_obj=None,
           target="local", target_obj="~\\cmStorage\\b")
