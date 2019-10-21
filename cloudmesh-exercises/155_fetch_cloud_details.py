"""
Script performs following tasks:
[X] Enlist all available virtual machine image lists
[ ] Enlist all available flavors of VM
[X] Enlist all virtual machines

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
import json

class cloudDetails:
    def __init__(self, cloudname='aws', configuration="~/.cloudmesh/cloudmesh.yaml"):
        self.cloudname = cloudname
        self.configuration = configuration
        self.yaml_content = Config(configuration)
        #pprint(yaml_content)
        self.kind = self.yaml_content[f"cloudmesh.cloud.{self.cloudname}.cm.kind"]
        banner(f"Working on {self.kind} cloud service.")
        if self.cloudname == "aws":
            #VERBOSE(self.yaml_content[f"cloudmesh.cloud.{self.cloudname}"])
            self.ACCESS_KEY = self.yaml_content[f"cloudmesh.cloud.{self.cloudname}.credentials.EC2_ACCESS_ID"]
            self.SECRET_KEY = self.yaml_content[f"cloudmesh.cloud.{self.cloudname}.credentials.EC2_SECRET_KEY"]
            self.REGION_ID  = self.yaml_content[f"cloudmesh.cloud.{self.cloudname}.credentials.region"]
            
            if self.ACCESS_KEY == 'TBD' or self.SECRET_KEY == 'TBD' or self.REGION_ID == 'TBD':
                Console.error("Critical details missing from .yaml file. TBD not allowed. Please check.")
        else:
            Console.error(f"\nProvider {self.cloudname} not supported")
            raise ValueError(f"Provider {self.cloudname} not supported")
        
    def enlistImages(self):
        banner(f"Fetching image list for {self.cloudname} cloud service.")
        if self.cloudname == "aws":
            
            try:
                ec2_instance = boto3.client(
                    'ec2',
                    aws_access_key_id=self.ACCESS_KEY,
                    aws_secret_access_key=self.SECRET_KEY,
                    region_name=self.REGION_ID
                    )
                
                StopWatch.start(f"Image list {self.cloudname}.")
                
                image_list = ec2_instance.describe_images()
                opDict= []
                opDict = [{'ImageId':i.get('ImageId'), 'ImageType': i.get('ImageType'), 'Description': i.get('Description'), 'Name': i.get('Name'), 'State':i.get('State'),'Public': i.get('Public'),'CreationDate':i.get('CreationDate')} for i in image_list['Images']]
                
                StopWatch.stop(f"Image list {self.cloudname}.")
                t = format(StopWatch.get(f"Image list {self.cloudname}."), '.2f')
                
                banner(f"Image list fetched for {self.cloudname} cloud service.\nTotal {len(opDict)} images fetched. Time taken {t} \nPrinting first 5 sample images:") 
                print(Printer.write(opDict[:6], output='table'))
                
                #Saving complete list to a file
                opFile = f"{self.cloudname}_Image_list.txt"
                with open(opFile,'w') as fo:
                    print(Printer.write(opDict, output='table'), file=fo)
                    
            except Exception as e:
                Console.error(f"Image list of {self.cloudname} can\'t be fetched. Error:\n{e}")
        else:
            Console.error(f"Provider {self.cloudname} not supported")
            raise ValueError(f"provider {self.cloudname} not supported")
                
    def enlistInstances(self):
        print("\n")
        banner(f"Fetching instance list for {self.cloudname} cloud service.")
        if self.cloudname == "aws":
            
            try:
                ec2_instance = boto3.client(
                    'ec2',
                    aws_access_key_id=self.ACCESS_KEY,
                    aws_secret_access_key=self.SECRET_KEY,
                    region_name=self.REGION_ID
                    )
                
                StopWatch.start(f"Instance list {self.cloudname}.")
                
                vm_instance_list = ec2_instance.describe_instances()
                opDict= []
                opDict= [{'ImageId':i.get('ImageId'), 'InstanceId':i.get('InstanceId'), 'InstanceType':i.get('InstanceType'), 'KeyName':i.get('KeyName'), 'LaunchTime':i.get('LaunchTime'), 'VpcId':i.get('VpcId'), 'Zone':i['Placement']['AvailabilityZone'], 'State':i['State']['Name']} for i in vm_instance_list['Reservations'][0]['Instances']]
                
                StopWatch.stop(f"Instance list {self.cloudname}.")
                t = format(StopWatch.get(f"Instance list {self.cloudname}."), '.2f')
                
                banner(f"Instance list fetched for {self.cloudname} cloud service.\nTotal {len(opDict)} instances fetched. Time taken {t} \nPrinting first 5 sample instances:") 
                print(Printer.write(opDict[:6], output='table'))
                
                #Saving complete list to a file
                opFile = f"{self.cloudname}_Instance_list.txt"
                with open(opFile,'w') as fo:
                    print(Printer.write(opDict, output='table'), file=fo)
                    
            except Exception as e:
                Console.error(f"Instance list of {self.cloudname} can\'t be fetched. Error:\n{e}")
        else:
            Console.error(f"Provider {self.cloudname} not supported")
            raise ValueError(f"provider {self.cloudname} not supported")

    def enlistFlavors(self):
        print("\n")
        banner(f"Fetching list of flavors for {self.cloudname} cloud service.")
        if self.cloudname == "aws":
            
            try:
                ec2_instance = boto3.client(
                    'pricing',
                    aws_access_key_id=str(self.ACCESS_KEY),
                    aws_secret_access_key=str(self.SECRET_KEY),
                    region_name='us-east-1'
                    )
                
                StopWatch.start(f"Flavor list {self.cloudname}.")
                print("CALLING FUNC.")
                #flavor_list = ec2_instance.describe_services(ServiceCode='AmazonEC2')
                flavor_list = ec2_instance.get_products(ServiceCode='AmazonEC2')
                print("CALLED FUNC.")
                opDict= []
                for i in flavor_list['PriceList']:
                    i = json.loads(i)
                    opDict.append(
                    {
                    'productFamily':i['product']['productFamily'],
                    'memory':i['product']['attributes']['memory'],
                    'instanceType':i['product']['attributes']['instanceType'],
                    'tenancy':i['product']['attributes']['tenancy'],
                    'pubdate':i['publicationDate']                    
                    }
                    )                
                StopWatch.stop(f"Flavor list {self.cloudname}.")
                t = format(StopWatch.get(f"Flavor list {self.cloudname}."), '.2f')
                
                banner(f"Flavor list fetched for {self.cloudname} cloud service.\nTotal {len(opDict)} flavors fetched. Time taken {t} \nPrinting first 5 sample flavors:") 
                print(Printer.write(opDict[:6], output='table'))
                
                #Saving complete list to a file
                opFile = f"{self.cloudname}_Flavor_list.txt"
                with open(opFile,'w') as fo:
                    print(Printer.write(opDict, output='table'), file=fo)
                
            except Exception as e:
                Console.error(f"Flavor list of {self.cloudname} can\'t be fetched. Error:\n{e}")
        else:
            Console.error(f"Provider {self.cloudname} not supported")
            raise ValueError(f"provider {self.cloudname} not supported")

        
def main():
    instance = cloudDetails(cloudname='aws')
    instance.enlistImages()
    instance.enlistInstances()
    instance.enlistFlavors()
    
if __name__ == "__main__":
    main()