import os
import shutil

def clean():
    path = os.getcwd() # get current working directory
    data_dir = os.path.join(path, "data") # create data directory
    os.makedirs(data_dir, exist_ok=True) # create data directory if it doesn't exist
    for file in os.listdir(path):
        if file.endswith(".py") or file.endswith(".exe"):
            continue
        else:
            file_path = os.path.join(path, file)
            if os.path.isdir(file_path):
                continue # skip directories
            shutil.move(file_path, os.path.join(data_dir, file)) # move file to data directory

clean()
