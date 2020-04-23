import sys
import time

f = None
#a variable assigned a value of 0 or None is considered "False" by Python

try:
    f = open("poem.txt")
    #our usual file-reading idiom
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end="")
        sys.stdout.flush() #so that it prints to the screen immediately
        print("Press ctrl+c now")
        #to make sure it runs for a while so we have time to cancel, arbitrary 2 second sleep after printing each line
        time.sleep(2)
except IOError:
    print("Could not find file poem.txt")
except KeyboardInterrupt:
    print("!! You cancelled the reading from the file.")
finally:
    if f: #(false)
        f.close()
    print("(Cleaning up: Closed the file)")
    #before the program exits, the file object is always closed
