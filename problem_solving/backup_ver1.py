#problem: create program that creates backups of important files

#design: 1. files/directories to be backed up should be specified in a list
#2. backup must be stored in a main backup directory
#3. files are backed up into a zip file
#4. name of the zip archive is the current date and time
#5. use zip command (note: since running windows I am using 3rd party 7zip,
# execute from cmd using '7z' (not 'zip' as in textbook), command 'a' to add files to archive)
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
#os.sep - gives directory separator "\\", or other relavant separator on any OS
#+ concatenates strings

#create target directory if it is not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

#added after the rest of program was created and run successfully from cmd
#one of many attempts at getting pycharm to recognize 7z as a command
os.system(r"cd ..\..\..\..\..\..\..\..\..\..\..\Program Files\7-Zip")
os.system("7z")

#5:
zip_command = "7z a {0} {1}".format(target, " ".join(source)) #string

#run the backup
print("Zip command is:")
print(zip_command)
print("Running:")
if os.system(zip_command) == 0: #os.system runs command as if it was run from the system
    print("Successful backup to", target)
else:
    print("Backup FAILED")

#this program runs successfully and creates backup zip drive when executed from command line
#IF the following command is executed first to make 7z executable from anywhere in cmd (not just inside 7-Zip folder):

#set PATH=%PATH%;C:\Program Files\7-Zip
#echo %PATH%
#7z


#but, can't make this program execute inside Pycharm where 7z is not recognized...
#have to get Pycharm to recognize and reference 7z.exe
#tried adding as an external tool. no success.
#trying to use os.system to execute 7z from inside 7-Zip folder "in shell" then echo

#the important part is that I understand how this program and all its commands work!
