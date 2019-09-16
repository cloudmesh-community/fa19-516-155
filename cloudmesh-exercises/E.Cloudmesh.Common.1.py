# fa19-516-155 E.Cloudmesh.Common.1
"""
Usage: E.Cloudmesh.Common.1.py [-h]

Function to convert input list to a dictionary and to demonstrate usage of cloudmesh utilities banner, HEADING, VERBOSE

Arguments:
  ipList    input list to convert to a dictionary.

Options:
-h --help
"""
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.util import HEADING
from cloudmesh.common.util import banner
from cloudmesh.common.console import Console


def toDict(ipList):
    HEADING()
    opDict = dict()
    if len(ipList) == 0:
        Console.error("Empty list provided. Please check.")
        return
    for idx, value in enumerate(ipList):
        opDict[idx] = value
    VERBOSE(opDict)
    return opDict


if __name__ == '__main__':
    ipList = ['a','b','c','d','e']
    banner("Using default list")
    toDict(ipList)
