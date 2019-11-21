from cloudmesh.common.Shell import Shell
from pprint import pprint


print("Starting debug")
result=Shell.execute("cms",["storage","--storage=local", "list","a"])

pprint(result)