# Cloudmesh Data Transfer service

Ketan Pimparkar   

## Abstract

TBD   
  

## Objective

Provide cloudmesh users an API and REST service to transfer files, directories from data storage of one cloud service provider to other cloud service provider.  
This packge will consider AWS S3 and Azure Blob storage for current implementation.  


## Motivation

Cloud technology evolves at a very fast rate. Due to which, policies and facilities provided by cloud service providers change as well. There could be various practical scenarios in which users want to transfer the data currently stored in AWS S3 to Azure Blob. Such scenarios could be change in pricing policy or storage capacity rules of AWS S3 or Azure Blob.  

Cloudmesh is a multicloud platform. With inclusion of data transfer service, a highly optimized and simple to use methos will be made available to cloudmesh users.   

## Architecture
TBD

## Technology
* Python
* cloudmesh storage
* OpenAPI 3.0.2
* REST

## Usage  

* API:  
```
cdt config --file=[ip_file]
cdt transfer --data=<file_name>  --copy=[True|False]
cdt stats
cdt -h
```

* REST service:
TBD


**Commands**
* cdt config:
    This command allows users to configure cloudmesh .yml file providing authentication details to cloud service providers. Additionally it will allow users to set s3_bucket_id and blob_endpoint_id.
    * s3_bucket_id: Bucket id of the S3 storage to be used for the data transfer.  
    * blob_endpoint_id: Azure Blob endpoint id to be used for the data transfer.
    
* cdt transfer:
    Command to transfer data from source to target. Uses queuing method to transfer multiple files. If `--copy` parameter is True then the original data of source will be kept as it is, otherwise it will be removed.
    
* cdt stats:
    Provides stats of executed transfer commands
    
    
**Arguments**
 
* ip_file: Configuration of AWS and Azure storages can be provided using a .yml file.  
* file_name: file/directry name to be transferred.  

**Options**

* -h  Help function
* --file  input config file
* --data  data to be transferred  
* --copy  boolean indicating if the data should be copied or moved  

## Benchmarks

TBD - Benchmark report to be created

## Testing

TBD - PyTest report to be created
