import pickle
#pickle is a Python standard module used to store any plain Python
#object and get it back later

#the name of the file where we will store the object
shoplistfile = "shoplist.data"
#the list of things to buy
shoplist = ["apple", "mango", "carrot"]

#write to the file
f = open(shoplistfile, "wb") #write mode in binary
#dump the object to a file
pickle.dump(shoplist, f) #this process is called pickling
f.close()

#destroy the shoplist variable
del shoplist

#read back from the storage
f = open(shoplistfile, "rb")
#load the object from the file
storedlist = pickle.load(f) #unpickling
print(storedlist)
f.close()

