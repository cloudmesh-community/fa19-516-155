# fa19-516-155 E.Cloudmesh.Common.2

"""
Usage: E.Cloudmesh.Common.2.py [-h]

Function to demonstrate usage of cloudmesh utility dotdict

Arguments:
  ipDict    input dict to check dotdict.

Options:
-h --help
"""

from cloudmesh.common.dotdict import dotdict


if __name__ == "__main__":
    ipDict = {'first': 'a', 'second': 'b', 'third': 'c', 'fourth': 'd', 'fifth': 'e'}
    dotDict = dotdict(ipDict)
    print(dotDict.first == ipDict['first'])
    print(dotDict.third == ipDict['third'])
    print(dotDict.fifth is ipDict['fifth'])
