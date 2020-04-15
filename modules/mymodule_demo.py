import mymodule

mymodule.say_hi()
print("Version", mymodule.__version__)

#using mymodule in a different python program


#using from..import syntax:
from mymodule import say_hi, __version__

say_hi()
print("Version", __version__)
#not preferable bc if the module already had a __version__ name declared there would be a clash


#or
from mymodule import *
#imports all public names, would not include __version__ bc it starts with underscores
#also not preferable. explicit is better than implicit.