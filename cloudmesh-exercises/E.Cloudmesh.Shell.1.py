# fa19-516-155 E.Cloudmesh.Shell.1
"""
Usage: E.Cloudmesh.Shell.1.py [-h]

Function to check if cmd5 and cms are installed successfully

Arguments:
   None

Options:
-h --help
"""

from cloudmesh.common.Shell import Shell
from cloudmesh.common.util import banner


class DemoCms:

    @staticmethod
    def checkcms():
        banner("Using CM Shell to confirm installation of cmd5 and cms:")
        result = Shell.command_exists('cms')
        print(result)


if __name__ == "__main__":
    demo = DemoCms()
    demo.checkcms()
