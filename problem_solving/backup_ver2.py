#same program to back up important files
#but with an improvement of allowing user to give each backup a name
#and saving backups in subdirectories organized by date
#if no name specified, still use date and time name format as ver1
#once again this program executable only from cmd (not within Pycharm), after executing:
    #set PATH=%PATH%C:\Program Files\7-Zip
    #echo %PATH%
    #7z
#to initalize 7z executable (3rd party (7-zip) file zipping software)

import os
import time

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

zip_command = "7z a {0} {1}".format(target, " ".join(source))

#run the backup
print("Zip command is:")
print(zip_command)
print("Running:")
if os.system(zip_command) == 0:
    print("Successful backup to", target)
else:
    print("Backup FAILED")
