import sys
from pathlib import Path
import zipfile
import tarfile
import rarfile
import py7zr

def extract_zip(file_path, extract_to):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def extract_rar(file_path, extract_to):
    with rarfile.RarFile(file_path, 'r') as rar_ref:
        rar_ref.extractall(extract_to)

def extract_tar(file_path, extract_to, mode='r:*'):
    with tarfile.open(file_path, mode) as tar_ref:
        tar_ref.extractall(extract_to)

def extract_7z(file_path, extract_to):
    with py7zr.SevenZipFile(file_path, mode='r') as seven_zip_ref:
        seven_zip_ref.extractall(extract_to)

def extract_file(file_path, extract_to):
    if not Path(extract_to).exists():
        extract_to.mkdir(parents=True, exist_ok=True)

    if file_path.endswith('.zip'):
        extract_zip(file_path, extract_to)
    elif file_path.endswith('.rar'):
        extract_rar(file_path, extract_to)
    elif file_path.endswith('.tar'):
        extract_tar(file_path, extract_to, mode='r:')
    elif file_path.endswith('.tar.gz'):
        extract_tar(file_path, extract_to, mode='r:gz')
    elif file_path.endswith('.tar.bz2'):
        extract_tar(file_path, extract_to, mode='r:bz2')
    elif file_path.endswith('.7z'):
        extract_7z(file_path, extract_to)
    else:
        print(f"\nUnsupported file format: {file_path}")
        return
    print(f"\nExtracted {file_path} to {extract_to}")

def main():
    print(f'Running {sys.argv[0]} ...')

    # Get everything after the .py script name
    args = sys.argv[1:]
    
    if len(args) == 0:
        print("\nNeed to supply a command line argument to the compressed file's path")
        return
    
    compressed_file_path = args[0]
    extracted_folder_name = Path(compressed_file_path).with_suffix('')
    extract_to_path = Path(compressed_file_path).parent / extracted_folder_name
    
    if not Path(compressed_file_path).exists():
        print(f'\nFile does not exists: {compressed_file_path}')
        return

    # print(f"\nDo you want to use this script to handle unzipping this file? \n\t{compressed_file_path} \n(YES = 'Y'/'Yes'/ENTER, NO = Anything else) ")
    # answer = input()
    # if answer.upper() in ["Y", "YES", ""]:
    #     pass
    # else:
    #     return

    # print(f"\nFile will be extracted to {extract_to_fullpath}. Rename the folder? \n(YES = Type in new name then ENTER, NO = ENTER) ")    
    # answer = input()
    # if len(answer) > 0:
    #     extracted_folder_name = answer
    #     extract_to_fullpath = Path(compressed_file_path).parent / extracted_folder_name
    # else:
    #     pass
    
    extract_file(compressed_file_path, extract_to_path)

if __name__ == "__main__":
    main()
    # print("\nPress Enter to exit...")
    # input()