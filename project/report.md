# Cloudmesh Data Transfer Service for AWS S3 and Azure Blob

Ketan Pimparkar, kpimpark@iu.edu, [fa19-516-155](https://github.com/cloudmesh-community/fa19-516-155)

* [Contributors](https://github.com/cloudmesh-community/fa19-516-155/graphs/contributors)
* [Insights](https://github.com/cloudmesh-community/fa19-516-155/pulse/monthly)
* [Code](https://github.com/cloudmesh/cloudmesh-storage)

## Objective

Provide cloudmesh users an API to transfer files,directories from data
storage of one cloud service provider to other cloud service provider.
This package will consider AWS S3 and Azure Blob storage for current
implementation.

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

* [cms transfer manual](https://github.com/cloudmesh-community/fa19-516-155/blob/master/project/transfer.md)
* The code developed for `cms transfer` command is available [here](https://github.com/cloudmesh/cloudmesh-transfer)

:o2: make sure the manual is in the code and her 80 chars wide so it can be printed better it seems slighty to wide.

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

Examples of  commands for `cms transfer`:

```bash
$ cms transfer list --target=local:'~/cmStorage/a'
```

> Copies bla bla




:o: please simplify and do not use a table

|**Function**|**Details**|
|-|-|
|**list**|**enlilst objects from the target storage provider**|
|**Provider**| transfer.Provider > transfer.{taregt_storage}.Provider|
|**Commands**|cms transfer list --target=local:|
||cms transfer list --target=local:"~\\cmStorage\\a"|
||cms transfer list --target=awss3:|
||cms transfer list --target=awss3:'/folder1'|
||cms transfer list --target=awss3:"\\folder1"|
||cms transfer list --target=azure:|
||cms transfer list --target=azure:'/folder1'|
||cms transfer list --target=azure:"\\folder1"|
||
|**delete**|**delete objects from target storage provider**|
|**Provider**| transfer.Provider > transfer.{target_storage}.Provider|
|**Commands**|cms transfer delete --target=local:'xyz.txt'|
||cms transfer delete --target=local:'a/a1.txt'|
||cms transfer delete --target=awss3:a.txt|
||cms transfer delete --target=awss3:'/folder1/fghh.txt'|
||cms transfer delete --target=awss3:'/folder1'|
||cms transfer delete --target=azure:anew.txt|
||cms transfer delete --target=azure:'/a1.txt'|
||cms transfer delete --target=azure:'/folder1'|
||
|**copy**|**copy objects from source storage provider to target storage provider**|
|**Provider**|transfer.Provider > transfer.{target_storage}.Provider|
|**Commands**|cms transfer copy --source=local:'~\cmStorage\a.txt' --target=awss3:|
||cms transfer copy --source=local:'~\cmStorage\a.txt' --target=azure:|
||cms transfer copy --source=awss3:a.txt --target=local:'~/cmStorage'|
||cms transfer copy --source=azure:'a.txt' --target=local:'~/cmStorage/'|
||cms transfer copy --source=awss3:anew.txt --target=azure:|
||cms transfer copy --source=awss3:anew.txt --target=azure:'/folder1'|
||cms transfer copy --source=azure:anew.txt --target=awss3:|
||cms transfer copy --source=azure:anew.txt --target=awss3:'/folder1'|

* cms storage copy command:

Due to change in project direction, code modifications were done to `cms
stoarge` in addition to `cms transfer` to implement object copy between two
storage providers. This code is available in `transfer` [branch of cloudmesh
storage.](https://github.com/cloudmesh/cloudmesh-storage)

```
   Usage:
       storage copy SOURCE DESTINATION [--recursive]

   Description:
       storage copy SOURCE DESTINATION
       Copies objects from SOURCE CSP to DESTINATION CSP
       SOURCE: awss3:"source_object_name"
       DESTINATION: azure:"target_object_name"
```

* Sample commands for `cms storage copy`:

:o2: 
please simplify as discussed

|Source|Target|storage copy command|
|-|-|-|
|awss3|local|cms storage copy awss3:'/a1.txt' local:'/cmStorage'|
|local|awss3|cms storage copy local:"~\cmStorage\folder1/" awss3:"/folder1/" --recursive|
|local|azure|cms storage copy local:"~\cmStorage\a1.txt" azure:'/folder1' --recursive|
|||cms storage copy local:"~\cmStorage\a1.txt" azure:'/' --recursive|
|azure|local|cms storage copy azure:'test_transfer_local_azure.txt' local:'~/cmStorage/'|
|awss3|azure|cms storage copy awss3:"anew.txt" azure:'/'|
|azure|awss3|cms storage copy azure:"anew.txt" awss3:'/'|

## Benchmarks

Benchmarking on `cms transfer` with cloudmesh's stopwatch utility.

[Transfer Benchmarks](https://github.com/cloudmesh/cloudmesh-transfer/blob/master/cloudmesh/transfer/tests/transfer-kpimparkar.txt)

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

* PyTests:

  * [cms transfer pytests](https://github.com/cloudmesh/cloudmesh-transfer/blob/master/cloudmesh/transfer/tests/test_transfer.py)
  * [cms storage pytests](https://github.com/cloudmesh/cloudmesh-storage/blob/transfer/tests/test_storage.py)

* Results of pytest execution:
  * [Results cms transfer pytests](https://github.com/cloudmesh/cloudmesh-transfer/tree/master/cloudmesh/transfer/tests)
  * [Results cms storage pytests for aws](https://github.com/cloudmesh-community/fa19-516-155/blob/master/project/test_storage_with_copy.txt)
  * [Results cms storage pytests for azure](https://github.com/cloudmesh-community/fa19-516-155/blob/master/project/test_storage_azure_with_copy.txt)

## Project direction

:o2: remove the section. what are the current features instead.
what are the limitations. 

* `cms transfer` command:
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
    cloudmesh storage providers. [cms-transfer](https://github.com/cloudmesh/cloudmesh-transfer)
  * Usage of azcopy was made less important due to time availability.

* `cms storage copy` command:
  * After code review of `cms transfer`, it was instructed to integrate a
    `copy` method in `cms storage`. This code is available at [cms-storage](https://github.com/cloudmesh/cloudmesh-storage/tree/transfer)

* cms cloud 1_local modifications:
  * Modifications to the 1_local test were done for windows. [Code](https://github.com/cloudmesh/cloudmesh-cloud/tree/master/tests/1_local)

## Configuration

Cloudmesh.yaml file configuration and `azcopy` installation is required:

:o2: can this be automated such as 

cms config storage add --whatever options are needed

cms config storage add --name=NAME --provider=PROVIDER --directory=DIRECTORY


### .yaml file configuration

* Location of .yaml file: C:\Users\{User}\.cloudmesh\cloudmesh.yaml
* Local storage configuration:

```bash
cloudmesh:   
  storage:
    ...
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
cloudmesh:
  storage
    ...
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
cloudmesh:
  storage:
    ...
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

:o2: TBD

## Progress

:o2: remove and evaluate if thsi si to be put into featuer section

* done. Installation of Cloudmesh and mongoDB in Windows10 Pro system
* done. Creation of AWS EC2 instance and S3 buckets
* done. Access AWS account using Cloudmesh CLI
* done. Define architecture of the transfer service
* done. Define docopt of the transfer service.
* done. Define test cases
* done. Creation of Azure account
* done. Use cms list/delete/get/put in Transfer command
* done. Copy files from local storage to AWS S3 and Azure Blob
* done. Copy objects between S3 and Blob storage
* done. Benchmarks
* done. PyTest execution report
* done. Update report.md
* done. Create `cms transfer` [manual](https://github.com/cloudmesh-community/fa19-516-155/blob/master/project/transfer.md)
* done. Validate formatting of report.md and manual with mdl
* done. Integrate `copy` method in `cms storage`
* done. Add pytest for `copy` and run `cms storage` pytests
* Update storage manual

## Limitations

:o2: as a colleague to test on other os

* `transfer` command is developed and tested on Windows 10 Pro
* Currently `transfer` command uses local storage as intermediate 
  storage for copying objects between two CSPs
* add azcopy, identify if there are other copy commands for example 
  oracle, google (e.g. if one line commands easy to implement, aslo as 
  these exist, you should be able to leverage other peoples implementation 
  and just add google and oragcle anyways to your storage copy. They have 
  provided instructions on how to get accounts. just get them and try it out ;-)
  that will be significantly boost your project ...


## References

* AzCopy <https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-s3?toc=%2fazure%2fstorage%2fblobs%2ftoc.json>
* AWS Boto3 API <https://boto3.amazonaws.com/v1/documentation/api/latest/index.html?id=docs_gateway>
* Cloudmesh manual <https://cloudmesh.github.io/cloudmesh-manual/preface/about.html>
* Install Azure python SDK <https://docs.microsoft.com/en-us/azure/python/python-sdk-azure-install>
* Azure python API usage <https://github.com/Azure-Samples/storage-blobs-python-quickstart/blob/master/example.py>
* Cloud computing book by Gregor von Laszewski <https://laszewski.github.io/book/cloud/>
* cloudmesh-cloud link missing (see manual)
* cloudmesh-storage link missing (see manual)
