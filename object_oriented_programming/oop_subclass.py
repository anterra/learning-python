class SchoolMember:
    """Represents any school member.""" #docstring
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("(Initialized SchoolMember: {})".format(self.name))

    def tell(self):
        """Tell my details."""
        print("Name:'{}' Age:'{}'".format(self.name, self.age), end = " ")
            #end=" " was included to allow the next thing printed to continue on the same line
            #(since subclasses are going to append additional information to list of things to be printed)

class Teacher(SchoolMember): #makes Teacher a subtype of class SchoolMember
    """Represents a teacher."""
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age) #init of base class is explicitly called
            #necessary because I am defining an __init__ method for Teacher, so Python won't automatically call the base class __init__
            #if no __init__ method called for Teacher, Pyhton would pull base class init automatically, so this wouldn't be necessary
        self.salary = salary
        print("(Initialized Teacher: {})".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print("Salary: '{:d}'".format(self.salary)) #{:d} tells the formatter to treat the argument as a decimal integer and format it as such
        #could have just used Teacher.tell if all I wanted was the tell method of SchoolMember instead of customizing this one to include salary
        #now, when calling Teacher.tell it will use the customized one. Python always looks for methods in the subclass first, and if nothing found, goes upward through base classes

class Student(SchoolMember):
    """Represents a student."""
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print("(Initialized Student: {})".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print("Marks: '{:d}'".format(self.marks))

t = Teacher("Ms. Kennedy", 40, 50000)
s = Student("Anterra", 25, 90)

#prints a blank line
print()

members = [t, s]
for member in members: #so what I've picked up on is you can use any word like "member" here to iterate over and it will automatically assign and work
    #Works for both Teachers and Students
    member.tell()