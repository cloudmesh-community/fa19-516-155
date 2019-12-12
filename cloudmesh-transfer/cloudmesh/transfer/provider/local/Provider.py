from cloudmesh.storage.StorageNewABC import StorageABC
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.console import Console
from cloudmesh.common.util import banner
from cloudmesh.common.console import Console
from cloudmesh.storage.provider.local.Provider import Provider as \
    StorageLocalProvider
from cloudmesh.common.Printer import Printer
from pathlib import Path
from pprint import pprint


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

        # Transfer local provider should always connect to storage local
        # provider hence using service = "local" by default
        self.storage_provider = StorageLocalProvider(service="local")

    def list(self, source=None, source_obj=None,
             target=None, target_obj=None, recursive=True):
        """
        To enlist content of "target object"
        :param source: source CSP - awss3/azure/local, None for list method
        :param source_obj: It can be file or folder, None for list method
        :param target: target CSP - awss3/azure/local
        :param target_obj: It can be file or folder
        :param recursive: enlist directories/sub-directories
        :return: dictionary enlisting objects
        """
        print("CALLING LOCAL PROVIDER'S LIST METHOD")
        # Storage local provider expects a path relative to the default
        # directory read from .yaml. Hence:
        target_path = Path(target_obj)
        relative_target = str(target_path.relative_to(*target_path.parts[:2]))
        # print("=======> ", relative_target)
        result = self.storage_provider.list(source=relative_target)

        op_result = []
        for idx, i in enumerate(result):
            op_dict = dict()
            op_dict['idx'] = idx+1
            op_dict['CSP'] = target
            op_dict['name'] = i['name']
            op_dict['size'] = i['size']
            op_dict['created'] = i['creation']
            op_dict['type'] = 'File' if i['file'] is True else 'Dir'
            op_dict['source'] = source
            op_dict['target'] = target
            op_dict['status'] = 'Available'
            op_result.append(op_dict)

        # pprint(op_result)
        table = Printer.flatwrite(op_result,
                                  sort_keys=["idx"],
                                  order=["idx", "source", "target", "name",
                                         "size", "type", "created",
                                         "status"],
                                  header=["S.No.", "Source CSP",
                                          "Target CSP", "Name", "Size",
                                          "Type", "Creation", "Status"])
        print(table)
        return op_result

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
        print("CALLING LOCAL PROVIDER'S DELETE METHOD")
        # Storage local provider expects a path relative to the default
        # directory read from .yaml. Hence:
        target_path = Path(target_obj).expanduser()
        if target_path.is_absolute():
            relative_target = str(target_path.relative_to(*target_path.parts[:2]))
        else:
            relative_target = str(target_path)

        print(target_path, "\n", relative_target)

        try:
            result = self.storage_provider.delete(source=relative_target)
            Console.ok(f"Deleted following objects from {target} storage. ")

            op_result = []
            for idx, i in enumerate(result):
                op_dict = dict()
                op_dict['idx'] = idx + 1
                op_dict['name'] = i['name']
                op_dict['size'] = i['size']
                op_dict['created'] = i['creation']
                op_dict['type'] = 'File' if i['file'] is True else 'Dir'
                op_dict['source'] = source
                op_dict['target'] = target
                op_dict['status'] = 'Deleted'
                op_result.append(op_dict)

            # pprint(op_result)
            table = Printer.flatwrite(op_result,
                                      sort_keys=["idx"],
                                      order=["idx", "source", "target", "name",
                                             "size", "type", "created",
                                             "status"],
                                      header=["S.No.", "Source CSP",
                                              "Target CSP", "Name", "Size",
                                              "Type", "Creation", "Status"])
            print(table)
            return op_result

        except FileNotFoundError as n:
            return Console.error(f"\nObject {target_obj} not found in "
                                 f"{target} storage.")
        except Exception as e:
            return Console.error(f"Error occurred: {e}")


# if __name__ == "__main__":
#     p = Provider(source=None, source_obj=None,
#                  target="local", target_obj="~\cmStorage")
#
#     p.list(source=None, source_obj=None,
#            target="local", target_obj="~\cmStorage")
#
#     # p.delete(source=None, source_obj=None,
#     #          target="local", target_obj="abcd.txt")
