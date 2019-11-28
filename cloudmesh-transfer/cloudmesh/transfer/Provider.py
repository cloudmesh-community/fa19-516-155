from cloudmesh.transfer.provider.awss3.Provider import Provider as AwsProvider
from cloudmesh.transfer.provider.azureblob.Provider import \
    Provider as AzureblobProvider
from cloudmesh.transfer.provider.local.Provider import Provider as LocalProvider
from cloudmesh.storage.StorageNewABC import StorageABC
from cloudmesh.mongo.DataBaseDecorator import DatabaseUpdate
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.util import banner
from cloudmesh.common.console import Console
from pprint import pprint


class Provider(StorageABC):

    def __init__(self, source=None, source_obj=None, target=None,
                 target_obj=None, config="~/.cloudmesh/cloudmesh.yaml"):

        # Reading .yaml for source CSP
        if source:
            super(Provider, self).__init__(service=source, config=config)

            self.source_kind = self.kind
            self.source_credentials = self.credentials

            print(f"Initializing source {self.source_kind} provider.")
            self.source_provider = self.init_provider(kind=self.source_kind,
                                                      source=source,
                                                      source_obj=source_obj,
                                                      target=target,
                                                      target_obj=target_obj)
        else:
            self.source_kind = None
            self.source_credentials = None

        # Reading .yaml for target CSP
        if target:
            super(Provider, self).__init__(service=target, config=config)

            self.target_kind = self.kind
            self.target_credentials = self.credentials

            print(f"Initializing target {self.source_kind} provider.")
            self.target_provider = self.init_provider(kind=self.target_kind,
                                                      source=source,
                                                      source_obj=source_obj,
                                                      target=target,
                                                      target_obj=target_obj)
        else:
            self.target_kind = None
            self.target_credentials = None

        banner(f"""In TRANSFER provider
        source csp = {self.source_kind}, source object = {source_obj}
        target csp = {self.target_kind}, target object = {target_obj}""")

    @staticmethod
    def init_provider(kind=None, source=None, source_obj=None,
                      target=None, target_obj=None):
        if kind == "local":
            return LocalProvider(source=source, source_obj=source_obj,
                                 target=target, target_obj=target_obj)
        elif kind == "awss3":
            return AwsProvider(source=source, source_obj=source_obj,
                               target=target, target_obj=target_obj)
        elif kind == "azureblob":
            return AzureblobProvider(source=source, source_obj=source_obj,
                                     target=target, target_obj=target_obj)
        else:
            Console.error(f"Transfer Local provider: CSP {kind} not yet "
                          f"implemented.")
            raise NotImplementedError

    #    @DatabaseUpdate()
    def list(self, source=None, source_obj=None,
                   target=None, target_obj=None, recursive=True):
        # VERBOSE(locals())
        print("MASTER provider LIST ====>\n", source, type(source))

        result = self.target_provider.list(source=source,
                                           source_obj=source_obj,
                                           target=target,
                                           target_obj=target_obj,
                                           recursive=True)
        return result

    def delete(self, source=None, source_obj=None,
                   target=None, target_obj=None, recursive=True):
        print("\nMASTER provider DELETE ====>\n", source, target)

        result = self.target_provider.delete(source=source,
                                             source_obj=source_obj,
                                             target=target,
                                             target_obj=target_obj,
                                             recursive=True)
        return result

    def copy(self, source=None, source_obj=None,
                   target=None, target_obj=None, recursive=True):
        print(f"\nMASTER provider COPY from {source} to {target}")

        if target == "local":
            print(f"Target is local hence redirected to {source} provider.")
            result = self.source_provider.copy(source=source,
                                               source_obj=source_obj,
                                               target=target,
                                               target_obj=target_obj,
                                               recursive=True)
        elif source == "local":
            print(f"Source is local hence redirected to {target} provider.")
            result = self.target_provider.copy(source=source,
                                               source_obj=source_obj,
                                               target=target,
                                               target_obj=target_obj,
                                               recursive=True)
        else:
            # For S3-blob and blob-S3 copy, connecting to target provider
            result = self.target_provider.copy(source=source,
                                               source_obj=source_obj,
                                               target=target,
                                               target_obj=target_obj,
                                               recursive=True)

        return result

