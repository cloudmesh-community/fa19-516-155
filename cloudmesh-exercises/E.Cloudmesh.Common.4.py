# fa19-516-155 E.Cloudmesh.Common.4
"""
Usage: E.Cloudmesh.Common.4.py [-h]

Function to demonstrate cloudmesh's Shell utility

Arguments:
   None

Options:
-h --help
"""

from cloudmesh.common.Shell import Shell
from cloudmesh.common.util import banner


class checkShell:
    def getcwd(self):
        dir = Shell.execute('pwd')
        print(f"Current directory is : {dir}")

    def getfilelist(self):
        files = Shell.ls("-lrt")
        print(f"List of files, from oldest to newest :\n{files}")

if __name__ == "__main__":
    demo = checkShell()
    banner("Getting current directory:")
    demo.getcwd()
    banner("Getting the file list:")
    demo.getfilelist()
