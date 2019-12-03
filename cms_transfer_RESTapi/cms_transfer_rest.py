import os, platform, subprocess, re
from flask import jsonify
from cloudmesh.transfer.Provider import Provider
from cloudmesh.configuration.Config import Config


def setup():
    config = Config(config_path="~/.cloudmesh/cloudmesh.yaml")
    spec = config["cloudmesh.storage"]
    global local_target
    local_target = spec["local"]["default"]["directory"]


def list():
    setup()
    target_CSP = "local"
    target_obj = local_target

    provider = Provider(source=None, source_obj=None,
                        target=target_CSP, target_obj=target_obj)

    result = provider.list(source=None, source_obj=None,
                           target=target_CSP, target_obj=target_obj,
                           recursive=True)
    return result
