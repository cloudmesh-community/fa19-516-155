import os
import stat
from pprint import pprint

import boto3
from botocore.exceptions import ClientError
from cloudmesh.storage.StorageABC import StorageABC
import oyaml as yaml
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.console import Console
from cloudmesh.common.util import banner
from cloudmesh.common.Printer import Printer
from cloudmesh.configuration.Config import Config

from pathlib import Path
from glob import glob
import os
import shutil


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

    def __init__(self, service=None, config="~/.cloudmesh/cloudmesh.yaml",
                 **kwargs):
        super().__init__(service=service, config=config)

        if kwargs.get("debug"):
            print("Inside init of local provider")
            print(self.kind)
            print(kwargs.get('sourceObj'))
            print(kwargs.get('target'))
            print(kwargs.get('targetObj'))
            print(self.credentials)

    # Processing --source/service and --target arguments separately.
    # This is a provider class for local storage hence --source/service will \
    # always be "local"

        self.sourceCSP = self.service

        try:
            self.config = Config(config_path=config)
            self.yaml_content_source = self.config["cloudmesh.storage." 
                                                   f"{self.sourceCSP}"]
            self.source_kind = self.yaml_content_source["cm"]["kind"]
            self.source_credentials = self.yaml_content_source["credentials"]

            print("Accessing local storage location.")
            if kwargs.get('sourceObj'):
                self.local_location = Path(self.yaml_content_source['default'][
                                      'directory'], kwargs.get('sourceObj'))
            else:
                self.local_location = self.yaml_content_source['default'][
                    'directory']

            print("===> ", type(self.local_location),
                  self.local_location.is_file(),
                  os.path.isfile(self.local_location.parts[-1]),
                  self.local_location.expanduser().is_file())

            if kwargs.get("debug"):
                print(f"\nLocal location to access {self.local_location}")


            if kwargs.get('target'):
                self.targetCSP = kwargs.get('target')
                self.yaml_content_target = self.config["cloudmesh.storage." 
                                                       f"{self.targetCSP}"]
                self.target_kind = self.yaml_content_target["cm"]["kind"]
                self.target_credentials = self.yaml_content_target[
                                                            "credentials"]
        except Exception as e:
            Console.error(f"Couldn't access cloudmesh.yaml. Error - {e}")
            return ()

        if kwargs.get("debug"):
            VERBOSE(self.yaml_content_source)
            if kwargs.get('target'):
                VERBOSE(self.yaml_content_target)

        banner(f"Source CSP: {self.source_kind}")
        if kwargs.get('target'):
            banner(f"Target CSP: {self.target_kind}")

        # Creating connection with the target CSP. This done only if the
        # --target argument is provided. Only "copy" command is expected to
        # have --target argument.

        if kwargs.get('target'):
            if self.target_kind == "awss3":
                print("Create AWS connection.")

                if 'TBD' == self.credentials["access_key_id"] or \
                        'TBD' == self.credentials["secret_access_key"] or \
                        'TBD' == self.credentials["region"]:
                    Console.error("Critical details missing from .yaml file. "
                                  "TBD  not allowed. Please check.")

                try:
                    self.s3_client = boto3.client(
                        's3',
                        aws_access_key_id=self.credentials["access_key_id"],
                        aws_secret_access_key=self.credentials[
                            "secret_access_key"],
                        region_name=self.credentials["region"]
                    )
                    Console.ok(f"Successful connection to {self.kind} is made.")
                except ClientError as e:
                    Console.error(e, prefix=True, traceflag=True)

            elif self.kind == "azureblob":
                print("Create Azure connection.")
                raise NotImplementedError
                return {}
            else:
                raise NotImplementedError
                return {}

# TODO - check hor to pass recursive argument from master provider & transfer.py

    def list(self, service=None, sourceObj=None, recursive=False):
        """
        Method to enlist all objects of target location.

        :param service: local/aws/azure
        :param source: target directory or file
        :param recursive: Boolean to indicate if sub components to be enlisted
        :return: list of lists containing objects from target location
        """
        if self.source_kind == "awss3":
            Console.error("This command should flow to AWS provider. Please "
                          "check.")
            return
        elif self.source_kind == "azureblob":
            Console.error("This command should flow to AWS provider. Please "
                          "check.")
            return
        elif self.source_kind == "local":
            banner(f"Executing list method for local storage:\nSource object "
                   f"is {self.local_location}")
            if self.local_location.exists():
                if self.local_location.expanduser().is_file():
                    os.chdir(os.path.split(self.local_location.expanduser())[0])

                    if len(glob(sourceObj)) > 0:
                        Console.ok("List of file(s):\n"
                                   f"{self.local_location.expanduser()}")
                    else:
                        Console.error(f"File not found "
                                      f"{self.local_location.expanduser()}")
                elif self.local_location.expanduser().is_dir():
                    os.chdir(self.local_location.expanduser())
                    Console.ok(f"List if files in {self.local_location}:\n")
                    for f in glob("**", recursive=recursive):
                        print(Path.cwd() / f)
            else:
                Console.error(f"Source object {self.local_location} does not "
                              f"exist.")
        else:
            raise NotImplementedError
            return {}

    def delete(self, service="local", sourceObj=None, recursive=False):
        """
        This method deletes file(s) / folder(s) from the source location.

        :param service: "local" for this provider
        :param sourceObj: A file or folder to delete
        :param recursive: Delete files from folder/subfolders
        :return: None
        """
        if self.source_kind == "awss3":
            Console.error("This command should flow to AWS provider. Please "
                          "check.")
            return
        elif self.source_kind == "azureblob":
            Console.error("This command should flow to AWS provider. Please "
                          "check.")
            return
        elif self.source_kind == "local":
            banner(f"Executing delete method for local storage:\nSource object "
                   f"is {self.local_location}")

            if self.local_location.exists():
                if self.local_location.expanduser().is_file():
                    os.chdir(os.path.split(self.local_location.expanduser())[0])

                    if len(glob(sourceObj)) > 0:
                        Console.ok("Following file will be removed:\n"
                                   f"{self.local_location.expanduser()}")
                        os.remove(self.local_location.expanduser())
                    else:
                        Console.error(f"File not found "
                                      f"{self.local_location.expanduser()}")
                elif self.local_location.expanduser().is_dir():
                    os.chdir(self.local_location.expanduser())
                    Console.ok(f"Following objects will be removed from: "
                               f"{self.local_location}:\n")
                    for f in glob("**", recursive=recursive):
                        print(Path.cwd() / f)

                    shutil.rmtree(self.local_location.expanduser())
            else:
                Console.error(f"Source object {self.local_location} does not exist.")
        else:
            raise NotImplementedError
            return {}


def main():
    print("Instantiating")
    # following instantiating for copy command
    # instance = Provider(service="local", sourceObj="abcd.txt", target="aws",
    #                     targetObj=None, debug=True)

    # Instantiating for list/delete command
    instance = Provider(service="local", sourceObj="a",
                        targetObj=None, debug=True)

    # instance.list(service="local", sourceObj="a", recursive=True)

    instance.delete(service="local", sourceObj="a", recursive=True)

if __name__ == "__main__":
    main()
