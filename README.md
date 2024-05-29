# Extract files to Downloads folder

Auto extract file to the D:\Downloads folder 

Works on Windows


## Set Up (Windows)

1. Clone this repo. Make sure you already have Python installed on your computer.

2. Open **Powershell**. `cd` into the cloned repo. Set up a virtual environment called `unzip_files` for this repo using Python's `venv`: 

```
py -m venv unzip_files
```

Or `python3 -m venv unzip_files`

3. Activate the virtual environment:

```
.\unzip_files\Scripts\Activate.ps1
```

4. Install the required packages:

```
py -m pip install -r requirements.txt
```

Or `python3 -m pip install -r requirements.txt`


## Building an executable (.exe) file

Run the Powershell script `.\build_app.ps1` by either:

- Right-click > Run with Powershell
- Or run `powershell build_app.ps1` in your Terminal

This will create a dist/ folder that contains the app's exe file.