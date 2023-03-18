import os

for dirpath, dirnames, filenames in os.walk('C:/Program Files'):
    for dirname in dirnames :
        print("Catalog:", os.path.join(dirpath, dirname))
    for filename in filenames :
        print("File:", os.path.join(dirpath, filename))
        print("File Size:", os.path.getsize(dirpath))