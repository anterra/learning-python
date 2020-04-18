#my first own program! no demo

#same program to backup important files
#but this time using the built in 'zipfile' module (part of standard library)
#so that program can be executed inside Pycharm
#not relying on os.system
#a solution to first 2 versions' problem!
#also preferable because this way program is self contained, not reliant on system's zip capabilities


import os
import time
from zipfile import ZipFile

source = [r"C:\Users\Anterra\FilesToBackUp"]

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

#a solution found on the internet for getting files out a directory:
#because using ZipFile I need to iterate over and add each file, not just add entire folder to zip as before
def get_file_paths(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths

with ZipFile(target, "w") as zip: #w = write mode
    print("{} is created".format(target))
    print("These files will be zipped:")
    file_paths = get_file_paths(" ".join(source))
    for file_name in file_paths:
        print(file_name)
    for file in file_paths:
        zip.write(file)
    print("Files backed up")

#just want to really clear on what the get_file_paths function is doing
#creating a list
#os.walk generates file names in a directory tree -- yields two lists, files and dirs
#also this creates folders Users -> Anterra -> FileToBackUp --> then all the acutal photos inside the zip folder
#instead of just the files