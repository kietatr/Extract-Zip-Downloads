# Auto Extract Downloaded Compressed (Zipped) Files

Auto extract downloaded compressed files (`.zip, .rar, .tar, .tar.gz, .tar.bz2, .7z`).

Useful for Firefox to automatically extract a compressed file after it's been downloaded.  

Works on Windows.


## Development Set Up (Windows)

1. Clone this repo. Make sure you already have Python installed on your computer.

2. Open **Powershell**. `cd` into the cloned repo. Set up a virtual environment called `venv` for this repo using Python's `venv`: 

```
py -m venv venv
```

Or `python3 -m venv venv`

3. Activate the virtual environment:

```
.\venv\Scripts\Activate.ps1
```

4. Install the required packages:

```
py -m pip install -r requirements.txt
```

Or `python3 -m pip install -r requirements.txt`


## Building the executable (.exe) file

Run the Powershell script `.\build_app.ps1` by either:

- **Right-click > Run with Powershell**
- Or run `powershell build_app.ps1` in your Terminal

This will create a dist/ folder that contains the app's .exe file.


## How to use with Firefox

In Firefox:
- Go to **Settings > General tab**. Scroll down to the **Applications** field
  - Or go to **Settings** and type in "zip" in the Search bar
- In the "Content type" column, look for **Compressed (zipped) Folder (application/zip)** and change the "Action" to use this built exe file.
