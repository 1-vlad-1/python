import os

def file_structure(path):
    for dirpath, dirnames, filenames in os.walk(path):
        for dirname in dirnames :
            print("Catalog:", os.path.join(dirpath, dirname))
        for filename in filenames :
            print("File:", os.path.join(dirpath, filename))
            print("File Size:", os.path.getsize(dirpath))

file_structure('C:/Users/TEMP')