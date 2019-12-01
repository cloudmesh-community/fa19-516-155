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

        self.storage_provider = StorageLocalProvider(service=target)

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
        relative_target = str(target_path.relative_to(*target_path.parts[:2]))
        # print("=======> ", relative_target)
        result = self.storage_provider.list(source=relative_target)

        op_result = []
        for idx, i in enumerate(result):
            op_dict = dict()
            op_dict['idx'] = idx+1
            op_dict['name'] = i['name']
            op_dict['size'] = i['size']
            op_dict['created'] = i['creation']
            op_dict['type'] = 'File' if i['file'] is True else 'Dir'
            op_result.append(op_dict)

        # pprint(op_result)
        table = Printer.flatwrite(op_result,
                                  sort_keys=["idx"],
                            order=["idx", "name", "size", "type", "created"],
                            header=["S.No.", "Name", "Size", "Type",
                                    "Creation"],)
        print(table)
        return op_result

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
                op_result.append(op_dict)

            # pprint(op_result)
            table = Printer.flatwrite(op_result,
                                      sort_keys=["idx"],
                                      order=["idx", "name", "size", "type",
                                             "created"],
                                      header=["S.No.", "Name", "Size", "Type",
                                              "Creation"], )
            print(table)
            return op_result

        except FileNotFoundError as n:
            return Console.error(f"\nObject {target_obj} not found in "
                                 f"{target} storage.")
        except Exception as e:
            return Console.error(f"Error occurred: {e}")


if __name__ == "__main__":
    p = Provider(source=None, source_obj=None,
                 target="local", target_obj="~\cmStorage")

    p.list(source=None, source_obj=None,
           target="local", target_obj="~\cmStorage")

    # p.delete(source=None, source_obj=None,
    #          target="local", target_obj="abcd.txt")
