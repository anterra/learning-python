#__init__ method
#is run as soon as an object of a class in instantiated
#useful to do any initialization -- passing initial values to your object

class Person:
    def __init__(self, name):
        self.name = name
        #2 different variables even though they're both called name
        #the first is just something called "name" that's part of the object self, dotted notation self.name
        #the other is local variable name

    def say_hi(self):
        print("Hello, my name is", self.name)

p = Person("Anterra") #only specifying 2nd parameter of class Person
p.say_hi()

#last 2 lines could also be written: Person("Anterra").say_hi()

#no need to explicity call the __init__ method
