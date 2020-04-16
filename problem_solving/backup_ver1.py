#problem: create program that creates backups of important files

#design: 1. files/directories to be backed up should be specified in a list
#2. backup msut be stored in a main backup directory
#3. files are backed up into a zip file
#4. name of the zip archive is the current date and time
#5. use zip command (note: since running windows I am using 3rd party 7zip, execute from cmd using '7z' (not 'zip'), command 'a' to add files to archive)
# to put the files in a zip archive

import os #provides functions for interacting with the operating system
import time

#1:
#Made a folder with some test files to back up in the following location
source = ["C:\\Users\Anterra\FilesToBackUp"] #source is a list

#2:
target_dir = "C:\\Users\Anterra\BackUp" #target_dir is a variable

#3 & 4:
target = target_dir + os.sep + time.strftime("%Y%m%d%H%M%S") + ".zip"

#create target directory if it is not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

#5:
zip_command = "7z a {0} {1}".format(target, " ".join(source))

#run the backup
print("Zip command is:")
print(zip_command)
print("Running:")
if os.system(zip_command) == 0:
    print("Successful backup to", target)
else:
    print("Backup FAILED")

#this program works successfully when executed from command line, because cmd has access to 7-Zip
#(to make 7z executable from anywhere in cmd (not just inside 7-Zip folder), had to use:

#set PATH=%PATH%;C:\Program Files\7-Zip
#echo %PATH%
#7z

#but, can't make it execute inside Pycharm where 7z is not recognized...
#have to get Pycharm to recognize and reference 7z.exe

