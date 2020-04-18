#adding update: simpler way of getting files out of source

import os
import time
from zipfile import ZipFile

source = r"C:\Users\Anterra\FilesToBackUp"

target_dir = r"C:\Users\Anterra\BackUp"

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime("%Y%m%d")
now = time.strftime("%H%M%S")

comment = input("Enter a comment --> ")
if len(comment) == 0:
    target = today + os.sep + now + ".zip"
else:
    target = today + os.sep + now + "_" + comment.replace(" ", "_") + ".zip"

if not os.path.exists(today):
    os.mkdir(today)
    print("Successfully created directory", today)

file_list = os.listdir(source) #list all the files in a directory
file_paths = os.path(file_list)
print(file_paths)

with ZipFile(target, "w") as zip: #w = write mode
    print("{} is created".format(target))
    print("These files will be zipped:")
    for each_file in file_list:
        print(each_file)
    for each_file in file_list: #need to be given paths, not a list
        zip.write(each_file)
    print("Files backed up")

#problem: program can't find the files.
#the list file_list is just a list of file names, with no paths ...