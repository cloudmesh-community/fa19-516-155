
```bash
(ENV3) C:\Study\IUMSDS\Fall2019\CloudComputing\fa19-516-155\cloudmesh-transfer\cloudmesh\transfer>pytest -v --capture=no tests/test_transfer.py
======================================================================================= test session starts ========================================================================================
platform win32 -- Python 3.7.4, pytest-5.2.2, py-1.8.0, pluggy-0.13.0 -- c:\study\iumsds\fall2019\cloudcomputing\env3\scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Study\IUMSDS\Fall2019\CloudComputing\fa19-516-155\cloudmesh-transfer
collected 13 items

tests\test_transfer.py::TestTransferS3Local::test_local_list
[35m
# ######################################################################
# test_local_list \tests\test_transfer.py 50
# ######################################################################
[0m
In storage new abc local
Initializing target None provider.
[34m
# ----------------------------------------------------------------------
# In LOCAL provider
#         source csp = None, source object = None
#         target csp = local, target object = ~\cmStorage/test_transfer_local_s3.txt
# ----------------------------------------------------------------------
[0m
In storage new abc local

storage local provider init
{'directory': '~\\cmStorage', 'password': 'None', 'userid': 'None'}
[34m
# ----------------------------------------------------------------------
# In TRANSFER provider
#         source csp = None, source object = None
#         target csp = local, target object = ~\cmStorage/test_transfer_local_s3.txt
# ----------------------------------------------------------------------
[0m
MASTER provider LIST ====>
 local ~\cmStorage/test_transfer_local_s3.txt
CALLING LOCAL PROVIDER'S LIST METHOD
L C:\Users\kpimp\cmStorage\test_transfer_local_s3.txt
====>  True
+-------+------------+------------+--------------------------------------------------+------+------+----------------------+-----------+
| S.No. | Source CSP | Target CSP | Name                                             | Size | Type | Creation             | Status    |
+-------+------------+------------+--------------------------------------------------+------+------+----------------------+-----------+
| 1     |            | local      | C:\Users\kpimp\cmStorage\test_transfer_local_s3. | 10   | File | 12/02/2019, 01:07:52 | Available |
|       |            |            | txt                                              |      |      |                      |           |
+-------+------------+------------+--------------------------------------------------+------+------+----------------------+-----------+
PASSED
tests\test_transfer.py::TestTransferS3Local::test_transfer_local_s3
[35m
# ######################################################################
# test_transfer_local_s3 \tests\test_transfer.py 66
# ######################################################################
[0m
In storage new abc local
Initializing source local provider.
[34m
# ----------------------------------------------------------------------
# In LOCAL provider
#         source csp = local, source object = ~\cmStorage\test_transfer_local_s3.txt
#         target csp = awss3, target object = \
# ----------------------------------------------------------------------
[0m
In storage new abc local

storage local provider init
{'directory': 'C:\\Users\\kpimp\\cmStorage',
 'password': 'None',
 'userid': 'None'}
In storage new abc awss3
Initializing target local provider.
[34m
# ----------------------------------------------------------------------
# In AWS S3 provider
#         source csp = local, source object = ~\cmStorage\test_transfer_local_s3.txt
#         target csp = awss3, target object = \
# ----------------------------------------------------------------------
[0m
In storage new abc awss3
[34m
# ----------------------------------------------------------------------
# In TRANSFER provider
#         source csp = local, source object = ~\cmStorage\test_transfer_local_s3.txt
#         target csp = awss3, target object = \
# ----------------------------------------------------------------------
[0m

MASTER provider COPY from local to awss3
Source is local hence redirected to awss3 provider.
CALLING AWS S3 PROVIDER'S GET METHOD FOR AWS S3 TO LOCAL COPY
{'action': 'put',
 'destination': '/',
 'recursive': True,
 'source': 'C:/Users/kpimp/cmStorage/test_transfer_local_s3.txt'}
'C:/Users/kpimp/cmStorage/test_transfer_local_s3.txt'
'/'
'C:/Users/kpimp/cmStorage/test_transfer_local_s3.txt'
''
'bucket-iris.json'
True
{'action': 'put',
 'destination': '/',
 'message': 'Source uploaded',
 'objlist': [{'contentLength': '10',
              'fileName': 'test_transfer_local_s3.txt',
              'lastModificationDate': 'Mon, 02 Dec 2019 10:28:13 GMT'}],
 'recursive': True,
 'source': 'C:/Users/kpimp/cmStorage/test_transfer_local_s3.txt'}
[32mCopied C:/Users/kpimp/cmStorage/test_transfer_local_s3.txt from local to awss3
Target object name is / [0m
+-------+------------+------------+----------------------------+------+------+-------------------------------+--------+
| S.No. | Source CSP | Target CSP | Name                       | Size | Type | Creation                      | Status |
+-------+------------+------------+----------------------------+------+------+-------------------------------+--------+
| 1     | local      | awss3      | test_transfer_local_s3.txt | 10   | File | Mon, 02 Dec 2019 10:28:13 GMT | Copied |
+-------+------------+------------+----------------------------+------+------+-------------------------------+--------+
[{'idx': 1,
  'lastmodified': 'Mon, 02 Dec 2019 10:28:13 GMT',
  'name': 'test_transfer_local_s3.txt',
  'size': '10',
  'source': 'local',
  'status': 'Copied',
  'target': 'awss3',
  'type': 'File'}]
PASSED
tests\test_transfer.py::TestTransferS3Local::test_list_s3
[35m
# ######################################################################
# test_list_s3 \tests\test_transfer.py 86
# ######################################################################
[0m
In storage new abc awss3
Initializing target None provider.
[34m
# ----------------------------------------------------------------------
# In AWS S3 provider
#         source csp = None, source object = None
#         target csp = awss3, target object = \test_transfer_local_s3.txt
# ----------------------------------------------------------------------
[0m
In storage new abc awss3
[34m
# ----------------------------------------------------------------------
# In TRANSFER provider
#         source csp = None, source object = None
#         target csp = awss3, target object = \test_transfer_local_s3.txt
# ----------------------------------------------------------------------
[0m
MASTER provider LIST ====>
 awss3 \test_transfer_local_s3.txt
CALLING AWS S3 PROVIDER'S LIST METHOD
'\\test_transfer_local_s3.txt'
'test_transfer_local_s3.txt'
'test_transfer_local_s3.txt'
'test_transfer_local_s3.txt'
'test_transfer_local_s3.txt'
+-------+------------+------------+----------------------------+------+------+-------------------------------+-----------+
| S.No. | Source CSP | Target CSP | Name                       | Size | Type | Creation                      | Status    |
+-------+------------+------------+----------------------------+------+------+-------------------------------+-----------+
| 1     |            | awss3      | test_transfer_local_s3.txt | 10   | File | Mon, 02 Dec 2019 10:28:13 GMT | Available |
+-------+------------+------------+----------------------------+------+------+-------------------------------+-----------+
PASSED
tests\test_transfer.py::TestTransferS3Local::test_transfer_s3_to_local
[35m
# ######################################################################
# test_transfer_s3_to_local \tests\test_transfer.py 103
# ######################################################################
[0m
In storage new abc awss3
Initializing source awss3 provider.
[34m
# ----------------------------------------------------------------------
# In AWS S3 provider
#         source csp = awss3, source object = \test_transfer_local_s3.txt
#         target csp = local, target object = ~\cmStorage\test_transfer_local_s3.txt
# ----------------------------------------------------------------------
[0m
In storage new abc awss3
In storage new abc local
Initializing target awss3 provider.
[34m
# ----------------------------------------------------------------------
# In LOCAL provider
#         source csp = awss3, source object = \test_transfer_local_s3.txt
#         target csp = local, target object = ~\cmStorage\test_transfer_local_s3.txt
# ----------------------------------------------------------------------
[0m
In storage new abc local

storage local provider init
{'directory': 'C:\\Users\\kpimp\\cmStorage',
 'password': 'None',
 'userid': 'None'}
[34m
# ----------------------------------------------------------------------
# In TRANSFER provider
#         source csp = awss3, source object = \test_transfer_local_s3.txt
#         target csp = local, target object = ~\cmStorage\test_transfer_local_s3.txt
# ----------------------------------------------------------------------
[0m

MASTER provider COPY from awss3 to local
Target is local hence redirected to awss3 provider.
CALLING AWS S3 PROVIDER'S GET METHOD FOR AWS S3 TO LOCAL COPY
'/test_transfer_local_s3.txt'
'~/cmStorage/test_transfer_local_s3.txt'
{'action': 'get',
 'destination': '~/cmStorage/test_transfer_local_s3.txt',
 'message': 'Source downloaded',
 'objlist': [{'contentLength': '10',
              'fileName': 'test_transfer_local_s3.txt',
              'lastModificationDate': 'Mon, 02 Dec 2019 10:28:13 GMT'}],
 'recursive': True,
 'source': '/test_transfer_local_s3.txt'}
[32mCopied /test_transfer_local_s3.txt from awss3 to local
Target object name is ~/cmStorage/test_transfer_local_s3.txt [0m
+-------+------------+------------+----------------------------+------+------+-------------------------------+--------+
| S.No. | Source CSP | Target CSP | Name                       | Size | Type | Creation                      | Status |
+-------+------------+------------+----------------------------+------+------+-------------------------------+--------+
| 1     | awss3      | local      | test_transfer_local_s3.txt | 10   | File | Mon, 02 Dec 2019 10:28:13 GMT | Copied |
+-------+------------+------------+----------------------------+------+------+-------------------------------+--------+
[{'idx': 1,
  'lastmodified': 'Mon, 02 Dec 2019 10:28:13 GMT',
  'name': 'test_transfer_local_s3.txt',
  'size': '10',
  'source': 'awss3',
  'status': 'Copied',
  'target': 'local',
  'type': 'File'}]
PASSED
tests\test_transfer.py::TestTransferS3Local::test_transfer_s3_to_azure
[35m
# ######################################################################
# test_transfer_s3_to_azure \tests\test_transfer.py 123
# ######################################################################
[0m
=======>  test_transfer_local_s3.txt
=======>  \
In storage new abc awss3
Initializing source awss3 provider.
[34m
# ----------------------------------------------------------------------
# In AWS S3 provider
#         source csp = awss3, source object = test_transfer_local_s3.txt
#         target csp = azure, target object = \
# ----------------------------------------------------------------------
[0m
In storage new abc awss3
In storage new abc azure
Initializing target awss3 provider.
[34m
# ----------------------------------------------------------------------
# In Azure Blob Storage provider
#         source csp = awss3, source object = test_transfer_local_s3.txt
#         target csp = azure, target object = \
# ----------------------------------------------------------------------
[0m
Init StorageABC
[34m
# ----------------------------------------------------------------------
# In TRANSFER provider
#         source csp = awss3, source object = test_transfer_local_s3.txt
#         target csp = azureblob, target object = \
# ----------------------------------------------------------------------
[0m

MASTER provider COPY from awss3 to azure
[34m
# ----------------------------------------------------------------------
# CALLING AZURE BLOB STORAGE PROVIDER'S GET METHOD FOR AWSS3 TO AZURE COPY
# ----------------------------------------------------------------------
[0m
In storage new abc awss3
'test_transfer_local_s3.txt'
'~/cmStorage'
{'action': 'get',
 'destination': '~/cmStorage',
 'message': 'Source downloaded',
 'objlist': [{'contentLength': '10',
              'fileName': 'test_transfer_local_s3.txt',
              'lastModificationDate': 'Mon, 02 Dec 2019 10:28:13 GMT'}],
 'recursive': True,
 'source': 'test_transfer_local_s3.txt'}
Fetched from s3 to local:


[35m
# ######################################################################
# put c:\study\iumsds\fall2019\cloudcomputing\cm\cloudmesh-storage\cloudmesh\storage\provider\azureblob\Provider.py 256
# ######################################################################
[0m
[{'cm': {'cloud': 'azure',
         'created': '2',
         'kind': 'storage',
         'name': 'test_transfer_local_s3.txt',
         'size': 10,
         'status': 'exists',
         'updated': '2'},
  'content': b'',
  'deleted': False,
  'metadata': {},
  'name': 'test_transfer_local_s3.txt',
  'properties': {'append_blob_committed_block_count': None,
                 'blob_tier': 'Cool',
                 'blob_tier_change_time': None,
                 'blob_tier_inferred': True,
                 'blob_type': 'BlockBlob',
                 'content_length': 10,
                 'content_range': None,
                 'deleted_time': None,
                 'etag': '"0x8D7771258B74914"',
                 'page_blob_sequence_number': None,
                 'remaining_retention_days': None,
                 'server_encrypted': True},
  'snapshot': None}]
[32mCopied C:\Users\kpimp\cmStorage\test_transfer_local_s3.txt from awss3 to azure
Target object name is / [0m
[{'cm': {'cloud': 'azure',
         'created': '2',
         'kind': 'storage',
         'name': 'test_transfer_local_s3.txt',
         'size': 10,
         'status': 'exists',
         'updated': '2'},
  'content': b'',
  'deleted': False,
  'metadata': {},
  'name': 'test_transfer_local_s3.txt',
  'properties': {'append_blob_committed_block_count': None,
                 'blob_tier': 'Cool',
                 'blob_tier_change_time': None,
                 'blob_tier_inferred': True,
                 'blob_type': 'BlockBlob',
                 'content_length': 10,
                 'content_range': None,
                 'deleted_time': None,
                 'etag': '"0x8D7771258B74914"',
                 'page_blob_sequence_number': None,
                 'remaining_retention_days': None,
                 'server_encrypted': True},
  'snapshot': None}]
+-------+------------+------------+----------------------------+------+------+---------------+--------+
| S.No. | Source CSP | Target CSP | Name                       | Size | Type | Creation      | Status |
+-------+------------+------------+----------------------------+------+------+---------------+--------+
| 1     | awss3      | azure      | test_transfer_local_s3.txt | 10   | File | Not Available | Copied |
+-------+------------+------------+----------------------------+------+------+---------------+--------+
[{'idx': 1,
  'lastmodified': 'Not Available',
  'name': 'test_transfer_local_s3.txt',
  'size': 10,
  'source': 'awss3',
  'status': 'Copied',
  'target': 'azure',
  'type': 'File'}]
PASSED
tests\test_transfer.py::TestTransferS3Local::test_transfer_local_to_azure
[35m
# ######################################################################
# test_transfer_local_to_azure \tests\test_transfer.py 147
# ######################################################################
[0m
In storage new abc local
Initializing source local provider.
[34m
# ----------------------------------------------------------------------
# In LOCAL provider
#         source csp = local, source object = ~\cmStorage\test_transfer_local_azure.txt
#         target csp = azure, target object = \
# ----------------------------------------------------------------------
[0m
In storage new abc local

storage local provider init
{'directory': 'C:\\Users\\kpimp\\cmStorage',
 'password': 'None',
 'userid': 'None'}
In storage new abc azure
Initializing target local provider.
[34m
# ----------------------------------------------------------------------
# In Azure Blob Storage provider
#         source csp = local, source object = ~\cmStorage\test_transfer_local_azure.txt
#         target csp = azure, target object = \
# ----------------------------------------------------------------------
[0m
Init StorageABC
[34m
# ----------------------------------------------------------------------
# In TRANSFER provider
#         source csp = local, source object = ~\cmStorage\test_transfer_local_azure.txt
#         target csp = azureblob, target object = \
# ----------------------------------------------------------------------
[0m

MASTER provider COPY from local to azure
Source is local hence redirected to azure provider.
[34m
# ----------------------------------------------------------------------
# CALLING AZURE BLOB STORAGE PROVIDER'S GET METHOD FOR LOCAL TO AZURE COPY
# ----------------------------------------------------------------------
[0m

[35m
# ######################################################################
# put c:\study\iumsds\fall2019\cloudcomputing\cm\cloudmesh-storage\cloudmesh\storage\provider\azureblob\Provider.py 256
# ######################################################################
[0m
[{'cm': {'cloud': 'azure',
         'created': '2',
         'kind': 'storage',
         'name': 'test_transfer_local_azure.txt',
         'size': 10,
         'status': 'exists',
         'updated': '2'},
  'content': b'',
  'deleted': False,
  'metadata': {},
  'name': 'test_transfer_local_azure.txt',
  'properties': {'append_blob_committed_block_count': None,
                 'blob_tier': 'Cool',
                 'blob_tier_change_time': None,
                 'blob_tier_inferred': True,
                 'blob_type': 'BlockBlob',
                 'content_length': 10,
                 'content_range': None,
                 'deleted_time': None,
                 'etag': '"0x8D777125918B4AD"',
                 'page_blob_sequence_number': None,
                 'remaining_retention_days': None,
                 'server_encrypted': True},
  'snapshot': None}]
[32mCopied C:/Users/kpimp/cmStorage/test_transfer_local_azure.txt from local to azure
Target object name is / [0m
[{'cm': {'cloud': 'azure',
         'created': '2',
         'kind': 'storage',
         'name': 'test_transfer_local_azure.txt',
         'size': 10,
         'status': 'exists',
         'updated': '2'},
  'content': b'',
  'deleted': False,
  'metadata': {},
  'name': 'test_transfer_local_azure.txt',
  'properties': {'append_blob_committed_block_count': None,
                 'blob_tier': 'Cool',
                 'blob_tier_change_time': None,
                 'blob_tier_inferred': True,
                 'blob_type': 'BlockBlob',
                 'content_length': 10,
                 'content_range': None,
                 'deleted_time': None,
                 'etag': '"0x8D777125918B4AD"',
                 'page_blob_sequence_number': None,
                 'remaining_retention_days': None,
                 'server_encrypted': True},
  'snapshot': None}]
+-------+------------+------------+-------------------------------+------+------+---------------+--------+
| S.No. | Source CSP | Target CSP | Name                          | Size | Type | Creation      | Status |
+-------+------------+------------+-------------------------------+------+------+---------------+--------+
| 1     | local      | azure      | test_transfer_local_azure.txt | 10   | File | Not Available | Copied |
+-------+------------+------------+-------------------------------+------+------+---------------+--------+
[{'idx': 1,
  'lastmodified': 'Not Available',
  'name': 'test_transfer_local_azure.txt',
  'size': 10,
  'source': 'local',
  'status': 'Copied',
  'target': 'azure',
  'type': 'File'}]
PASSED
tests\test_transfer.py::TestTransferS3Local::test_list_azure
[35m
# ######################################################################
# test_list_azure \tests\test_transfer.py 168
# ######################################################################
[0m
In storage new abc azure
Initializing target None provider.
[34m
# ----------------------------------------------------------------------
# In Azure Blob Storage provider
#         source csp = None, source object = None
#         target csp = azure, target object = \test_transfer_local_azure.txt
# ----------------------------------------------------------------------
[0m
Init StorageABC
[34m
# ----------------------------------------------------------------------
# In TRANSFER provider
#         source csp = None, source object = None
#         target csp = azureblob, target object = \test_transfer_local_azure.txt
# ----------------------------------------------------------------------
[0m
MASTER provider LIST ====>
 azure \test_transfer_local_azure.txt
CALLING AZURE BLOB STORAGE PROVIDER'S LIST METHOD
\test_transfer_local_azure.txt
/test_transfer_local_azure.txt True

[35m
# ######################################################################
# list c:\study\iumsds\fall2019\cloudcomputing\cm\cloudmesh-storage\cloudmesh\storage\provider\azureblob\Provider.py 513
# ######################################################################
[0m
File  :  test_transfer_local_azure.txt
Folder:
[32m
List of objects from azure CSP for object /test_transfer_local_azure.txt:
[0m
+-------+------------+------------+-------------------------------+------+------+---------------+-----------+
| S.No. | Source CSP | Target CSP | Name                          | Size | Type | Creation      | Status    |
+-------+------------+------------+-------------------------------+------+------+---------------+-----------+
| 1     |            | azure      | test_transfer_local_azure.txt | 10   | File | Not Available | Available |
+-------+------------+------------+-------------------------------+------+------+---------------+-----------+
PASSED
tests\test_transfer.py::TestTransferS3Local::test_transfer_azure_to_local
[35m
# ######################################################################
# test_transfer_azure_to_local \tests\test_transfer.py 186
# ######################################################################
[0m
In storage new abc azure
Initializing source azureblob provider.
[34m
# ----------------------------------------------------------------------
# In Azure Blob Storage provider
#         source csp = azure, source object = \test_transfer_local_azure.txt
#         target csp = local, target object = ~\cmStorage\test_transfer_local_azure.txt
# ----------------------------------------------------------------------
[0m
Init StorageABC
In storage new abc local
Initializing target azureblob provider.
[34m
# ----------------------------------------------------------------------
# In LOCAL provider
#         source csp = azure, source object = \test_transfer_local_azure.txt
#         target csp = local, target object = ~\cmStorage\test_transfer_local_azure.txt
# ----------------------------------------------------------------------
[0m
In storage new abc local

storage local provider init
{'directory': 'C:\\Users\\kpimp\\cmStorage',
 'password': 'None',
 'userid': 'None'}
[34m
# ----------------------------------------------------------------------
# In TRANSFER provider
#         source csp = azureblob, source object = \test_transfer_local_azure.txt
#         target csp = local, target object = ~\cmStorage\test_transfer_local_azure.txt
# ----------------------------------------------------------------------
[0m

MASTER provider COPY from azure to local
Target is local hence redirected to azure provider.
[34m
# ----------------------------------------------------------------------
# CALLING AZURE BLOB STORAGE PROVIDER'S GET METHOD FOR AZURE TO LOCAL COPY
# ----------------------------------------------------------------------
[0m

[35m
# ######################################################################
# get c:\study\iumsds\fall2019\cloudcomputing\cm\cloudmesh-storage\cloudmesh\storage\provider\azureblob\Provider.py 101
# ######################################################################
[0m
File  :  test_transfer_local_azure.txt
Folder:
WARNING: A file already exists with same name, overwrite issued
[32mCopied /test_transfer_local_azure.txt from azure to local
Target object name is ~/cmStorage/test_transfer_local_azure.txt [0m
[{'cm': {'cloud': 'azure',
         'created': '2',
         'kind': 'storage',
         'name': 'test_transfer_local_azure.txt',
         'size': 10,
         'status': 'exists',
         'updated': '2'},
  'content': None,
  'deleted': False,
  'metadata': {},
  'name': 'test_transfer_local_azure.txt',
  'properties': {'append_blob_committed_block_count': None,
                 'blob_tier': None,
                 'blob_tier_change_time': None,
                 'blob_tier_inferred': False,
                 'blob_type': 'BlockBlob',
                 'content_length': 10,
                 'content_range': 'bytes 0-9/10',
                 'deleted_time': None,
                 'etag': '"0x8D777125918B4AD"',
                 'page_blob_sequence_number': None,
                 'remaining_retention_days': None,
                 'server_encrypted': True},
  'snapshot': None}]
+-------+------------+------------+-------------------------------+------+------+---------------+--------+
| S.No. | Source CSP | Target CSP | Name                          | Size | Type | Creation      | Status |
+-------+------------+------------+-------------------------------+------+------+---------------+--------+
| 1     | azure      | local      | test_transfer_local_azure.txt | 10   | File | Not Available | Copied |
+-------+------------+------------+-------------------------------+------+------+---------------+--------+
[{'idx': 1,
  'lastmodified': 'Not Available',
  'name': 'test_transfer_local_azure.txt',
  'size': 10,
  'source': 'azure',
  'status': 'Copied',
  'target': 'local',
  'type': 'File'}]
PASSED
tests\test_transfer.py::TestTransferS3Local::test_transfer_azure_to_s3
[35m
# ######################################################################
# test_transfer_azure_to_s3 \tests\test_transfer.py 207
# ######################################################################
[0m
In storage new abc azure
Initializing source azureblob provider.
[34m
# ----------------------------------------------------------------------
# In Azure Blob Storage provider
#         source csp = azure, source object = \test_transfer_local_azure.txt
#         target csp = awss3, target object = \
# ----------------------------------------------------------------------
[0m
Init StorageABC
In storage new abc awss3
Initializing target azureblob provider.
[34m
# ----------------------------------------------------------------------
# In AWS S3 provider
#         source csp = azure, source object = \test_transfer_local_azure.txt
#         target csp = awss3, target object = \
# ----------------------------------------------------------------------
[0m
In storage new abc awss3
[34m
# ----------------------------------------------------------------------
# In TRANSFER provider
#         source csp = azureblob, source object = \test_transfer_local_azure.txt
#         target csp = awss3, target object = \
# ----------------------------------------------------------------------
[0m

MASTER provider COPY from azure to awss3
CALLING AWS S3 PROVIDER'S GET METHOD FOR AWS S3 TO LOCAL COPY
Init StorageABC

[35m
# ######################################################################
# get c:\study\iumsds\fall2019\cloudcomputing\cm\cloudmesh-storage\cloudmesh\storage\provider\azureblob\Provider.py 101
# ######################################################################
[0m
File  :  test_transfer_local_azure.txt
Folder:
Fetched from azure blob to local:

[{'cm': {'cloud': 'azure',
         'created': '2',
         'kind': 'storage',
         'name': 'test_transfer_local_azure.txt',
         'size': 10,
         'status': 'exists',
         'updated': '2'},
  'content': None,
  'deleted': False,
  'metadata': {},
  'name': 'test_transfer_local_azure.txt',
  'properties': {'append_blob_committed_block_count': None,
                 'blob_tier': None,
                 'blob_tier_change_time': None,
                 'blob_tier_inferred': False,
                 'blob_type': 'BlockBlob',
                 'content_length': 10,
                 'content_range': 'bytes 0-9/10',
                 'deleted_time': None,
                 'etag': '"0x8D777125918B4AD"',
                 'page_blob_sequence_number': None,
                 'remaining_retention_days': None,
                 'server_encrypted': True},
  'snapshot': None}]
29
C:\Users\kpimp\cmStorage\test_transfer_local_azure.txt
{'action': 'put',
 'destination': '/',
 'recursive': False,
 'source': 'C:\\Users\\kpimp\\cmStorage\\test_transfer_local_azure.txt'}
'C:\\Users\\kpimp\\cmStorage\\test_transfer_local_azure.txt'
'/'
'C:/Users/kpimp/cmStorage/test_transfer_local_azure.txt'
''
'bucket-iris.json'
True
{'action': 'put',
 'destination': '/',
 'message': 'Source uploaded',
 'objlist': [{'contentLength': '10',
              'fileName': 'test_transfer_local_azure.txt',
              'lastModificationDate': 'Mon, 02 Dec 2019 10:28:21 GMT'}],
 'recursive': False,
 'source': 'C:\\Users\\kpimp\\cmStorage\\test_transfer_local_azure.txt'}
[32mCopied C:\Users\kpimp\cmStorage\test_transfer_local_azure.txt from azure to awss3
Target object name is / [0m
+-------+------------+------------+-------------------------------+------+------+-------------------------------+--------+
| S.No. | Source CSP | Target CSP | Name                          | Size | Type | Creation                      | Status |
+-------+------------+------------+-------------------------------+------+------+-------------------------------+--------+
| 1     | azure      | awss3      | test_transfer_local_azure.txt | 10   | File | Mon, 02 Dec 2019 10:28:21 GMT | Copied |
+-------+------------+------------+-------------------------------+------+------+-------------------------------+--------+
[{'idx': 1,
  'lastmodified': 'Mon, 02 Dec 2019 10:28:21 GMT',
  'name': 'test_transfer_local_azure.txt',
  'size': '10',
  'source': 'azure',
  'status': 'Copied',
  'target': 'awss3',
  'type': 'File'}]
PASSED
tests\test_transfer.py::TestTransferS3Local::test_delete_s3
[35m
# ######################################################################
# test_delete_s3 \tests\test_transfer.py 228
# ######################################################################
[0m
In storage new abc awss3
Initializing target None provider.
[34m
# ----------------------------------------------------------------------
# In AWS S3 provider
#         source csp = None, source object = None
#         target csp = awss3, target object = \test_transfer_local_s3.txt
# ----------------------------------------------------------------------
[0m
In storage new abc awss3
[34m
# ----------------------------------------------------------------------
# In TRANSFER provider
#         source csp = None, source object = None
#         target csp = awss3, target object = \test_transfer_local_s3.txt
# ----------------------------------------------------------------------
[0m

MASTER provider DELETE ====>
 None awss3
CALLING AWS S3 PROVIDER'S DELETE METHOD
'\\test_transfer_local_s3.txt'
{'action': 'delete',
 'message': 'Source Deleted',
 'objlist': [{'contentLength': '10',
              'fileName': 'test_transfer_local_s3.txt',
              'lastModificationDate': 'Mon, 02 Dec 2019 10:28:13 GMT'}],
 'recursive': True,
 'source': '\\test_transfer_local_s3.txt'}
[32mDeleted following objects from awss3 CSP:
 [0m
+-------+------------+------------+----------------------------+------+------+-------------------------------+---------+
| S.No. | Source CSP | Target CSP | Name                       | Size | Type | Creation                      | Status  |
+-------+------------+------------+----------------------------+------+------+-------------------------------+---------+
| 1     |            | awss3      | test_transfer_local_s3.txt | 10   | File | Mon, 02 Dec 2019 10:28:13 GMT | Deleted |
+-------+------------+------------+----------------------------+------+------+-------------------------------+---------+
PASSED
tests\test_transfer.py::TestTransferS3Local::test_delete_local
[35m
# ######################################################################
# test_delete_local \tests\test_transfer.py 246
# ######################################################################
[0m
In storage new abc local
Initializing target None provider.
[34m
# ----------------------------------------------------------------------
# In LOCAL provider
#         source csp = None, source object = None
#         target csp = local, target object = test_transfer_local_s3.txt
# ----------------------------------------------------------------------
[0m
In storage new abc local

storage local provider init
{'directory': 'C:\\Users\\kpimp\\cmStorage',
 'password': 'None',
 'userid': 'None'}
[34m
# ----------------------------------------------------------------------
# In TRANSFER provider
#         source csp = None, source object = None
#         target csp = local, target object = test_transfer_local_s3.txt
# ----------------------------------------------------------------------
[0m

MASTER provider DELETE ====>
 None local
CALLING LOCAL PROVIDER'S DELETE METHOD
test_transfer_local_s3.txt
 test_transfer_local_s3.txt
L C:\Users\kpimp\cmStorage\test_transfer_local_s3.txt
====>  True
C:\Users\kpimp\cmStorage\test_transfer_local_s3.txt
[32mDeleted following objects from local storage. [0m
+-------+------------+------------+--------------------------------------------------+------+------+----------------------+---------+
| S.No. | Source CSP | Target CSP | Name                                             | Size | Type | Creation             | Status  |
+-------+------------+------------+--------------------------------------------------+------+------+----------------------+---------+
| 1     |            | local      | C:\Users\kpimp\cmStorage\test_transfer_local_s3. | 10   | File | 12/02/2019, 01:07:52 | Deleted |
|       |            |            | txt                                              |      |      |                      |         |
+-------+------------+------------+--------------------------------------------------+------+------+----------------------+---------+
PASSED
tests\test_transfer.py::TestTransferS3Local::test_delete_azure
[35m
# ######################################################################
# test_delete_azure \tests\test_transfer.py 264
# ######################################################################
[0m
In storage new abc azure
Initializing target None provider.
[34m
# ----------------------------------------------------------------------
# In Azure Blob Storage provider
#         source csp = None, source object = None
#         target csp = azure, target object = \test_transfer_local_azure.txt
# ----------------------------------------------------------------------
[0m
Init StorageABC
[34m
# ----------------------------------------------------------------------
# In TRANSFER provider
#         source csp = None, source object = None
#         target csp = azureblob, target object = \test_transfer_local_azure.txt
# ----------------------------------------------------------------------
[0m

MASTER provider DELETE ====>
 None azure
CALLING AZURE BLOB STORAGE PROVIDER'S DELETE METHOD

[35m
# ######################################################################
# delete c:\study\iumsds\fall2019\cloudcomputing\cm\cloudmesh-storage\cloudmesh\storage\provider\azureblob\Provider.py 345
# ######################################################################
[0m
File  :  test_transfer_local_azure.txt
Folder:
[{'cm': {'cloud': 'azure',
         'created': '2',
         'kind': 'storage',
         'name': 'test_transfer_local_azure.txt',
         'size': 10,
         'status': 'deleted',
         'updated': '2'},
  'content': b'',
  'deleted': False,
  'metadata': {},
  'name': 'test_transfer_local_azure.txt',
  'properties': {'append_blob_committed_block_count': None,
                 'blob_tier': 'Cool',
                 'blob_tier_change_time': None,
                 'blob_tier_inferred': True,
                 'blob_type': 'BlockBlob',
                 'content_length': 10,
                 'content_range': None,
                 'deleted_time': None,
                 'etag': '"0x8D777125918B4AD"',
                 'page_blob_sequence_number': None,
                 'remaining_retention_days': None,
                 'server_encrypted': True},
  'snapshot': None}]
[32mDeleted following objects from provided object /test_transfer_local_azure.txt[0m
+-------+------------+------------+-------------------------------+------+------+---------------+---------+
| S.No. | Source CSP | Target CSP | Name                          | Size | Type | Creation      | Status  |
+-------+------------+------------+-------------------------------+------+------+---------------+---------+
| 1     |            | azure      | test_transfer_local_azure.txt | 10   | File | Not Available | Deleted |
+-------+------------+------------+-------------------------------+------+------+---------------+---------+
PASSED
tests\test_transfer.py::TestTransferS3Local::test_results
[35m
# ######################################################################
# test_results \tests\test_transfer.py 282
# ######################################################################
[0m
[34m
# ----------------------------------------------------------------------
# Benchmark results for TRANSFER service
# ----------------------------------------------------------------------
[0m

+-------------------+-----------------------------------------------------------------------------------+
| Machine Attribute | Value                                                                             |
+-------------------+-----------------------------------------------------------------------------------+
| cpu_count         | 4                                                                                 |
| mac_version       |                                                                                   |
| machine           | ('AMD64',)                                                                        |
| mem_available     | 517.6 MiB                                                                         |
| mem_free          | 517.6 MiB                                                                         |
| mem_percent       | 87.1%                                                                             |
| mem_total         | 3.9 GiB                                                                           |
| mem_used          | 3.4 GiB                                                                           |
| node              | ('DESKTOP-HUC37G2',)                                                              |
| platform          | Windows-10-10.0.18362-SP0                                                         |
| processor         | ('Intel64 Family 6 Model 78 Stepping 3, GenuineIntel',)                           |
| processors        | Windows                                                                           |
| python            | 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] |
| release           | ('10',)                                                                           |
| sys               | win32                                                                             |
| system            | Windows                                                                           |
| user              |                                                                                   |
| version           | 10.0.18362                                                                        |
| win_version       | ('10', '10.0.18362', 'SP0', '')                                                   |
+-------------------+-----------------------------------------------------------------------------------+
+-------------------------------+-------+---------------------+-----+----------------------+------+---------+-------------+---------------------------------+
| timer                         | time  | start               | tag | node                 | user | system  | mac_version | win_version                     |
+-------------------------------+-------+---------------------+-----+----------------------+------+---------+-------------+---------------------------------+
| List local for awss3 provider | 0.005 | 2019-12-02 10:28:11 |     | ('DESKTOP-HUC37G2',) |      | Windows |             | ('10', '10.0.18362', 'SP0', '') |
| Transfer local to awss3       | 2.147 | 2019-12-02 10:28:11 |     | ('DESKTOP-HUC37G2',) |      | Windows |             | ('10', '10.0.18362', 'SP0', '') |
| List s3 for awss3 provider    | 1.493 | 2019-12-02 10:28:13 |     | ('DESKTOP-HUC37G2',) |      | Windows |             | ('10', '10.0.18362', 'SP0', '') |
| Transfer awss3 to local       | 1.097 | 2019-12-02 10:28:15 |     | ('DESKTOP-HUC37G2',) |      | Windows |             | ('10', '10.0.18362', 'SP0', '') |
| Transfer awss3 to azure       | 1.836 | 2019-12-02 10:28:16 |     | ('DESKTOP-HUC37G2',) |      | Windows |             | ('10', '10.0.18362', 'SP0', '') |
| Transfer local to azure.      | 0.603 | 2019-12-02 10:28:18 |     | ('DESKTOP-HUC37G2',) |      | Windows |             | ('10', '10.0.18362', 'SP0', '') |
| List azure.                   | 0.555 | 2019-12-02 10:28:18 |     | ('DESKTOP-HUC37G2',) |      | Windows |             | ('10', '10.0.18362', 'SP0', '') |
| Transfer azure to local.      | 1.12  | 2019-12-02 10:28:20 |     | ('DESKTOP-HUC37G2',) |      | Windows |             | ('10', '10.0.18362', 'SP0', '') |
| Delete s3                     | 1.086 | 2019-12-02 10:28:21 |     | ('DESKTOP-HUC37G2',) |      | Windows |             | ('10', '10.0.18362', 'SP0', '') |
| Delete local                  | 0.048 | 2019-12-02 10:28:22 |     | ('DESKTOP-HUC37G2',) |      | Windows |             | ('10', '10.0.18362', 'SP0', '') |
| Delete azure                  | 0.646 | 2019-12-02 10:28:22 |     | ('DESKTOP-HUC37G2',) |      | Windows |             | ('10', '10.0.18362', 'SP0', '') |
+-------------------------------+-------+---------------------+-----+----------------------+------+---------+-------------+---------------------------------+

PASSED

========================================================================================= warnings summary =========================================================================================
c:\study\iumsds\fall2019\cloudcomputing\env3\lib\site-packages\win32\lib\pywintypes.py:2
  c:\study\iumsds\fall2019\cloudcomputing\env3\lib\site-packages\win32\lib\pywintypes.py:2: DeprecationWarning: the imp module is deprecated in favour of importlib; see the module's documentation for alternative uses
    import imp, sys, os

C:\Program Files\Python37\lib\site-packages\botocore\vendored\requests\packages\urllib3\_collections.py:1
C:\Program Files\Python37\lib\site-packages\botocore\vendored\requests\packages\urllib3\_collections.py:1
  C:\Program Files\Python37\lib\site-packages\botocore\vendored\requests\packages\urllib3\_collections.py:1: DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated, and in 3.8 it will stop working
    from collections import Mapping, MutableMapping

c:\study\iumsds\fall2019\cloudcomputing\env3\lib\site-packages\boxsdk\pagination\page.py:5
  c:\study\iumsds\fall2019\cloudcomputing\env3\lib\site-packages\boxsdk\pagination\page.py:5: DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated, and in 3.8 it will stop working
    from collections import Sequence

c:\study\iumsds\fall2019\cloudcomputing\env3\lib\site-packages\boxsdk\pagination\box_object_collection.py:14
  c:\study\iumsds\fall2019\cloudcomputing\env3\lib\site-packages\boxsdk\pagination\box_object_collection.py:14: DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated, and in 3.8 it will stop working
    class BoxObjectCollection(collections.Iterator, object):

c:\study\iumsds\fall2019\cloudcomputing\env3\lib\site-packages\_pytest\mark\structures.py:325
  c:\study\iumsds\fall2019\cloudcomputing\env3\lib\site-packages\_pytest\mark\structures.py:325: PytestUnknownMarkWarning: Unknown pytest.mark.incremental - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/latest/mark.html
    PytestUnknownMarkWarning,

-- Docs: https://docs.pytest.org/en/latest/warnings.html
================================================================================= 13 passed, 6 warnings in 14.53s ==================================================================================

(ENV3) C:\Study\IUMSDS\Fall2019\CloudComputing\fa19-516-155\cloudmesh-transfer\cloudmesh\transfer>
```
