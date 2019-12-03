
# Cloudmesh Data Transfer Service for AWS S3 and Azure Blob

Cloudmesh is a multicloud platform. Cloud technology evolves at a very fast
rate. Due to which, policies and facilities provided by cloud service
providers change as well. There could be various practical scenarios in which
users want to transfer the data currently stored in AWS S3 to Azure Blob.
Such scenarios could be change in pricing policy or storage capacity rules
of AWS S3 or Azure Blob.

With inclusion of data transfer service, a highly optimized and simple to use
methods will be made available to cloudmesh users.

The code of cloudmesh transfer utility is available at:

* [Source code](https://github.com/cloudmesh-community/fa19-516-155/tree/master/cloudmesh-transfer)

## Configuration

Cloudmesh .yaml file configuration and `azcopy` installation is required:

### .yaml file configuration

Cloudmesh uses `cloudmesh.yaml` to configure all the parameters required for
obtaining access to storage services of various CSPs. Examples of sample
configurations for local, AWS S3 and Azure blob storage services are provided:

* Location of .yaml file: `C:\Users\{user_name}\.cloudmesh\cloudmesh.yaml`
* Local storage configuration:
  * `default.directory` is the location of local storage

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

* AWS S3 storage configuration:
  * `access_key_id` and `secret_access_key` are to be fetched from the AWS
    console `AWS IAM service -> Users -> Security Credentials`
  * `bucket` is name of the default AWS S3 bucket used for storage service
  * `region` is AWS geographic region in which the S3 bucket is present

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
  * `account_name` and `account_key` are Azure creedentials to be fetched from
    Azure portal `Home -> Storage accounts -> {storage account name} -> Settings
     -> Access keys`
  * `container` has the name of the default Blob container to be used.
    Container name can be fetched from Azure portal `Home -> Storage accounts
    -> {storage account name} -> Storage Explorer -> BLOB CONTAINER`

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
        AZURE_REGION: northcentralus
```

### `azcopy` installation

TBD

## Execution

Command line utility `cms transfer` provides help, list, delete and copy
methods to handle objects residing on CSPs such as local storage, AWS S3 and
Azure blob storage.

### help method

`help` argument shows the doc string of the `cms transfer` utility. It provides
brief description of available methods and their usage:

```bash
$ cms help transfer
Command transfer
================

::

  Usage:
    transfer copy --source=awss3:source_obj --target=azure:target_obj
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
    awss3:source_obj  Combination of cloud name and the source object
                      name
    source_obj        Source object. Can be file or a directory.
    azure:target_obj  Combination of cloud name and the target object
                      name
    target_obj        Target object. Can be file or a directory.
    transfer_id       A unique id/name assigned by cloudmesh to each
                      transfer instance.


  Options:
    -h                          Help function.
    --source=awss3:source_obj   Specify source cloud and source object.
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

### list method

`list` method allows users to enlist all the objects present in a storage
container. It supports local, AWS S3 and Azure blob storage services.

* Command to enlist objects from the root of AWS S3 container:

```bash
$ cms transfer list --target=awss3:

+-------+------------+------------+-------------------------------+-------+------+-------------------------------+-----------+
| S.No. | Source CSP | Target CSP | Name                          | Size  | Type | Creation                      | Status    |
+-------+------------+------------+-------------------------------+-------+------+-------------------------------+-----------+
| 1     |            | awss3      | Iris.json                     | 16692 | File | Wed, 17 Jul 2019 03:37:37 GMT | Available |
| 2     |            | awss3      | test_transfer_local_azure.txt | 10    | File | Mon, 02 Dec 2019 10:28:21 GMT | Available |
+-------+------------+------------+-------------------------------+-------+------+-------------------------------+-----------+
```

### copy method

`copy` method allows users to copy objects from one cloud storage provider to
 another. It supports local, AWS S3 and Azure blob storage services.

* Command to copy a file from AWS S3 to root of Azure blob storage:

```bash
$ cms transfer copy --source=awss3:"test_transfer_local_azure.txt" --target=azure:

+-------+------------+------------+-------------------------------+------+------+---------------+--------+
| S.No. | Source CSP | Target CSP | Name                          | Size | Type | Creation      | Status |
+-------+------------+------------+-------------------------------+------+------+---------------+--------+
| 1     | awss3      | azure      | test_transfer_local_azure.txt | 10   | File | Not Available | Copied |
+-------+------------+------------+-------------------------------+------+------+---------------+--------+
```

### delete method

`delete` allows users to delete objects from a container of the cloud storage
 provider. It supports local, AWS S3 and Azure blob storage services.

* Command to delete an object from root of the default AWS S3 bucket

```bash
$ cms transfer delete --target=awss3:"test_transfer_local_azure.txt"

+-------+------------+------------+-------------------------------+------+------+-------------------------------+---------+
| S.No. | Source CSP | Target CSP | Name                          | Size | Type | Creation                      | Status  |
+-------+------------+------------+-------------------------------+------+------+-------------------------------+---------+
| 1     |            | awss3      | test_transfer_local_azure.txt | 10   | File | Mon, 02 Dec 2019 10:28:21 GMT | Deleted |
+-------+------------+------------+-------------------------------+------+------+-------------------------------+---------+
```

## Programming Interface

Cloudmesh transfer provides a simple programming API interface that user can
use to implement methods such as list, delete and copy. We highlight a simple
example for enlisting objects form the local storage provider:

```python
from cloudmesh.transfer.Provider import Provider
from pprint import pprint

target_CSP = "local"
target_obj = "sample_file.txt"

provider = Provider(source=None, source_obj=None,
                    target=target_CSP, target_obj=target_obj)

result = provider.list(source=None, source_obj=None,
                       target=target_CSP, target_obj=target_obj,
                       recursive=True)

pprint(result)
```

## Pytests

Script to test the transfer service can be accessed under tests folder using
the following pytest commands:

```bash
pytest -v --capture=no tests/test_transfer.py
```

* Results: [Pytest execution report and benchmark details](https://github.com/cloudmesh-community/fa19-516-155/blob/master/cloudmesh-transfer/cloudmesh/transfer/tests/transfer-kpimpark.md)