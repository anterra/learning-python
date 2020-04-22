#fields -- data. ordinary variables that are bound to the namespaces of classes and objects
#hence their names valid only within the context of their classes/objects

#2 types of fields: class variables and object variables
#class variables: shared. accessed by all instances of that class
#any time one object makes a change to a class variable, change seen by all other instances

#object variable: owned by each individual object
#not shared, not related to field by the same name in different instance

class Robot:

    #class variable:
    population = 0

    def __init__(self, name):
        """Initializes the data"""
        self.name = name #using self. because its object variable
        print("(Initializing {})".format(self.name))
        Robot.population += 1 #using Robot. because its class variable
                              #could also self.__class__.population (object.__class__ refers to the object's class)

    def die(self):
        """I am dying."""
        print("{} is being destroyed!".format(self.name))
        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(Robot.population))

    def say_hi(self):
        """Greeting by the robot.

        Yeah, they can do that."""
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod #this is a decorator
    def how_many(cls):
        """Prints the current population."""
        print("We have {:d} robots.".format(cls.population))

droid1 = Robot("R2-D2")
droid1.say_hi() #using self. because its object method
Robot.how_many() #using Robot. because its class method

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()
