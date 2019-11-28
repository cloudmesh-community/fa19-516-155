from cloudmesh.storage.StorageNewABC import StorageABC
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.util import banner
from cloudmesh.common.console import Console
from cloudmesh.storage.provider.awss3.Provider import Provider as \
    StorageAwss3Provider
from cloudmesh.storage.provider.azureblob.Provider import Provider as \
    StorageAzureblobProvider
from pathlib import Path
from pprint import pprint


class Provider(StorageABC):
    """
    Provider class for Azure blob storage.
    This class allows transfer of objects from and to Azure Blob storage
    container
    Default parameters are read from ~/.cloudmesh/cloudmesh.yaml :

    azure:
      cm:
        active: false
        heading: AWS
        host: azure.mocrosoft.com
        label: azure_blob
        kind: azureblob
        version: TBD
        service: storage
      default:
        resource_group: Cloudmesh
        location: 'East US'
      credentials:
        account_name: ***
        account_key: ***
        container: transferreddata
        AZURE_TENANT_ID: xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
        AZURE_SUBSCRIPTION_ID: xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
        AZURE_APPLICATION_ID: xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
        AZURE_SECRET_KEY: TBD
        AZURE_REGION: northcentralus    """

    def __init__(self, source=None, source_obj=None, target=None,
                 target_obj=None, config="~/.cloudmesh/cloudmesh.yaml"):

        banner(f"""In Azure Blob Storage provider
        source csp = {source}, source object = {source_obj}
        target csp = {target}, target object = {target_obj}""")

        # This is a provider for Azure Blob hence initializing storage's AWS S3
        # provider by default

        self.storage_provider = StorageAzureblobProvider(service='azure')


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
        print("CALLING AZURE BLOB STORAGE PROVIDER'S LIST METHOD")
        # Storage local provider expects a path relative to the default
        # directory read from .yaml. Hence:
        # target_path = Path(target_obj)
        # relative_target = target_path.relative_to(*target_path.parts[:2])
        print(target_obj)
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
        print("CALLING AZURE BLOB STORAGE PROVIDER'S DELETE METHOD")

        result = self.storage_provider.delete(source=target_obj, recursive=True)

        # TODO : Print a table using printer utility of cm

        Console.ok(f"Deleted following objects from provided object "
                   f"{target_obj}")
        pprint(result)

    def copy(self, source=None, source_obj=None,
                   target=None, target_obj=None,
                   recursive=True):
        print("CALLING AWS S3 PROVIDER'S GET METHOD FOR AWS S3 TO LOCAL COPY")

        if target_obj is None:
            target_obj = source_obj

        if target == "local":
            result = self.storage_provider.get(source=source_obj,
                                               destination=target_obj,
                                               recursive=recursive)
        elif target == "awss3":
            source_obj = str(Path(source_obj).expanduser()).replace("\\", "/")

            result = self.storage_provider.put(source=source_obj,
                                               destination=target_obj,
                                               recursive=recursive)
        else:
            raise NotImplementedError
        # TODO : Print a table using printer utility of cm

        Console.ok(f"Copied {source_obj} from {source} to {target}\nTarget "
                   f"object name is {target_obj} ")
        pprint(result)


if __name__ == "__main__":
    p = Provider(source=None, source_obj=None,
                 target="azure", target_obj="\\")

    p.list(source=None, source_obj=None,
           target="azure", target_obj="/folder1")

    # p.delete(source=None, source_obj=None,
    #          target="awss3", target_obj="/folder1")

    # p.copy(source="awss3", source_obj="/folder1",
    #        target="local", target_obj="~\\cmStorage",
    #        recursive=True)

    # p.copy(source="local", source_obj="~\\cmStorage\\folder1",
    #        target="awss3", target_obj="/folder1/",
    #        recursive=True)
