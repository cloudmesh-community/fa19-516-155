import boto3
from botocore.exceptions import ClientError
from cloudmesh.storage.StorageNewABC import StorageABC
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.console import Console
from cloudmesh.common.util import banner
from cloudmesh.configuration.Config import Config

from pathlib import Path
from glob import glob
import os, shutil, queue

from azure.storage.blob import BlockBlobService


class Provider(StorageABC):
    """
    Provider class for AWS storage.
    This class allows transfer of objects from AWS S3 bucket to Azure blob
    storage container.

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
        # This is a provider class for aws storage hence --source/service will
        # always be "aws"

        self.sourceCSP = self.service

        try:
            self.config = Config()
            self.yaml_content_source = self.config["cloudmesh.storage."
                                                   f"{self.sourceCSP}"]
            self.source_kind = self.yaml_content_source["cm"]["kind"]
            self.source_credentials = self.yaml_content_source["credentials"]

            self.container = self.source_credentials["container"]

            print("Accessing AWS S3 details:\n")

            if 'TBD' == self.source_credentials["access_key_id"] \
                    or 'TBD' == self.source_credentials["secret_access_key"] \
                    or 'TBD' == self.source_credentials["region"]:
                Console.error("Critical details missing from .yaml file. "
                              "TBD  not allowed. Please check.")

            try:
                self.s3_client = boto3.client(
                    's3',
                    aws_access_key_id=self.source_credentials[
                        "access_key_id"],
                    aws_secret_access_key=self.source_credentials[
                        "secret_access_key"],
                    region_name=self.source_credentials["region"]
                )
                Console.ok(
                    f"Successful connection to {self.kind} is "
                    f"made.")
            except ClientError as e:
                Console.error(e, prefix=True, traceflag=True)

            if kwargs.get('sourceObj'):
                self.local_location = Path(self.yaml_content_source['default'][
                                               'directory'],
                                           kwargs.get('sourceObj'))
            else:
                self.local_location = self.yaml_content_source['default'][
                    'directory']

            if kwargs.get("debug"):
                print(f"\nLocal location to access {self.local_location}")

            if kwargs.get('target'):
                self.targetCSP = kwargs.get('target')
                self.yaml_content_target = self.config["cloudmesh.storage."
                                                       f"{self.targetCSP}"]
                self.target_kind = self.yaml_content_target["cm"]["kind"]
                self.target_credentials = self.yaml_content_target[
                    "credentials"]

                # Taking the default directory as the target container for
                # local storage
                if self.target_kind == "local":
                    self.target_container = self.yaml_content_target[
                        'default']['directory']
                else:
                    self.target_container = self.target_credentials["container"]

                banner("self.target_container: ", self.target_container)
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
            if self.target_kind == "local":
                print("Local storage connected.")

                # if 'TBD' == self.target_credentials["access_key_id"] \
                #         or 'TBD' == self.target_credentials["secret_access_key"] \
                #         or 'TBD' == self.target_credentials["region"]:
                #     Console.error("Critical details missing from .yaml file. "
                #                   "TBD  not allowed. Please check.")
                #
                # try:
                #     self.s3_client = boto3.client(
                #         's3',
                #         aws_access_key_id=self.target_credentials[
                #             "access_key_id"],
                #         aws_secret_access_key=self.target_credentials[
                #             "secret_access_key"],
                #         region_name=self.target_credentials["region"]
                #     )
                #     Console.ok(
                #         f"Successful connection to {self.target_kind} is "
                #         f"made.")
                # except ClientError as e:
                #     Console.error(e, prefix=True, traceflag=True)

            elif self.target_kind == "azureblob":
                banner("Connecting to Azure Blob Storage.")

                self.azure_acct_name = self.target_credentials['account_name']
                self.azure_acct_key = self.target_credentials['account_key']
                self.target_container = self.target_credentials['container']

                try:
                    self.blob_service = BlockBlobService(self.azure_acct_name,
                                                         self.azure_acct_key)

                    print("Successfully connected to Azure Blob storage.")
                except Exception as e:
                    print("Connection to Azure failed:", e)

            else:
                raise NotImplementedError

    def list(self, service='aws', sourceObj=None, recursive=True):
        """
        Method to enlist all objects of source location.

        :param service: local/aws/azure
        :param sourceObj: source directory or file
        :param recursive: Boolean to indicate if sub components to be enlisted
        :return: list of lists containing objects from target location
        """
        if self.source_kind == "awss3":
            banner(f"Executing list method for aws s3 storage:\nSource object "
                   f"is {self.local_location}")

            print(
                self.s3_client.list_objects(Bucket=self.container)['Contents'])
            print(type(
                self.s3_client.list_objects(Bucket=self.container)['Contents']))

            for key in self.s3_client.list_objects(Bucket=self.container)[
                'Contents']:
                print(key['Key'])

        elif self.source_kind == "azureblob":
            Console.error("This command should flow to AWS provider. Please "
                          "check.")
            return
        elif self.source_kind == "local":

            Console.error("This command should flow to local provider. Please "
                          "check.")
            return
        else:
            raise NotImplementedError
            return

    def delete(self, service="aws", sourceObj=None, recursive=False):
        """
        This method deletes file(s) / folder(s) from the source location.

        :param service: "aws" for this provider
        :param sourceObj: A file or folder to delete
        :param recursive: Delete files from folder/subfolders
        :return: None
        """
        # TODO: delete folders and/or multiple files
        # https://www.edureka.co/community/31907/how-to-delete-a-folder-in-s3-bucket-using-boto3-using-python
        # https://docs.aws.amazon.com/code-samples/latest/catalog/python-s3-delete_objects.py.html

        if self.source_kind == "awss3":
            banner(f"Executing delete method for aws s3 storage:\nSource "
                   f"object is {self.local_location}")

            try:
                resp = self.s3_client.delete_object(Bucket=self.container,
                                                    Key=sourceObj)

                print(resp)
            except ClientError as e:
                Console.error("Object could not be deleted from S3 bucket.")

        elif self.source_kind == "azureblob":
            Console.error("This command should flow to azure provider. Please "
                          "check.")
            return
        elif self.source_kind == "local":
            Console.error("This command should flow to local provider. Please "
                          "check.")
        else:
            raise NotImplementedError
            return {}

    def copy(self, service="aws", sourceObj="abcd.txt", target="local",
             targetObj=None, debug=True):
        """
        copy method copies files/directories from local storage to target CSP

        :param service:  "aws" for this provider
        :param sourceObj: A file/directory to be copied
        :param targetObj: Name of the target object
        :param debug: Boolean indicating debug mode
        :return: None
        """
        # To copy the whole cmStorage directory, pls provide sourceObj=None

        # Validating if target S3 bucket/blob container exists
        if self.target_kind == 'local':
            if Path(self.target_container).expanduser().is_dir():
                Console.ok(f"local storage {self.target_container} exists.")
            else:
                Console.error(f"AWS local storage {self.target_container} does "
                              f"not exist.")
                return
        elif self.target_kind == 'azureblob':
            if self.blob_service.exists(self.target_container):
                Console.ok(f"Azure blob container {self.target_container} "
                           f"exists")
            else:
                Console.error(f"Azure blob container {self.target_container} "
                              f"does not exist.")
                return
        else:
            raise NotImplementedError

            # TODO : Check CLI option
            # CLI option
            # aws s3 cp C:\Users\kpimp\cmStorage
            # s3://bucket-iris.json/cmStorage --recursive

        # TODO: Check if source file/dir exists in S3 bucket
        # Deciding the source location of file/directory to be copied
        # if sourceObj:
        #     self.local_location = Path(self.yaml_content_source['default'][
        #                                    'directory'], sourceObj)
        #     print("=====> local location ", self.local_location)
        # else:
        #     sourceObj = "cmStorage"
        #     self.local_location = self.yaml_content_source['default'][
        #         'directory']

        if targetObj is None:
            targetObj = sourceObj

        source_path = Path(self.local_location)
        object_queue = queue.Queue()

        # Creating a queue with all the objects to be copied to local
        # TODO: implement queue
        if self.target_kind == "local":
            # constructing targetObj as a string of absolute path of target
            # location
            targetObj = str(Path(self.target_container).expanduser().joinpath(
                targetObj))
            try:
                s3_resource = boto3.resource('s3')
                print(self.container, sourceObj, targetObj)
                s3_resource.meta.client.download_file(self.container, sourceObj,
                                                      targetObj)
                Console.ok("Downloaded file: ", sourceObj)
            except Exception as e:
                print(e)
        elif self.target_kind == "azureblob":
            raise NotImplementedError

        # Reading queue and uploading objects to S3/Blob
        # while object_queue.qsize() > 0:
        #     try:
        #         obj = object_queue.get(block=False, timeout=5)
        #
        #         if self.target_kind == 'awss3':
        #
        #             try:
        #                 response = self.s3_client.upload_file(obj,
        #                                                       self.target_container,
        #                                                       targetObj)
        #                 Console.ok(f"Uploaded {obj} to S3 bucket.")
        #             except ClientError as e:
        #                 Console.error(f"{obj} could not be uploaded to S3 "
        #                               f"bucket.")
        #
        #         elif self.target_kind == 'azureblob':
        #
        #             try:
        #                 response = self.blob_service.create_blob_from_path(
        #                     self.target_container,
        #                     targetObj,
        #                     obj)
        #             except Exception as e:
        #                 Console.error(f"{obj} could not be uploaded to the "
        #                               f"blob.")
        #         else:
        #             Console.error("Tried uploading objects to: ",
        #                           self.target_kind)
        #             raise NotImplementedError
        #     except queue.Empty:
        #         Console.ok(f"All objects uploaded to {self.container} of "
        #                    f"{self.target_kind}")
        #         break


def main():
    # Instantiating for list/delete command
    # instance = Provider(service="aws", sourceObj="a",
    #                    targetObj=None, debug=True)

    # instance.list(service="aws", sourceObj=None, recursive=True)

    # instance.delete(service="local", sourceObj="abcd.txt", recursive=True)

    # following instantiating for copy command
    instance = Provider(service="aws", sourceObj="abcd.txt", target="local",
                        targetObj=None, debug=True)

    instance.copy(service="aws", sourceObj='abcd.txt', target="local",
                  targetObj=None, debug=True)


if __name__ == "__main__":
    main()
