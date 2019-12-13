from cloudmesh.storage.StorageNewABC import StorageABC
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.configuration.Config import Config
from cloudmesh.common.util import banner
from cloudmesh.common.console import Console
from cloudmesh.storage.provider.awss3.Provider import Provider as \
    StorageAwss3Provider
from cloudmesh.storage.provider.azureblob.Provider import Provider as \
    StorageAzureblobProvider
from pathlib import Path
from pprint import pprint
from cloudmesh.common.Printer import Printer


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

    @staticmethod
    def print_table(result, status=None, source=None, target=None):
        op_result = []
        for idx, i in enumerate(result):
            op_dict = dict()
            op_dict['idx'] = idx + 1
            op_dict['source'] = source
            op_dict['name'] = i['name']
            op_dict['size'] = i['cm']['size']
            op_dict['lastmodified'] = "Not Available"
            op_dict['type'] = 'File'
            op_dict['status'] = status
            op_dict['target'] = target
            op_result.append(op_dict)

        # pprint(op_result)
        table = Printer.flatwrite(op_result,
                                  sort_keys=["idx"],
                                  order=["idx", "source", "target", "name",
                                         "size", "type", "lastmodified",
                                         "status"],
                                  header=["S.No.", "Source CSP",
                                          "Target CSP", "Name", "Size",
                                          "Type", "Creation", "Status"])
        print(table)
        return op_result

    def list(self, source=None, source_obj=None,
             target=None, target_obj=None,
             recursive=True):
        """
        To enlist content of "target object"
        :param source: source CSP - awss3/azure/local, None for list method
        :param source_obj: It can be file or folder, None for list method
        :param target: target CSP - awss3/azure/local
        :param target_obj: It can be file or folder
        :param recursive: enlist directories/sub-directories
        :return: dictionary enlisting objects
        """
        print("CALLING AZURE BLOB STORAGE PROVIDER'S LIST METHOD")

        # print("=============> ", target_obj)
        if target_obj:
            target_obj = target_obj.replace("\\", "/")
        else:
            target_obj = '/'
        # print(target_obj, recursive)
        result = self.storage_provider.list(source=target_obj,
                                            recursive=recursive)

        if result is None:
            return Console.error(f"List of object(s) couldn't be fetched from " 
                                 f"{target} CSP for object {target_obj}. "
                                 f"Please check.")
        else:
            Console.ok(f"\nList of objects from {target} CSP for object " 
                       f"{target_obj}:\n")
            # pprint(result)
            return self.print_table(result, status="Available",
                                    source=source, target=target)

    def delete(self, source=None, source_obj=None,
               target=None, target_obj=None,
               recursive=True):
        """
        To delete content of "target object"
        :param source: source CSP - awss3/azure/local, None for delete method
        :param source_obj: It can be file or folder, None for delete method
        :param target: target CSP - awss3/azure/local
        :param target_obj: It can be file or folder
        :param recursive: enlist directories/sub-directories
        :return: dictionary enlisting deleted objects
        """
        print("CALLING AZURE BLOB STORAGE PROVIDER'S DELETE METHOD")

        target_obj = target_obj.replace("\\", "/")
        result = self.storage_provider.delete(source=target_obj, recursive=True)

        if result is None:
            return Console.error(f"Objects couldn't be deleted from " 
                                 f"{target} CSP for object {target_obj}. "
                                 f"Please check.")
        else:
            Console.ok(f"Deleted following objects from provided object "
                       f"{target_obj}")
            # pprint(result)
            return self.print_table(result, status="Deleted", source=source,
                                    target=target)

    def copy(self, source=None, source_obj=None,
             target=None, target_obj=None,
             recursive=True):
        """
        Copy objects from source to target storage
        :param source: source CSP - awss3/azure/local
        :param source_obj: It can be file or folder
        :param target: target CSP - awss3/azure/local
        :param target_obj: It can be file or folder
        :param recursive: enlist directories/sub-directories
        :return: dictionary enlisting copied objects
        """
        banner(f"CALLING AZURE BLOB STORAGE PROVIDER'S GET METHOD FOR "
               f"{source.upper()} TO {target.upper()} COPY")

        if target_obj is None:
            target_obj = source_obj

        target_obj = target_obj.replace("\\", "/")
        source_obj = source_obj.replace("\\", "/")

        if target == "local":

            result = self.storage_provider.get(source=source_obj,
                                               destination=target_obj,
                                               recursive=recursive)
        elif target == "azure":
            source_obj = str(Path(source_obj).expanduser()).replace("\\", "/")

            if source == "awss3":
                source_provider = StorageAwss3Provider(service='awss3')
                config = Config(config_path="~/.cloudmesh/cloudmesh.yaml")

                spec = config["cloudmesh.storage"]
                local_target = spec["local"]["default"]["directory"]
                local_target = local_target.replace("\\", "/")

                result = source_provider.get(source=source_obj,
                                             destination=local_target,
                                             recursive=recursive)
                print("Fetched from s3 to local:\n")
                # pprint(result)
                # TODO: return error if get fails, no put required

                source_obj = Path(Path(local_target).expanduser() / source_obj)

            result = self.storage_provider.put(source=source_obj,
                                               destination=target_obj,
                                               recursive=recursive)
        else:
            raise NotImplementedError

        if result is None:
            return Console.error(f"Object {source_obj} couldn't be copied "
                                 f"from {source} to {target}. Please check.")
        else:
            Console.ok(f"Copied {source_obj} from {source} to {target}\nTarget "
                       f"object name is {target_obj} ")
            pprint(result)
            return self.print_table(result, status="Copied", source=source,
                                    target=target)


# if __name__ == "__main__":
#     p = Provider(source=None, source_obj=None,
#                  target="azure", target_obj="\\")
#
#     # p.list(source=None, source_obj=None,
#     #        target="azure", target_obj="\\folder1")
#
#     # p.delete(source=None, source_obj=None,
#     #          target="azure", target_obj="\\folder1")
#
    # p.copy(source="azure", source_obj="a.txt",
    #        target="local", target_obj="~/cmStorage",
    #        recursive=True)
#
#     # p.copy(source="local", source_obj="~\\cmStorage\\folder1",
#     #        target="azure", target_obj="\\folder1",
#     #        recursive=True)
#     p.copy(source="awss3", source_obj="abcd.txt",
#            target="azure", target_obj="\\folder1",
#            recursive=True)

