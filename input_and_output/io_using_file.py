poem = """\
Programming is fun 
When the work is done
if you wanna make your work also fun: 
    use Python!
"""

#open for 'w'riting
f = open("poem.txt", "w")
#write text to file
f.write(poem)
#close the file
f.close()

#If no mode is specified,
#'r'read mode is assumed by default
f = open("poem.txt")
while True:
    line = f.readline()
    #Zero length indicates EOF
    if len(line) == 0:
        break
    #the "line" already has a newline
    #at the end of each line
    #since it is reading from a file
    print(line, end="")
#close the file
f.close()