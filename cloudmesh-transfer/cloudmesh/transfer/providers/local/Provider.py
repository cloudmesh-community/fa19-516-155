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

        self.targetCSP = kwargs.get('target')
        try:
            self.config = Config(config_path=config)
            self.yaml_content = self.config["cloudmesh.storage." \
                                            f"{self.targetCSP}"]
        except Exception as e:
            Console.error(f"Couldn't access cloudmesh.yaml. Error - {e}")
            return ()

        if kwargs.get("debug"):
            pprint(self.yaml_content)

        self.kind = self.yaml_content["cm"]["kind"]
        self.credentials = self.yaml_content["credentials"]

        banner(f"Working on {self.kind} cloud service.")

        if self.kind == "awss3":
            print("Create AWS connection.")

            if 'TBD' == self.credentials["access_key_id"] or \
                    'TBD' == self.credentials["secret_access_key"] or \
                    'TBD' == self.credentials["region"]:
                Console.error("Critical details missing from .yaml file. TBD "
                              "not allowed. Please check.")

            try:
                self.s3_client = boto3.client(
                    's3',
                    aws_access_key_id=self.credentials["access_key_id"],
                    aws_secret_access_key=self.credentials["secret_access_key"],
                    region_name=self.credentials["region"]
                )
                Console.ok(f"Successful connection to {self.kind} is made.")
            except ClientError as e:
                Console.error(e, prefix=True, traceflag=True)

        elif self.kind == "azureblob":
            print("Create Azure connection.")
            raise NotImplementedError
            return {}

        elif self.kind == "local":
            print("Accessing local storage location.")
            if kwargs.get('targetObj'):
                self.local_location = Path(self.yaml_content['default'][
                                               'directory'],
                                           kwargs.get('targetObj'))
            else:
                self.local_location = self.yaml_content['default'][
                    'directory']

            if kwargs.get("debug"):
                print(f"\nLocal location to access {self.local_location}")

        else:
            raise NotImplementedError
            return {}

    def list(self, service=None, target=None, recursive=False):
        """
        Method to enlist all objects of target location.

        :param service: local/aws/azure
        :param target: target directory or file
        :param recursive: Boolean to indicate if sub components to be enlisted
        :return: list of lists containing objects from target location
        """
        if self.kind == "awss3":
            pass
        elif self.kind == "azureblob":
            pass
        elif self.kind == "local":
            pass
        else:
            raise NotImplementedError
            return {}

def main():
    print("Instantiating")
    instance = Provider(service="local", sourceObj="abcd.txt", target="aws",
                        targetObj=None, debug=True)

    instance.list(service="local", target=None)

if __name__ == "__main__":
    main()
