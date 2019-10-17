"""
Script performs following tasks:
[X] Enlist all available virtual machine image lists
[ ] Enlist all available flavors of VM
[ ] Enlist all virtual machines

Supported cloud service providers:
[X] AWS
[ ] Azure
"""
import oyaml as yaml
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.console import Console
from cloudmesh.common.util import banner
from cloudmesh.common.Printer import Printer
from cloudmesh.configuration.Config import Config
from cloudmesh.common.util import path_expand
from pprint import pprint
import boto3

class cloudDetails:
    def __init__(self, cloudname='aws', configuration="~/.cloudmesh/cloudmesh.yaml"):
        self.cloudname = cloudname
        self.configuration = configuration
        self.yaml_content = Config(configuration)
        #pprint(yaml_content)
        self.kind = self.yaml_content[f"cloudmesh.cloud.{self.cloudname}.cm.kind"]
        banner(f"Working on {self.kind} cloud service.")
        
    def enlistImages(self):
        banner(f"Fetching image list for {self.cloudname} cloud service.")
        if self.cloudname == "aws":
            #VERBOSE(self.yaml_content[f"cloudmesh.cloud.{self.cloudname}"])
            ACCESS_KEY = self.yaml_content[f"cloudmesh.cloud.{self.cloudname}.credentials.EC2_ACCESS_ID"]
            SECRET_KEY = self.yaml_content[f"cloudmesh.cloud.{self.cloudname}.credentials.EC2_SECRET_KEY"]
            REGION_ID  = self.yaml_content[f"cloudmesh.cloud.{self.cloudname}.credentials.region"]
            
            if ACCESS_KEY == 'TBD' or SECRET_KEY == 'TBD' or REGION_ID == 'TBD':
                Console.error("Critical details missing from .yaml file. TBD not allowed. Please check.")
            
            try:
                ec2_instance = boto3.client(
                    'ec2',
                    aws_access_key_id=ACCESS_KEY,
                    aws_secret_access_key=SECRET_KEY,
                    region_name=REGION_ID
                    )
                
                #ec2_instance = boto3.client('ec2')
                
                #vm_instance_list = ec2_instance.describe_instances()
                
                StopWatch.start(f"Image list {self.cloudname}.")
                
                image_list = ec2_instance.describe_images()
                
                print("\nLength = " , len(image_list['Images']), "\n", type(image_list))
                #opList = [[i.get('ImageId'), i.get('ImageType'), i.get('Description'), i.get('Name'), i.get('State'), i.get('Public'), i.get('Platform'),i.get('CreationDate')] for i in image_list['Images']]
                opList = [{'ImageId':i.get('ImageId'), 'ImageType': i.get('ImageType'), 'Description': i.get('Description'), 'Name': i.get('Name'), 'State':i.get('State'),'Public': i.get('Public'),'CreationDate':i.get('CreationDate')} for i in image_list['Images']]
                
                StopWatch.stop(f"Image list {self.cloudname}.")
                t = format(StopWatch.get(f"Image list {self.cloudname}."), '.2f')
                
                banner(f"Image list fetched for {self.cloudname} cloud service.\nTotal {len(opList)} images fetched. Time taken {t} \nPrinting first 5 sample images:") 
                print(Printer.write(opList[:6], output='table'))
                
            
            except Exception as e:
                Console.error(f"Image list of {self.cloudname} can\'t be fetched. Error:\n{e}")
        else:
            Console.error(f"Provider {self.cloudname} not supported")
            raise ValueError(f"provider {self.cloudname} not supported")
                
def main():
    instance = cloudDetails(cloudname='aws')
    instance.enlistImages()
    
if __name__ == "__main__":
    main()