
# coding: UTF-8

# ZIP_Backup_Creator.py

import zipfile
import os

with zipfile.ZipFile ('backup.zip', 'w') as zip_file:

    for file in os.listdir ():
        
        if file.endswith ('.sql'):
            
            zip_file.write (file)
            
print ('Backup created is successful!')
