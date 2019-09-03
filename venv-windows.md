
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
![title](Create_venv.png)

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
    - This command creates a new directory with name as the name of the virtual environment.  
![title](activate_venv.png)

#### d] Enlisting available packages
- As we have used `--system-site-packages`, we expect that all python packages available in the global version will be available in the virtual environment as well.
- Any package can be installed in this virtual environment using pip :  
    **`pip install <package name>`**
- Use following command to enlist only locally installed packages :  
    **`pip list`**
- Use `pip list` command to enlist all packages:    
![title](global_packages.png)  

- To get list of packages installed locally:  
    **`pip list --local`**  
![title](local_packages.png)  

#### e] Deactivating the virtual environment  
- To deactivate the virtual environment, run following command:  
   **`deactivate`**  
- This will disconnect the virtual environment.  



