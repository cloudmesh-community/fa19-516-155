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

            print(f"Initializing {self.source_kind} provider.")
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

            print(f"Initializing {self.source_kind} provider.")
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
    #    def get(self, source=None, destination=None, recursive=False):
    #        """
    #        gets the content of the source on the server to the local destination
    #
    #        :param source: the source file on the server
    #        :type source: string
    #        :param destination: the destination location ion teh local machine
    #        :type destination: string
    #        :param recursive: True if the source is a directory and ned to be copied recursively
    #        :type recursive: boolean
    #        :return: cloudmesh cm dict
    #        :rtype: dict
    #        """
    #
    #        VERBOSE(f"get {source} {destination} {recursive}")
    #        d = self.provider.get(source=source, destination=destination, recursive=recursive)
    #        return d
    #
    #    @DatabaseUpdate()
    #    def put(self, source=None, destination=None, recursive=False):
    #
    #        service = self.service
    #        VERBOSE(f"put {service} {source} {destination}")
    #        d = self.provider.put(source=source, destination=destination, recursive=recursive)
    #        return d
    #
    #    @DatabaseUpdate()
    #    def createdir(self, directory=None):
    #
    #        # BUG DOES NOT FOLLOW SPEC
    #        VERBOSE(f"create_dir {directory}")
    #        VERBOSE(directory)
    #        service = self.service
    #        d = self.provider.create_dir(service=service, directory=directory)
    #        return d
    #
    #    @DatabaseUpdate()
    #    def delete(self, source=None):
    #        """
    #        deletes the source
    #
    #        :param source: The source
    #        :return: The dict representing the source
    #        """
    #
    #        service = self.service
    #        VERBOSE(f"delete filename {service} {source}")
    #        d = self.provider.delete(service=service, source=source)
    #        # raise ValueError("must return a value")
    #        return d
    #
    #    def search(self, directory=None, filename=None, recursive=False):
    #
    #        # BUG DOES NOT FOLLOW SPEC
    #        VERBOSE(f"search {directory}")
    #        d = self.provider.search(directory=directory, filename=filename, recursive=recursive)
    #        return d
    #
    #    @DatabaseUpdate()
    def list(self, source=None, dir_only=False, recursive=False):
        #
        #        # BUG DOES NOT FOLLOW SPEC
        VERBOSE(f"list {source}")
        VERBOSE(locals())
        # print("storage-provider ====>\n", source, type(source))
##
#        # TODO : Changed following code #KP
#        # d = self.provider.list(source=source, dir_only=dir_only, recursive=recursive)
#
#        d = self.provider.list(source=source[0], recursive=recursive)
#
#        print("||||| IN master provider |||| \n", d)
#        return d
#
#    def tree(self, source):
#
#        data = self.provider.list(source=source)
#
#        # def dict_to_tree(t, s):
#        #    if not isinstance(t, dict) and not isinstance(t, list):
#        #       print ("    " * s + str(t))
#        #    else:
#        #        for key in t:
#        #            print ("    " * s + str(key))
#        #            if not isinstance(t, list):
#        #                dict_to_tree(t[key], s + 1)
#        #
#        # dict_to_tree(d, 0)
#
#        pprint(data)
#
