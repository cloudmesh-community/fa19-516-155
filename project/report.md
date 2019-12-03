
# Cloudmesh Data Transfer Service for AWS S3 and Azure Blob

Ketan Pimparkar, [fa19-516-155](https://github.com/cloudmesh-community/fa19-516-155)

## Objective

Provide cloudmesh users an API and REST service to transfer files,
directories from data storage of one cloud service provider to other
cloud service provider. This package will consider AWS S3 and Azure Blob
storage for current implementation.

## Motivation

Cloud technology evolves at a very fast rate. Due to which, policies and
facilities provided by cloud service providers change as well. There
could be various practical scenarios in which users want to transfer the
data currently stored in AWS S3 to Azure Blob. Such scenarios could be
change in pricing policy or storage capacity rules of AWS S3 or Azure
Blob.

Cloudmesh is a multicloud platform. With inclusion of data transfer
service, a highly optimized and simple to use methods will be made
available to cloudmesh users.

## Architecture

* Architecture diagram:

![CM Transfer Architecture Diagram](images/gregor-cloudmesh-storage.png)

Diagram credit: Prof. Gregor

## Technology

* AWS S3
* Azure blob storage
* Python 3.7
* cloudmesh storage
* OpenAPI 3.0.2
* REST

## Usage

* API:
* The code is available [here](https://github.com/cloudmesh-community/fa19-516-155/tree/master/cloudmesh-transfer)

```
     Usage:
       transfer copy --source=awss3:source_obj --target=azure:target_obj [-r]
       transfer list --target=awss3:target_obj
       transfer delete --target=awss3:target_obj


     This command is part of Cloudmesh's multi-cloud storage service.
     Command allows users to transfer files/directories from storage of
     one Cloud Service Provider (CSP) to storage of other CSP.
     Current implementation is to transfer data between Azure blob
     storage and AWS S3 bucket.
     AWS S3/ Azure Blob storage credentials and container details will
     be fetched from storage section of "~\.cloudmesh\cloudmesh.yaml"


     Arguments:
       awss3:source_obj  Combination of cloud name and the source object name
       source_obj        Source object. Can be file or a directory.
       azure:target_obj  Combination of cloud name and the target object name
       target_obj        Target object. Can be file or a directory.
       transfer_id       A unique id/name assigned by cloudmesh to each
                         transfer instance.


     Options:
       --id=transfer_id            Unique id/name of the transfer instance.
       -h                          Help function.
       --source=aws:source_obj     Specify source cloud and source object.
       --target=azure:target_obj   Specify target cloud and target object.
       -r                          Recursive transfer for folders.


     Description:
       transfer copy --source=<awss3:source_obj>
                     --target=<azure:target_obj> [-r]
           Copy file/folder from source to target. Source/target CSPs
           and name of the source/target objects to be provided.
           Optional argument "-r" indicates recursive copy.

       transfer list --target=awss3:target_obj
           Enlists available files on target CSP at target object

       transfer delete --target=awss3:target_obj
           Deletes target object from the target CSP.

     Examples:
       transfer copy --source=awss3:sampleFileS3.txt
                     --target=azure:sampleFileBlob.txt

```

* Providers for `cms transfer`:

|Function|Command|Provider|
|-----|-------|--------|
|**list**|cms transfer list --target=local:"~\\cmStorage\\b"|transfer.Provider > transfer.local.Provider|
||cms transfer list --target=awss3: |transfer.Provider > transfer.awss3.Provider|
||cms transfer list --target=azure:"\\folder1" |transfer.Provider > transfer.azureblob.Provider|
|**delete**|cms transfer delete --target=local:"~\\cmStorage\\b"| transfer.Provider > transfer.local.Provider|
||cms transfer delete --target=awss3:"folder1\\a1.txt"|transfer.Provider > transfer.awss3.Provider|
||cms transfer delete --target=azure:"\\folder1\\abcd.txt"|transfer.Provider > transfer.azureblob.Provider|
|**copy**|cms transfer copy --source=awss3:"/folder1"--target=local:"~\\cmStorage\\folder1"|transfer.Provider > transfer.awss3.Provider|
||cms transfer copy --source=local:"~\\cmStorage\\folder1" --target=awss3:"/folder1\/"|transfer.Provider > transfer.awss3.Provider|
||cms transfer copy --source=azure:a1.txt --target=local:"~\\cmStorage\\folder1"|transfer.Provider > transfer.azureblob.Provider|
||cms transfer copy --source=local:"~\\cmStorage\\folder1" --target=azure:"\\folder1"|transfer.Provider > transfer.azureblob.Provider|

* REST service:

TBD

## Benchmarks

Benchmarking done with cloudmesh's stopwatch utility. Detailed results are
available at [Transfer Benchmarks](https://github.com/cloudmesh-community/fa19-516-155/blob/master/cloudmesh-transfer/cloudmesh/transfer/tests/transfer-kpimpark.md)

## Testing

* Following PyTests are created to test the working of transfer command.
  * List local.
  * List s3.
  * List azure.
  * Transfer local to awss3
  * Transfer awss3 to local
  * Transfer awss3 to azure
  * Transfer azure to awss3
  * Transfer local to azure.
  * Transfer azure to local.
  * Delete s3
  * Delete local
  * Delete azure

* PyTests are available at this [location](https://github.com/cloudmesh-community/fa19-516-155/blob/master/cloudmesh-transfer/cloudmesh/transfer/tests/test_transfer.py)
* [Results of PyTest execution.](https://github.com/cloudmesh-community/fa19-516-155/blob/master/cloudmesh-transfer/cloudmesh/transfer/tests/transfer-kpimpark.md)

## Project direction

* Initially `transfer` command was thought as part of `cms storage`.
  Modifications to `cms storage` were done to incorporate `transfer`.
* This approach was changed later on to make `cms transfer` an independent
  command.
* Initial development of `cms transfer` was done by using native python API
  of AWS S3 `Boto3` and Azure Blob `BlockBlobService`. This approach was
  changed to use `cms storage` providers.
* Code developed with native API was then discarded. It can be found at this
  [location](https://github.com/cloudmesh-community/fa19-516-155/tree/master/bkp_cloudmesh-transfer).
* As per the current approach, list/delete/copy methods are implemented using
  cloudmesh storage providers. [Code location](https://github.com/cloudmesh-community/fa19-516-155/tree/master/cloudmesh-transfer)
  
## Configuration

Cloudmesh .yaml file configuration and `azcopy` installation is required:

### .yaml file configuration

* Location of .yaml file: C:\Users\{User}\.cloudmesh\cloudmesh.yaml
* Local storage configuration:

```bash
    storage:
        local:
          cm:
            s3active: true
            blobactive: true
            heading: local_to_CSP
            host: localhost
            kind: local
            label: local_storage
            version: 0.1
            service: storage
          default:
            directory: ~\cmStorage
          credentials:
            userid: None
            password: None
```

* default.directory is the location of local storage
* AWS S3 storage configuration:

```bash
    awss3:
      cm:
        active: false
        heading: homedir
        host: aws.com
        label: home-dir
        kind: awss3
        version: TBD
        service: storage
      default:
        directory: /
      credentials:
        access_key_id: XXX
        secret_access_key: XXX
        bucket: XXX
        region: us-east-2
```

* Azure Blob storage configuration:

```bash
    azure:
      cm:
        active: false
        heading: AWS
        host: azure.mocrosoft.com
        label: azure_blob
        kind: azureblob
        version: TBD
        service: storage
      default:
        resource_group: Cloudmesh
        location: 'East US'
      credentials:
        account_name: ***
        account_key: ***
        container: transferreddata
        AZURE_TENANT_ID: xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
        AZURE_SUBSCRIPTION_ID: xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
        AZURE_APPLICATION_ID: xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
        AZURE_SECRET_KEY: TBD
        AZURE_REGION: northcentralus    """
```

### azcopy installation

TBD

## Progress

* done. Installation of Cloudmesh and mongoDB in Windows10 Pro system
* done. Creation of AWS EC2 instance and S3 buckets
* done. Access AWS account using Cloudmesh CLI
* done. Define architecture of the transfer service
* done. [Define docopt of the transfer service](https://github.com/cloudmesh-community/fa19-516-155/tree/master/cloudmesh-transfer)
* done. Define test cases
* done. Creation of Azure account
* done. Use cms list/delete/get/put in Transfer command
* done. Copy files from local storage to AWS S3 and Azure Blob
* done. Copy objects between S3 and Blob storage
* done. Benchmarks
* done. PyTest execution report
* done. Update report.md
* done. Create `cms transfer` manual
* done. Validate formatting of report.md and manual with mdl

## Limitations

* `transfer` command is developed and tested on Windows 10 Pro
* Currently `transfer` command uses local storage as intermediate storage for
 copying objects between two CSPs

## References

* AzCopy: <https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-s3?toc=%2fazure%2fstorage%2fblobs%2ftoc.json>
* AWS Boto3 API: <https://boto3.amazonaws.com/v1/documentation/api/latest/index.html?id=docs_gateway>
* Cloudmesh manual: <https://cloudmesh.github.io/cloudmesh-manual/preface/about.html>
* Install Azure python SDK: <https://docs.microsoft.com/en-us/azure/python/python-sdk-azure-install>
* Azure python API usage: <https://github.com/Azure-Samples/storage-blobs-python-quickstart/blob/master/example.py>
* Cloud computing book by Prof. Grogor: <https://laszewski.github.io/book/cloud/>
