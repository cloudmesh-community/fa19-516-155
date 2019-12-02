###############################################################
# pytest -v --capture=no tests/test_transfer_awss3.py
# pytest -v tests/test_transfer_awss3.py
# pytest -v --capture=no tests/test_transfer_awss3.py:TestTransferS3Local.<METHIDNAME>
###############################################################
import os
from pathlib import Path
from pprint import pprint

import pytest
from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.parameter import Parameter
from cloudmesh.common.util import HEADING
from cloudmesh.common.util import banner
from cloudmesh.common.util import path_expand
from cloudmesh.common.util import writefile
from cloudmesh.common.variables import Variables
from cloudmesh.storage.Provider import Provider
from cloudmesh.transfer.provider.awss3.Provider import Provider as AwsProvider
from cloudmesh.transfer.provider.azureblob.Provider import \
    Provider as AzureblobProvider
from cloudmesh.transfer.provider.local.Provider import Provider as LocalProvider
from cloudmesh.transfer.Provider import Provider
from cloudmesh.configuration.Config import Config

from pprint import pprint

# cms set storage=awss3

@pytest.mark.incremental
class TestTransferS3Local:

    def setup(self):
        config = Config(config_path="~/.cloudmesh/cloudmesh.yaml")
        spec = config["cloudmesh.storage"]
        local_target = spec["local"]["default"]["directory"]
        # print("=============> ", local_target)
        # print("=============> ", str(Path(local_target)))

        self.file_name = "test_transfer_local_s3.txt"
        self.azure_file_name = "test_transfer_local_azure.txt"

        # Create a dummy file in local storage at local_target
        self.location = f"{local_target}/{self.file_name}"
        writefile(path_expand(self.location), content="Test file.")

        self.location_azure = f"{local_target}/{self.azure_file_name}"
        writefile(path_expand(self.location_azure), content="Test file.")

    def test_local_list(self):
        HEADING()
        target_CSP = "local"
        target_obj = self.location

        StopWatch.start("List local for awss3 provider")
        provider = Provider(source=None, source_obj=None,
                            target=target_CSP, target_obj=target_obj)

        result = provider.list(source=None, source_obj=None,
                               target=target_CSP, target_obj=target_obj,
                               recursive=True)

        StopWatch.stop("List local for awss3 provider")
        assert self.file_name in result[0]['name']

    def test_transfer_local_s3(self):
        HEADING()
        source_CSP = "local"
        target_CSP = "awss3"
        source_obj = str(Path(self.location))
        target_obj = "\\"

        StopWatch.start("Transfer local to awss3")

        provider = Provider(source=source_CSP, source_obj=source_obj,
                            target=target_CSP, target_obj=target_obj)

        result = provider.copy(source=source_CSP, source_obj=source_obj,
                               target=target_CSP, target_obj=target_obj,
                               recursive=True)
        StopWatch.stop("Transfer local to awss3")

        pprint(result)
        assert result is not None

    def test_list_s3(self):
        HEADING()
        target_CSP = "awss3"
        target_obj = str(Path("\\") / self.file_name)
        # print("===========> ", target_obj)

        StopWatch.start("List s3 for awss3 provider")
        provider = Provider(source=None, source_obj=None,
                            target=target_CSP, target_obj=target_obj)

        result = provider.list(source=None, source_obj=None,
                               target=target_CSP, target_obj=target_obj,
                               recursive=True)

        StopWatch.stop("List s3 for awss3 provider")
        assert self.file_name in result[0]['name']

    def test_transfer_s3_to_local(self):
        HEADING()
        source_CSP = "awss3"
        target_CSP = "local"
        source_obj = str(Path("\\") / self.file_name)
        target_obj = str(Path(self.location))

        StopWatch.start("Transfer awss3 to local")

        provider = Provider(source=source_CSP, source_obj=source_obj,
                            target=target_CSP, target_obj=target_obj)

        result = provider.copy(source=source_CSP, source_obj=source_obj,
                               target=target_CSP, target_obj=target_obj,
                               recursive=True)
        StopWatch.stop("Transfer awss3 to local")

        pprint(result)
        assert result is not None

    def test_transfer_s3_to_azure(self):
        HEADING()
        source_CSP = "awss3"
        target_CSP = "azure"
        source_obj = str(self.file_name)
        target_obj = str(Path("\\"))
        stopwatch_tag = "Transfer awss3 to azure"

        print("=======> ", source_obj)
        print("=======> ", target_obj)

        StopWatch.start(stopwatch_tag)

        provider = Provider(source=source_CSP, source_obj=source_obj,
                            target=target_CSP, target_obj=target_obj)

        result = provider.copy(source=source_CSP, source_obj=source_obj,
                               target=target_CSP, target_obj=target_obj,
                               recursive=True)
        StopWatch.stop(stopwatch_tag )

        pprint(result)
        assert result is not None

    def test_transfer_local_to_azure(self):
        HEADING()
        source_CSP = "local"
        target_CSP = "azure"
        source_obj = str(Path(self.location_azure))
        target_obj = "\\"
        stopwatch_tag = "Transfer local to azure."

        StopWatch.start(stopwatch_tag)

        provider = Provider(source=source_CSP, source_obj=source_obj,
                            target=target_CSP, target_obj=target_obj)

        result = provider.copy(source=source_CSP, source_obj=source_obj,
                               target=target_CSP, target_obj=target_obj,
                               recursive=True)
        StopWatch.stop(stopwatch_tag)

        pprint(result)
        assert result is not None

    def test_list_azure(self):
        HEADING()
        target_CSP = "azure"
        target_obj = str(Path("\\") / self.azure_file_name)
        stopwatch_tag = "List azure."
        # print("===========> ", target_obj)

        StopWatch.start(stopwatch_tag)
        provider = Provider(source=None, source_obj=None,
                            target=target_CSP, target_obj=target_obj)

        result = provider.list(source=None, source_obj=None,
                               target=target_CSP, target_obj=target_obj,
                               recursive=True)

        StopWatch.stop(stopwatch_tag)
        assert self.azure_file_name in result[0]['name']

    def test_transfer_azure_to_local(self):
        HEADING()
        source_CSP = "azure"
        target_CSP = "local"
        source_obj = str(Path("\\") / self.azure_file_name)
        target_obj = str(Path(self.location_azure))
        stopwatch_tag = "Transfer azure to local."

        StopWatch.start(stopwatch_tag)

        provider = Provider(source=source_CSP, source_obj=source_obj,
                            target=target_CSP, target_obj=target_obj)

        result = provider.copy(source=source_CSP, source_obj=source_obj,
                               target=target_CSP, target_obj=target_obj,
                               recursive=False)
        StopWatch.stop(stopwatch_tag)

        pprint(result)
        assert result is not None

    def test_transfer_azure_to_s3(self):
        HEADING()
        source_CSP = "azure"
        target_CSP = "awss3"
        source_obj = str(Path("\\") / self.azure_file_name)
        target_obj = str(Path("\\"))
        stopwatch_tag = "Transfer azure to local."

        StopWatch.start(stopwatch_tag)

        provider = Provider(source=source_CSP, source_obj=source_obj,
                            target=target_CSP, target_obj=target_obj)

        result = provider.copy(source=source_CSP, source_obj=source_obj,
                               target=target_CSP, target_obj=target_obj,
                               recursive=False)
        StopWatch.stop(stopwatch_tag)

        pprint(result)
        assert result is not None

    def test_delete_s3(self):
        HEADING()
        target_CSP = "awss3"
        target_obj = str(Path("\\") / self.file_name)
        stopwatch_tag = "Delete s3"
        # print("===========> ", target_obj)

        StopWatch.start(stopwatch_tag)
        provider = Provider(source=None, source_obj=None,
                            target=target_CSP, target_obj=target_obj)

        result = provider.delete(source=None, source_obj=None,
                                 target=target_CSP, target_obj=target_obj,
                                 recursive=True)

        StopWatch.stop(stopwatch_tag)
        assert self.file_name in result[0]['name']

    def test_delete_local(self):
        HEADING()
        target_CSP = "local"
        target_obj = self.file_name
        stopwatch_tag = "Delete local"
        # print("===========> ", target_obj)

        StopWatch.start(stopwatch_tag)
        provider = Provider(source=None, source_obj=None,
                            target=target_CSP, target_obj=target_obj)

        result = provider.delete(source=None, source_obj=None,
                                 target=target_CSP, target_obj=target_obj,
                                 recursive=True)

        StopWatch.stop(stopwatch_tag)
        assert self.file_name in result[0]['name']

    def test_delete_azure(self):
        HEADING()
        target_CSP = "azure"
        target_obj = str(Path("\\") / self.azure_file_name)
        stopwatch_tag = "Delete azure"
        # print("===========> ", target_obj)

        StopWatch.start(stopwatch_tag)
        provider = Provider(source=None, source_obj=None,
                            target=target_CSP, target_obj=target_obj)

        result = provider.delete(source=None, source_obj=None,
                                 target=target_CSP, target_obj=target_obj,
                                 recursive=True)

        StopWatch.stop(stopwatch_tag)
        assert self.azure_file_name in result[0]['name']

    def test_results(self):
        HEADING()
        # storage = self.p.service
        service = "TRANSFER"
        banner(f"Benchmark results for {service} service")
        StopWatch.benchmark(csv=False)
