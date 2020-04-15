#modules

#standard library modules

import sys

print("The command line arguments are:")
for i in sys.argv:
    print(i)

print("\n\nThe PYTHONPATH is", sys.path, "\n")

#sys is a compiled module (written in Python), contains functionality related to the system
#sys.argv is list of strings, contains the command line arguments

#executed from command line > 'py module_using_sys.py we are arguments'
#(each argument is separated by white space)
#the name of the script running is always the first argument in sys.argv list

#sys.path contains list of directory names where modules imported from
