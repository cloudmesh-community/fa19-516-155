
## E516 - Cloud Computing

### Creation of virtual environment on Windows 10

#### a] Using venv 
- Connect to the command prompt using `cmd` in run option.
- Navigate to the desired working folder.    
- Use following command to create a virtual environment :  
    **`python -m venv ENV3 --system-site-packages`**
    - python -m venv : searches for `venv` and executes the command
    - ENV3 : is the name of the virtual environment that we want to create
    - `--system-site-packages` : is an optional argument. Adding this argument allows the virtual environment to access global python packages in addition to the locally installed packages. Changes made in the virtual environment are not propogated to the global packages.    
    - This command creates a new directory with name as the name of the virtual environment.  
```
C:\Study\IUMSDS\Fall2019\CloudComputing>python -m venv ENV3 --system-site-packages

C:\Study\IUMSDS\Fall2019\CloudComputing>

C:\Study\IUMSDS\Fall2019\CloudComputing>dir
 Volume in drive C is Local Disk
 Volume Serial Number is 0A18-A088

 Directory of C:\Study\IUMSDS\Fall2019\CloudComputing

09/03/2019  01:49 AM    <DIR>          .
09/03/2019  01:49 AM    <DIR>          ..
09/02/2019  11:18 PM        24,948,243 Cloud Computing.epub
09/03/2019  01:47 AM    <DIR>          ENV3
08/27/2019  11:41 PM           575,178 vonLaszewski-e516-syllabus.epub
09/02/2019  11:18 AM           590,615 vonLaszewski-e516.epub
08/28/2019  11:03 PM           626,193 vonLaszewski-writing.epub
09/03/2019  02:32 AM    <DIR>          Week2
               4 File(s)     26,740,229 bytes
               4 Dir(s)  49,465,192,448 bytes free

C:\Study\IUMSDS\Fall2019\CloudComputing>
```

#### b] Using virtualenv
- Alternatively we can use python package `virtualenv` to create the virtual environment.
- Advantage of using `virtualenv` is that it allows us to choose the python version with which we want to create the virtual environment.
- Use following command to create a virtual environment :  
    **`virtualenv --python=C:\Program Files\Python37 ENV3`**
    - `--python` : to specify the python to be used in the virtual environment.
    - ENV3 : Name of the virtual environment.  

#### c] Activate the virtual environment
- We need to activate the virtual environment in order to run our programs in the virtual environment instead of the global python version.
- Navigate to the directory where the virtual environment was created and use following command:  
    **`ENV3\Scripts\activate.bat`**
    - This runs the `activate.bat` file which activates the virtual environment.
    - The prompt shows the name of the virtual environment, indicating successful activation of the virtual environment.

```
C:\Study\IUMSDS\Fall2019\CloudComputing>ENV3\Scripts\activate.bat

(ENV3) C:\Study\IUMSDS\Fall2019\CloudComputing>where python
C:\Study\IUMSDS\Fall2019\CloudComputing\ENV3\Scripts\python.exe
C:\Program Files\Python37\python.exe
C:\Program Files\Python36\python.exe

(ENV3) C:\Study\IUMSDS\Fall2019\CloudComputing>
```

#### d] Enlisting available packages
- As we have used `--system-site-packages`, we expect that all python packages available in the global version will be available in the virtual environment as well.
- Any package can be installed in this virtual environment using pip :  
    **`pip install <package name>`**
- Use following command to enlist only locally installed packages :  
    **`pip list`**
- Use `pip list` command to enlist all packages:    
```
(ENV3) C:\Study\IUMSDS\Fall2019\CloudComputing>pip list
Package                           Version
--------------------------------- ---------
asn1crypto                        0.24.0
attrs                             18.2.0
Automat                           0.7.0
awscli                            1.16.192
backcall                          0.1.0
beautifulsoup4                    4.6.3
bleach                            2.1.3
blis                              0.2.4
bokeh                             1.3.4
boto3                             1.9.182
botocore                          1.12.182
certifi                           2018.4.16
```

- To get list of packages installed locally:  
    **`pip list --local`**  
```
(ENV3) C:\Study\IUMSDS\Fall2019\CloudComputing>pip list --local
Package    Version
---------- -------
pip        19.0.3
setuptools 40.8.0
```
#### e] Deactivating the virtual environment  
- To deactivate the virtual environment, run following command:  
   **`deactivate`**  
- This will disconnect the virtual environment.  
```
(ENV3) C:\Study\IUMSDS\Fall2019\CloudComputing>deactivate
C:\Study\IUMSDS\Fall2019\CloudComputing>
```



