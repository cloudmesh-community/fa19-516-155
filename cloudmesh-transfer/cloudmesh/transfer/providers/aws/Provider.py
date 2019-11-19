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

    """
    def __init__(self, service=None, config="~/.cloudmesh/cloudmesh.yaml",
                 **kwargs):
        super().__init__(service=service, config=config)
