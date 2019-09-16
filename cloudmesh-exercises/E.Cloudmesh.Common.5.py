# fa19-516-155 E.Cloudmesh.Common.5
"""
Usage: E.Cloudmesh.Common.5.py [-h]

Function to demonstrate cloudmesh's StopWatch utility

Arguments:
   None

Options:
-h --help
"""

from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.util import banner
import time

class Common5:

    @staticmethod
    def getfibonacci():
        banner("Fetching 100th number of the Fibonacci series")
        StopWatch.start("Fibo")
        a, b = 0, 1
        for i in range(100):
            # print(a)
            a, b = a + b, a
        print(b)
        StopWatch.stop("Fibo")
        print(StopWatch.get("Fibo",5))
        # print(StopWatch.benchmark())


if __name__ == "__main__":
    demo = Common5()
    demo.getfibonacci()
