from cloudmesh.storage.StorageNewABC import StorageABC
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.console import Console
from cloudmesh.common.util import banner
from cloudmesh.common.console import Console
# from cloudmesh.storage.provider.local.Provider import Provider as \
#     StorageLocalProvider

from cloudmesh.storage.provider.awss3.Provider import Provider as \
    StorageAwss3Provider
from pathlib import Path
from pprint import pprint

# from azure.storage.blob import BlockBlobService


class Provider(StorageABC):
    """
    Provider class for aws s3 storage.
    This class allows transfer of objects from and to AWS S3 bucket

    Default parameters are read from ~/.cloudmesh/cloudmesh.yaml :

    awss3:
      cm:
        active: false
        heading: homedir
        host: aws.com
        label: home-dir
        kind: awss3
        version: TBD
        service: storage
      default:
        directory: /
      credentials:
        access_key_id: XXX
        secret_access_key: XXX
        bucket: XXX
        region: us-east-2
    """

    def __init__(self, source=None, source_obj=None, target=None,
                 target_obj=None, config="~/.cloudmesh/cloudmesh.yaml"):

        banner(f"""In AES S3 provider
        source csp = {source}, source object = {source_obj}
        target csp = {target}, target object = {target_obj}""")

        # This is a provider for AWS S3 hence initializing storage's AWS S3
        # provider by default
        self.storage_provider = StorageAwss3Provider(service=target)


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
        print("CALLING AWS S3 PROVIDER'S LIST METHOD")
        # Storage local provider expects a path relative to the default
        # directory read from .yaml. Hence:
        # target_path = Path(target_obj)
        # relative_target = target_path.relative_to(*target_path.parts[:2])

        result = self.storage_provider.list(source=target_obj, recursive=True)

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
        print("CALLING AWS S3 PROVIDER'S DELETE METHOD")

        result = self.storage_provider.delete(source=target_obj, recursive=True)

        # TODO : Print a table using printer utility of cm

        Console.ok(f"Deleted following objects from provided object "
                   f"{target_obj}")
        pprint(result)


if __name__ == "__main__":
    p = Provider(source=None, source_obj=None,
                 target="awss3", target_obj="\\")

    # p.list(source=None, source_obj=None,
    #         target="awss3", target_obj="/folder1")

    # p.delete(source=None, source_obj=None,
    #          target="awss3", target_obj="/folder1")
