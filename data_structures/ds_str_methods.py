#this is a string object
name = "Swaroop"

if name.startswith("Swa"):
    print("Yes, the string starts with 'Swa'")

if "a" in name:
    print("Yes, it contains the string 'a'")

if name.find("war") != -1: #.find method returns -1 if unsuccessful in finding substring
    print("Yes, it contains the string 'war'")

delimiter = "_*_"
mylist = ["Brazil", "Russia", "India", "China"]
print(delimiter.join(mylist)) #returns a bigger string
